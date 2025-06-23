import requests

if __name__ == "__main__":
	url = "https://127.0.0.1:8000"
	r = requests.get(f"{url}/livros")
	print(r.text)
	livro = {
		"titulo" : "Python como Programar",
		"ano" : 2024,
		"edicao" : 1
	}
	r = requests.post(f"{url}/livros", data=livro)
	print(r.status_code)
	print(r.text)