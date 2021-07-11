
from os import lseek


class location :
    
    def __init__ (self,name:str):
        self.name = name

    def __str__ (self): 
        return self.name


class roydad :

    def __init__ (self,name:str):
        self.name = name 

    def __str__ (self): 
        return self.name

class List(list):
    def random_unit (self):
        from random import randint
        if len(self) == 0 : return None
        return self[randint(0,len(self)-1)]


def load (path) -> dict:
    import json 
    s = open (path,'r').read()
    S = json.loads(s)

   
    return_sourse = {
        "location" : List(S['Locations']),
        "roydad" : List(S['Roydads']),
        "time_sleep" : S['time_sleep'],
        "max_time" : S['max_time']
    }
    return return_sourse