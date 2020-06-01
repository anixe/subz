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
| dates | room | rules | status | cnt | remark |
|-------|------|-------|--------|-----|--------|
|       |      |       |        |     |        |

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
markets_excluded = ["pl"]
clients = ["TEST"]
clients_excluded = ["TEST"]
brands = ["TEST"]
destinations = ["TEST"]
source = "TEST"
channel = "TEST"
sales_channel = "TEST"
channel_hotel_code = "TEST"
scrape = false
revision = 0
type = "D"
tz = "CET"
missing_avl_eq_to_no_avl = false
purchase_id = "TEST"
tenant = "test"
source_contract_id = "TEST_123"
parent_id = "TEST_1"
default_meal = "per_room"
product = "hotel"

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

class SubzInsertSectionContractSpo(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[CONTRACT]
parent_id = "TEST_1"
spo_prio = "1"
spo_codes = ["TEST"]

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
| code | description | grp |
|------|-------------|-----|
|      |             |     |

""")


class SubzInsertSectionDefRoom(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[DEF.ROOM]
| code | description | occ | grp | properties | base_meal |
|------|-------------|-----|-----|------------|-----------|
|      |             |     |     |            |           |

""")

class SubzInsertSectionQueryTransform(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[QUERY.TRANSFORM]
|  occupancy   | func | args | rate_rules |
|--------------|------|------|------------|
| A*C*         | ASC  |      |            |
| C1[0:1]      | DEL  |      |            |
| A1C1[14:255] | SUB  | A2   |            |

""")

class SubzInsertSectionRateBase(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[RATE.BASE]
| dates | charge | room | occ | meal | amount | rules | rp | id |
|-------|--------|------|-----|------|--------|-------|----|----|
|       |        |      |     |      |        |       |    |    |

""")

class SubzInsertSectionRateCnx(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[RATE.CNX]
| dates | time | room | rules | rp | applic | calc | remark | id |
|-------|------|------|-------|----|--------|------|--------|----|
|       |      |      |       |    |        |      |        |    |

""")

class SubzInsertSectionRateDiscount(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[RATE.DISCOUNT]
| dates | rules | rate | comp | occ | applic | reduct | remark | rp | id |
|-------|-------|------|------|-----|--------|--------|--------|----|----|
|       |       |      |      |     |        |        |        |    |  0 |

""")

class SubzInsertSectionRateDiscountGroup(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[RATE.DISCOUNT_GROUP]
| disc_id/group_id | group_id | strategy | name |
|------------------|----------|----------|------|
|                  |          |          |      |

""")

class SubzInsertSectionRatePlan(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[RATE.PLAN]
| dates | code | description | rooms | rules | props |
|-------|------|-------------|-------|-------|-------|
|       |      |             |       |       |       |

""")

class SubzInsertSectionRateRule(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[RATE.RULE]
| dates | room | when | meal | rules | rp |
|-------|------|------|------|-------|----|
|       |      |      |      |       |    |

""")

class SubzInsertSectionRateSupplement(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[RATE.SUPPLEMENT]
| dates | rules | rate | comp | occ | kind | chg | calc | remark | rp | id |
|-------|-------|------|------|-----|------|-----|------|--------|----|----|
|       |       |      |      |     |      |     |      |        |    | 0  |

""")

class SubzInsertSectionTax(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[TAX]
| dates | rules | rate | comp | occ | applic | calc | remark | id |
|-------|-------|------|------|-----|--------|------|--------|----|
|       |       |      |      |     |        |      |        |  0 |

""")

class SubzInsertSectionRestriction(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[RESTRICTION]
| room | occupancy | meal | rp | forbid | remark | id |
|------|-----------|------|----|--------|--------|----|
|      |           |      |    |        |        |  0 |

""")

class SubzInsertSectionTest(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[TEST]
| query | total | comment |
|-------|-------|---------|
|       |       |         |

""")

class SubzInsertSectionRateSupplementCat(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[RATE.SUPPLEMENT_CAT]
| cat | id | name |
|-----|----|------|
|     |    |      |

""")

class SubzInsertSectionRateDiscountCat(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[RATE.DISCOUNT_CAT]
| cat | id | name |
|-----|----|------|
|     |    |      |

""")

class SubzInsertSectionConfig(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[CONFIG]
| name | value | remark |
|------|-------|--------|
|      |       |        |

""")

class SubzInsertSectionCustomInfo(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, """[CUSTOM_INFO]
| name | value | remark |
|------|-------|--------|
|      |       |        |

""")
