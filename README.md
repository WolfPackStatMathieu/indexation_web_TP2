# Indexation Web - TP2

Ce projet Python implémente un système d'indexation web en suivant un algorithme spécifié. L'objectif est de créer un index inversé et un index positionnel à partir d'une liste de documents récupérés via un crawler.

## Structure du Projet après lancement du main

```
.
├── crawled_urls.json
├── crawled_urls_test.json
├── index.json
├── main.py
├── metadata.json
├── README.md
├── requirements.txt
├── title.pos_index.json

```

- `crawled_urls.json`: Fichier JSON contenant la liste de documents récupérés.
- `crawled_urls_test.json`: Fichier JSON de test contenant une liste réduite de documents.
- `index.json`: Fichier JSON contenant l'index inversé global. Créé dans le main et non indexé par git
- `main.py`: Script principal contenant le code pour générer l'index inversé et l'index positionnel.
- `metadata.json`: Fichier JSON contenant des statistiques sur les documents. Créé dans le main et non indexé par git
- `title.pos_index.json`: Fichier JSON contenant l'index positionnel spécifique au champ "title". Créé dans le main et non indexé par git

## Installation des Dépendances

```bash
pip install -r requirements.txt
```

## Exécution du Code

```bash
python main.py
```

## Description du Code

- Le script `main.py` charge la liste de documents depuis le fichier JSON.
- Il effectue une tokenization et un traitement optionnel (stemming) sur les champs `url`, `title`, `content`, et `h1`.
- Il construit un index inversé global et un index positionnel spécifique au champ "title".
- Des statistiques sur les documents sont calculées et enregistrées dans `metadata.json`.
- L'index inversé est enregistré dans `index.json`.
- L'index positionnel est enregistré dans `title.pos_index.json`.

N'hésitez pas à explorer et modifier le code en fonction de vos besoins.