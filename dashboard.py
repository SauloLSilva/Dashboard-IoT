from datetime import datetime
from Models.sqlitedb import Sqlitedb
from time import sleep

sqlite = Sqlitedb()

while True:

    dia = datetime.now().strftime('%Y-%m-%d')

    sleep(1.5)
    total_acessos = sqlite.count_total_acesso()
    acesso_dia = sqlite.count_entrada_dia(dia)
    saida_dia = sqlite.count_saida_dia(dia)
    total_dia = int(acesso_dia) + int(saida_dia)
    ultimo_acesso = sqlite.check_last_acesso()

    print('*' * 35)
    print('total de acessos:', total_acessos)
    print(ultimo_acesso)
    print('total entrada:', acesso_dia) 
    print('total saida:', saida_dia)
    print('*' * 35)