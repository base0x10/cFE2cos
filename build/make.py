#!/usr/bin/env python2.7
import sys, getopt
import os
import shutil
import subprocess as sp

# Set variables
print("=== Setting Variables ===")
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

CFE_HEADERS_TO_COPY = [
    "build/cpu1/inc/cfe_platform_cfg.h",
    "build/cpu1/inc/osconfig.h",
    "build/mission_inc/cfe_mission_cfg.h",
    "osal/src/os/inc/*",
    "psp/fsw/pc-composite/inc/*",
    "psp/fsw/inc/*"]

IGNORE_CLOCK_SKEW = False
OUT = ""
if(IGNORE_CLOCK_SKEW):
    print "IGNORE_CLOCK_SKEW = TRUE"
    OUT = " 2>&1 | grep -vP 'Clock skew|in the future'"

# Execute build
if "-c" in sys.argv:
    print("=== Cleaning composite ===")
    sp.check_call("rm -rf *", shell=True, cwd=COMPOSITE_TRANSFER_DIR)
    sp.check_call("make clean" + OUT, shell=True, cwd=COMPOSITE_MAKE_ROOT)
    print("=== Cleaning cFE ===")
    sp.check_call("make clean" + OUT, shell=True, cwd=CFE_MAKE_ROOT)

print("=== Copying headers ===")

if not os.path.exists(COMPOSITE_CFE_HEADER_DESTINATION):
    print("cFE header destination folder not found. Creating it now.")
    os.makedirs(COMPOSITE_CFE_HEADER_DESTINATION)

for header in CFE_HEADERS_TO_COPY:
    sp.check_call("cp " + CFE_DIR + header + " " + COMPOSITE_CFE_HEADER_DESTINATION, shell=True)


print("=== Building cFE ===")
sp.check_call("make config" + OUT, shell=True, cwd=CFE_MAKE_ROOT)
sp.check_call("make" + OUT, shell=True, cwd=CFE_MAKE_ROOT)

print("=== Copying cFE Object ===")
OBJECT_SOURCE = CFE_OBJECT_LOCATION + CFE_OBJECT_NAME
OBJECT_DESTINATION = COMPOSITE_CFE_COMPONENT_ROOT + CFE_OBJECT_NAME
if os.path.exists(OBJECT_DESTINATION):
    os.remove(OBJECT_DESTINATION)
if not os.path.exists(OBJECT_SOURCE):
    raise RuntimeError("Could not find cFE object to copy!")
shutil.copy(OBJECT_SOURCE, OBJECT_DESTINATION)
print("Copied {} to {}".format(OBJECT_SOURCE, OBJECT_DESTINATION))

print("=== Building composite ===")
sp.check_call("make" + OUT, shell=True, cwd=COMPOSITE_MAKE_ROOT)
sp.check_call("make cp" + OUT, shell=True, cwd=COMPOSITE_MAKE_ROOT)
