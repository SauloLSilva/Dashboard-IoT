from multiprocessing import Pool
import os
import time
from Models.sqlitedb import Sqlitedb
import webbrowser

webbrowser.open('show.html')

sqlite = Sqlitedb()

sqlite.criar_tabelas()

def run_process(process):
    os.system('sudo python3 {0}'.format(process))
    time.sleep(2.5)

process = ('UDP.py', 'dashboard.py',)
pool = Pool(processes=2)
pool.map(run_process, process)