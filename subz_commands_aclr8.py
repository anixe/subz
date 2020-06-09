import sublime
import sublime_plugin
import datetime
try:
  from .subz_tools_aclr8 import *
  from .subz_tools_subl import *
  from .subz_sections import *
except ValueError:
  from subz_tools_aclr8 import *
  from subz_tools_subl import *
  from subz_sections import *

class SubzAclr8Version(sublime_plugin.WindowCommand):
  def run(self):
    run_aclr8_command("--version", append_output_panel)

class SubzAclr8Tests(sublime_plugin.WindowCommand):
  def run(self):
    path, is_temporary = save_ion()
    run_aclr8_command("test " + path, lambda output: self.on_success(output, path, is_temporary), lambda: self.on_fail(path, is_temporary))

  def on_success(self, output, path, is_temporary):
    append_output_panel(output + "All tests passed.")
    self.remove_temp(path, is_temporary)

  def on_fail(self, path, is_temporary):
    self.remove_temp(path, is_temporary)

  def remove_temp(self, path, is_temporary):
    if is_temporary:
      os.remove(path)

class SubzAclr8Query(sublime_plugin.WindowCommand):
  last_query = None

  def run(self):
    today = datetime.date.today()
    checkin = datetime.datetime(year=today.year + 1, month=1, day=1)

    today_formatted = today.strftime("%Y%m%d")
    checkin_formatted = checkin.strftime("%Y%m%d")

    view = self.window.active_view()
    hotel_code = get_contract_section_string_type_value(view, "hotel_code", "TEST")
    source = get_contract_section_string_type_value(view, "source", "TEST")

    ask_user(
      "Enter the query: ",
      SubzAclr8Query.last_query or "HB{0}${1}:{2}/{3}+1/A1".format(today_formatted, source, hotel_code, checkin_formatted),
      self.run_aclr8_command
    )

  def run_aclr8_command(self, query):
    path, is_temporary = save_ion()
    SubzAclr8Query.last_query = query
    run_aclr8_command("repl " + path, lambda output: self.on_success(output, path, is_temporary), lambda: self.on_fail(path, is_temporary), query)

  def on_success(self, output, path, is_temporary):
    append_output_panel(output)
    self.remove_temp(path, is_temporary)

  def on_fail(self, path, is_temporary):
    self.remove_temp(path, is_temporary)

  def remove_temp(self, path, is_temporary):
    if is_temporary:
      os.remove(path)