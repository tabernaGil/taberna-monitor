import requests
from bs4 import BeautifulSoup

url = "https://www.kabum.com.br/produto/235987/placa-de-video-rx-6600-cld-8g-asrock-amd-radeon-8gb-gddr6-90-ga2rzz-00uanf"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
}

def consultar():
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Tenta encontrar por diferentes seletores da Kabum
        preco = soup.find('h4', {'class': 'finalPrice'}) or \
                soup.find('span', {'class': 'priceCard'}) or \
                soup.select_one('h4.finalPrice')

        if preco:
            print(f"✅ Preço na Kabum: {preco.get_text().strip()}")
        else:
            print("⚠️ O preço ainda está escondido. Vou tentar outro método na próxima!")
            # Imprime um pedaço do site para a gente analisar se precisar
            print(f"Status da página: {response.status_code}")
    except Exception as e:
        print(f"Erro na consulta: {e}")

if __name__ == "__main__":
    consultar()
