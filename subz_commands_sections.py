import sublime
import sublime_plugin
try:
  from .subz_tools_subl import *
  from .subz_sections import *
except ValueError:
  from subz_tools_subl import *
  from subz_sections import *

class SubzInsertSectionAvlAllocCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, AVL_ALLOC)

class SubzInsertSectionAvlInv(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, AVL_INV)

class SubzInsertSectionAvlState(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, AVL_STATE)

class SubzInsertSectionContractFull(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, CONTRACT_FULL)

class SubzInsertSectionContractMinimal(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, CONTRACT_MINIMAL)

class SubzInsertSectionContractSpo(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, CONTRACT_SPO)

class SubzInsertSectionDefHotel(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, DEF_HOTEL)

class SubzInsertSectionDefMeal(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, DEF_MEAL)

class SubzInsertSectionDefRoom(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, DEF_ROOM)

class SubzInsertSectionQueryTransform(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, QUERY_TRANSFORM)

class SubzInsertSectionRateBase(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, RATE_BASE)

class SubzInsertSectionRateCnx(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, RATE_CNX)

class SubzInsertSectionRateDiscount(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, RATE_DISCOUNT)

class SubzInsertSectionRateDiscountGroup(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, RATE_DISCOUNT_GROUP)

class SubzInsertSectionRatePlan(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, RATE_PLAN)

class SubzInsertSectionRateRule(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, RATE_RULE)

class SubzInsertSectionRateSupplement(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, RATE_SUPPLEMENT)

class SubzInsertSectionTax(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, TAX)

class SubzInsertSectionTaxGroup(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, TAX_GROUP)

class SubzInsertSectionRestriction(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, RESTRICTION)

class SubzInsertSectionTest(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, TEST)

class SubzInsertSectionRateSupplementCat(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, RATE_SUPPLEMENT_CAT)

class SubzInsertSectionRateDiscountCat(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, RATE_DISCOUNT_CAT)

class SubzInsertSectionConfig(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, CONFIG)

class SubzInsertSectionCustomInfo(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, CUSTOM_INFO)

class SubzReformatAriz(sublime_plugin.TextCommand):
  def run(self, edit):
    SubzAddAllSectionsHeaders.run(self, edit)
    SubzFormatAllSections.run(self, edit)

class SubzAddAllSectionsHeaders(sublime_plugin.TextCommand):
  def run(self, edit):
    for section in SECTIONS_WITH_COLUMN_HEADERS:
      section_lines = split_section_to_lines(section)
      header_regex = section_header_regex(section_lines)
      basic_header = section_basic_header(section_lines)

      find_and_replace(self, edit, header_regex, basic_header)

class SubzFormatAllSections(sublime_plugin.TextCommand):
  def run(self, edit):
    result = is_package_installed("Table Editor")

    if result == False:
      sublime.message_dialog("To format sections you need to install Package 'Table Editor'\nhttps://packagecontrol.io/packages/Table%20Editor")
    else:
      self.view.sel().clear()

      header_regions = self.view.find_all(r"^\|-", 0)
      number_of_regions = len(header_regions)

      if number_of_regions == 0:
        sublime.message_dialog("To format sections you need to add all section headers first\nLines with '|-' are required")
      else:
        for region in header_regions:
          self.view.sel().add(region)
        sublime.active_window().run_command('table_editor_next_field')
        self.view.sel().clear()