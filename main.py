from pessoa import *

def main():
    funcionario = Funcionario("joao")
    cliente = Cliente("natalia")
    maratona = Maratona()
    maratona.correr(cliente)
    maratona.correr(funcionario)

if __name__ == "__main__":
    main()