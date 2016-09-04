import sublime
import sublime_plugin


class BuildOnSave(sublime_plugin.EventListener):
    def on_post_save(self, view):
        prefs = sublime.load_settings("BuildOnSave.sublime-settings")
        if view.settings().get('build_on_save', True):
            file_ext = view.file_name().split('.')[-1]
            if file_ext in prefs.get("build_on_save_filetypes"):
                view.window().run_command("build")
