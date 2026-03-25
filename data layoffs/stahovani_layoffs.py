import os
import requests
import pandas as pd
from urllib.parse import urlparse


# Krok 1: Načti CSV soubor s daty
csv_path = (r"C:\Users\zpjev\Downloads\Layoffs.fyi  - Tech Layoffs Tracker.csv")
df = pd.read_csv(csv_path)

# Krok 2: Vyberme prvních 10 odkazů na články + firmu
top_articles = df[["Company", "Source"]].dropna().head(10)

# Krok 3: Vytvoř složku, kam se budou ukládat články
os.makedirs("clanky", exist_ok=True)

# Krok 4: Pro každý článek stáhneme HTML a uložíme do složky firmy
for index, row in top_articles.iterrows():
    company = row["Company"].strip().replace(" ", "_")
    url = row["Source"]

    try:
        # Stáhni článek
        response = requests.get(url, timeout=10)
        html_content = response.text

        # Vytvoř složku podle názvu firmy
        folder_path = os.path.join("clanky", company)
        os.makedirs(folder_path, exist_ok=True)

        # Vytvoř název souboru z domény (např. cnn_com.html)
        domain = urlparse(url).netloc.replace(".", "_")
        file_name = f"{domain}.html"

        # Ulož soubor
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(html_content)

        print(f"✅ Uložen článek pro firmu: {company}")

    except Exception as e:
        print(f"❌ Chyba při stahování článku pro firmu {company}: {e}")



from bs4 import BeautifulSoup  # knihovna pro práci s HTML

for root, dirs, files in os.walk("C:/Users/zpjev/OneDrive/Plocha/DA_Python/clanky", "r", encoding="utf-8"):
    for file_name in files:
        if file_name.endswith(".html"):
            file_path = os.path.join(root, file_name)

            try:
                with open(file_path, encoding="utf-8") as file:
                    soup = BeautifulSoup(file, "html.parser")
                    text = soup.get_text()

                if "AI" in text or "artificial intelligence" in text:
                    print(f"🧠 AI zmíněna v souboru: {file_path}")
                else:
                    print(f"⚪ Bez zmínky o AI: {file_path}")

            except Exception as e:
                print(f"❌ Chyba při čtení souboru {file_path}: {e}")