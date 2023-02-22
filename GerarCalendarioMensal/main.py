# Gerar Calendário Mensal
import calendar as cld

def gerarCelandarioDoMes(ano,mes):

    print(f"{ano} {mes}")

    print(cld.month(ano,mes))


if __name__ == '__main__':
    gerarCelandarioDoMes(2023,2)
