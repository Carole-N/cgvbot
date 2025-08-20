# CGVbot

> Assistant juridique spécialisé dans les Conditions Générales de Vente (CGV), utilisable en ligne de commande. Ce projet a été réalisé dans le cadre d’un exercice pédagogique sur le fine-tuning d’un modèle OpenAI.

---

## Table des matières

1. [Description](#description)
2. [Fonctionnalités](#fonctionnalités)
3. [Pré-requis](#pré-requis)
4. [Technologies et langages](#technologies-et-langages)
5. [Guide d'installation](#guide-dinstallation)
6. [Guide de développement](#guide-de-développement)
7. [Architecture du projet](#architecture-du-projet)
8. [Licence](#licence)
9. [Créateurs du projet](#créateurs-du-projet)

---

## Description

CGVbot est un assistant conversationnel conçu pour répondre automatiquement aux questions juridiques relatives aux Conditions Générales de Vente (paiement, rétractation, livraison, garantie, données personnelles). Il s’appuie sur un modèle GPT-4.1 nano fine-tuné et fonctionne en ligne de commande :

1. L'utilisateur pose une question via la console (`app.py`)  
2. Le pré-prompt métier est injecté dans la requête  
3. La requête est envoyée au modèle fine-tuné via l'API OpenAI  
4. La réponse est affichée dans la console  
5. L'échange est enregistré dans la base SQLite  
6. Adminer permet de consulter les logs via le conteneur Docker

---

## Fonctionnalités

- Chargement d’un pré-prompt métier  
- Appel à un modèle fine-tuné sur des CGV au format `.jsonl`  
- Affichage des réponses dans la console Python  
- Enregistrement des échanges dans une base SQLite  
- Déploiement dans un conteneur Docker avec Adminer pour visualisation  

---

## Pré-requis

- Python 3.10+  
- Accès à l’API OpenAI avec droits de fine-tuning  
- Docker installé et configuré  
- Git installé  

---

## Technologies et langages

| Outil / Langage     | Usage                                  |
|---------------------|----------------------------------------|
| Python              | Backend et logique métier              |
| OpenAI API          | Fine-tuning et génération de réponses  |
| SQLite              | Stockage des logs                      |
| Docker + Adminer    | Conteneurisation et visualisation DB   |
| JSONL               | Format d’entraînement du modèle        |
| Git / GitHub        | Versioning et dépôt du projet          |

---

## Guide d'installation

```bash
# Création de l'environnement virtuel
python3 -m venv .venv
source .venv/bin/activate

# Installation des dépendances
pip install -r requirements.txt

# Lancement de l'application
python app.py
```

---

## Guide de développement

- `app.py` . logique principale du chatbot  
- `sql.py` . gestion des interactions avec la base SQLite  
- `config.json` . paramétrage du pré-prompt métier  
- `train.jsonl` . exemples utilisés pour le fine-tuning  
- Table `logs` . enregistrement des prompts et réponses  

---

## Architecture du projet

Le projet CGVbot repose sur une architecture modulaire articulée autour de quatre composants principaux :

```
+---------------------+
|     app.py          | <-- Interface console utilisateur
+---------------------+
          |
          v
+---------------------+        +---------------------+
|   OpenAI API        |<-----> |   train.jsonl       | <-- Données d'entraînement
+---------------------+        +---------------------+
          |
          v
+---------------------+
|   Pré-prompt métier | <-- Chargé depuis config.json
+---------------------+
          |
          v
+---------------------+
|   SQLite (logs)     | <-- Stockage des échanges
+---------------------+
          |
          v
+---------------------+
|   Adminer (Docker)  | <-- Visualisation de la base
+---------------------+
```

---

## Licence

Ce projet est réalisé dans un cadre pédagogique. Le code est mis à disposition sous la licence MIT.

---

## Créateurs du projet

### - Carole Novak       [GitHub](https://github.com/Carole-N/cgvbot) • [LinkedIn](https://www.linkedin.com/in/carole-novak-76a69a269/)

### - Lucas Henneuse       [GitHub](https://github.com/lucasHENNEUSE/cgvbot) • [LinkedIn](https://www.linkedin.com/in/lucas-henneuse-21076325a/)