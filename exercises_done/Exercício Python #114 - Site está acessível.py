# Exercício 114: Crie um código em que teste se o site pudim está acessível pelo computador usado.

import requests

def check_site(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"O site {url} está acessível.")
        else:
            print(f"O site {url} retornou o status code {response.status_code}.")
    except requests.RequestException as e:
        print(f"Ocorreu um erro ao tentar acessar o site {url}: {e}")

check_site("http://www.pudim.com.br")
