# Eddie Kim
# Edited May 31 2021

import json
import sys
from os import path

import Parsing

# If I use 'with' statements, then these files would need to be opened and closed many times, possibly affecting the efficiency.
#   So I chose open it once globally, pass it around as arguments and then close it at the end of the module.
cm = open("./data/core-modules.json", "rt")
mdm = open("./data/module-distro-map.json", "rt")
coreModules  = json.load(cm)
moduleDistroMap = json.load(mdm)

# printed when --help flag is used.
def printHelp():
  print()
  print("Usage: python3.[6..9] ResolveDepTree.py [--option argument1 argument2 ...]")
  print("Options:")
  print("  --name [name1] [name2] ...   :: The name(s) of distribution(s) for which dependencies should be resolved.")
  print("  --help                       :: print out this help and exit the program.")
  print("Example: `python3.9 ResolveDepTree.py --name DateTime Package-Stash`")
  print("Notes: ")
  print("  There must be at least one option specified, and at least one name if the option specified is `--name`.")
  print("  This script (and thus the other module for this script, Parsing.py) should be placed within the same directory as the folder containing all the distros, which must be named `data/`.")
  print("  You must have python 3.6 or later installed, and use whichever version you installed to run this program.")

# check errors or other corner cases that would end the program immediately.
def checkCornerCases(argv):
  if len(argv) <= 1:
    print("Please make sure to include a flag. Try `python ResolveDepTree.py --help` for details.")
    sys.exit()

  if argv[1] != "--help" and argv[1] != "--name":
    print(argv[1] + " is not a valid flag option. See `python ResolveDepTree.py --help` to see all valid flag options.")
    sys.exit()

  if "--help" in argv:
    printHelp()
    sys.exit()

  if argv[1] == "--name" and len(argv) <= 2: 
    print("At least one distribution name must be specified after the `--name` flag.")
    sys.exit()

  if len(argv[1:]) != len(set(argv[1:])):
    print("You have provided duplicate flags or values. Please make sure there aren't any and try again.")
    sys.exit()

checkCornerCases(sys.argv)

# Parse necessary META.json files, possibly recursively. Print the resulting object.
dict = {}
for i in range(2, len(sys.argv)):
  dict[sys.argv[i]] = Parsing.parseAndCollect(sys.argv[i], coreModules, moduleDistroMap)
print(json.dumps(dict, indent=4))

cm.close()
mdm.close()
