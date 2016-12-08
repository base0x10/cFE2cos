Building
========

Since most of our source code is either headers that are getting copied from
somewhere, or shared between two complex build systems, getting all these
different parts to talk to each other is tricky. Right now, I've written a
python script to do this work, but I think eventually a Makefile should be
written to maintain consistency with the rest of the codebase. Anyway, here is
how to build and run the cFE on composite:
```shell
# Starting from the cFE2cos directory on your development VM (or machine)

# To build the project
# Run this the first time you build
cd cFE-6.5.0-OSS-release/build/cpu1
make config
cd ../../..

cd composite/src
make config
make init
cd ../..

# Run this every time you reboot
cd cFE-6.5.0-OSS-release
. ./setvars.sh
cd ..

# And run this every time you want to rebuild
cd build
./make.py
cd ..

# And to run it
cd composite/transfer
./qemu.sh cFE_booter.sh
```

Since the actual building code can be hard to understand, here is an overview of
the steps taken to build this project:
1. Clean composite and the cFE, so that we're starting from the same place every
    time.
2. Copy all the shared headers from the cFE into the composite cFE_booter
    component, so that the code there can include the right header macros.
2. Build the cFE for the composite target (which is really just a bunch of
    stubs), which produces an object file with a bunch of undefined symbols.
3. Copy the produced object, and all its other miscellaneous files, into the
    Composite cFE_booter component.
4. Build composite, including the cFE_booter component. Compiling the source
    files in this component should provide object files containing the symbols
    that are undefined in the cFE object. When composite links this component
    together, all the symbols will be defined, and the final object file will
    be a bootable composite component.

Running the whole thing once built is actually a lot more straightforward. It is
simply running composite
