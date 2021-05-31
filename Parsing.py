import json
import sys
from os import path

import data

def checkFileExistence(pathToFile):
  if path.exists(pathToFile) == False:
    return False

# takes in name of the module, goes through its META.json file and returns a list of the names of all the distros it requires.
def parseAndCollect(distro, coreModules, moduleDistroMap):
  pathToFile = "./data/" + distro + "/META.json"
  requiredDistros = {}
  if checkFileExistence(pathToFile) == False:
    print(pathToFile + " does not exist. Will still try to resolve the dependency for the rest of the distro names if any.")
    return requiredDistros

  with open(pathToFile, "rt") as f:
    meta = json.load(f)

    if "prereqs" not in meta or "runtime" not in meta["prereqs"] or "requires" not in meta["prereqs"]["runtime"]:
      return requiredDistros  # i.e. return an empty dict. This module doesn't depend on anything (for our purposes).

    for mod in meta["prereqs"]["runtime"]["requires"]:
      # check for errors or ignore-conditions
      if mod in coreModules or mod == "perl":
        continue
      if mod not in moduleDistroMap:
        print(mod + " is not in \"./data/core-modules.json\". Please make sure it is mapped to a distro name.")
        sys.exit()

      distro = moduleDistroMap[mod]
      
      # recurse for the distro.
      requiredDistros[distro] = parseAndCollect(distro, coreModules, moduleDistroMap)
  return requiredDistros