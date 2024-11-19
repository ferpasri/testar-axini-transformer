import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import json
from transformer.json_to_dsl import generate_dsl_from_json

def test_generate_dsl():
    # Example JSON input
    example_json = {
  "initial_url": "https://para.testar.org/parabank/index.htm",
  "initial_title": "ParaBank | Welcome | Online Banking",
  "states": [
    {
      "id": "SA10acdwe54e3379749613",
      "title": "ParaBank | Welcome | Online Banking"
    },
    {
      "id": "SA1ec8jbr52d1987302593",
      "title": "ParaBank | Site Map"
    }
  ],
  "actions": [
    {
      "id": "WAc7jjlv82505510887",
      "desc": "Left Click at 'Site Map'",
      "webHref": "sitemap.htm"
    },
    {
      "id": "WAfqiihs71281549880",
      "desc": "Left Click at 'Home'",
      "webHref": "index.htm"
    }
  ],
  "transitions": [
    {
      "sourceStateId": "SA10acdwe54e3379749613",
      "actionId": "WAc7jjlv82505510887",
      "targetStateId": "SA1ec8jbr52d1987302593"
    },
    {
      "sourceStateId": "SA1ec8jbr52d1987302593",
      "actionId": "WAfqiihs71281549880",
      "targetStateId": "SA10acdwe54e3379749613"
    }
  ]
}

    # Expected DSL output
    expected_dsl = """
timeout 30.0
external 'extern'

def Left_Click_at_Site_Map()
  receive 'click_link',
  constraint: %(selector == "a[href*='sitemap.htm']")
  send 'page_title',
  constraint: %(_title == "ParaBank | Site Map")
end

def Left_Click_at_Home()
  receive 'click_link',
  constraint: %(selector == "a[href*='index.htm']")
  send 'page_title',
  constraint: %(_title == "ParaBank | Welcome | Online Banking")
end

process('testar'){

  channel('extern') {
    stimulus 'visit', '_url' => :string
    stimulus 'click_link', 'selector' => :string
    response 'page_title', '_title' => :string, '_url' => :string
  }

  var 'initial_url', :string, 'https://para.testar.org/parabank/index.htm'

  state 'start'
  receive 'visit',
  constraint: "_url == initial_url"
  send 'page_title',
  constraint: %(_title == "ParaBank | Welcome | Online Banking")
  goto 'ParaBank | Welcome | Online Banking'

  state 'ParaBank | Welcome | Online Banking'
  Left_Click_at_Site_Map()
  goto 'ParaBank | Site Map'

  state 'ParaBank | Site Map'
  Left_Click_at_Home()
  goto 'ParaBank | Welcome | Online Banking'

}
"""

    # Run the transformer
    generated_dsl = generate_dsl_from_json(example_json)

    # Assert output matches expected
    assert generated_dsl.strip() == expected_dsl.strip()
