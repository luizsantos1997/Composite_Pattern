from Component import Component
import itertools

class Composite(Component):
    arquivos = list() # Creating List of Component

    def __init__(self,nome):
        self.nomeArquivo = nome

    def __printNomeArquivo__(self):
        print(self.__getNomeArquivo__())

        for lista in iter(self.arquivos):
            print(lista.__printNomeArquivo__())


    def __addArquivo__(self,novoArquivo):
        try:
            self.arquivos.append(novoArquivo)
        except BaseException:
            print("Não foi possível adicionar arquivo: ",novoArquivo," - Error: ",BaseException.args)
    def __removeArquivo__(self,nomeArquivo):
        try:
            for arquivo in iter(self.arquivos):
                if arquivo.__getNomeArquivo__().__eq__(nomeArquivo):
                    self.arquivos.remove(nomeArquivo)
                    return
        except BaseException:
            print(BaseException.args)

    def __getArquivo__(self,nomeArquivo):
        try:
            for arquivo in iter(self.arquivos):
                if arquivo.__getNomeArquivo__().__eq__(nomeArquivo):
                    return nomeArquivo

        except BaseException:
            print(BaseException.args)