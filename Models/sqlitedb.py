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
    
                if saida > entrada:
                    colaborador = """select nome from acessos where data_saida = '{}'""".format(saida)
                    ultimo_acesso = self.db_query(self._database, colaborador)[0][0]
                    return 'Saída de {}, data: {}'.format(ultimo_acesso, entrada)
        except:
            return 0
        
    def count_total_acesso(self):
        count_entrada = """select count(*) from acessos;"""
        count_saida = """select count(*) from acessos where data_saida != '';"""

        entrada = self.db_query(self._database, count_entrada)[0][0]
        saida = self.db_query(self._database, count_saida)[0][0]

        return int(entrada)+ int(saida)