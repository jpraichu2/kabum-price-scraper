# Importa as bibliotecas que acabamos de instalar
import requests
from bs4 import BeautifulSoup

# O alvo da nossa caça
URL = "https://www.kabum.com.br"

# Cabeçalhos para simular um navegador real e evitar ser bloqueado
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# 1. Fazendo a requisição para o site
print("Buscando a página da Kabum!...")
try:
    response = requests.get(URL, headers=HEADERS)
    response.raise_for_status() # Lança um erro se a requisição falhou (ex: erro 404)

    # 2. "Parseando" o HTML com o BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # 3. Encontrando e imprimindo o título da página
    page_title = soup.find('title').get_text()

    print("\nConexão bem-sucedida!")
    print(f"O título da página é: {page_title.strip()}")

except requests.exceptions.RequestException as e:
    print(f"\nFalha ao se conectar com o site: {e}")