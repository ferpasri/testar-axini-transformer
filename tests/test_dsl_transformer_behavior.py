import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import json
from transformer_behavior.json_to_dsl import generate_dsl_from_json

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
      "AbstractID": "SAz81bbj4032384742328",
      "WebTitle": "ParaBank | Register for Free Online Account Access"
    },
    {
      "AbstractID": "SA7nl9iz54d629734882",
      "WebTitle": "ParaBank | Services"
    },
    {
      "AbstractID": "SA1ds4me050c2709856404",
      "WebTitle": "ParaBank | Customer Care"
    },
    {
      "AbstractID": "SA1b437g4462809859715",
      "WebTitle": "ParaBank | About Us"
    },
    {
      "AbstractID": "SAh2esgu54d4104967621",
      "WebTitle": "ParaBank | Welcome | Online Banking"
    },
    {
      "AbstractID": "SAxsp8ho4043437916393",
      "WebTitle": "ParaBank | Customer Lookup"
    }
  ],
  "ConcreteAction": [
    {
      "AbstractID": "WAins0hp121499597695",
      "Desc": "Left Click at 'Forgot login info?'",
      "WebHref": "lookup.htm"
    },
    {
      "AbstractID": "WA1oonxs382794398274",
      "Desc": "Left Click at 'Register'",
      "WebHref": "register.htm"
    },
    {
      "AbstractID": "WA1wrmn41909853392",
      "Desc": "Left Click at 'home'",
      "WebHref": "index.htm"
    },
    {
      "AbstractID": "WAnvmsfy82319745855",
      "Desc": "Left Click at 'Services'",
      "WebHref": "services.htm"
    },
    {
      "AbstractID": "WAza3lr2a124909007",
      "Desc": "Left Click at 'Contact Us'",
      "WebHref": "contact.htm"
    },
    {
      "AbstractID": "WAfqiihs71281549880",
      "Desc": "Left Click at 'contact'",
      "WebHref": "contact.htm"
    },
    {
      "AbstractID": "WAc7jjlv82505510887",
      "Desc": "Left Click at 'Site Map'",
      "WebHref": "sitemap.htm"
    },
    {
      "AbstractID": "WA1j4zgt53052675811",
      "Desc": "Left Click at 'about'",
      "WebHref": "about.htm"
    },
    {
      "AbstractID": "WAruktht82256300634",
      "Desc": "Left Click at 'About Us'",
      "WebHref": "about.htm"
    },
    {
      "AbstractID": "WA1cc1r43521422318",
      "Desc": "Left Click at 'Home'",
      "WebHref": "index.htm"
    },
    {
      "AbstractID": "WAdqva8v91474786502",
      "Desc": "Left Click at 'Read More'",
      "WebHref": "services.htm"
    }
  ],
  "ConcreteTransitions": [
    {
      "Source": "SA1ec8jbr52d1987302593",
      "Target": "SAxsp8ho4043437916393",
      "Action": "WAins0hp121499597695"
    },
    {
      "Source": "SA1ec8jbr52d1987302593",
      "Target": "SAz81bbj4032384742328",
      "Action": "WA1oonxs382794398274"
    },
    {
      "Source": "SA1ec8jbr52d1987302593",
      "Target": "SAh2esgu54d4104967621",
      "Action": "WA1wrmn41909853392"
    },
    {
      "Source": "SA1ec8jbr52d1987302593",
      "Target": "SA7nl9iz54d629734882",
      "Action": "WAnvmsfy82319745855"
    },
    {
      "Source": "SA1ec8jbr52d1987302593",
      "Target": "SA1ds4me050c2709856404",
      "Action": "WAza3lr2a124909007"
    },
    {
      "Source": "SA1ec8jbr52d1987302593",
      "Target": "SA1ds4me050c2709856404",
      "Action": "WAfqiihs71281549880"
    },
    {
      "Source": "SA1ec8jbr52d1987302593",
      "Target": "SA1ec8jbr52d1987302593",
      "Action": "WAc7jjlv82505510887"
    },
    {
      "Source": "SA1ec8jbr52d1987302593",
      "Target": "SA1b437g4462809859715",
      "Action": "WA1j4zgt53052675811"
    },
    {
      "Source": "SA1ec8jbr52d1987302593",
      "Target": "SA1b437g4462809859715",
      "Action": "WAruktht82256300634"
    },
    {
      "Source": "SA1ec8jbr52d1987302593",
      "Target": "SAh2esgu54d4104967621",
      "Action": "WA1cc1r43521422318"
    },
    {
      "Source": "SAxsp8ho4043437916393",
      "Target": "SAxsp8ho4043437916393",
      "Action": "WAins0hp121499597695"
    },
    {
      "Source": "SAxsp8ho4043437916393",
      "Target": "SAh2esgu54d4104967621",
      "Action": "WA1wrmn41909853392"
    },
    {
      "Source": "SAxsp8ho4043437916393",
      "Target": "SA1b437g4462809859715",
      "Action": "WA1j4zgt53052675811"
    },
    {
      "Source": "SAxsp8ho4043437916393",
      "Target": "SA1ds4me050c2709856404",
      "Action": "WAza3lr2a124909007"
    },
    {
      "Source": "SAxsp8ho4043437916393",
      "Target": "SA7nl9iz54d629734882",
      "Action": "WAnvmsfy82319745855"
    },
    {
      "Source": "SAxsp8ho4043437916393",
      "Target": "SA1ds4me050c2709856404",
      "Action": "WAfqiihs71281549880"
    },
    {
      "Source": "SAxsp8ho4043437916393",
      "Target": "SAh2esgu54d4104967621",
      "Action": "WA1cc1r43521422318"
    },
    {
      "Source": "SAxsp8ho4043437916393",
      "Target": "SA1b437g4462809859715",
      "Action": "WAruktht82256300634"
    },
    {
      "Source": "SAxsp8ho4043437916393",
      "Target": "SAz81bbj4032384742328",
      "Action": "WA1oonxs382794398274"
    },
    {
      "Source": "SAxsp8ho4043437916393",
      "Target": "SA1ec8jbr52d1987302593",
      "Action": "WAc7jjlv82505510887"
    },
    {
      "Source": "SA1b437g4462809859715",
      "Target": "SAh2esgu54d4104967621",
      "Action": "WA1cc1r43521422318"
    },
    {
      "Source": "SA1b437g4462809859715",
      "Target": "SA1b437g4462809859715",
      "Action": "WA1j4zgt53052675811"
    },
    {
      "Source": "SA1b437g4462809859715",
      "Target": "SA7nl9iz54d629734882",
      "Action": "WAnvmsfy82319745855"
    },
    {
      "Source": "SA1b437g4462809859715",
      "Target": "SA1b437g4462809859715",
      "Action": "WAruktht82256300634"
    },
    {
      "Source": "SA1b437g4462809859715",
      "Target": "SA1ds4me050c2709856404",
      "Action": "WAza3lr2a124909007"
    },
    {
      "Source": "SA1b437g4462809859715",
      "Target": "SA1ec8jbr52d1987302593",
      "Action": "WAc7jjlv82505510887"
    },
    {
      "Source": "SA1b437g4462809859715",
      "Target": "SAz81bbj4032384742328",
      "Action": "WA1oonxs382794398274"
    },
    {
      "Source": "SA1b437g4462809859715",
      "Target": "SA1ds4me050c2709856404",
      "Action": "WAfqiihs71281549880"
    },
    {
      "Source": "SA1b437g4462809859715",
      "Target": "SAxsp8ho4043437916393",
      "Action": "WAins0hp121499597695"
    },
    {
      "Source": "SA1b437g4462809859715",
      "Target": "SAh2esgu54d4104967621",
      "Action": "WA1wrmn41909853392"
    },
    {
      "Source": "SA1ds4me050c2709856404",
      "Target": "SA1ec8jbr52d1987302593",
      "Action": "WAc7jjlv82505510887"
    },
    {
      "Source": "SA1ds4me050c2709856404",
      "Target": "SA1ds4me050c2709856404",
      "Action": "WAza3lr2a124909007"
    },
    {
      "Source": "SA1ds4me050c2709856404",
      "Target": "SA1b437g4462809859715",
      "Action": "WA1j4zgt53052675811"
    },
    {
      "Source": "SA1ds4me050c2709856404",
      "Target": "SAh2esgu54d4104967621",
      "Action": "WA1wrmn41909853392"
    },
    {
      "Source": "SA1ds4me050c2709856404",
      "Target": "SAxsp8ho4043437916393",
      "Action": "WAins0hp121499597695"
    },
    {
      "Source": "SA1ds4me050c2709856404",
      "Target": "SA1ds4me050c2709856404",
      "Action": "WAfqiihs71281549880"
    },
    {
      "Source": "SA1ds4me050c2709856404",
      "Target": "SAz81bbj4032384742328",
      "Action": "WA1oonxs382794398274"
    },
    {
      "Source": "SA1ds4me050c2709856404",
      "Target": "SAh2esgu54d4104967621",
      "Action": "WA1cc1r43521422318"
    },
    {
      "Source": "SA1ds4me050c2709856404",
      "Target": "SA1b437g4462809859715",
      "Action": "WAruktht82256300634"
    },
    {
      "Source": "SA1ds4me050c2709856404",
      "Target": "SA7nl9iz54d629734882",
      "Action": "WAnvmsfy82319745855"
    },
    {
      "Source": "SAz81bbj4032384742328",
      "Target": "SA7nl9iz54d629734882",
      "Action": "WAnvmsfy82319745855"
    },
    {
      "Source": "SAz81bbj4032384742328",
      "Target": "SA1ec8jbr52d1987302593",
      "Action": "WAc7jjlv82505510887"
    },
    {
      "Source": "SAz81bbj4032384742328",
      "Target": "SAh2esgu54d4104967621",
      "Action": "WA1wrmn41909853392"
    },
    {
      "Source": "SAz81bbj4032384742328",
      "Target": "SA1b437g4462809859715",
      "Action": "WA1j4zgt53052675811"
    },
    {
      "Source": "SAz81bbj4032384742328",
      "Target": "SAxsp8ho4043437916393",
      "Action": "WAins0hp121499597695"
    },
    {
      "Source": "SAz81bbj4032384742328",
      "Target": "SAh2esgu54d4104967621",
      "Action": "WA1cc1r43521422318"
    },
    {
      "Source": "SAz81bbj4032384742328",
      "Target": "SAz81bbj4032384742328",
      "Action": "WA1oonxs382794398274"
    },
    {
      "Source": "SAz81bbj4032384742328",
      "Target": "SA1ds4me050c2709856404",
      "Action": "WAfqiihs71281549880"
    },
    {
      "Source": "SAz81bbj4032384742328",
      "Target": "SA1b437g4462809859715",
      "Action": "WAruktht82256300634"
    },
    {
      "Source": "SAz81bbj4032384742328",
      "Target": "SA1ds4me050c2709856404",
      "Action": "WAza3lr2a124909007"
    },
    {
      "Source": "SA7nl9iz54d629734882",
      "Target": "SAxsp8ho4043437916393",
      "Action": "WAins0hp121499597695"
    },
    {
      "Source": "SA7nl9iz54d629734882",
      "Target": "SAh2esgu54d4104967621",
      "Action": "WA1wrmn41909853392"
    },
    {
      "Source": "SA7nl9iz54d629734882",
      "Target": "SA1ds4me050c2709856404",
      "Action": "WAfqiihs71281549880"
    },
    {
      "Source": "SA7nl9iz54d629734882",
      "Target": "SA1ec8jbr52d1987302593",
      "Action": "WAc7jjlv82505510887"
    },
    {
      "Source": "SA7nl9iz54d629734882",
      "Target": "SA1b437g4462809859715",
      "Action": "WAruktht82256300634"
    },
    {
      "Source": "SA7nl9iz54d629734882",
      "Target": "SA1b437g4462809859715",
      "Action": "WA1j4zgt53052675811"
    },
    {
      "Source": "SA7nl9iz54d629734882",
      "Target": "SAz81bbj4032384742328",
      "Action": "WA1oonxs382794398274"
    },
    {
      "Source": "SA7nl9iz54d629734882",
      "Target": "SA1ds4me050c2709856404",
      "Action": "WAza3lr2a124909007"
    },
    {
      "Source": "SA7nl9iz54d629734882",
      "Target": "SAh2esgu54d4104967621",
      "Action": "WA1cc1r43521422318"
    },
    {
      "Source": "SA7nl9iz54d629734882",
      "Target": "SA7nl9iz54d629734882",
      "Action": "WAnvmsfy82319745855"
    },
    {
      "Source": "SAh2esgu54d4104967621",
      "Target": "SA1ds4me050c2709856404",
      "Action": "WAza3lr2a124909007"
    },
    {
      "Source": "SAh2esgu54d4104967621",
      "Target": "SAh2esgu54d4104967621",
      "Action": "WA1wrmn41909853392"
    },
    {
      "Source": "SAh2esgu54d4104967621",
      "Target": "SA1b437g4462809859715",
      "Action": "WA1j4zgt53052675811"
    },
    {
      "Source": "SAh2esgu54d4104967621",
      "Target": "SA1ds4me050c2709856404",
      "Action": "WAfqiihs71281549880"
    },
    {
      "Source": "SAh2esgu54d4104967621",
      "Target": "SA7nl9iz54d629734882",
      "Action": "WAdqva8v91474786502"
    },
    {
      "Source": "SAh2esgu54d4104967621",
      "Target": "SAxsp8ho4043437916393",
      "Action": "WAins0hp121499597695"
    },
    {
      "Source": "SAh2esgu54d4104967621",
      "Target": "SA1ec8jbr52d1987302593",
      "Action": "WAc7jjlv82505510887"
    },
    {
      "Source": "SAh2esgu54d4104967621",
      "Target": "SA1b437g4462809859715",
      "Action": "WAruktht82256300634"
    },
    {
      "Source": "SAh2esgu54d4104967621",
      "Target": "SAz81bbj4032384742328",
      "Action": "WA1oonxs382794398274"
    },
    {
      "Source": "SAh2esgu54d4104967621",
      "Target": "SA7nl9iz54d629734882",
      "Action": "WAnvmsfy82319745855"
    },
    {
      "Source": "SAh2esgu54d4104967621",
      "Target": "SAh2esgu54d4104967621",
      "Action": "WA1cc1r43521422318"
    }
  ]
}

    # Expected DSL output
    expected_dsl = """
timeout 10.0
external 'extern'

def Left_Click_at_Forgot_login_info?()
  receive 'click_link', constraint: %(selector == "a[href*='lookup.htm']")
  send 'page_title', constraint: %(_title == "ParaBank | Customer Lookup")
end

def Left_Click_at_Register()
  receive 'click_link', constraint: %(selector == "a[href*='register.htm']")
  send 'page_title', constraint: %(_title == "ParaBank | Register for Free Online Account Access")
end

def Left_Click_at_home()
  receive 'click_link', constraint: %(selector == "a[href*='index.htm']")
  send 'page_title', constraint: %(_title == "ParaBank | Welcome | Online Banking")
end

def Left_Click_at_Services()
  receive 'click_link', constraint: %(selector == "a[href*='services.htm']")
  send 'page_title', constraint: %(_title == "ParaBank | Services")
end

def Left_Click_at_Contact_Us()
  receive 'click_link', constraint: %(selector == "a[href*='contact.htm']")
  send 'page_title', constraint: %(_title == "ParaBank | Customer Care")
end

def Left_Click_at_contact()
  receive 'click_link', constraint: %(selector == "a[href*='contact.htm']")
  send 'page_title', constraint: %(_title == "ParaBank | Customer Care")
end

def Left_Click_at_Site_Map()
  receive 'click_link', constraint: %(selector == "a[href*='sitemap.htm']")
  send 'page_title', constraint: %(_title == "ParaBank | Site Map")
end

def Left_Click_at_about()
  receive 'click_link', constraint: %(selector == "a[href*='about.htm']")
  send 'page_title', constraint: %(_title == "ParaBank | About Us")
end

def Left_Click_at_About_Us()
  receive 'click_link', constraint: %(selector == "a[href*='about.htm']")
  send 'page_title', constraint: %(_title == "ParaBank | About Us")
end

def Left_Click_at_Home()
  receive 'click_link', constraint: %(selector == "a[href*='index.htm']")
  send 'page_title', constraint: %(_title == "ParaBank | Welcome | Online Banking")
end

def Left_Click_at_Read_More()
  receive 'click_link', constraint: %(selector == "a[href*='services.htm']")
  send 'page_title', constraint: %(_title == "ParaBank | Services")
end

process('testar') {

  channel('extern') {
    stimulus 'visit', '_url' => :string
    stimulus 'click_link', 'selector' => :string
    response 'page_title', '_title' => :string, '_url' => :string
  }

  behavior('launch') {
    receive 'visit',
    constraint: "_url == initial_url"
    send 'page_title',
    constraint: %(_title == "ParaBank | Welcome | Online Banking")
  }
  behavior('ParaBank | Site Map', :non_terminating) {
    repeat {
      o { Left_Click_at_Forgot_login_info?(); behave_as 'ParaBank | Customer Lookup' }
      o { Left_Click_at_Register(); behave_as 'ParaBank | Register for Free Online Account Access' }
      o { Left_Click_at_home(); behave_as 'ParaBank | Welcome | Online Banking' }
      o { Left_Click_at_Services(); behave_as 'ParaBank | Services' }
      o { Left_Click_at_Contact_Us(); behave_as 'ParaBank | Customer Care' }
      o { Left_Click_at_contact(); behave_as 'ParaBank | Customer Care' }
      o { Left_Click_at_Site_Map(); behave_as 'ParaBank | Site Map' }
      o { Left_Click_at_about(); behave_as 'ParaBank | About Us' }
      o { Left_Click_at_About_Us(); behave_as 'ParaBank | About Us' }
      o { Left_Click_at_Home(); behave_as 'ParaBank | Welcome | Online Banking' }
    }
  }
  behavior('ParaBank | Customer Lookup', :non_terminating) {
    repeat {
      o { Left_Click_at_Forgot_login_info?(); behave_as 'ParaBank | Customer Lookup' }
      o { Left_Click_at_home(); behave_as 'ParaBank | Welcome | Online Banking' }
      o { Left_Click_at_about(); behave_as 'ParaBank | About Us' }
      o { Left_Click_at_Contact_Us(); behave_as 'ParaBank | Customer Care' }
      o { Left_Click_at_Services(); behave_as 'ParaBank | Services' }
      o { Left_Click_at_contact(); behave_as 'ParaBank | Customer Care' }
      o { Left_Click_at_Home(); behave_as 'ParaBank | Welcome | Online Banking' }
      o { Left_Click_at_About_Us(); behave_as 'ParaBank | About Us' }
      o { Left_Click_at_Register(); behave_as 'ParaBank | Register for Free Online Account Access' }
      o { Left_Click_at_Site_Map(); behave_as 'ParaBank | Site Map' }
    }
  }
  behavior('ParaBank | About Us', :non_terminating) {
    repeat {
      o { Left_Click_at_Home(); behave_as 'ParaBank | Welcome | Online Banking' }
      o { Left_Click_at_about(); behave_as 'ParaBank | About Us' }
      o { Left_Click_at_Services(); behave_as 'ParaBank | Services' }
      o { Left_Click_at_About_Us(); behave_as 'ParaBank | About Us' }
      o { Left_Click_at_Contact_Us(); behave_as 'ParaBank | Customer Care' }
      o { Left_Click_at_Site_Map(); behave_as 'ParaBank | Site Map' }
      o { Left_Click_at_Register(); behave_as 'ParaBank | Register for Free Online Account Access' }
      o { Left_Click_at_contact(); behave_as 'ParaBank | Customer Care' }
      o { Left_Click_at_Forgot_login_info?(); behave_as 'ParaBank | Customer Lookup' }
      o { Left_Click_at_home(); behave_as 'ParaBank | Welcome | Online Banking' }
    }
  }
  behavior('ParaBank | Customer Care', :non_terminating) {
    repeat {
      o { Left_Click_at_Site_Map(); behave_as 'ParaBank | Site Map' }
      o { Left_Click_at_Contact_Us(); behave_as 'ParaBank | Customer Care' }
      o { Left_Click_at_about(); behave_as 'ParaBank | About Us' }
      o { Left_Click_at_home(); behave_as 'ParaBank | Welcome | Online Banking' }
      o { Left_Click_at_Forgot_login_info?(); behave_as 'ParaBank | Customer Lookup' }
      o { Left_Click_at_contact(); behave_as 'ParaBank | Customer Care' }
      o { Left_Click_at_Register(); behave_as 'ParaBank | Register for Free Online Account Access' }
      o { Left_Click_at_Home(); behave_as 'ParaBank | Welcome | Online Banking' }
      o { Left_Click_at_About_Us(); behave_as 'ParaBank | About Us' }
      o { Left_Click_at_Services(); behave_as 'ParaBank | Services' }
    }
  }
  behavior('ParaBank | Register for Free Online Account Access', :non_terminating) {
    repeat {
      o { Left_Click_at_Services(); behave_as 'ParaBank | Services' }
      o { Left_Click_at_Site_Map(); behave_as 'ParaBank | Site Map' }
      o { Left_Click_at_home(); behave_as 'ParaBank | Welcome | Online Banking' }
      o { Left_Click_at_about(); behave_as 'ParaBank | About Us' }
      o { Left_Click_at_Forgot_login_info?(); behave_as 'ParaBank | Customer Lookup' }
      o { Left_Click_at_Home(); behave_as 'ParaBank | Welcome | Online Banking' }
      o { Left_Click_at_Register(); behave_as 'ParaBank | Register for Free Online Account Access' }
      o { Left_Click_at_contact(); behave_as 'ParaBank | Customer Care' }
      o { Left_Click_at_About_Us(); behave_as 'ParaBank | About Us' }
      o { Left_Click_at_Contact_Us(); behave_as 'ParaBank | Customer Care' }
    }
  }
  behavior('ParaBank | Services', :non_terminating) {
    repeat {
      o { Left_Click_at_Forgot_login_info?(); behave_as 'ParaBank | Customer Lookup' }
      o { Left_Click_at_home(); behave_as 'ParaBank | Welcome | Online Banking' }
      o { Left_Click_at_contact(); behave_as 'ParaBank | Customer Care' }
      o { Left_Click_at_Site_Map(); behave_as 'ParaBank | Site Map' }
      o { Left_Click_at_About_Us(); behave_as 'ParaBank | About Us' }
      o { Left_Click_at_about(); behave_as 'ParaBank | About Us' }
      o { Left_Click_at_Register(); behave_as 'ParaBank | Register for Free Online Account Access' }
      o { Left_Click_at_Contact_Us(); behave_as 'ParaBank | Customer Care' }
      o { Left_Click_at_Home(); behave_as 'ParaBank | Welcome | Online Banking' }
      o { Left_Click_at_Services(); behave_as 'ParaBank | Services' }
    }
  }
  behavior('ParaBank | Welcome | Online Banking', :non_terminating) {
    repeat {
      o { Left_Click_at_Contact_Us(); behave_as 'ParaBank | Customer Care' }
      o { Left_Click_at_home(); behave_as 'ParaBank | Welcome | Online Banking' }
      o { Left_Click_at_about(); behave_as 'ParaBank | About Us' }
      o { Left_Click_at_contact(); behave_as 'ParaBank | Customer Care' }
      o { Left_Click_at_Read_More(); behave_as 'ParaBank | Services' }
      o { Left_Click_at_Forgot_login_info?(); behave_as 'ParaBank | Customer Lookup' }
      o { Left_Click_at_Site_Map(); behave_as 'ParaBank | Site Map' }
      o { Left_Click_at_About_Us(); behave_as 'ParaBank | About Us' }
      o { Left_Click_at_Register(); behave_as 'ParaBank | Register for Free Online Account Access' }
      o { Left_Click_at_Services(); behave_as 'ParaBank | Services' }
      o { Left_Click_at_Home(); behave_as 'ParaBank | Welcome | Online Banking' }
    }
  }
  var 'initial_url', :string, 'https://para.testar.org/parabank/index.htm'

  call 'launch'
  behave_as 'ParaBank | Welcome | Online Banking'

}
"""

    # Run the transformer
    generated_dsl = generate_dsl_from_json(example_json)

    # Assert output matches expected
    assert generated_dsl.strip() == expected_dsl.strip()
