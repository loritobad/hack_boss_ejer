from  config.config import config
from  menu.menu import layout

from data.data import load_data





if __name__ == '__main__':
    
    config()
    
    load_data()
    
    layout()
   

