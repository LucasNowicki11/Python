import sys
#print('\n\n', sys.argv, '\n\n')

if __name__ == '__main__':
    print(sys.argv)
if len(sys.argv) ==1 :
    print('es necesario colocar un argumento')
else:
    print(sys.argv[1])
#        print(param)
#        

#import sys
#cadena = sys.argv[1]
#repeticiones = int(sys.argv[2])
#for repeticion in   range(repeticiones):
#    print(cadena)
#