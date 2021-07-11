from sys import path
from labrary import fos 
from load_settings import load 
import pathlib
import time
local_path = str(pathlib.Path().absolute())
setting_location = local_path + fos() + "setting.json"

S = load(setting_location)




from platform import system as si

ba = {'Windows':'cls','Linux':'clear'} 
clear = ba[si()]


def fix (Len:int,first:str,secound:str):
    if len(first+secound) >= Len:
        return first+secound
    return first + " " * (Len - len(first+secound)) + secound

class loading:
    def __init__ (self,Len:int):
        self.len = Len
        self.loc = 0
    def next(self):
        self.loc += 1
        r =  "[%s%s]"%('.'*self.loc,' '*int(self.len-self.loc))
        if self.loc == self.len :
            self.loc = 0
        return r



def main():

    import os
    from time import sleep
    
    Locations = S['location']
    Roydads   = S[ 'roydad' ]
    time_sleep = S['time_sleep']
    max_time = S['max_time']

    os.system(clear)
    input('Hellow!\n ready? ')
    os.system(clear)


    last_location_selected = ""
    last_roydad_selected = ""
  

    while True :



        q = 0
        start_time = time.time()
        load = loading(4)
        while time.time() - start_time <= time_sleep :
            print(fix(24,Locations.random_unit(),load.next()) , end='\r')
            sleep(max_time)
            q =+ 1
        


        location_selected = Locations.random_unit()
        while location_selected == last_location_selected:
            location_selected = Locations.random_unit()
        print(' '*24,end='\r')
        print(location_selected)
        last_location_selected = location_selected








        q = 0
        start_time = time.time()
        load = loading(4)
        while time.time() - start_time <= time_sleep :
            print(fix(24,Roydads.random_unit(),load.next()) , end='\r')
            sleep(max_time)
            q =+ 1


        roydad_selected = Roydads.random_unit()
        while roydad_selected == last_roydad_selected :
            roydad_selected = Roydads.random_unit()
        print(' '*24,end='\r')
        print(roydad_selected)
        last_roydad_selected = roydad_selected

        input('\nnext? ')
        os.system(clear)


if __name__ == '__main__':
    main()