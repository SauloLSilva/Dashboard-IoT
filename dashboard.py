import datetime
from Models.sqlitedb import Sqlitedb
import matplotlib.pyplot as plt
import numpy as np
import time

sqlite = Sqlitedb()

def graph_dia(entrada, saida, por_entrada, por_saida, acesso):

    try:
        y = np.array([por_entrada, por_saida])

        mylabels = ["\nEntrada = {}".format(entrada), "Saida = {}".format(saida),]

        plt.pie(y, labels = mylabels, shadow=True, explode=(0.1, 0.1), autopct='%1.2f%%')
        plt.title('Total de acessos Hoje = {}\n Ultimo acesso: {}'.format(entrada+saida, acesso))
        plt.savefig("dia.png")
        time.sleep(5)
        plt.close()
    except Exception as err:
        print(err)

def graph_ult_dias():

    # data = datetime.datetime.now().strftime('%Y-%m-%d').replace('','-').split('-')

    data = datetime.datetime.now()
    sete_dias = datetime.timedelta(days = 7)
    seis_dias = datetime.timedelta(days = 6)
    cinco_dias = datetime.timedelta(days = 5)
    quatro_dias = datetime.timedelta(days = 4)
    tres_dias = datetime.timedelta(days = 3)
    dois_dias = datetime.timedelta(days = 2)
    ultimo_dia = datetime.timedelta(days = 1)

    sete_data = str(data - sete_dias).replace('-','').split(' ')[0]
    sete_dia = '{}-{}-{}'.format(sete_data[0:4],sete_data[4:6], sete_data[6:8])
    try:
        sete_entrada = sqlite.count_entrada_dia(sete_dia)
    except:
        sete_entrada = 0
    try:
        sete_saida = sqlite.count_saida_dia(sete_dia)
    except:
        sete_saida = 0

    sete = int(sete_entrada) + int(sete_saida)

    seis_data = str(data - seis_dias).replace('-','').split(' ')[0]
    seis_dia = '{}-{}-{}'.format(seis_data[0:4],seis_data[4:6], seis_data[6:8])
    try:
        seis_entrada = sqlite.count_entrada_dia(seis_dia)
    except:
        seis_entrada = 0
    try:
        seis_saida = sqlite.count_saida_dia(seis_dia)
    except:
        seis_saida = 0

    seis = int(seis_entrada) + int(seis_saida)

    cinco_data = str(data - cinco_dias).replace('-','').split(' ')[0]
    cinco_dia = '{}-{}-{}'.format(cinco_data[0:4],cinco_data[4:6], cinco_data[6:8])
    try:
        cinco_entrada = sqlite.count_entrada_dia(cinco_dia)
    except:
        cinco_entrada = 0
    try:
        cinco_saida = sqlite.count_saida_dia(cinco_dia)
    except:
        cinco_saida = 0

    cinco = int(cinco_entrada) + int(cinco_saida)

    quatro_data = str(data - quatro_dias).replace('-','').split(' ')[0]
    quatro_dia = '{}-{}-{}'.format(quatro_data[0:4],quatro_data[4:6], quatro_data[6:8])
    try:
        quatro_entrada = sqlite.count_entrada_dia(quatro_dia)
    except:
        quatro_entrada = 0
    try:
        quatro_saida = sqlite.count_saida_dia(quatro_dia)
    except:
        quatro_saida = 0

    quatro = int(quatro_entrada) + int(quatro_saida)

    tres_data = str(data - tres_dias).replace('-','').split(' ')[0]
    tres_dia = '{}-{}-{}'.format(tres_data[0:4],tres_data[4:6], tres_data[6:8])
    try:
        tres_entrada = sqlite.count_entrada_dia(tres_dia)
    except:
        tres_entrada = 0
    try:
        tres_saida = sqlite.count_saida_dia(tres_dia)
    except:
        tres_saida = 0

    tres = int(tres_entrada) + int(tres_saida)

    dois_data = str(data - dois_dias).replace('-','').split(' ')[0]
    dois_dia = '{}-{}-{}'.format(dois_data[0:4],dois_data[4:6], dois_data[6:8])
    try:
        dois_entrada = sqlite.count_entrada_dia(dois_dia)
    except:
        dois_entrada = 0
    try:
        dois_saida = sqlite.count_saida_dia(dois_dia)
    except:
        dois_saida = 0

    dois = int(dois_entrada) + int(dois_saida)

    um_data = str(data - ultimo_dia).replace('-','').split(' ')[0]
    um_dia = '{}-{}-{}'.format(um_data[0:4],um_data[4:6], um_data[6:8])
    try:
        um_entrada = sqlite.count_entrada_dia(um_dia)
    except:
        um_entrada = 0
    try:
        um_saida = sqlite.count_saida_dia(um_dia)
    except:
        um_saida = 0

    um = int(um_entrada) + int(um_saida)

    year = [sete_dia, seis_dia, cinco_dia, quatro_dia, tres_dia, dois_dia, um_dia]
    unit = [sete, seis, cinco, quatro, tres, dois, um]
    
    # Plot the bar graph
    plot = plt.bar(year, unit, width=0.7)


    # Add the data value on head of the bar
    for value in plot:
        height = value.get_height()
        plt.text(value.get_x() + value.get_width()/2.,
                1.002*height,'%d' % int(height), ha='center', va='bottom')
    
    # Add labels and title
    plt.grid(False)
    plt.title("Total de acesso últimos 7 dias: {}".format(sete+seis+cinco+quatro+tres+dois+um))
    plt.xlabel("Dia")
    plt.ylabel("Quantidade")
    plt.xticks(size = 8)
    
    # Display the graph on the screen
    plt.savefig("mes.png")
    plt.close()

def porc_dia(por_dia, porc_outros_dias, total_mes, total_dia):

    try:
        y = np.array([por_dia, porc_outros_dias])

        mylabels = ["Hoje = {}".format(total_dia), "Outros dias = {}".format(total_mes - total_dia),]

        plt.pie(y, labels = mylabels, shadow=True, explode=(0.1, 0.1), autopct='%1.2f%%')
        plt.title('Total de acessos no Mês = {}'.format(total_mes))
        plt.savefig("mes_prc.png")
        time.sleep(5)
        plt.close()
    except Exception as err:
        print(err)

def porc_mes(por_mes, porc_outros_meses, total_ano, total_mes):

    try:
        y = np.array([por_mes, porc_outros_meses])

        mylabels = ["Nesse mês = {}".format(total_mes), "Outros meses = {}".format(total_ano - total_mes),]

        plt.pie(y, labels = mylabels, shadow=True, explode=(0.1, 0.1), autopct='%1.2f%%')
        plt.title('Total de acessos no Ano = {}'.format(total_ano))
        plt.savefig("ano_prc.png")
        time.sleep(5)
        plt.close()
    except Exception as err:
        print(err)

def cor(valor):
    if 'Manhã' in valor:
        cor = 'red'
        return cor
    if 'Tarde' in valor:
        cor = 'yellow'
        return cor
    if 'Noite' in valor:
        cor = 'blue'
        return cor
    else:
        return 'black'


def horario_pico():
    data = datetime.datetime.now()
    sete_dias = datetime.timedelta(days = 7)
    seis_dias = datetime.timedelta(days = 6)
    cinco_dias = datetime.timedelta(days = 5)
    quatro_dias = datetime.timedelta(days = 4)
    tres_dias = datetime.timedelta(days = 3)
    dois_dias = datetime.timedelta(days = 2)
    ultimo_dia = datetime.timedelta(days = 1)

    sete_data = str(data - sete_dias).replace('-','').split(' ')[0]
    sete_dia = '{}-{}-{}'.format(sete_data[0:4],sete_data[4:6], sete_data[6:8])

    seis_data = str(data - seis_dias).replace('-','').split(' ')[0]
    seis_dia = '{}-{}-{}'.format(seis_data[0:4],seis_data[4:6], seis_data[6:8])

    cinco_data = str(data - cinco_dias).replace('-','').split(' ')[0]
    cinco_dia = '{}-{}-{}'.format(cinco_data[0:4],cinco_data[4:6], cinco_data[6:8])

    quatro_data = str(data - quatro_dias).replace('-','').split(' ')[0]
    quatro_dia = '{}-{}-{}'.format(quatro_data[0:4],quatro_data[4:6], quatro_data[6:8])

    tres_data = str(data - tres_dias).replace('-','').split(' ')[0]
    tres_dia = '{}-{}-{}'.format(tres_data[0:4],tres_data[4:6], tres_data[6:8])

    dois_data = str(data - dois_dias).replace('-','').split(' ')[0]
    dois_dia = '{}-{}-{}'.format(dois_data[0:4],dois_data[4:6], dois_data[6:8])

    um_data = str(data - ultimo_dia).replace('-','').split(' ')[0]
    um_dia = '{}-{}-{}'.format(um_data[0:4],um_data[4:6], um_data[6:8])

    try:
        pico_7 = sqlite.periodo_pico(sete_dia)
        valor_7 = pico_7[1]
        periodo_7 = pico_7[0]
    except Exception as err:
        valor_7 = 0
        periodo_7 = 'sem_dados'

    try:
        pico_6 = sqlite.periodo_pico(seis_dia)
        valor_6 = pico_6[1]
        periodo_6 = pico_6[0]
    except:
        valor_6 = 0
        periodo_6 = 'sem_dados'

    try:
        pico_5 = sqlite.periodo_pico(cinco_dia)
        valor_5 = pico_5[1]
        periodo_5 = pico_5[0]
    except:
        valor_5 = 0
        periodo_5 = 'sem_dados'

    try:
        pico_4 = sqlite.periodo_pico(quatro_dia)
        valor_4 = pico_4[1]
        periodo_4 = pico_4[0]
    except:
        valor_6 = 0
        periodo_6 = 'sem_dados'

    try:
        pico_3 = sqlite.periodo_pico(tres_dia)
        valor_3 = pico_3[1]
        periodo_3 = pico_3[0]
    except:
        valor_3 = 0
        periodo_3 = 'sem_dados'

    try:
        pico_2 = sqlite.periodo_pico(dois_dia)
        valor_2 = pico_2[1]
        periodo_2 = pico_2[0]
    except:
        valor_2 = 0
        periodo_2 = 'sem_dados'

    try:
        pico_1 = sqlite.periodo_pico(um_dia)
        valor_1 = pico_1[1]
        periodo_1 = pico_1[0]
    except:
        valor_1 = 0
        periodo_1 = 'sem_dados'

    
    year_2 = [sete_dia, seis_dia, cinco_dia, quatro_dia, tres_dia, dois_dia, um_dia]
    unit_2 = [valor_7, valor_6, valor_5, valor_4, valor_3, valor_2, valor_1]

    color_2 = [cor(periodo_7),cor(periodo_6),cor(periodo_5),cor(periodo_4),cor(periodo_3),cor(periodo_2),cor(periodo_1)]
    
    # Plot the bar graph
    plot = plt.bar(year_2, unit_2, width=0.7, color=color_2)


    # Add the data value on head of the bar
    for value in plot:
        height = value.get_height()
        plt.text(value.get_x() + value.get_width()/2.,
                1.002*height,'%d' % int(height), ha='center', va='bottom')
    
    # Add labels and title
    plt.grid(False)
    plt.title("Período de pico últimos 7 dias")
    plt.xlabel("Dia")
    plt.ylabel("Acessos no período de pico")
    plt.xticks(size = 8)
    color_label = {'Manhã':'red', 'Tarde':'yellow', 'Noite':'blue'}         
    labels = list(color_label.keys())
    handles = [plt.Rectangle((0,0),1,1, color=color_label[label]) for label in labels]
    plt.legend(handles, labels)
    
    # Display the graph on the screen
    plt.savefig("pico_dia.png")
    plt.close()



def main():
    while True:

        dia = datetime.datetime.now().strftime('%Y-%m-%d')
        mes = datetime.datetime.now().strftime('%Y-%m')

        acesso_dia = sqlite.count_entrada_dia(dia)
        saida_dia = sqlite.count_saida_dia(dia)
        entrada_mes = sqlite.count_entrada_mes(mes)
        saida_mes = sqlite.count_saida_mes(mes)
        ultimo_acesso = sqlite.check_last_acesso()
        total_acessos = sqlite.count_total_acesso()
        total_dia = int(acesso_dia) + int(saida_dia)
        total_mes = int(entrada_mes) + int(saida_mes)

        try:
            por_entr_dia = acesso_dia/total_dia*100
        except:
            por_entr_dia = 0.1

        try:
            por_sai_dia = saida_dia/total_dia*100
        except:
            por_sai_dia = 0.1

        try:
            por_dia = total_dia/total_mes*100
            porc_outros_dias = 100- por_dia
        except:
            por_dia = 0.1
            porc_outros_dias = 0.1

        try:
            por_mes = total_mes/total_acessos*100
            porc_outros_mes = 100- por_mes
        except:
            por_mes = 0.1
            porc_outros_mes = 0.1      
      

        graph_dia(acesso_dia, saida_dia, por_entr_dia, por_sai_dia, ultimo_acesso)
        porc_dia(por_dia, porc_outros_dias, total_mes, total_dia)
        porc_mes(por_mes, porc_outros_mes, total_acessos, total_mes)
        graph_ult_dias()
        horario_pico()

main()