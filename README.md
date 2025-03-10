# testar-axini-transformer

# Setup (windows_start.bat)
reate a Python virtual environment
`python -m venv venv`

Activate the virtual environment
`call venv\Scripts\activate`

Install dependencies from requirements.txt
`pip install -r requirements.txt`

# Usage example

`cd src`

then  

`python main.py state example_parabank.json axini_parabank_state_choice.txt`  

or  

`python main.py behavior example_parabank.json axini_parabank_behavior.txt`  

# Test execution

`cd tests`  

then  

`pytest test_dsl_transformer_state_choice.py`  

or  

`pytest test_dsl_transformer_behavior.py`  