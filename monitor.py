import requests
import re

url = "https://www.kabum.com.br/produto/235987/placa-de-video-rx-6600-cld-8g-asrock-amd-radeon-8gb-gddr6-90-ga2rzz-00uanf"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "pt-BR,pt;q=0.9",
    "Connection": "keep-alive",
    "Referer": "https://www.google.com/"
}

def consultar():
    try:
        # Usamos uma sessão para manter "cookies" e parecer um humano
        session = requests.Session()
        response = session.get(url, headers=headers, timeout=20)
        
        # Procuramos o padrão de preço no texto bruto
        texto = response.text
        # Busca padrão R$ 1.234,56 ou R$1.234,56
        precos = re.findall(r'R\$\s?[\d\.]+\,\d{2}', texto)
        
        if precos:
            # Filtramos para pegar valores que façam sentido para uma placa (acima de 1000)
            lista_limpa = [p for p in precos if int(p.split('$')[1].split(',')[0].replace('.', '')) > 1000]
            if lista_limpa:
                print(f"✅ PREÇO ENCONTRADO: {lista_limpa[0]}")
            else:
                print(f"✅ Preço capturado: {precos[0]}")
        else:
            print("⚠️ A Kabum bloqueou a visão por agora. O robô tentará novamente em 4 horas.")
            
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    consultar()
