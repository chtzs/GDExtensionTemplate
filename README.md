# Description

This project is a CMake-based gdextension template to simplify gdextension development.

# Dependencies

+ Python3 >= 3.8
+ godot-cpp >= 4.1

# How to use

## Prepare
Clone this repository.
```bash
git clone https://github.com/chtzs/GDExtensionTemplate 

mv GDExtensionTemplate [your-project-name] # rename
```

After that, open `CMakeLists.txt` in the root directory, find lines like this:
```cmake
# Main project information
project( 
    GDExtensionExample
    LANGUAGES
        CXX
    VERSION
        0.1.0
)
```
Rename GDExtensionExample to your project name.

Okay, it's as simple as that.

## Compile

```bash
# First, make a directory to store all configs and output files
mkdir build
cd build

# Then, using cmake to generate Makefile (Release by default)
cmake .. -DCMAKE_BUILD_TYPE=Debug

# Build project
make
```

The output lies on the `build/output`. It looks like this:
```txt
build
└── output
    ├── GDExtensionExample.gdextension
    └── lib
        └── Darwin-universal
            └── libGDExtensionExample-debug.dylib
```

Switch to your Godot project. Make a directory called "bin" and copy all files under "output" to this directory. It should looks like this:

```txt
/Users/haotian/Documents/GameProjects/stars
├── bin
│   ├── GDExtensionExample.gdextension
│   └── lib
│       └── Darwin-universal
│           └── libGDExtensionExample-debug.dylib
├── export_presets.cfg
├── icon.svg
├── icon.svg.import
├── project.godot
├── root.tscn
└── scripts
```