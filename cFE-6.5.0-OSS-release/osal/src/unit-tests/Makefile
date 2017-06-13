# TODO: Support for printf testing - minimal tests are performed in oscore, but osprintf is much more thorough

CC = gcc
C_VERSION = c99

TESTS = oscore-test osfile-test osnetwork-test ostimer-test osfilesys-test osloader-test

IGNORE = oscore-test/ut_oscore_test_arinc653.c oscore-test/ut_oscore_test_vxworks.c osfile-test/ut_osfile_test_arinc653.c osfilesys-test/ut_osfilesys_test_arinc653.c osfilesys-test/ut_osfilesys_test_vxworks.c ostimer-test/ut_ostimer_test_arinc653.c osloader-test/ut_osloader_test_arinc653.c osnetwork-test/ut_osnetwork_test_arinc653.c shared/ut_psp_voltab_stubs_arinc653.c shared/ut_psp_voltab_stubs_vxworks.c
SOURCE_FILES := $(foreach test, $(TESTS), $(wildcard $(test)/*.c)) $(wildcard shared/*.c)
SOURCE_FILES := $(filter-out $(IGNORE), $(SOURCE_FILES))

CFLAGS = -std=$(C_VERSION) -DOS_USE_EMBEDDED_PRINTF -DLOG_TO_STDOUT_TOO -DCOMPOSITE_OS -fno-stack-protector -c -I ../bsp/pc-composite/config -I ./shared -I ../os/inc -I ./osfile-test

all:
	$(CC) $(CFLAGS) $(SOURCE_FILES)
