SublimeOnSaveBuild Sublime Plugin
=================================

This is a simple plugin for [Sublime Text 2](http://www.sublimetext.com/2) to
trigger a build on each save.

Not all projects might need this plugin, especially if the build operation is
lengthy. However, if you have a build that does things like pre-processing CSS
via tools like [LessCSS](http://lesscss.org) and stitching all JS files together,
this might be very handy.

Installation
------------

Clone this repo into your Sublime Text 2 Packages directory
###Linux
    cd ~/.config/sublime-text-2/Packages/
    git clone git://github.com/alexnj/SublimeOnSaveBuild.git

###Mac
    cd ~/"Library/Application Support/Sublime Text 2/Packages/"
    git clone git://github.com/alexnj/SublimeOnSaveBuild.git

Usage
-----
1. Make sure you have a build operation set up in Sublime and you are able to
   build on CTRL+B or CMD+B.
2. Hit your favorite shortcut to Save.


Only for specific projects
------------

I added the setting `saveOnBuild` control if the build process should be triggered or not. It's simple:

1. Disable global saveOnBuild in your user settings:

		{
			"saveOnBuild": false
		}

2. Create a Project with a build system
3. Open the **PROJECTNAME.sublime-project** file
4. Activate the feature only for this project:

		{
			"settings": {
				"saveOnBuild": true
			}
		}

5. Thats it!


*Good luck!*