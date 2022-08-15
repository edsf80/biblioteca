from aluno import Aluno

class AlunoDao:

    def __init__(self):
        self.__data = [
            Aluno('123456789', 'Teste', 17, 'Informática'), 
            Aluno('987654321', 'Teste 2', 16, 'Informática'),
            Aluno('999999999', 'Teste 3', 17, 'Meio Ambiente')
        ]

    def listar(self):
        return self.__data

    def criar(self, aluno):
        self.__data.append(aluno)