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

`python main.py example_parabank.json axini_parabank_model.txt`

# Test execution

`cd tests`

`pytest test_dsl_transformer.py`