import json
import os
import jsonschema
from jsonschema import validate, ValidationError

def validate_pacchi(data, schema):
    validi = []
    non_validi = []
    
    for idx, tappa in enumerate(data.get("spedizione", []), start=1):
        try:
            validate(instance=tappa, schema=schema["properties"]["spedizione"]["items"])
            validi.append(tappa)
        except ValidationError as e:
            print(f"Errore nella tappa {idx}: {e.message}")
            non_validi.append(tappa)
    
    return validi, non_validi

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    json_file_path = os.path.join(script_dir, "EX_2_Tracking.json")
    schema_file_path = os.path.join(script_dir, "EX_2_Tracking_schema.json")
    output_file_path = os.path.join(script_dir, "EX_2_Tracking_output.json")

    validi, non_validi = validate_pacchi(json_file_path, schema_file_path)
    
    print("\nTappe valide:")
    for tappa in validi:
        print(f" - Luogo: {tappa['luogo']}, Data e ora: {tappa['data_ora']}")
    
    print("\nTappe NON valide:")
    for tappa in non_validi:
        print(f" - Luogo: {tappa.get('luogo', 'Mancante')}")
    
    output_data = {"spedizione": validi}
    with open(output_file_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=4, ensure_ascii=False)
    print(f"\nRecord validi salvati in '{output_file_path}'.")

if __name__ == "__main__":
    main()
