import sublime
import sublime_plugin
import os

class BuildOnSave(sublime_plugin.EventListener):
    """the main command class"""

    def on_post_save(self, view):
        # Get project data (if available)
        project_data = view.window().project_data()

        # --- Get Settings, with Project Settings Overriding Global ---
        if project_data and "settings" in project_data and "build_on_save" in project_data["settings"]:
            build_on_save_settings = project_data["settings"]["build_on_save"]
        else: #Fallback on Global Settings
            settings = sublime.load_settings("BuildOnSave.sublime-settings")
            build_on_save_settings = settings.get("build_on_save", {})

        logging_enabled = build_on_save_settings.get("logging", False)  # Get logging setting

        if not build_on_save_settings.get("enabled", True):
            if logging_enabled:
                print("BuildOnSave: Skipping. Plugin is disabled in the settings.")
            return

        file_name = view.file_name()
        if not file_name:
            if logging_enabled:
                print("BuildOnSave: No file name for the view.")
            return

        # Get the syntax file path
        syntax_file = view.settings().get('syntax')
        if not syntax_file:
            if logging_enabled:
                print("BuildOnSave: No syntax defined for the view.")
            return

        # Extract the syntax name
        syntax_name = os.path.splitext(os.path.basename(syntax_file))[0]

        if not syntax_name:
            if logging_enabled:
                print("BuildOnSave: No syntax name found for the view.")
            return

        logging_enabled = build_on_save_settings.get("logging", False)  # Get logging setting
        delay = build_on_save_settings.get("delay", 0)
        build_system_map = build_on_save_settings.get("build_system_map", {})

        # doesn't seem to currently work...
        show_panel = build_on_save_settings.get("show_panel_on_build", False) # Get setting

        build_system_name = build_system_map.get(syntax_name)

        if build_system_name:
            def trigger_build():
                always_run_default = build_on_save_settings.get("always_run_default", True)

                # Prioritize project-defined build systems
                if project_data and "build_systems" in project_data:
                    for build_system in project_data["build_systems"]:
                        # Found a matching build system in the project
                        if "name" in build_system and build_system["name"] == build_system_name:
                            # Construct the build command arguments
                            build_args = {}
                            for key, value in build_system.items():
                                if key != "name":  # Exclude the 'name' key itself
                                    if isinstance(value, str):
                                        build_args[key] = sublime.expand_variables(value, view.window().extract_variables())
                            # Conditionally add output-related arguments
                            # doesn't seem to currently work...
                            build_args["quiet"] = not show_panel

                            if logging_enabled:
                                print("BuildOnSave: Running \"{}\"".format(build_system_name))
                            # Run the build command with the constructed arguments
                            view.window().run_command("exec", build_args)

                    if always_run_default:
                        if logging_enabled:
                            print("BuildOnSave: Running default build system for the view.")
                        # Found a matching build system in the project
                        view.window().run_command("build", {"variant": ""}) # Run the *default* build variant
                        return  # Exit the function after triggering the build

            # if logging_enabled:
                # print("BuildOnSave: Running variant \"{}\"".format(build_system_name))
            # If no matching project build system was found, fall back to variant
            # view.window().run_command("build", {"variant": build_system_name})

            if delay > 0:
                sublime.set_timeout_async(trigger_build, delay)
            else:
                trigger_build()
        else:
            if logging_enabled:
                print("BuildOnSave: No build system found for syntax {}".format(syntax_name))
