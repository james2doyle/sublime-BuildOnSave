BuildOnSave SublimeText Plugin
=================================
_(forked from [SublimeSaveOnBuild](https://github.com/alexnj/SublimeOnSaveBuild))_

This is a simple plugin for [Sublime Text](http://www.sublimetext.com/) to
trigger a build on each save.

Not all projects might need this plugin, especially if the build operation is
lengthy. However, if you have a build that does things like pre-processing CSS
via tools like [LessCSS](http://lesscss.org) and stitching all JS files together,
this might be very handy.

Installation
------------

Clone this repo into your Sublime Text Packages directory
###Linux
    cd ~/.config/sublime-text/Packages/
    git clone git://github.com/smsrkr/BuildOnSave.git

###Mac
    cd ~/"Library/Application Support/Sublime Text/Packages/"
    git clone git://github.com/smsrkr/BuildOnSave.git

Usage
-----
1. Make sure you have a build operation set up in Sublime and you are able to
   build on CTRL+B or CMD+B.
2. Hit your favorite shortcut to Save.


Only for specific projects
------------

I added the setting `build_on_save` control if the build process should be triggered or not. It's simple:

1. Disable global `build_on_save` in your user settings:

		{
			"build_on_save": false
		}

2. Create a Project with a build system
3. Open the **PROJECTNAME.sublime-project** file
4. Activate the feature only for this project:

		{
			"settings": {
				"build_on_save": true
			}
		}

5. Thats it!


*Good luck!*
