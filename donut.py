#Made BY K9IGHTMARE
#REFRENCES:Stackoverflow
#Time Spent:5.5 hours
#Please follow if you liked the code you can always change your mind :)
import os
from math import sin, cos

def main():
    a=0
    b=0

    
    clear = "cls"
    if os.name == "posix":
        clear = "clear"

    os.system(clear)
    while True:
        z = [0 for _ in range(7040)]
        screen = [' ' for _ in range(1760)]

        j=0
        while j<6.28:
            j+=0.07
            i=0
            while i<6.28:
                i+=0.02

                sinA=sin(a)
                cosA=cos(a)
                cosB=cos(b)
                sinB=sin(b)

                sini=sin(i)
                cosi=cos(i)
                cosj=cos(j)
                sinj=sin(j)

                cosj2=cosj+2
                mess=1/(sini*cosj2*sinA+sinj*cosA+5)
                t=sini*cosj2*cosA-sinj* sinA

                
                x = int(40+30*mess*(cosi*cosj2*cosB-t*sinB))
                
                y = int(12+15*mess*(cosi*cosj2*sinB +t*cosB))
                
                o = int(x+80*y)
                N = int(8*((sinj*sinA-sini*cosj*cosA)*cosB-sini*cosj*sinA-sinj*cosA-cosi *cosj*sinB))

                if 0<y<22 and 0<x<80 and z[o] < mess:
                    z[o]=mess
                    screen[o]=".,-~:;=!*#$@"[N if N>0 else 0]

        
        os.system(clear)
        for index, char in enumerate(screen):
            if index % 80 == 0:
                print()
            else:
                print(char, end='')

        
        a+=0.04
        b+=0.02

if __name__ == "__main__":
    main()
