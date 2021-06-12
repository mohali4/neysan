from sys import path
from labrary import fos 
from load_settings import load 
import pathlib
local_path = str(pathlib.Path().absolute())
setting_location = local_path + fos() + "setting.json"

S = load(setting_location)




from platform import system as si

ba = {'Windows':'cls','Linux':'clear'} 
clear = ba[si()]




def main():

    import os
    from time import sleep
    
    Locations = S['location']
    Roydads   = S[ 'roydad' ]
    
    os.system(clear)
    input('Hellow!\n ready? ')
    os.system(clear)



    for q in range(0,4) :
        print("loading location%s"%('.'*q) , end='\r')
        sleep(1)
        qa = q

    location_selected = Locations.random_unit()
    print(' '*30,end='\r')
    print(location_selected)
    last_location_selected = location_selected





    for q in range(0,4) :
        print("loading roydad%s"%('.'*q) , end='\r')
        sleep(1)
        qa = q

    roydad_selected = Roydads.random_unit()
    print(' '*30,end='\r')
    print(roydad_selected)
    last_roydad_selected = roydad_selected


    while True :
        input('next? ')
        os.system(clear)
        


        for q in range(0,4) :
            print("loading location%s"%('.'*(q)) , end='\r')
            sleep(1)
            qa = q
        
        
         
        while location_selected == last_location_selected:
            location_selected = Locations.random_unit()
        print(' '*30,end='\r')
        print(location_selected)
        last_location_selected = location_selected





        for q in range(0,4) :
            print("loading roydad%s"%('.'*q) , end='\r')
            sleep(1)
            qa = q

        while roydad_selected == last_roydad_selected :
            roydad_selected = Roydads.random_unit()
        print(' '*30,end='\r')
        print(roydad_selected)
        last_roydad_selected = roydad_selected


if __name__ == '__main__':
    main()