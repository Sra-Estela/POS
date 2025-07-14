import requests

def buscar_pedido():
    try:
        id_pedido = int(input("Digite o ID do pedido que deseja buscar: "))
    except ValueError:
        print("ID inválido! Digite um número inteiro.")
        return

    url = f"http://127.0.0.1:8000/pedido/{id_pedido}"
    response = requests.get(url)

    if response.status_code == 200:
        pedido = response.json()
        for chave, valor in pedido.items():
            print(f"{chave}: {valor}")
    elif response.status_code == 404:
        print("Erro 404: Pedido não encontrado.")
    else:
        print(f"Erro ao buscar o pedido. Código: {response.status_code}")

if __name__ == "__main__":
    buscar_pedido()
