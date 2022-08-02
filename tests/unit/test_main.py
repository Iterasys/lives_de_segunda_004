# bibliotecas
import pytest
from main import somar_dois_numeros


# funções teste de unidade
def teste_somar_dois_numeros():
    # 1 Configura
    # 1.1 Dados de Entrada
    numeroA = 7
    numeroB = 5
    # 1.2 Resultados Esperados
    resultado_esperado = 12
    # 2 Executa
    resultado_obtido = somar_dois_numeros(numeroA, numeroB)
    # 3 Valida
    assert resultado_obtido == resultado_esperado


lista_para_somar = {
    (4, 6, 10),
    (10, -3, 7),
    (5, 0, 5)
}

@pytest.mark.parametrize('numeroA, numeroB, resultado_esperado', lista_para_somar)
def teste_somar_dois_numeros_da_lista(numeroA, numeroB, resultado_esperado):
    # 1 Configura
    # 1.1 Dados de Entrada e Resultado Esperado vem da lista
    # 2 Executa
    resultado_obtido = somar_dois_numeros(numeroA, numeroB)
    # 3 Valida
    assert resultado_obtido == resultado_esperado