import re
import sublime
import sublime_plugin

try:
  from .subz_tools import *
except ValueError:
  from subz_tools import *

class SubzPromptIonFilterToLinesCommand(sublime_plugin.WindowCommand):
    def run(self, search_args = '::'):
        text_to_find = get_latest_search()

        if len(search_args) > 2:
            text_to_find = search_args

        sublime.active_window().show_input_panel('Filter ION (write h for help)', text_to_find, self.on_text_to_find_entered, None, None)

    def on_text_to_find_entered(self, text_to_find):
        set_latest_search(text_to_find)
        sublime.save_settings("subz.sublime-settings")

        if self.window.active_view():
            self.window.active_view().run_command('subz_ion_filter_to_lines', { "arguments": text_to_find })

class SubzIonFilterToLinesCommand(sublime_plugin.TextCommand):
    def run(self, edit, arguments):
        search_type        = 'string'
        invert_search      = False
        text_to_find       = ''
        lines_to_keep      = []
        sections_to_filter = []
        current_section    = SectionType.Other

        args = arguments.split(':', 2)

        if len(args) == 3:
            if 'r' in args[0]:
                search_type   = 'regex'
            if 'd' in args[0]:
                search_type   = 'date'
            if 'e' in args[0]:
                invert_search = True
            self.parse_section_args(args[1], sections_to_filter)

            text_to_find = args[2]

            view = self.view
            sel = view.sel()

            sel.clear()
            region = sublime.Region(0, view.size());
            sel.add(region)

            for r in self.view.sel():
                for line_r in self.view.lines(r):
                    line = self.view.substr(line_r)
                    current_section = self.process_line(line, search_type, invert_search, text_to_find, current_section, sections_to_filter, lines_to_keep)
    
            text = '\n'.join(lines_to_keep)
            self.create_new_tab(text)
        else:
            text = '\nWrong number of arguments passed\nRequired three groups of arguments separated by \":\" -  search_arguments:section_arguments:text_to_search\nOptions:\n\tSearch arguments (can be separated by comma delimiter):\n\t\tr - regex search,\n\t\ts - string search (DEFAULT),\n\t\td - date search,\n\t\ti - lines including search text (DEFAULT),\n\t\te - lines excluding search text\n\tSections arguments (can be separated by comma delimiter):\n\t\tba - sections: RATE.BASE, RATE.SUPPLEMENT, RATE.DISCOUNT, RATE.RULE, RESTRICTION, DEF.ROOM,\n\t\tte - TEST,\n\t\tco - CONTRACT,\n\t\tdh - DEF.HOTEL,\n\t\tdm - DEF.MEAL,\n\t\tdr - DEF.ROOM,\n\t\trp - RATE.PLAN,\n\t\trb - RATE.BASE,\n\t\tru - RATE.RULE,\n\t\trs - RATE.SUPPLEMENT,\n\t\trd - RATE.DISCOUNT,\n\t\tdg - RATE.DISCOUNT_GROUP,\n\t\trr - RESTRICTION,\n\t\tqt - QUERY.TRANSFORM,\n\t\trc - RATE.CNX,\n\t\trt - RATE.TAX,\n\t\trm - RATE.MARKUP,\n\t\taa - AVL.ALLOC,\n\t\tas - AVL.STATE,\n\t\tai - AVL.INV,\nExample commands:\n\t:dr:P1:2 - search for lines including string P1:2 in DEF.ROOM section\n\tde:rb:20180101:20180110 - search for lines in RATE.BASE section which dose not contain passed date in section DATES column\n\tri:rsrd:P[1-2] - search lines matching regex in RATE.SUPPLEMENT and RATE.DISCOUNT sections'
            self.create_new_tab(text)

    def parse_section_args(self, arguments, sections_to_filter):
        if 'te' in arguments:
            sections_to_filter.append(SectionType.Test)
        if 'co' in arguments:
            sections_to_filter.append(SectionType.Contract)
        if 'dh' in arguments:
            sections_to_filter.append(SectionType.DefHotel)
        if 'dm' in arguments:
            sections_to_filter.append(SectionType.DefMeal)
        if 'dr' in arguments:
            sections_to_filter.append(SectionType.DefRoom)
        if 'rp' in arguments:
            sections_to_filter.append(SectionType.RatePlan)
        if 'rb' in arguments:
            sections_to_filter.append(SectionType.RateBase)
        if 'ru' in arguments:
            sections_to_filter.append(SectionType.RateRule)
        if 'rs' in arguments:
            sections_to_filter.append(SectionType.RateSupplement)
        if 'rd' in arguments:
            sections_to_filter.append(SectionType.RateDiscount)
        if 'dg' in arguments:
            sections_to_filter.append(SectionType.RateDiscountGroup)
        if 'rr' in arguments:
            sections_to_filter.append(SectionType.Restriction)
        if 'qt' in arguments:
            sections_to_filter.append(SectionType.QueryTransform)
        if 'rc' in arguments:
            sections_to_filter.append(SectionType.RateCnx)
        if 'ta' in arguments:
            sections_to_filter.append(SectionType.Tax)
        if 'rm' in arguments:
            sections_to_filter.append(SectionType.RateMarkup)
        if 'aa' in arguments:
            sections_to_filter.append(SectionType.AvlAlloc)
        if 'as' in arguments:
            sections_to_filter.append(SectionType.AvlState)
        if 'ai' in arguments:
            sections_to_filter.append(SectionType.AvlInv)
        if 'rdc' in arguments:
            sections_to_filter.append(SectionType.RateDiscountCat)
        if 'rsc' in arguments:
            sections_to_filter.append(SectionType.RateSupplementalCat)
        if 'cfg' in arguments:
            sections_to_filter.append(SectionType.Config)
        if 'ci' in arguments:
            sections_to_filter.append(SectionType.CustomInfo)
        if 'ba' in arguments:
            sections_to_filter.append(SectionType.RateSupplement)
            sections_to_filter.append(SectionType.RateDiscount)
            sections_to_filter.append(SectionType.RateRule)
            sections_to_filter.append(SectionType.RateBase)
            sections_to_filter.append(SectionType.Restriction)
            sections_to_filter.append(SectionType.DefRoom)

    def process_line(self, line, search_type, invert_search, text_to_find, current_section, sections_to_filter, lines_to_keep):
        if current_section == SectionType.Other or current_section not in sections_to_filter:
            return self.other_section(line, search_type, invert_search, text_to_find, lines_to_keep)
        else:
            return self.process_section(line, search_type, invert_search, text_to_find, current_section, lines_to_keep)
    
    def other_section(self, line, search_type, invert_search, text_to_find, lines_to_keep):
        lines_to_keep.append(line)
        return self.get_section_type(line)

    def get_section_type(self, line):
        if "[TEST]" in line:
            return SectionType.Test
        elif "[CONTRACT]" in line:
            return SectionType.Contract
        elif "[DEF.HOTEL]" in line:
            return SectionType.DefHotel
        elif "[DEF.MEAL]" in line:
            return SectionType.DefMeal
        elif "[DEF.ROOM]" in line:
            return SectionType.DefRoom
        elif "[RATE.PLAN]" in line:
            return SectionType.RatePlan
        elif "[RATE.BASE]" in line:
            return SectionType.RateBase
        elif "[RATE.RULE]" in line:
            return SectionType.RateRule
        elif "[RATE.SUPPLEMENT]" in line:
            return SectionType.RateSupplement
        elif "[RATE.DISCOUNT]" in line:
            return SectionType.RateDiscount
        elif "[RATE.DISCOUNT_GROUP]" in line:
            return SectionType.RateDiscountGroup
        elif "[RATE.CNX]" in line:
            return SectionType.RateCnx
        elif "[TAX]" in line:
            return SectionType.Tax
        elif "[RATE.MARKUP]" in line:
            return SectionType.RateMarkup
        elif "[RESTRICTION]" in line:
            return SectionType.Restriction
        elif "[QUERY.TRANSFORM]" in line:
            return SectionType.QueryTransform
        elif "[AVL.ALLOC]" in line:
            return SectionType.AvlAlloc
        elif "[AVL.STATE]" in line:
            return SectionType.AvlState
        elif "[AVL.INV]" in line:
            return SectionType.AvlInv
        elif "[RATE.DISCOUNT_CAT]" in line:
            return SectionType.RateDiscountCat
        elif "[RATE.SUPPLEMENT_CAT]" in line:
            return SectionType.RateSupplementalCat
        elif "[CONFIG]" in line:
            return SectionType.Config
        elif "[CUSTOM_INFO]" in line:
            return SectionType.CustomInfo
        else:
            return SectionType.Other

    def process_section(self, line, search_type, invert_search, text_to_find, current_section, lines_to_keep):
        section_header_regex = r"^\|[^\d\[\]\*\:\{\}\,][\s\|a-z\_]*[^\d\[\]\*\:\{\}\,]*\|$"
        section_regex        = r"^\[[A-Z].*\]$"

        if re.search(section_header_regex, line):
            lines_to_keep.append(line)
            return current_section
        else:
            if re.search(section_header_regex, line):
                lines_to_keep.append(line)
                return current_section
            else:
                if not line:
                    lines_to_keep.append(line)
                    return SectionType.Other
                else:
                    if re.search(section_regex, line):
                        self.global_section(line, search_type, invert_search, text_to_find, lines_to_keep)
                        return SectionType.Other
                    else:
                        self.search(line, search_type, invert_search, text_to_find, lines_to_keep)
                        return current_section
                   
    def search(self, line, search_type, invert_search, text_to_find, lines_to_keep):
        if search_type == 'date':
            if invert_search == False:
                self.search_date(line, text_to_find, False, lines_to_keep)
            else:
                self.search_date(line, text_to_find, True, lines_to_keep)
        elif search_type == 'regex':
            if invert_search == False:
                if re.search(text_to_find, line):
                    lines_to_keep.append(line)
            else:
                if re.search(text_to_find, line) == None:
                    lines_to_keep.append(line)
        else:
            if invert_search == False:
                if text_to_find in line:
                    lines_to_keep.append(line)
            else:
                if text_to_find not in line:
                    lines_to_keep.append(line)

    def search_date(self, line, text_to_find, invert_search, lines_to_keep):
        start_date_to_find,   end_date_to_find   = self.split_to_dates(text_to_find, False)
        start_date_from_line, end_date_from_line = self.split_to_dates(line, True)

        if start_date_to_find == 0 or end_date_to_find == 0 or start_date_from_line == 0 or end_date_from_line == 0:
            lines_to_keep.append(line)
        else:
            dates_intersect = self.dates_intersect(start_date_to_find, end_date_to_find, start_date_from_line, end_date_from_line)
            if dates_intersect == True and invert_search == False:
                lines_to_keep.append(line)
            if dates_intersect == False and invert_search == True:
                lines_to_keep.append(line)

    def dates_intersect(self, start_date_to_find, end_date_to_find, start_date_from_line, end_date_from_line):
        return start_date_from_line >= start_date_to_find and start_date_from_line <= end_date_to_find or end_date_from_line >= start_date_to_find and end_date_from_line <= end_date_to_find or start_date_to_find >= start_date_from_line and end_date_to_find <= end_date_from_line

    def split_to_dates(self, text_to_split, parse_line):
        weekdays_pattern  = re.compile(r'[W,A,D]\[[1-7]{0,7}\]')
        date_type_pattern = re.compile(r'[A,I,P,W]')
        dates             = ''

        if parse_line:
            dates_column = text_to_split.split('|', 2)[1]
            dates        = re.sub(weekdays_pattern, '', dates_column)
            dates        = re.sub(date_type_pattern, '', dates)
            dates        = re.sub(r'\s+', '', dates, flags=re.UNICODE)
        else:
            dates = text_to_split

        dates_array = dates.split(':')

        if len(dates_array) == 1:
            start_date = self.parse_date_to_int(dates_array[0])
            return start_date, start_date
        else:
            start_date = self.parse_date_to_int(dates_array[0])
            end_date   = self.parse_date_to_int(dates_array[1])
            return start_date, end_date

    def parse_date_to_int(self, date):
        if len(date) != 8:
            return 0
        try:
            return int(date)
        except ValueError:
            return 0
      
    def create_new_tab(self, text):
        results_view = self.view.window().new_file()
        results_view.set_name('Filter Results')
        results_view.set_scratch(True)
        results_view.settings().set('word_wrap', self.view.settings().get('word_wrap'))
        results_view.run_command('append', {'characters': text, 'force': True, 'scroll_to_end': False})
        results_view.set_syntax_file(self.view.settings().get('syntax'))

class SectionType():
    Test                = 0
    Contract            = 1
    DefHotel            = 2
    DefMeal             = 3
    DefRoom             = 4
    RatePlan            = 5
    RateBase            = 6
    RateRule            = 7
    RateSupplement      = 8
    RateDiscount        = 9
    RateDiscountGroup   = 10
    Restriction         = 11
    QueryTransform      = 12
    RateCnx             = 13
    Tax                 = 14
    RateMarkup          = 15
    AvlAlloc            = 16
    AvlState            = 17
    AvlInv              = 18
    RateDiscountCat     = 19
    RateSupplementalCat = 20
    Config              = 21
    CustomInfo          = 22
    Other               = 23
