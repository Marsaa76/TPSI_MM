import json
import jsonschema
from jsonschema import validate, ValidationError


def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def compute_esito(risultato, intervallo):
    """Calcola l'esito confrontando il risultato con l'intervallo di riferimento."""
    if risultato < intervallo["min"]:
        return "troppo basso"
    elif risultato > intervallo["max"]:
        return "valore elevato"
    else:
        return "ok"

def validate_esami(data, schema):
    validi = []
    non_validi = []
    
    for idx, esame in enumerate(data.get("esami", []), start=1):
        try:
            # Validazione iniziale tramite schema
            validate(instance=esame, schema=schema["properties"]["esami"]["items"])
            # Ricalcola l'esito (opzionale: qui si verifica la correttezza dei dati)
            esame["esito"] = compute_esito(esame["risultato"], esame["intervallo"])
            validi.append(esame)
        except ValidationError as e:
            print(f"Errore nel record esame {idx}: {e.message}")
            non_validi.append(esame)
    
    return validi, non_validi

def main():
    dati = load_json("EX_5_Medical_Results.json")
    schema = load_json("EX_5_Medical_Results_schema.json")
    
    validi, non_validi = validate_esami(dati, schema)
    
    print("\nEsami validi:")
    for esame in validi:
        print(f" - {esame['nome']} {esame['cognome']} ({esame['analisi']}): {esame['risultato']} {esame['unita']} => {esame['esito']}")
    
    print("\nEsami NON validi:")
    for esame in non_validi:
        print(f" - {esame.get('nome', 'Nome mancante')} {esame.get('cognome', 'Cognome mancante')}")
    
    output_data = {"esami": validi}
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=4, ensure_ascii=False)
    print(f"\nRecord validi salvati in '{EX_5_Medical_Results_output.json}'.")

if __name__ == "__main__":
    main()
