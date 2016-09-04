BuildOnSave - SublimeText Plugin
=================================

A plugin for [Sublime Text](http://www.sublimetext.com) that triggers the build
command after each save.


Installation
------------

### Package Control
  + Select **Package Control: Add Repository** from the Command Palette.
  + Add `https://github.com/smsrkr/BuildOnSave`.
  + Select **Package Control: Install Package** from the Command Palette.
  + Search for and install `BuildOnSave`.

### Without Package Control
+ #### Linux/OSX
  ```batch
  cd "path/to/SublimeText/Packages/"
  git clone git://github.com/smsrkr/BuildOnSave.git
  ```

+ #### Windows
  ```batch
  cd "path\to\SublimeText\Packages\"
  git clone git://github.com/smsrkr/BuildOnSave.git
  ```


Configuration
-------------

1. Add and activate the `build_on_save` setting to your ST **User Settings**:
```json
{
  "build_on_save": true
}
```

2. Edit the package setting `build_on_save_filetypes` if needed.<br>
   This setting selects filetypes to build after save.

Usage
-----
1. Make sure your build systems are set up properly.
2. Now just save a file, and the build command should run on it. <br>
   (If the file's extension exists in `build_on_save_filetypes`.)

3. Toggle Build-on-Save on a per file basis with **Tools | Build on Save**.
3. You can control build-on-save for individual projects too. <br>
   Simply configure the `.sublime-project` file, like so:
```json
{
  "settings":
  {
    "build_on_save": true
  }
}
```


*Good Luck!*


_A fork of [SublimeSaveOnBuild](https://github.com/alexnj/SublimeOnSaveBuild)_
