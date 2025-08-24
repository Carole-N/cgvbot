# 📁 sql.py
import mysql.connector as mysql
from datetime import datetime

def sauvegarder_echange(prompt, response, timestamp, status):
    connexion = mysql.connect(
        host='db',
        user='root',
        password='example',
        database='cgvbot',
        port=3306
    )

    curseur = connexion.cursor()
    requete = """
        INSERT INTO logs (
        prompt, response, timestamp, status)
        VALUES (%s, %s, %s, %s)
    """
    valeurs = (prompt, response, timestamp, status)
    curseur.execute(requete, valeurs)
    connexion.commit()

    curseur.close()
    connexion.close()

def chercher_reponse_existante(prompt):
    connexion = mysql.connect(
        host='db',
        user='root',
        password='example',
        database='cgvbot',
        port=3306
    )

    curseur = connexion.cursor()
    requete = """
        SELECT response FROM logs
        WHERE prompt = %s
        ORDER BY timestamp DESC
        LIMIT 1
    """
    curseur.execute(requete, (prompt,))
    resultat = curseur.fetchone()

    curseur.close()
    connexion.close()

    if resultat:
        return resultat[0]
    else:
        return None
