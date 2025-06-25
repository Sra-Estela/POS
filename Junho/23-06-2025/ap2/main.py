#VERSÃO 1 __________________________________
# import requests

# if __name__ == "__main__":
# 	url = "https://127.0.0.1:8000"
# 	r = requests.get(f"{url}/livros")
# 	print(r.text)
# 	livro = {
# 		"titulo" : "Python como Programar",
# 		"ano" : 2024,
# 		"edicao" : 1
# 	}
# 	r = requests.post(f"{url}/livros", data=livro)
# 	print(r.status_code)
# 	print(r.text)

#VERSÃO 2 __________________________________
# import requests

# if __name__ == "__main__":
#     url = "http://127.0.0.1:8000"
#     r = requests.get(f"{url}/livros")
#     print(r.text)
#     livro = {
#         "titulo": "Python como Programar",
#         "ano": 2024,
#         "edicao": 1
#     }
#     r = requests.post(f"{url}/livros",json=livro)
#     print(r.status_code)
#     print(r.text)
#     pesquisa = "Python como Programar"
#     r = requests.get(f"{url}/livros/{pesquisa}")
#     print(r.status_code)
#     print(r.text)
#     r = requests.delete(f"{url}/livros/{pesquisa}")
#     print(r.status_code)

import requests

url = "http://127.0.0.1:8000"

def listar_livros():
    r = requests.get(f"{url}/livros")
    print("Livros cadastrados:")
    print(r.text)

def pesquisar_livro():
    titulo = input("Digite o título do livro para pesquisa: ")
    r = requests.get(f"{url}/livros/{titulo}")
    print(f"Status: {r.status_code}")
    print(r.text)

def cadastrar_livro():
    titulo = input("Título: ")
    ano = int(input("Ano: "))
    edicao = int(input("Edição: "))
    livro = {
        "titulo": titulo,
        "ano": ano,
        "edicao": edicao
    }
    r = requests.post(f"{url}/livros", json=livro)
    print(f"Status: {r.status_code}")
    print(r.text)

def deletar_livro():
    titulo = input("Digite o título do livro para deletar: ")
    r = requests.delete(f"{url}/livros/{titulo}")
    print(f"Status: {r.status_code}")
    print(r.text)

def editar_livro():
    titulo_antigo = input("Digite o título do livro que deseja editar: ")
    r = requests.get(f"{url}/livros/{titulo_antigo}")
    if r.status_code == 404:
        print("Livro não encontrado.")
        return

    print("Informe os novos dados:")
    titulo = input("Novo Título: ")
    ano = int(input("Novo Ano: "))
    edicao = int(input("Nova Edição: "))
    livro_atualizado = {
        "titulo": titulo,
        "ano": ano,
        "edicao": edicao
    }
    r = requests.put(f"{url}/livros/{titulo_antigo}", json=livro_atualizado)
    print(f"Status: {r.status_code}")
    print(r.text)

if _name_ == "_main_":
    while True:
        print("\n=== MENU ===")
        print("1 - Listar todos os livros")
        print("2 - Pesquisar livro por título")
        print("3 - Cadastrar um livro")
        print("4 - Deletar um livro")
        print("5 - Editar um livro")
        print("6 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_livros()
        elif opcao == "2":
            pesquisar_livro()
        elif opcao == "3":
            cadastrar_livro()
        elif opcao == "4":
            deletar_livro()
        elif opcao == "5":
            editar_livro()
        elif opcao == "6":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")