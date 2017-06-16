# OSAL Unit Tests for Composite
## Build process overview
0. The compiler is given the unit test headers and source and links them together, leaving the actual implementations of OSAL methods as stubs. This process creates an individual `.o` file for each test file.
0. `.o` files are copied to the `test` directory in `cFE_booter` (the component's directory in Composite).
0. The Composite-specific `shared/ut_main_composite.h` is copied to the `cFE_booter/test/shared` directoy. This header contains function definitions for running the different unit tests.
0. `cFE_booter` is compiled normally during the Composite build process, which links the implementations of OSAL methods to the previously created objects.

## Notes
* Components that do not expose interfaces (those in `no_interface`) cannot share code between each other. Therefore, we insert the unit test method directly into `cFE_entrypoint.c`, which is where cFE initialization logic takes place. This will not change until the cFE itself is made an `interface`.
* To aid with gradually implementing OSAL methods, `UT_os_log_api()` in `shared/ut_os_stubs.c` has been edited to print the result of the test directly. The default strategy that OSAL uses is to print the results of unit tests at the end of all tests; this would prevent us from unit testing certain methods without implementing *all* of them. The Composite-specific implementation (`shared/ut_os_stubs_composite.c`) also converts the test result codes to a more human-readable format.
* Unit test source files with names ending with `_composite` contain Composite-specific code for the unit test suite; these files have priority over their non-`_composite` counterparts. Additionally `shared/ut_composite_main` and `shared/ut_composite_misc` provide definitions necessary for the cFE component to interface with these customized unit tests.
* Since we lack the ability to load applications, the `OS_Application_Startup` methods in each unit test category have been renamed so as to avoid naming conflicts. These methods now follow the naming convention `Composite_UT_<name of test>()`.
