# Adicione a biblioteca 'json' no topo do arquivo
import requests
from bs4 import BeautifulSoup
import json # <-- NOVA IMPORTAÇÃO

# Cole a URL do produto que você escolheu aqui
URL = "https://www.kabum.com.br/produto/171436/mouse-gamer-motospeed-v50-branco-rgb-macro-4000-dpi-white" 

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

print(f"Buscando dados do produto em: {URL[:50]}...")
try:
    response = requests.get(URL, headers=HEADERS)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')

    # --- NOSSA NOVA LÓGICA COMEÇA AQUI ---
    
    # 1. Encontre a "mina de ouro": a tag <script> com os dados estruturados
    # O 'type' é a nossa etiqueta de identificação precisa
    data_script = soup.find('script', type='application/ld+json')

    if data_script:
        # 2. Extraia o texto de dentro da tag e converta de texto para um objeto Python
        product_data = json.loads(data_script.string)

        # 3. Agora podemos pegar as informações de forma limpa e direta
        product_name = product_data.get('name')
        product_price = product_data.get('offers', {}).get('price')
        product_sku = product_data.get('sku')
        availability = product_data.get('offers', {}).get('availability')

        print("\n--- Dados do Produto Encontrados ---")
        print(f"Nome: {product_name}")
        print(f"Preço: R$ {product_price}")
        print(f"SKU: {product_sku}")
        print(f"Disponibilidade: {availability}")
        print("-----------------------------------")

    else:
        print("\nNão foi possível encontrar o script de dados estruturados (JSON-LD) na página.")
        print("O site pode ter mudado sua estrutura.")

except requests.exceptions.RequestException as e:
    print(f"\nFalha ao se conectar com o site: {e}")
except json.JSONDecodeError:
    print("\nFalha ao decodificar os dados JSON da página.")