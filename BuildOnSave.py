import sublime, sublime_plugin, re

class BuildOnSave( sublime_plugin.EventListener ):
    def on_post_save( self, view ):
        settings = sublime.load_settings( "BuildOnSave.sublime-settings" )

        if view.settings().get('build_on_save', True):
          if re.search( settings.get( "filename_filter" ), view.file_name() ):
              view.window().run_command( "build" )
