import sys
from utils.file_handler import read_json_file, write_dsl_file
from transformer.json_to_dsl import generate_dsl_from_json

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_json_file> <output_dsl_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Read JSON, generate DSL, and save to file
    json_data = read_json_file(input_file)
    dsl_output = generate_dsl_from_json(json_data)
    write_dsl_file(output_file, dsl_output)
    print(f"DSL file generated at {output_file}")

if __name__ == "__main__":
    main()
