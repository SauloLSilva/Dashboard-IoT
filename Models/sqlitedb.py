import sqlite3

class Sqlitedb(object):

    def __init__(self, database_full_path="accesso_dados.db"):
        self._database = database_full_path

    def db_query(self, database, query):

        connection = sqlite3.connect(database, timeout=10)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        fetch = cursor.fetchall()

        cursor.close()
        connection.close()

        return fetch
    
    def criar_tabelas(self):

        try:
            connection = sqlite3.connect(self._database)
            cursor = connection.cursor()
            query = """CREATE TABLE IF NOT EXISTS acessos(
                        id_acesso integer not null PRIMARY KEY AUTOINCREMENT,
                        colaborador varchar(30) not null,
                        nome varchar(30) not null,
                        data_entrada DATETIME,
                        data_saida DATETIME);"""
            cursor.execute(query)

            del cursor
            connection.close()
            return 'created tables!'

        except:
            return 'erro ao criar as tabelas'
    
    def check_acesso(self, colaborador ,nome, data):
        check_acesso = """SELECT max(id_acesso), data_entrada, data_saida FROM acessos
                    WHERE colaborador = '{0}'""".format(colaborador)

        dados = self.db_query(self._database, check_acesso)

        id_acesso = dados[0][0]

        if id_acesso == None:
            insert_acesso = """INSERT INTO acessos(nome, colaborador, data_entrada, data_saida)
                    VALUES('{}','{}','{}','')""".format(nome, colaborador, data)
            self.db_query(self._database, insert_acesso)
                
        else:
            saida = dados[0][2]
            if saida != '':
                insert_acesso = """INSERT INTO acessos(nome, colaborador, data_entrada, data_saida)
                        VALUES('{}','{}','{}','')""".format(nome, colaborador, data)
                self.db_query(self._database, insert_acesso)
            else:
                insert_saida = """UPDATE acessos
                        SET data_saida = '{0}'
                        WHERE colaborador = '{1}' AND id_acesso = {2}""".format(data, colaborador, id_acesso)

                self.db_query(self._database, insert_saida)

    def count_entrada_dia(self, data):
        check_acesso = """select count(*) from acessos where data_entrada like '%{}%';""".format(data)

        try:
            return self.db_query(self._database, check_acesso)[0][0]
        except:
            return 0
    
    def count_saida_dia(self, data):
        check_acesso = """select count(*) from acessos where data_saida like '%{}%';""".format(data)
        try:
            return self.db_query(self._database, check_acesso)[0][0]
        except:
            return 0
        
    def count_entrada_mes(self, data):
        check_acesso = """select count(*) from acessos where data_entrada like '%{}%';""".format(data)

        try:
            return self.db_query(self._database, check_acesso)[0][0]
        except:
            return 0
    
    def count_saida_mes(self, data):
        check_acesso = """select count(*) from acessos where data_saida like '%{}%';""".format(data)
        try:
            return self.db_query(self._database, check_acesso)[0][0]
        except:
            return 0
    
    def check_last_acesso(self):
        ultima_entrada = """select max(data_entrada) from acessos;"""
        ultima_saida = """select max(data_saida) from acessos;"""

        entrada = self.db_query(self._database, ultima_entrada)[0][0]
        saida = self.db_query(self._database, ultima_saida)[0][0]

        try:

            if saida == '':
                colaborador = """select nome from acessos where data_entrada = '{}'""".format(entrada)
                ultimo_acesso = self.db_query(self._database, colaborador)[0][0]
                return 'Entrada de {}, data: {}'.format(ultimo_acesso, entrada)
            
            else:
                if entrada > saida:
                    colaborador = """select nome from acessos where data_entrada = '{}'""".format(entrada)
                    ultimo_acesso = self.db_query(self._database, colaborador)[0][0]
                    return 'Entrada de {}, data: {}'.format(ultimo_acesso, entrada)
    
                else: 
                    colaborador = """select nome from acessos where data_saida = '{}'""".format(saida)
                    ultimo_acesso = self.db_query(self._database, colaborador)[0][0]
                    return 'Saída de {}, data: {}'.format(ultimo_acesso, saida)
        except:
            return 0
        
    def count_total_acesso(self):
        count_entrada = """select count(*) from acessos;"""
        count_saida = """select count(*) from acessos where data_saida != '';"""

        entrada = self.db_query(self._database, count_entrada)[0][0]
        saida = self.db_query(self._database, count_saida)[0][0]

        return int(entrada)+ int(saida)

    def periodo_pico(self, dia):
        try:
            periodo_manha = '''select count(data_entrada) from acessos where data_entrada between '{} 06:00:00' and '{} 12:29:59';'''.format(dia,dia)
            periodo_tarde = '''select count(data_entrada) from acessos where data_entrada between '{} 12:30:00' and '{} 18:00:00';'''.format(dia,dia)
            periodo_noite = '''select count(data_entrada) from acessos where data_entrada between '{} 18:00:01' and '{} 23:59:59';'''.format(dia,dia)

            manha = self.db_query(self._database, periodo_manha)[0][0]
            tarde = self.db_query(self._database, periodo_tarde)[0][0]
            noite = self.db_query(self._database, periodo_noite)[0][0]
            # print(manha, tarde,noite)

            if manha > tarde and manha > tarde:
                pico = 'Manhã'
                acesso = manha
            if tarde > noite and tarde > noite:
                pico = 'Tarde'
                acesso = tarde
            if noite > manha and noite > tarde:
                pico = 'Noite'
                acesso = noite

            return pico, acesso
        except:
            return 'sem dados', 0
        
    def mes_pico(self, dia):
        try:
            dia_acesso = 0
            manha_total = 0
            tarde_total = 0
            noite_total = 0

            for dia_acesso in range(1,31):
                if dia_acesso < 10:
                    dia_acesso = '0{}'.format(dia_acesso)
                periodo_manha = '''SELECT count (data_entrada) from acessos where data_entrada between '{}-{} 06:00:00' and '{}-{} 12:29:59';'''.format(dia, dia_acesso, dia, dia_acesso)
                periodo_tarde = '''SELECT count (data_entrada) from acessos where data_entrada between '{}-{} 12:30:00' and '{}-{} 18:00:00';'''.format(dia, dia_acesso, dia, dia_acesso)
                periodo_noite = '''SELECT count (data_entrada) from acessos where data_entrada between '{}-{} 18:00:01' and '{}-{} 23:59:59';'''.format(dia, dia_acesso, dia, dia_acesso)

                manha = self.db_query(self._database, periodo_manha)[0][0]
                tarde = self.db_query(self._database, periodo_tarde)[0][0]
                noite = self.db_query(self._database, periodo_noite)[0][0]

                manha_total += manha
                tarde_total += tarde
                noite_total += noite

            if manha_total > tarde_total and manha_total > noite_total:
                pico = 'Manhã'
                acesso = manha_total
            if tarde_total > manha_total and tarde_total > noite_total:
                pico = 'Tarde'
                acesso = tarde_total
            if noite_total > manha_total and noite_total > tarde_total:
                pico = 'Noite'
                acesso = noite_total

            return pico, acesso
        
        except Exception as err:
            return 'sem dados', 0
