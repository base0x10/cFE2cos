# cFE2cos
> core Flight Executive + Composite = win

This project is the project for porting NASA's core Flight Executive to the
Composite operating system.

## Getting started

When the project actually works, this is where we'll write how to get actually
run the cFE on Composite. (It's going to be awesome!)

## Developing

If you want to get started working on this project, then you have two options.
If you are not on a 32 bit linux machine (specifically ubuntu 14 is known to work) then you'll want to use our `Vagrantfile` to boot up a
VM suitable for development (this requires vagrant to be installed, either with
a package manager, or from the vagrant
[website](https://www.vagrantup.com/docs/installation/):

```shell
# Clone cFE2cos and init and update composite submodule
git clone https://github.com/Others/cFE2cos.git
cd cFE2cos/
git submodule init composite/
git submodule update composite/
# Boot up the VM (creating it if it doesn't exist yet)
vagrant up
# SSH into the VM, and hack away! (The repository will be linked into ~/cFE2cos)
vagrant ssh -- -Y
# But make sure to shut it down when you're done...
vagrant halt
```

Alternatively, if you're already on an up to date Linux machine (we're looking
for Ubuntu 14 -- 32 bit), then you can have a go at developing directly on bare
metal. To do this you just need to run `provision.sh` (beware that this *will*
require you to enter your password):

```shell
git clone https://github.com/Others/cFE2cos.git
cd cFE2cos/
git submodule init composite/
git submodule update composite/
./provision.sh
```


### Building and Running Composite

If you want to hack on the version of Composite we're using, then you're going
to want to build it. Building Composite is pretty annoying, and its Makefiles
produce pretty oblique output. But here are the commands you'll need to run:

```shell
# Starting from the cFE2cos directory on your development VM (or machine)
cd composite/src
make config
make init
make
make cp
```

And then to run the micro_boot version and verify that it's built correctly:
```shell
# Starting from the cFE2cos directory on your development VM (or machine)
cd composite/transfer
./qemu.sh micro_boot.sh
```

At this point if it worked you'll see the system print `Micro Booter done.`, and
then loop forever. To escape qemu, type `control-a` then `c` then `q` then
`enter`.

### Building and Running the cFE

Building and running the cFE is not difficult, but I'll defer to _NASA's_
excellent README on the subject. You can find that in the
`cFE-6.5.0-OSS-release` folder. (Note that the correct version of `osal` is
already included.)

## Features

This is where we'll write about all the great functionality we've implemented:

## Contributing

Once we come up with some development procedure guidelines we'll put them here!

## Licensing

Once we figure out what license is appropriate we'll put it here.
