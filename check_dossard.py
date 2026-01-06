import requests
from bs4 import BeautifulSoup

URL = "https://www.timepulse.fr/cession_dossard.php?id_epreuve=16429"

def check():
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(URL, headers=headers, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")
    text = soup.get_text().lower()
    return "aucune cession" not in text

if check():
    print("DOSSARD_DISPO")
else:
    print("RAS")
