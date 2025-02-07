import json
import os
import jsonschema
from jsonschema import validate, ValidationError

def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def validate_misurazioni(data, schema):
    validi = []
    non_validi = []
    
    for idx, record in enumerate(data.get("misurazioni", []), start=1):
        try:
            validate(instance=record, schema=schema["properties"]["misurazioni"]["items"])
            validi.append(record)
        except ValidationError as e:
            print(f"Errore nel record {idx}: {e.message}")
            non_validi.append(record)
    
    return validi, non_validi

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    json_file_path = os.path.join(script_dir, "EX_3_Health.json")
    schema_file_path = os.path.join(script_dir, "EX_3_Health_schema.json")
    output_file_path = os.path.join(script_dir, "EX_3_Health_output.json")

    data = load_json(json_file_path)
    schema = load_json(schema_file_path)
    
    validi, non_validi = validate_misurazioni(data, schema)
        
    print("\nMisurazioni valide:")
    for m in validi:
        print(f" - Tipo: {m['tipo']}, Valore: {m['valore']}")
        
    print("\nMisurazioni NON valide:")
    for m in non_validi:
        print(f" - Tipo: {m.get('tipo', 'Mancante')}")
        
    output_data = {"misurazioni": validi}
    with open(output_file_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=4, ensure_ascii=False)
    print(f"\nRecord validi salvati in '{output_file_path}'.")

if __name__ == "__main__":
    main()
