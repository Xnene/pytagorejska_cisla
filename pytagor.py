# Using for loop
#for i in list:


import math
import os

#nejvetsi spolecny delitel 
def gcd(a, b):
    while (b != 0):
        c = b
        b = a % b
        a = c
  
    return a



tmp_c_multy = []
tmp_pythagor =[]

clear = lambda: os.system('cls')
clear()

for a in range(1, 101):
    for b in range(1, 101): 
        c = math.sqrt(a**2 + b**2)
        if  float(c).is_integer():
           # print("{0} - {1}  = {2}".format(x,y,c))
            res_pyth_combi_found = [a,b,int(c)]
            res_pyth_combi_found.sort() 
            if not ( res_pyth_combi_found in tmp_pythagor ):
                if not c in tmp_c_multy:
                    # zobrazime si delitel
                   if (gcd(a,c) == 1) and (gcd(b,c) == 1):
                        print("founded pythagoras number \t "+str(res_pyth_combi_found)+ " delitel "  + str(gcd(a,c))+ "\t" + str(gcd(b,c)) )
                        tmp_c_multy.append(int(c))
                        tmp_pythagor.append(res_pyth_combi_found)
                    
            

#print(tmp_pythagor)

#res_pythagor.sort()
tmp_c_multy.sort()

result_pytagoras = []
result_pytagoras = tmp_pythagor
                  
#print(result_pytagoras)

result_pytagoras.sort()       
j=1
for show_i in result_pytagoras:
    print(" " + str(j) + str(show_i))
    j+= 1
    
 
 
print("celkem jsme našli " + str(len(result_pytagoras)))       
        

        