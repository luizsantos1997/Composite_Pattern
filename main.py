from ArquivoTexto import ArquivoTexto
from Component import Component
from Composite import Composite

class main:

    minhaPasta = Composite("Minha Pasta/")
    meuText1 = ArquivoTexto("Text 1.txt")
    meuText2 = ArquivoTexto("Text 2.txt")

    minhaPasta.__addArquivo__(meuText1)
    minhaPasta.__addArquivo__(meuText2)

    minhaPasta.__printNomeArquivo__()