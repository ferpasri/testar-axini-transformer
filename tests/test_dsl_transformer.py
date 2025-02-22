import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import json
from transformer.json_to_dsl import generate_dsl_from_json

def test_generate_dsl():
    # Example JSON input
    example_json = {
  "InitialUrl": "https://para.testar.org/parabank/index.htm",
  "InitialPage": "ParaBank | Welcome | Online Banking",
  "ConcreteState": [
    {
      "AbstractID": "SA1ec8jbr52d1987302593",
      "WebTitle": "ParaBank | Site Map"
    },
    {
      "AbstractID": "SA1mr9m7y54e4092431614",
      "WebTitle": "ParaBank | Welcome | Online Banking"
    }
  ],
  "ConcreteAction": [
    {
      "AbstractID": "WA1wrmn41909853392",
      "Desc": "Left Click at 'home'",
      "WebHref": "index.htm"
    },
    {
      "AbstractID": "WA1cc1r43521422318",
      "Desc": "Left Click at 'Home'",
      "WebHref": "index.htm"
    },
    {
      "AbstractID": "WAc7jjlv82505510887",
      "Desc": "Left Click at 'Site Map'",
      "WebHref": "sitemap.htm"
    }
  ],
  "ConcreteTransitions": [
    {
      "Source": "SA1ec8jbr52d1987302593",
      "Target": "SA1mr9m7y54e4092431614",
      "Action": "WA1wrmn41909853392"
    },
    {
      "Source": "SA1ec8jbr52d1987302593",
      "Target": "SA1mr9m7y54e4092431614",
      "Action": "WA1cc1r43521422318"
    },
    {
      "Source": "SA1mr9m7y54e4092431614",
      "Target": "SA1mr9m7y54e4092431614",
      "Action": "WA1wrmn41909853392"
    },
    {
      "Source": "SA1mr9m7y54e4092431614",
      "Target": "SA1mr9m7y54e4092431614",
      "Action": "WA1cc1r43521422318"
    },
    {
      "Source": "SA1ec8jbr52d1987302593",
      "Target": "SA1ec8jbr52d1987302593",
      "Action": "WAc7jjlv82505510887"
    },
    {
      "Source": "SA1mr9m7y54e4092431614",
      "Target": "SA1ec8jbr52d1987302593",
      "Action": "WAc7jjlv82505510887"
    }
  ]
}

    # Expected DSL output
    expected_dsl = """
timeout 30.0
external 'extern'

def Left_Click_at_home()
  receive 'click_link',
  constraint: %(selector == "a[href*='index.htm']")
  send 'page_title',
  constraint: %(_title == "ParaBank | Welcome | Online Banking")
end

def Left_Click_at_Home()
  receive 'click_link',
  constraint: %(selector == "a[href*='index.htm']")
  send 'page_title',
  constraint: %(_title == "ParaBank | Welcome | Online Banking")
end

def Left_Click_at_Site_Map()
  receive 'click_link',
  constraint: %(selector == "a[href*='sitemap.htm']")
  send 'page_title',
  constraint: %(_title == "ParaBank | Site Map")
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

  state 'ParaBank | Site Map'
    choice {
      o { Left_Click_at_home(); goto 'ParaBank | Welcome | Online Banking' }
      o { Left_Click_at_Home(); goto 'ParaBank | Welcome | Online Banking' }
      o { Left_Click_at_Site_Map(); goto 'ParaBank | Site Map' }
    }
  state 'ParaBank | Welcome | Online Banking'
    choice {
      o { Left_Click_at_home(); goto 'ParaBank | Welcome | Online Banking' }
      o { Left_Click_at_Home(); goto 'ParaBank | Welcome | Online Banking' }
      o { Left_Click_at_Site_Map(); goto 'ParaBank | Site Map' }
    }
}
"""

    # Run the transformer
    generated_dsl = generate_dsl_from_json(example_json)

    # Assert output matches expected
    assert generated_dsl.strip() == expected_dsl.strip()
