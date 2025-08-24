from openai import OpenAI
from dotenv import load_dotenv
from sql import sauvegarder_echange, chercher_reponse_existante
from datetime import datetime
import os

# Charger les variables d'environnement
load_dotenv()

# Créer le client OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Définir le prompt
prompt = "Write a one-sentence bedtime story about a unicorn."

# Vérifier si une réponse existe déjà pour ce prompt
reponse_existante = chercher_reponse_existante(prompt)

if reponse_existante:
    print("Réponse déjà enregistrée :")
    print(reponse_existante)
else:
    try:
        # Appeler l'API
        response = client.chat.completions.create(
            model="openai/gpt-4.1-nano-2025-04-14",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        # Extraire le texte de la réponse
        response_text = response.choices[0].message.content

        # Afficher la réponse
        print(response_text)

        # Enregistrer dans la base
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = "success"
        sauvegarder_echange(prompt, response_text, timestamp, status)

    except Exception as e:
        print("Erreur lors de l'appel à l'API :", e)

        # Enregistrer l'erreur dans la base
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = "error"
        sauvegarder_echange(prompt, str(e), timestamp, status)
