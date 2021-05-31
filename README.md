# ResolveDepTree

## Description

This program will output, to `stdout`, a `json` object that resolves the dependencies of distributions specified after the `--name` flag.

For details about usage and directory structure, see below.

## Usage:
```
python3.[6..9] ResolveDepTree.py [--option argument1 argument2 ...]
Options:
  --name [name1] [name2] ...  :: The name(s) of distribution(s) for which dependencies should be resolved.
  --help                      :: print out this help and exit the program.
```
Example: `python3.9 ResolveDepTree.py --name DateTime Package-Stash`<br/>
Notes:<br/>
There must be at least one option specified, and at least one name if the option specified is `--name`.<br/>
This script (and thus the other module for this script, Parsing.py) should be placed within the same directory as the folder containing all the distros (which must be named `data/`).<br/>
You must have python 3.6 or later installed, and use whichever version you installed to run this program.

## Directory Structure

You want your directory to look like this:

* data/
  * distribution1
  * distribution2
  * ...
* ResolveDepTree.py
* Parsing.py
* README.md

## Prerequisites

You need to have Ubuntu Xenial installed (Other Ubuntu versions may work, but have not been tested).

You must also have python 3.6 or later installed.<br/>
To do this, perform the following steps:
```
sudo apt update
sudo apt install software-properties-common
sudo add-apt repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.6
```

Once you do this, `cd` into the directory illustrated above, and run in the command shell/terminal with syntax as shown in the usage help.
