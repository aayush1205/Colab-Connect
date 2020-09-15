from config import conf
from connect import connect

class obj:

    def __init__(self):
        self.token = conf()

    def make_connection(self):
        connect()
    
    def configure(self):
        conf()




