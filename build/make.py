#!/usr/bin/env python2.7
# cFE2cos build script. Builds Composite and the cFE and links the two together.
import argparse
import os
import shutil
import subprocess as sp
import glob

# Load command line arguments.
parser = argparse.ArgumentParser(description='Copy cFE files over to Composite and build Composite with cFE support.')
parser.add_argument('-c', '--clean', dest='clean', action='store_true', help='Clean the Composite build directory before building it.')
parser.add_argument('-i', '--ignore-clock-skew', dest='skew', action='store_true', help='Ignore clock skew warnings when building.')
parser.add_argument('-f', '--first-time', dest='first', action='store_true', help='Also run init steps when building.')
parser.add_argument('-u', '--unit-tests', dest='unit_tests', action='store_true', help='Build unit tests.')

args = parser.parse_args()

print """
#######################
## SETTING VARIABLES ##
#######################
"""

# Set static variables.
ROOT = "../"
print "ROOT: {}".format(ROOT)

COMPOSITE_DIR = ROOT + "composite/"
COMPOSITE_TRANSFER_DIR = COMPOSITE_DIR + "transfer/"
COMPOSITE_MAKE_ROOT = COMPOSITE_DIR + "src/"
COMPOSITE_CFE_COMPONENT_ROOT = COMPOSITE_DIR + "src/components/implementation/no_interface/cFE_booter/"
COMPOSITE_CFE_HEADER_DESTINATION = COMPOSITE_CFE_COMPONENT_ROOT + "gen/"
print "COMPOSITE_DIR: {}".format(COMPOSITE_DIR)
print "COMPOSITE_TRANSFER_DIR: {}".format(COMPOSITE_TRANSFER_DIR)
print "COMPOSITE_MAKE_ROOT: {}".format(COMPOSITE_MAKE_ROOT)
print "COMPOSITE_CFE_COMPONENT_ROOT: {}".format(COMPOSITE_CFE_COMPONENT_ROOT)
print "COMPOSITE_CFE_HEADER_DESTINATION: {}".format(COMPOSITE_CFE_HEADER_DESTINATION)

CFE_DIR = ROOT + "cFE-6.5.0-OSS-release/"
CFE_MAKE_ROOT = CFE_DIR + "build/cpu1/"
CFE_OBJECT_LOCATION = CFE_MAKE_ROOT + "exe/"
CFE_OBJECT_NAME = "composite_cFE.o"
print "CFE_DIR: {}".format(CFE_DIR)
print "CFE_MAKE_ROOT: {}".format(CFE_MAKE_ROOT)
print "CFE_OBJECT_LOCATION: {}".format(CFE_OBJECT_LOCATION)
print "CFE_OBJECT_NAME: {}".format(CFE_OBJECT_NAME)

COMPOSITE_CFE_UT_DESTINATION = COMPOSITE_CFE_COMPONENT_ROOT+ "test/"
OSAL_UT_DIR = CFE_DIR + "osal/src/unit-tests/"
OSAL_UT_OBJECTS_TO_COPY = [
    "ut_os_stubs.o",
    "ut_oscore_binsem_test.o",
    "ut_oscore_countsem_test.o",
    "ut_oscore_exception_test.o",
    "ut_oscore_interrupt_test.o",
    "ut_oscore_misc_test.o",
    "ut_oscore_mutex_test.o",
    "ut_oscore_queue_test.o",
    "ut_oscore_task_test.o",
    "ut_oscore_test_composite.o",
    "ut_psp_voltab_stubs.o"
]
OSAL_UT_HEADERS_TO_COPY = [
    "oscore-test",
    "osfile-test",
    "osfilesys-test",
    "osloader-test",
    "osnetwork-test",
    "osprintf-test",
    "ostimer-test",
    "shared"
]

CFE_HEADERS_TO_COPY = [
    "build/cpu1/inc/cfe_platform_cfg.h",
    "build/cpu1/inc/osconfig.h",
    "build/mission_inc/cfe_mission_cfg.h",
    "osal/src/os/inc/*",
    "psp/fsw/pc-composite/inc/*",
    "psp/fsw/inc/*"
]

# Just some shell magic to load the environment variable exports needed to build cFE.
cfe_env = sp.Popen(["bash", "-c", "trap 'env' exit; cd {} && source \"$1\" > /dev/null 2>&1".format(CFE_DIR),
       "_", "setvars.sh"], shell=False, stdout=sp.PIPE).communicate()[0]
os.environ.update(dict([line.split('=', 1) for line in filter(None, cfe_env.split("\n"))]))

print """
##############
## BUILDING ##
##############
"""

OUT = ""
if args.skew:
    "Warnings about clock skew will not be printed."
    OUT = " 2>&1 | grep -vP 'Clock skew|in the future'"

# Execute build
if args.clean:
    print "=== Cleaning Composite ==="
    sp.check_call("rm -rf *", shell=True, cwd=COMPOSITE_TRANSFER_DIR)
    sp.check_call("make clean" + OUT, shell=True, cwd=COMPOSITE_MAKE_ROOT)
    print "=== Cleaning cFE ==="
    sp.check_call("make clean" + OUT, shell=True, cwd=CFE_MAKE_ROOT)

print "=== Copying headers ==="
if not os.path.exists(COMPOSITE_CFE_HEADER_DESTINATION):
    print "cFE header destination folder not found. Creating it now."
    os.makedirs(COMPOSITE_CFE_HEADER_DESTINATION)
for header in CFE_HEADERS_TO_COPY:
    sp.check_call("cp " + CFE_DIR + header + " " + COMPOSITE_CFE_HEADER_DESTINATION, shell=True)

if args.unit_tests:
    print "=== Building unit tests ==="
    sp.call("make" + OUT, shell=True, cwd=OSAL_UT_DIR)
    if os.path.exists(COMPOSITE_CFE_UT_DESTINATION):
        shutil.rmtree(COMPOSITE_CFE_UT_DESTINATION)
    os.mkdir(COMPOSITE_CFE_UT_DESTINATION)
    print "Copying UT objects..."
    for obj in OSAL_UT_OBJECTS_TO_COPY:
        print(obj)
        shutil.copy(OSAL_UT_DIR + obj, COMPOSITE_CFE_UT_DESTINATION)
        print "Copied {} to {}".format(obj, COMPOSITE_CFE_UT_DESTINATION)
    print "Copying UT headers..."
    for folder in OSAL_UT_HEADERS_TO_COPY:
        shutil.copytree(OSAL_UT_DIR + folder, COMPOSITE_CFE_UT_DESTINATION + folder)
        print "Copied {} to {}".format(folder, COMPOSITE_CFE_UT_DESTINATION)

print "=== Building cFE ==="

sp.check_call("make" + OUT, shell=True, cwd=CFE_MAKE_ROOT)

print "=== Copying cFE Object ==="
OBJECT_SOURCE = CFE_OBJECT_LOCATION + CFE_OBJECT_NAME
OBJECT_DESTINATION = COMPOSITE_CFE_COMPONENT_ROOT + CFE_OBJECT_NAME
if os.path.exists(OBJECT_DESTINATION):
    os.remove(OBJECT_DESTINATION)
if not os.path.exists(OBJECT_SOURCE):
    raise RuntimeError("Could not find cFE object to copy!")
shutil.copy(OBJECT_SOURCE, OBJECT_DESTINATION)
print "Copied {} to {}".format(OBJECT_SOURCE, OBJECT_DESTINATION)

print "=== Building Composite ==="
if args.first:
    sp.check_call("make config" + OUT, shell=True, cwd=COMPOSITE_MAKE_ROOT)
    sp.check_call("make init" + OUT, shell=True, cwd=COMPOSITE_MAKE_ROOT)

sp.check_call("make" + OUT, shell=True, cwd=COMPOSITE_MAKE_ROOT)
sp.check_call("make cp" + OUT, shell=True, cwd=COMPOSITE_MAKE_ROOT)
