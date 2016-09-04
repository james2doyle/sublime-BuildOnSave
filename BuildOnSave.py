import sublime
import sublime_plugin


class BuildOnSave(sublime_plugin.EventListener):
    """the main command class"""

    def on_post_save(self, view):
        """triggers after save"""
        prefs = sublime.load_settings("BuildOnSave.sublime-settings")
        if view.settings().get('build_on_save', True):
            file_ext = view.file_name().split('.')[-1]
            if file_ext in prefs.get("build_on_save_filetypes"):
                view.window().run_command("build")


class ToggleBuildOnSaveCommand(sublime_plugin.TextCommand):
    """toggle settings"""

    # HACK it works!
    # TODO figure out ST plugin api

    def run(self, edit):
        """runs when the command is called"""
        if self.view.settings().get('build_on_save', True):
            self.view.settings().set('build_on_save', False)
        else:
            self.view.settings().set('build_on_save', True)

    def is_checked(self):
        """updates menu item check mark"""
        return self.view.settings().get('build_on_save', True)
