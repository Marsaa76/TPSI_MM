import json
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
    dati = load_json("EX_3_Health.json")
    schema = load_json("EX_3_Health_schema.json")
    
    validi, non_validi = validate_misurazioni(dati, schema)
    
    print("\nMisurazioni valide:")
    for m in validi:
        print(f" - Tipo: {m['tipo']}, Valore: {m['valore']}")
    
    print("\nMisurazioni NON valide:")
    for m in non_validi:
        print(f" - Tipo: {m.get('tipo', 'Mancante')}")
    
    output_data = {"misurazioni": validi}
    with open("EX_3_Health_output.json", "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=4, ensure_ascii=False)
    print(f"\nRecord validi salvati in '{EX_3_Health_output.json}'.")

if __name__ == "__main__":
    main()
