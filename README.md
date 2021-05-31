# ResolveDepTree

## Usage: <br/>
```
python ResolveDepTree.py [--option argument1 argument2 ...]
Options:
    --name [name1] [name2] ...   :: The name(s) of distribution(s) for which dependencies should be resolved.
    --help                       :: print out this help and exit the program.
```
Notes:<br/>
There must be at least one option specified, and at least one name if the option specified is "--name".<br/>
This script (and thus the other module for this script, Parsing.py) should be placed within the same directory as the folder containing all the distros (which must be named "data").

## Directory Structure

You want your directory to look like this:

* data/
* ResolveDepTree.py
* Parsing.py
* README.md

## Prerequisites

To run this script, you must have python 3.6 or later installed.

To do this, perform the following steps:
```
sudo apt update
sudo apt install software-properties-common
sudo add-apt repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.6
```

Once you do this, `cd` into the directory illustrated above, and run as shown in the usage help.
