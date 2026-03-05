import json
from main import app  # Import de votre instance "Chef d'Orchestre" FastAPI

def export_schema():
    # On force FastAPI à générer le dictionnaire OpenAPI
    openapi_schema = app.openapi()
    
    # On sauvegarde ce dictionnaire dans le dossier de documentation de Sphinx
    with open("../docs/openapi.json", "w", encoding="utf-8") as f:
        json.dump(openapi_schema, f, indent=2)
        
    print("Schéma OpenAPI exporté avec succès dans docs/openapi.json")

if __name__ == "__main__":
    export_schema()