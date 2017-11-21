import sublime
import sublime_plugin
try:
  from .subz_tools_subl import *
except ValueError:
  from subz_tools_subl import *

class SubzInsertSectionAvlAllocCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[AVL.ALLOC]
| room | rules | iclass | inv_id |
|------|-------|--------|--------|
* Caution: this is under development *
|      |       |        |        |
""")

class SubzInsertSectionAvlInv(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[AVL.INV]
| dates | iclass | id |
|-------|--------|----|
* Caution: this is under development *
|       |        |    |

""")

class SubzInsertSectionAvlState(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[AVL.STATE]
| dates | room | rules | status | count | remark |
|-------|------|-------|--------|-------|--------|
|       |      |       |        |       |        |

""")

class SubzInsertSectionContractFull(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[CONTRACT]
id = "TEST"
name = "TEST"
currency = "EUR"
active = true
hotel_code = "TEST"
city = "TEST"
booking = "20000101:29991210"
markets = ["TEST"]
clients = ["TEST"]
brands = ["TEST"]
destinations = ["TEST"]
source = "TEST"
update_mode = "W"
channel = "TEST"
channel_hotel_code = "TEST"
scrape = false
revision = 0
type = "D"
timezone = "CET"
missing_avl_eq_to_no_avl = false

""")

class SubzInsertSectionContractMinimal(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[CONTRACT]
id = "TEST"
currency = "EUR"
hotel_code = "TEST"
city = "TEST"
destinations = ["TEST"]
source = "TEST"

""")

class SubzInsertSectionDefHotel(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[DEF.HOTEL]
| hotel_code | name | category | country | city | resort | destination_name | city_name | postal | street | lat | lon | json |
|------------|------|----------|---------|------|--------|------------------|-----------|--------|--------|-----|-----|------|
|            |      |          |         |      |        |                  |           |        |        |     |     |      |

""")

class SubzInsertSectionDefMeal(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[DEF.MEAL]
| meal | description | group |
|------|-------------|-------|
|      |             |       |

""")


class SubzInsertSectionDefRoom(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[DEF.ROOM]
| room | description | occupancy | group | facilities | base_meal | props |
|------|-------------|-----------|-------|------------|-----------|-------|
|      |             |           |       |            |           |       |

""")

class SubzInsertSectionQueryTransform(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[QUERY.TRANSFORM]
|  occupancy   | func | args |
|--------------|------|------|
| A*C*         | ASC  |      |
| C1[0:1]      | DEL  |      |
| A1C1[14:255] | SUB  | A2   |

""")

class SubzInsertSectionRateBase(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[RATE.BASE]
| dates | charge | room | occupancy | meal | amount | query | rate_plan | id |
|-------|--------|------|-----------|------|--------|-------|-----------|----|
|       |        |      |           |      |        |       |           |    |

""")

class SubzInsertSectionRateCnx(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[RATE.CNX]
| arrival | time_to_arrival | rate_rules | query_rules | rate_plan | applicative | cost | remark | id |
|---------|-----------------|------------|-------------|-----------|-------------|------|--------|----|
|         |                 |            |             |           |             |      |        |    |

""")

class SubzInsertSectionRateDiscount(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[RATE.DISCOUNT]
| dates | query | rate | component | occupancy | applicative | reduction | remark | rate_plan | id |
|-------|-------|------|-----------|-----------|-------------|-----------|--------|-----------|----|
|       |       |      |           |           |             |           |        |           |  0 |

""")

class SubzInsertSectionRateDiscountGroup(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[RATE.DISCOUNT_GROUP]
| combine |
|---------|
|         |

""")

class SubzInsertSectionRatePlan(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[RATE.PLAN]
| dates | code | description | rooms | query | props |
|-------|------|-------------|-------|-------|-------|
|       |      |             |       |       |       |

""")

class SubzInsertSectionRateRule(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[RATE.RULE]
| dates | room | occupancy | meal | rules | rate_plan |
|-------|------|-----------|------|-------|-----------|
|       |      |           |      |       |           |

""")

class SubzInsertSectionRateSupplement(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[RATE.SUPPLEMENT]
| dates | query | rate | component | occupancy | kind | charge | calc | remark | rate_plan | id |
|-------|-------|------|-----------|-----------|------|--------|------|--------|-----------|----|
|       |       |      |           |           |      |        |      |        |           |    |

""")

class SubzInsertSectionRateTax(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[RATE.TAX]
| dates | rate | occupancy | charge_type | charge_amt | charge_max | remark | priority | id |
|-------|------|-----------|-------------|------------|------------|--------|----------|----|
|       |      |           |             |            |            |        |        0 |  0 |

""")

class SubzInsertSectionRestriction(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[RESTRICTION]
| room | occupancy | meal | rate_plan | forbid | remark | id |
|------|-----------|------|-----------|--------|--------|----|
|      |           |      |           |        |        |    |

""")

class SubzInsertSectionTest(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[TEST]
| query | total | comment |
|-------|-------|---------|
|       |       |         |

""")

