import requests
from bs4 import BeautifulSoup

# Link da RX 6600 na Kabum
url = "https://www.kabum.com.br/produto/235987/placa-de-video-rx-6600-cld-8g-asrock-amd-radeon-8gb-gddr6-90-ga2rzz-00uanf"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

def consultar():
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Procura o preço final no código da Kabum
        preco = soup.find('h4', {'class': 'finalPrice'})
        if preco:
            print(f"✅ Preço encontrado no Studio Taberna: {preco.get_text()}")
        else:
            print("❌ Preço não encontrado. O site pode ter mudado.")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    consultar()
