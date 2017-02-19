Building
========
Since most of our source code is either headers that are getting copied from
somewhere, or shared between two complex build systems, getting all these
different parts to talk to each other is tricky. To bridge the two distinct
systems being compiled, we use this external script. 

After the script has successfully been run, cFE can be run:

```shell
# From the root of the repository
cd composite/transfer
./qemu.sh cFE_booter.sh
```

Since the actual building code can be hard to understand, here is an overview of
the steps taken to build this project:

1. Copy all the shared headers from the cFE into the Composite `cFE_booter`
    component, so that the code there can include the right header macros.
1. Build the cFE for our custom Composite target (which is really just a bunch of
    stubs), which produces an object file with a bunch of undefined symbols.
1. Copy the produced object, and all its other miscellaneous files, into the
    Composite `cFE_booter` component.
1. Build Composite, including the `cFE_booter` component. Compiling the source
    files in this component should provide object files containing the symbols
    that are undefined in the cFE object. When Composite links this component
    together, all the symbols will be defined, and the final object file will
    be a bootable Composite component.
