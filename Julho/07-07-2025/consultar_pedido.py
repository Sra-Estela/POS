# arquivo: consultar_pedido.py
import requests

url_base = "http://127.0.0.1:8000/pedido/"

def main():
    try:
        id_pedido = int(input("Digite o ID do pedido: "))
        response = requests.get(f"{url_base}{id_pedido}")

        if response.status_code == 200:
            print("\n📦 Dados do Pedido:")
            for chave, valor in response.json().items():
                print(f"{chave}: {valor}")
        elif response.status_code == 404:
            print("\n❌ Pedido não encontrado.")
        else:
            print("\n⚠️ Erro inesperado:", response.status_code)

    except ValueError:
        print("❗ Por favor, digite um número válido.")
    except requests.exceptions.ConnectionError:
        print("🔌 Não foi possível conectar à API. Ela está rodando?")

if __name__ == "__main__":
    main()
