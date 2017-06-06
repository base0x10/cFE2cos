# OSAL Unit Tests for Composite
## Build process overview
0. The compiler is given the unit test headers and source and links them together, leaving the actual implementations of OSAL methods as stubs. This process creates an individual `.o` file for each test file.
0. `.o` files are copied to the `test` directory in `cFE_booter` (the component's directory in Composite).
0. Headers in the `os*-test` directories are copied to `cFE_booter/test` as well in order for the component to call `OS_Application_Startup` `cFE_entrypoint.c`.
0. `cFE_booter` is compiled normally during the Composite build process, which links the implementations of OSAL methods to the previously created objects.

## Notes
* The build process will likely throw a number of errors regarding function signatures ­ several functions are prototyped with `const char*` as arguments but are implemented with `char *`. It is currently unknown whether these errors are a result of the linking method or simply an mistake in OSAL.
* Components that do not expose interfaces (those in `no_interface`) cannot share code between each other. Therefore, we insert the unit test method directly into `cFE_entrypoint.c`, which is where cFE initialization logic takes place.
