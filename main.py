class Aluno:
    def __init__(self, nome: str, nota1: float, nota2: float):
        self.__nome = nome
        self.__nota1 = nota1
        self.__nota2 = nota2

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome: str):
        self.__nome = nome

    def get_nota1(self):
        return self.__nota1

    def set_nota1(self, nota1: float):
        self.__nota1 = nota1

    def get_nota2(self):
        return self.__nota2

    def set_nota2(self, nota2: float):
        self.__nota2 = nota2

    def calcular_media(self):
        return (self.__nota1 + self.__nota2) / 2

if __name__ == "__main__":
    aluno = Aluno("João", 7.5, 8.0)

    print(f"Nome do aluno: {aluno.get_nome()}")
    print(f"Nota 1: {aluno.get_nota1()}")
    print(f"Nota 2: {aluno.get_nota2()}")

    print(f"Média: {aluno.calcular_media()}")

    aluno.set_nota1(9.0)
    aluno.set_nota2(9.5)
    print("\nApós alterar as notas:")
    print(f"Nova Média: {aluno.calcular_media()}")
