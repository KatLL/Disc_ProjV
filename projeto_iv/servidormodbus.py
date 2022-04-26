from pyModbusTCP.server import DataBank, ModbusServer
import random
from time import sleep


class ServidorMODBUS():
    '''
    Classe ServidorMODBUS
    '''
    def __init__(self, host_ip, port):
        '''
        Constructor 
        '''
        self._server = ModbusServer(host=host_ip,port=port,no_block=True)
        self._db = DataBank

    def run(self):
        """
        execut server modbus
        """
        lista = [300,2,3,4,5,6,7]
        try:
            self._server.start()
            print("Server ONLINE")
            i = 0
            while True: 
                #for i in range(0,7):
                if i == 7:
                    i = 0
                self._db.set_words(1000,[lista[i]])
                i+=1
                print('=========================')
                print('Table Modbus')
                print (f'Holding Register \r\n R1000 {self._db.get_words(1000)} \r\n R2000 {self._db.get_words(2000)}')
                print (f'Coil \r\n R1000 {self._db.get_bits(1000)}')
                sleep(1)
        except Exception as e:
            print("Erro: ", e.args)