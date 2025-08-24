import os
from openai import OpenAI

OPENAI_TOKEN = os.getenv("OPENAI_API_KEY")  # ← correspond au nom dans .env
OPENAI_FILE_ID = "file-XeZhoJ2DDB5wBX4QtWNuMP"
OPENAI_MODEL = "gpt-4.1-nano-2025-04-14"

client = OpenAI(api_key=OPENAI_TOKEN)

try:
    ft_job = client.fine_tuning.jobs.create(
        training_file=OPENAI_FILE_ID,
        model=OPENAI_MODEL
    )
    print("Fine Tune Job has been created with id", ft_job.id)
except Exception as erreur:
    print("Erreur lors de la création du fine-tuning :", erreur)
