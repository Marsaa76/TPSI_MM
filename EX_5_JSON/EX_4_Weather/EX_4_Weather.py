import json
import jsonschema
from jsonschema import validate, ValidationError

def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def validate_rilevazioni(data, schema):
    validi = []
    non_validi = []
    
    for idx, record in enumerate(data.get("rilevazioni", []), start=1):
        try:
            validate(instance=record, schema=schema["properties"]["rilevazioni"]["items"])
            validi.append(record)
        except ValidationError as e:
            print(f"Errore nella rilevazione {idx}: {e.message}")
            non_validi.append(record)
    
    return validi, non_validi

def main():
    dati = load_json("EX_4_Weather.json")
    schema = load_json("EX_4_Weather_schema.json")
    
    validi, non_validi = validate_rilevazioni(dati, schema)
    
    print("\nRilevazioni valide:")
    for r in validi:
        print(f" - Data/ora: {r['data_ora']}, Temperatura: {r['temperatura']}°C")
    
    print("\nRilevazioni NON valide:")
    for r in non_validi:
        print(f" - Data/ora: {r.get('data_ora', 'Mancante')}")
    
    output_data = {"rilevazioni": validi}
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=4, ensure_ascii=False)
    print(f"\nRecord validi salvati in '{EX_4_Weather_output.json}'.")

if __name__ == "__main__":
    main()
