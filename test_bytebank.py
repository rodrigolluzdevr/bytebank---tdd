from codigo.bytebank import Funcionario
import pytest

class TesteClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):
        entrada = '13/03/2000' # Given-ContextoInicial
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade() #When-ação

        assert resultado == esperado # Then-desfecho

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = 'Lucas Carvalho ' #Given-ContextoInicial
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome() #When-Ação

        assert resultado == esperado # Then-desfecho

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000 # given
        entrada_nome = 'Paulo Bragança'
        esperado=90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario() # when
        resultado = funcionario_teste.salario

        assert resultado == esperado # then

    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada_salario = 1000
        esperado = 100

        funcionario_teste = Funcionario('Yasmin', '13/03/1997', entrada_salario)
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado  # then

    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada_salario = 1000000 #given

            funcionario_teste = Funcionario('Yasmin', '13/03/1997', entrada_salario)
            resultado = funcionario_teste.calcular_bonus()

            assert resultado  # then