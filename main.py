import json
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from collections import defaultdict

# Charger la liste d'URLs à partir du fichier JSON
with open('crawled_urls_test.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Initialiser les variables pour les statistiques
num_documents = len(data)
num_tokens_global = 0
num_tokens_title = 0
# num_tokens_content = 0
num_tokens_h1 = 0
average_tokens_per_document = 0
index = defaultdict(list)

# Initialiser le stemmer de Porter
porter_stemmer = PorterStemmer()

# Parcourir chaque document dans la liste
for document in data:
    # Extraire les informations nécessaires
    url = document['url']
    title = document['title']
    # content = document['content']
    # h1 = document['h1']

    # Tokenization et stemming des titres, du contenu et de h1
    tokens_title = [porter_stemmer.stem(token.lower()) for token in word_tokenize(title)]
    # tokens_content = [porter_stemmer.stem(token.lower()) for token in word_tokenize(content)]
    # tokens_h1 = [porter_stemmer.stem(token.lower()) for token in word_tokenize(h1)]

    # Mise à jour des statistiques globales
    num_tokens_global += len(tokens_title) #+ len(tokens_content) + len(tokens_h1)
    num_tokens_title += len(tokens_title)
    # num_tokens_content += len(tokens_content)
    # num_tokens_h1 += len(tokens_h1)

    # Mise à jour de l'index
    for token in tokens_title:# + tokens_content + tokens_h1:
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
    # 'num_tokens_content': num_tokens_content,
    # 'num_tokens_h1': num_tokens_h1,
    'average_tokens_per_document': average_tokens_per_document
}

with open('metadata.json', 'w', encoding='utf-8') as metadata_file:
    json.dump(metadata, metadata_file, ensure_ascii=False, indent=2)
