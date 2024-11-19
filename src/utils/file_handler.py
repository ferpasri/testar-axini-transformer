def read_json_file(filepath):
    import json
    with open(filepath, 'r') as f:
        return json.load(f)

def write_dsl_file(filepath, content):
    with open(filepath, 'w') as f:
        f.write(content)
