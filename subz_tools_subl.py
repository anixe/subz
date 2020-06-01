import sublime
import sublime_plugin
try:
  from .subz_tools_io import *
  from .subz_tools import *
except ValueError:
  from subz_tools_io import *
  from subz_tools import *

class SubzAppendCommand(sublime_plugin.TextCommand):
    def run(self, edit, text):
      current_syntax = self.view.settings().get("syntax")
      self.view.set_syntax_file("Packages/Text/Plain text.tmLanguage")
      size = self.view.size()
      if size != 0:
        self.view.insert(edit, size, "\n\n\n")
      size = self.view.size()
      self.view.insert(edit, size, text)
      self.view.set_viewport_position((0, self.view.text_to_layout(size+1)[1]))
      self.view.set_syntax_file(current_syntax)

def insert_ariz_section(plugin, edit, header):
  plugin.view.insert(edit, plugin.view.sel()[0].begin(), header)

def ask_user(caption, default_value, on_done, on_change=None, on_cancel=None):
  return sublime.Window.show_input_panel(sublime.active_window(), caption, default_value, on_done, on_change, on_cancel)

def append_output_panel(text):
  get_output_panel().run_command("subz_append", {"text": text})

def get_output_panel():
  panel = sublime.active_window().get_output_panel("subz")
  sublime.active_window().run_command("show_panel", {"panel": "output.subz"})
  return panel

def append_output_view(text):
  get_output_view().run_command("subz_append", {"text": text})

def get_output_view():
  output_view = get_output_view.output_view
  if output_view == None or not output_view.is_valid() or output_view.window() == None:
    output_view = sublime.active_window().new_file()
    output_view.set_name("Sublime-Z Results")
    output_view.set_scratch(True)
    if is_package_installed("ANSIescape"):
      output_view.set_syntax_file("Packages/ANSIescape/ANSI.tmLanguage")
    elif get_show_ansi_escape_hint():
      if sublime.ok_cancel_dialog(
        "Hint: you can install ANSIescape package to get rid of ANSI escape codes and get colorful output instead.",
        "Don't remind me in the future"
      ) == sublime.DIALOG_YES:
        set_show_ansi_escape_hint(False)

  output_view.window().focus_view(output_view)
  get_output_view.output_view = output_view

  return get_output_view.output_view
get_output_view.output_view = None

def is_package_installed(name):
  return is_file(os.path.join(sublime.installed_packages_path(), name + ".sublime-package"))

def find_and_replace(self, edit, old_text, new_text):
    header_region = self.view.find(old_text, 0)
    self.view.replace(edit, header_region, new_text)
