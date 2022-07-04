from time import sleep
from pyModbusTCP.client import ModbusClient 
import sqlite3
import datetime

db=sqlite3.connect('banco_automacao_.db')
c = db.cursor()
#c.execute("CREATE TABLE temperatura__ (data datetime, temperatura float)")
#c.execute("DROP TABLE temperatura__")
#c.execute ("DELETE FROM temperatura__;")
class ClienteMODBUS():

    def __init__(self, server_ip,porta,scan_time=1):
        self._cliente = ModbusClient(host=server_ip,port = porta)
        self._scan_time = scan_time

    def lerDado(self, tipo, addr):
        if tipo == 1:
            return self._cliente.read_holding_registers(addr,1)[0]

    def atendimento(self):
        self._cliente.open()
        atendimento = True
        while atendimento:
            sel = '1'
            if sel == '1':
                addr = '1000'
                nvezes = '10'
                tipo = '1'
                for i in range(0,int(nvezes)):
                    currentDateTime = datetime.datetime.now()
                    dado = self.lerDado(int(tipo), int(addr))
                    print(f"leitura {i+1}: {dado}",currentDateTime)
                    print('INSERT INTO temperatura VALUES("{}", {});'.format(currentDateTime ,dado))
                    c.execute('INSERT INTO temperatura__ VALUES("{}", {});'.format(currentDateTime ,dado))
                    db.commit()
                    sleep (self._scan_time)
        