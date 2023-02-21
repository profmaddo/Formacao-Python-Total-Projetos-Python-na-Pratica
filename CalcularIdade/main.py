# Calcular a Idade com base na data atual e a data de nascimento, ano, mes, dia.

def calcularIdade(ano, mes, dia):

    import datetime as dt

    dataAtual = dt.datetime.now().date()

    dataNascimento = dt.date(ano,mes,dia)



    print(f'Data de Nascimento, {dataNascimento}')
    print(f'Data Atual, {dataAtual}')

if __name__ == '__main__':
    calcularIdade(2000,10,2)
