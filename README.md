BuildOnSave - SublimeText Plugin
=================================

A plugin for [Sublime Text](http://www.sublimetext.com) that triggers the build
command after each save.

_A fork of [SublimeSaveOnBuild](https://github.com/alexnj/SublimeOnSaveBuild)_
_A fork of [SublimeSaveOnBuild](https://github.com/bdeshi/sublime-BuildOnSave)_

> This fork allows the user to pick which build system you want to run. It also uses Syntaxes for the mapping instead of file extensions.


Installation
------------

### Package Control
  + Select **Package Control: Add Repository** from the Command Palette.
  + Add `https://github.com/james2doyle/sublime-BuildOnSave`.
  + Select **Package Control: Install Package** from the Command Palette.
  + Search for and install `BuildOnSave`.

### Without Package Control
+ #### Linux/OSX
  ```batch
  cd "path/to/SublimeText/Packages/"
  git clone git://github.com/james2doyle/sublime-BuildOnSave.git
  ```

+ #### Windows
  ```batch
  cd "path\to\SublimeText\Packages\"
  git clone git://github.com/james2doyle/sublime-BuildOnSave.git
  ```


Configuration
-------------

1. You can control build-on-save for individual projects. <br>
   Simply configure the `.sublime-project` file, like so:

```json
{
  "settings": {
    "build_on_save": {
      // print details on what is happening
      "logging": false,
      // enable or disable build-on-save
      "enabled": true,
      // run the default build system when there is no match
      "always_run_default": true,
      // panel toggle
      "show_panel_on_build": false,
      // delay the build in case there is a reason
      "delay": 0,
      // Build-on-save will apply only to these file extensions
      "build_system_map": {
        // The keys are syntax names
        // The values are the NAMES of Sublime Text build systems
        // (as they appear in the Tools -> Build System menu).

        // Examples:
        // "HTML (Blade)": "Project - Format Blade File", // this is the "name" of a Project build system
        // "JavaScript": "NodeJs", // this is the "name" of a build system
        // "C++": "Make", // this is the "name" of a build system
      }
    }
  }
}
```

Usage
-----
1. Make sure your build systems are set up properly.
2. Now just save a file, and the build command should run on it. <br>
   (If the file's syntax exists and a build system is found.)

*Good Luck!*

_A fork of [SublimeSaveOnBuild](https://github.com/alexnj/SublimeOnSaveBuild)_
_A fork of [SublimeSaveOnBuild](https://github.com/bdeshi/sublime-BuildOnSave)_
