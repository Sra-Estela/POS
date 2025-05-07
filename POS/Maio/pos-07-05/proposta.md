## Design da API do Sistema de Biblioteca

Esta atividade requer o design de uma API para um sistema de biblioteca. O sistema deve gerenciar as seguintes entidades:

### Entidades:

*   **Usuário:**
    *   `username`: `str`
    *   `password`: `str`
    *   `data_criacao`: `datetime` (data de criação)

*   **Livro:**
    *   `titulo`: `str` (título)
    *   `ano`: `int` (ano)
    *   `edicao`: `int` (edição)

*   **Biblioteca:**
    *   `nome`: `str` (nome)
    *   `acervo`: `List[Livro]` (acervo de livros)
    *   `usuario`: `List[Usuário]` (lista de usuários)

*   **Empréstimo:**
    *   `usuario`: `Usuário`
    *   `livro`: `Livro`
    *   `data_emprestimo`: `datetime` (data do empréstimo)
    *   `data_devolucao`: `datetime` (data da devolução)

### Requisitos da API:

Crie uma API com os seguintes métodos para cada entidade:

*   `GET`: Recuperar dados da entidade
*   `POST`: Criar uma nova entidade
*   `DELETE`: Excluir uma entidade existente