import json
import nltk
from collections import defaultdict


# Charger la liste d'URLs à partir du fichier JSON
with open('votre_fichier.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Initialiser les variables pour les statistiques
num_documents = len(data)
num_tokens_global = 0
num_tokens_title = 0
num_tokens_content = 0
average_tokens_per_document = 0
index = defaultdict(list)

# Parcourir chaque document dans la liste
for document in data:
    # Extraire les informations nécessaires
    url = document['url']
    title = document['title']
    content = document['content']

    # Tokenization des titres et du contenu
    tokens_title = nltk.word_tokenize(title.lower())
    tokens_content = nltk.word_tokenize(content.lower())

    # Mise à jour des statistiques globales
    num_tokens_global += len(tokens_title) + len(tokens_content)
    num_tokens_title += len(tokens_title)
    num_tokens_content += len(tokens_content)

    # Mise à jour de l'index
    for token in tokens_title + tokens_content:
        index[token].append(url)

# Calcul des statistiques finales
average_tokens_per_document = num_tokens_global / num_documents

# Enregistrement de l'index dans un fichier JSON
with open('title_non_pos_index.json', 'w', encoding='utf-8') as index_file:
    json.dump(index, index_file, ensure_ascii=False, indent=2)

# Enregistrement des statistiques dans un fichier JSON
metadata = {
    'num_documents': num_documents,
    'num_tokens_global': num_tokens_global,
    'num_tokens_title': num_tokens_title,
    'num_tokens_content': num_tokens_content,
    'average_tokens_per_document': average_tokens_per_document
}

with open('metadata.json', 'w', encoding='utf-8') as metadata_file:
    json.dump(metadata, metadata_file, ensure_ascii=False, indent=2)
