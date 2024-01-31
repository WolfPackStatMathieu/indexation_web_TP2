import json
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from collections import defaultdict

# Charger la liste de documents à partir du fichier JSON
with open('crawled_urls_test.json', 'r', encoding='utf-8') as file:
    documents = json.load(file)

# Initialiser l'index vide
index = defaultdict(list)

# Initialiser le stemmer de Porter
porter_stemmer = PorterStemmer()

# Initialiser les variables pour les statistiques
num_documents = len(documents)
num_tokens_global = 0
average_tokens_per_document = 0

# Parcourir chaque document dans la liste
for i, document in enumerate(documents):
    # Extraire les informations nécessaires
    url = document['url']
    title = document['title']
    content = document['content']
    h1 = document['h1']

    # Tokenization des champs url, title, content, h1
    tokens_url = word_tokenize(url.lower())
    tokens_title = word_tokenize(title.lower())
    tokens_content = word_tokenize(content.lower())
    tokens_h1 = word_tokenize(h1.lower())

    # Optionnel: Traitement de chaque token (ex: stemming)
    processed_tokens_url = [porter_stemmer.stem(token) for token in tokens_url]
    processed_tokens_title = [porter_stemmer.stem(token) for token in tokens_title]
    processed_tokens_content = [porter_stemmer.stem(token) for token in tokens_content]
    processed_tokens_h1 = [porter_stemmer.stem(token) for token in tokens_h1]

    # Construction de l'index inversé pour chaque champ
    tokens_all = processed_tokens_url + processed_tokens_title + processed_tokens_content + processed_tokens_h1
    num_tokens_global += len(tokens_all)
    
    # Créer une liste inversée pour chaque token
    for token in set(tokens_all):
        index[token].append(i)

# Calcul des statistiques finales
average_tokens_per_document = num_tokens_global / num_documents

# Enregistrement de l'index dans un fichier JSON
with open('index.json', 'w', encoding='utf-8') as index_file:
    json.dump(index, index_file, ensure_ascii=False, indent=2)

# Enregistrement des statistiques dans un fichier JSON
metadata = {
    'num_documents': num_documents,
    'num_tokens_global': num_tokens_global,
    'average_tokens_per_document': average_tokens_per_document
}

with open('metadata.json', 'w', encoding='utf-8') as metadata_file:
    json.dump(metadata, metadata_file, ensure_ascii=False, indent=2)
