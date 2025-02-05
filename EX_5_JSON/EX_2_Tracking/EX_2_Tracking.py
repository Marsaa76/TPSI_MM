import json
import jsonschema
from jsonschema import validate, ValidationError

DATA_FILE = "tracciamento_pacchi.json"
SCHEMA_FILE = "schema_tracciamento_pacchi.json"
OUTPUT_FILE = "tracciamento_pacchi_valid.json"

def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

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
    dati = load_json(DATA_FILE)
    schema = load_json(SCHEMA_FILE)
    
    validi, non_validi = validate_pacchi(dati, schema)
    
    print("\nTappe valide:")
    for tappa in validi:
        print(f" - Luogo: {tappa['luogo']}, Data e ora: {tappa['data_ora']}")
    
    print("\nTappe NON valide:")
    for tappa in non_validi:
        print(f" - Luogo: {tappa.get('luogo', 'Mancante')}")
    
    output_data = {"spedizione": validi}
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=4, ensure_ascii=False)
    print(f"\nRecord validi salvati in '{OUTPUT_FILE}'.")

if __name__ == "__main__":
    main()
