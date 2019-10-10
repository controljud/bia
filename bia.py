import time
from classes.bio import Bio
from classes.mundo import Mundo

bio = Bio()
mundo = Mundo()
coordenadas = mundo.retornaCoordenadas()

bios = []
bio.nascer('José')
bios.append(bio)
while (len(bios) > 0):
    time.sleep(1)
    bio.imprimir()
    
    
    print(bio.eixo_x, bio.eixo_y, bio.fome)
    bios.remove(bio)