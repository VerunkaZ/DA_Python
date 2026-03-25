import json

# Načtení dat ze souboru
with open('dataset_nedele_2.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Předpokládejme, že URL jsou uloženy v nějakém poli nebo ve slovnících
# Například v každé položce jako 'url' klíč

urls = []

def find_urls(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key.lower() == 'url' and isinstance(value, str):
                urls.append(value)
            else:
                find_urls(value)
    elif isinstance(obj, list):
        for item in obj:
            find_urls(item)

# Vyhledání všech URL v datasetu
find_urls(data)

# Vypsání počtu URL a volitelně i seznam
print(f"Počet nalezených URL: {len(urls)}")
# print(urls)  # Pokud chceš vidět seznam URL