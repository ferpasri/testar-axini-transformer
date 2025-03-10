import sys
from utils.file_handler import read_json_file, write_dsl_file

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <transformer_choice> <input_json_file> <output_dsl_file>")
        print("Transformer choices: state, behavior")
        sys.exit(1)

    transformer_choice = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    # Select the appropriate transformer module
    if transformer_choice == "state":
        from transformer_state_choice.json_to_dsl import generate_dsl_from_json
    elif transformer_choice == "behavior":
        from transformer_behavior.json_to_dsl import generate_dsl_from_json
    else:
        print("Invalid transformer choice! Use 'state' or 'behavior'.")
        sys.exit(1)

    # Read JSON, generate DSL, and save to file
    json_data = read_json_file(input_file)
    dsl_output = generate_dsl_from_json(json_data)
    write_dsl_file(output_file, dsl_output)
    print(f"DSL file generated at {output_file}")

if __name__ == "__main__":
    main()
