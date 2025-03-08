from database import criar_tabelas

import livro
import usuario
import emprestimo
def menu():

    while True:
        print("\nBiblioteca")
        print(" 1- Cadastrar Usuário")
        print(" 2- Cadastrar Livros")
        print(" 3- Listar Livros Disponiveis")
        print(" 4- Emprestar Livro")
        print(" 5- Devolver Livro")
        print(" 00- Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            usuario.cadastrar_usuario()
        elif opcao == "2":
            livro.cadastrar_livro()
        elif opcao == "3":
            livro.listar_livros_disponiveis()
        elif opcao == "4":
            emprestimo.emprestar_livro()
        elif opcao == "5":
            emprestimo.devolver_livro()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")                

if __name__ == "__main__":
    menu()
    