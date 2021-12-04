# Using for loop
#for i in list:


import math
import os

tmp_c_multy = []
tmp_pythagor =[]

clear = lambda: os.system('cls')
clear()

for x in range(1, 101):
    for y in range(1, 101): 
        c = math.sqrt(x**2 + y**2)
        if  float(c).is_integer():
           # print("{0} - {1}  = {2}".format(x,y,c))
            res_pyth_combi_found = [x,y,int(c)]
            res_pyth_combi_found.sort() 
            if not ( res_pyth_combi_found in tmp_pythagor ):
                if not c in tmp_c_multy:
                    tmp_c_multy.append(int(c))
                    tmp_pythagor.append(res_pyth_combi_found)
                    
            

#print(tmp_pythagor)

#res_pythagor.sort()
tmp_c_multy.sort()

result_pytagoras = []

                  
#print(result_pytagoras)

result_pytagoras.sort()       
j=1
for show_i in result_pytagoras:
    print(" " + str(j) + str(show_i))
    j+= 1
    
 
 
print("celkem jsme našli " + str(len(result_pytagoras)))       
        

        