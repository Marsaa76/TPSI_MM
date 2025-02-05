import json
import os
import jsonschema
from jsonschema import validate, ValidationError

# Percorsi dei file
DATA_FILE = "EX_1_Catalog.json"
SCHEMA_FILE = "EX_1_Catalog_schema.json"
OUTPUT_FILE = "EX_1_Catalog_output.json"

def load_json(file_path):
    """Carica e restituisce il contenuto di un file JSON."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def validate_libri(data, schema):
    """Valida ogni libro e restituisce due liste: validi e non validi."""
    libri_validi = []
    libri_non_validi = []
    
    for idx, libro in enumerate(data.get("libri", []), start=1):
        try:
            validate(instance=libro, schema=schema["properties"]["libri"]["items"])
            libri_validi.append(libro)
        except ValidationError as e:
            print(f"Errore nel record {idx}: {e.message}")
            libri_non_validi.append(libro)
    
    return libri_validi, libri_non_validi

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    json_file_path = os.path.join(script_dir, "EX_1_Catalog.json")
    schema_file_path = os.path.join(script_dir, "EX_1_Catalog_schema.json")
    output_file_path = os.path.join(script_dir, "EX_1_Catalog_output.json")
    
    # Valida i libri
    libri_validi, libri_non_validi = validate_libri(json_file_path, schema_file_path)
    
    print("\nLibri validi:")
    for libro in libri_validi:
        print(f" - {libro['titolo']} di {libro['autore']}")
    
    print("\nLibri NON validi:")
    for libro in libri_non_validi:
        print(f" - {libro.get('titolo', 'Titolo mancante')}")
    
    # Salva i record validi in un nuovo file JSON
    output_data = {"libri": libri_validi}
    with open(output_file_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=4, ensure_ascii=False)
    print(f"\nRecord validi salvati in '{output_file_path}'.")

if __name__ == "__main__":
    main()
