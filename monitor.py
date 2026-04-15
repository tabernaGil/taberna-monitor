import requests
import re

url = "https://www.kabum.com.br/produto/235987/placa-de-video-rx-6600-cld-8g-asrock-amd-radeon-8gb-gddr6-90-ga2rzz-00uanf"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
}

def consultar():
    try:
        response = requests.get(url, headers=headers, timeout=15)
        html = response.text
        
        # Busca qualquer padrão de preço (R$ 1.234,56) no texto da página
        precos = re.findall(r'R\$\s?[\d\.]+\,\d{2}', html)
        
        if precos:
            # Pegamos o primeiro preço que aparece (geralmente é o principal)
            print(f"✅ Preço capturado no Studio Taberna: {precos[0]}")
        else:
            print("⚠️ O site escondeu o preço, mas o robô vai tentar de novo em 4 horas!")
            
    except Exception as e:
        print(f"Erro na consulta: {e}")

if __name__ == "__main__":
    consultar()
