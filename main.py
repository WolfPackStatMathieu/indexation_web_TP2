# Importer les bibliothèques nécessaires
import json
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from collections import defaultdict

# Charger la liste de documents à partir du fichier JSON
with open('crawled_urls.json', 'r', encoding='utf-8') as file:
    documents = json.load(file)

# Initialiser l'index inversé vide
index = defaultdict(list)

# Initialiser l'index positionnel vide
pos_index = defaultdict(lambda: defaultdict(list))  # Index positionnel

# Initialiser le stemmer de Porter
porter_stemmer = PorterStemmer()

# Initialiser les variables pour les statistiques
num_documents = len(documents)
num_tokens_global = 0
average_tokens_per_document = 0

num_tokens_url = 0
num_tokens_title = 0
num_tokens_content = 0
num_tokens_h1 = 0

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
    
    # Mise à jour des statistiques par champ
    num_tokens_url += len(tokens_url)
    num_tokens_title += len(tokens_title)
    num_tokens_content += len(tokens_content)
    num_tokens_h1 += len(tokens_h1)
    
    # Créer une liste inversée pour chaque token
    for token in set(tokens_all):
        if i not in index[token]:
            index[token].append(i)
            
    # Index positionnel sur les titres
    
    # Construction de l'index positionnel pour le champ title
    for position, token in enumerate(processed_tokens_title):
        pos_index[token][i].append(position)

# Calcul des statistiques finales
average_tokens_per_document = num_tokens_global / num_documents
average_tokens_per_url = num_tokens_url / num_documents
average_tokens_per_title = num_tokens_title / num_documents
average_tokens_per_content = num_tokens_content / num_documents
average_tokens_per_h1 = num_tokens_h1 / num_documents

# Enregistrement des statistiques dans un fichier JSON
metadata = {
    'num_documents': num_documents,
    'num_tokens_global': num_tokens_global,
    'average_tokens_per_document': average_tokens_per_document,
    'average_tokens_per_url': average_tokens_per_url,
    'average_tokens_per_title': average_tokens_per_title,
    'average_tokens_per_content': average_tokens_per_content,
    'average_tokens_per_h1': average_tokens_per_h1
}

with open('metadata.json', 'w', encoding='utf-8') as metadata_file:
    json.dump(metadata, metadata_file, ensure_ascii=False, indent=2)

# Enregistrement de l'index inversé dans un fichier JSON
with open('index.json', 'w', encoding='utf-8') as index_file:
    # Utiliser json.dumps avec des séparateurs personnalisés pour obtenir le formatage souhaité
    output = json.dumps(index, ensure_ascii=False, indent=2, separators=(',', ': '))
    index_file.write(output)

# Enregistrement de l'index positionnel dans un fichier JSON
with open('title.pos_index.json', 'w', encoding='utf-8') as pos_index_file:
    json.dump(pos_index, pos_index_file, ensure_ascii=False, indent=2)
    
print("FINI")
