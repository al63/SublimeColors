import sublime, sublime_plugin
import os

class SublimeColorsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        pref_settings = sublime.load_settings('Preferences.sublime-settings')
        try:
            self.schemes
        except:
            self.cur_scheme = 0
            self.schemes = []
            settings = sublime.load_settings('SublimeColors.sublime-settings')
            scheme_names = settings.get('schemes')
            starting_scheme = os.path.basename(pref_settings.get('color_scheme'))
            for name in scheme_names:
                name += ".tmTheme"
                self.schemes.append(name)
                if starting_scheme == name:
                    self.cur_scheme = len(self.schemes)
            if self.cur_scheme == len(self.schemes):
                self.cur_scheme = 0

        pref_settings.set('color_scheme', os.path.join('Packages','Color Scheme - Default', self.schemes[self.cur_scheme]))
        self.cur_scheme += 1
        self.cur_scheme = self.cur_scheme % len(self.schemes)
        sublime.save_settings('Preferences.sublime-settings')