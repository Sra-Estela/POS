import requests

URL = "http://127.0.0.1:8000/veiculos"

def menu():
    print("\n==== MENU ====")
    print("1 - Cadastrar veículo")
    print("2 - Listar veículos")
    print("3 - Buscar por placa")
    print("4 - Atualizar veículo")
    print("5 - Deletar veículo")
    print("0 - Sair")

def cadastrar():
    veiculo = {
        "nome": input("Nome: "),
        "marca": input("Marca: "),
        "modelo": input("Modelo: "),
        "placa": input("Placa: ")
    }
    resposta = requests.post(URL, json=veiculo)
    print(resposta.json())

def listar():
    resposta = requests.get(URL)
    for v in resposta.json():
        print(v)

def buscar():
    placa = input("Placa: ")
    resposta = requests.get(f"{URL}/{placa}")
    print(resposta.json())

def atualizar():
    placa = input("Placa atual do veículo: ")
    veiculo = {
        "nome": input("Novo nome: "),
        "marca": input("Nova marca: "),
        "modelo": input("Novo modelo: "),
        "placa": input("Nova placa: ")
    }
    resposta = requests.put(f"{URL}/{placa}", json=veiculo)
    print(resposta.json())

def deletar():
    placa = input("Placa do veículo a deletar: ")
    resposta = requests.delete(f"{URL}/{placa}")
    print(resposta.json())

def main():
    while True:
        menu()
        opcao = input("Escolha: ")
        if opcao == '1':
            cadastrar()
        elif opcao == '2':
            listar()
        elif opcao == '3':
            buscar()
        elif opcao == '4':
            atualizar()
        elif opcao == '5':
            deletar()
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
