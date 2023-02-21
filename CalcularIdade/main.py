# Calcular a Idade com base na data atual e a data de nascimento, ano, mes, dia.
import datetime as dt

def calcularIdade(ano, mes, dia):

    dataAtual = dt.datetime.now().date()

    dataNascimento = dt.date(ano,mes,dia)

    calculoDaIdade = int((dataAtual-dataNascimento).days / 365.25)

    print(f'Data de Nascimento, {dataNascimento}')
    print(f'Data Atual, {dataAtual}')
    print(f'Sua idade é: {calculoDaIdade} anos')

if __name__ == '__main__':
    calcularIdade(1965,12,2)


