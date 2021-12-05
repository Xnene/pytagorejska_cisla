import math
import os
# clear console
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

#nejvetsi spolecny delitel 
#Greatest common divisor
def gcd(a, b):
    while (b != 0):
        c = b
        b = a % b
        a = c
  
    return a


# funkce k nalezeni pytagorjekych cislel abc  
# basic == true index [0] = jenom zakladni trojice)   
# basic != index [0] = jenom zakladni trojice, index[1] = i s násobky 
# basic != index [0] = jenom zakladni trojice, index[1] = i s násobky,  index[2] = bez dvojic s prohozenim ab
def search_pythagoras_numbers(max_a, max_b, basic = True):

    tmp_list_uniq_c = []
    tmp_list_pythagoras_found_numbers =[]
    tmp_list_pythagoras_found_basic_numbers =[]
    tmp_list_pythagoras_found_withou_switch_numbers = []


    for a in range(1, max_a+1):
        for b in range(1, max_b+1): 
            c = math.sqrt(a**2 + b**2)
            if  float(c).is_integer():

                res_pyth_combi_found = [int(c),b,a]       
                #test jedinečnosti 
                if not ( res_pyth_combi_found in tmp_list_pythagoras_found_numbers ):
                    #show combination c , a , b  
                    #print("\t c: " +str(c)+"\t b: " +str(b)+"\t a: " +str(a))  
                    tmp_list_pythagoras_found_numbers.append(res_pyth_combi_found)
                    
                    # test na odstranení prehozených kombinace ab , ba 
                    if not c in tmp_list_uniq_c:
                        tmp_list_pythagoras_found_withou_switch_numbers.append(res_pyth_combi_found)
                        
                        #  Nalzezení základní pytagorijské trojice a zobrazime si divisor
                        if (gcd(a,c) == 1) and (gcd(b,c) == 1):
                            #print("found  basic pythagoras numbers \t "+str(res_pyth_combi_found)+ "\t divisor "  + str(gcd(a,c))+ "\t" + str(gcd(b,c)) )
                            tmp_list_uniq_c.append(int(c))
                            tmp_list_pythagoras_found_basic_numbers.append(res_pyth_combi_found)
    if basic:
        out = [tmp_list_pythagoras_found_basic_numbers]
    else:
        out = [tmp_list_pythagoras_found_basic_numbers,tmp_list_pythagoras_found_numbers,tmp_list_pythagoras_found_withou_switch_numbers]
    
    return out                

# nejake to zobrazeni             
def show_list_number(list_of_numbers):
    print("found following numbers in list ")
    j=1
    for show_i in list_of_numbers:
        #print("found  basic pythagoras numbers \t "+str(res_pyth_combi_found)+ "\t divisor "  + str(gcd(a,c))+ "\t" + str(gcd(b,c)) )
        print(" " + str(j) + "\t "+str(show_i)+ "\t divisor "  + str(gcd(show_i[1],show_i[0])))
        j+= 1
    print("Amount of numbers found " + str(len(list_of_numbers)))      
        

clearConsole()
print("Start searching pythagoras numbers 1.6")


result_pytagoras_basic = search_pythagoras_numbers(100,100,False)[0]
result_pytagoras_mutli = search_pythagoras_numbers(100,100,False)[1]
result_pytagoras_without_switch = search_pythagoras_numbers(100,100,False)[2]
                  
show_list_number(result_pytagoras_basic)

show_list_number(result_pytagoras_mutli)

show_list_number(result_pytagoras_without_switch)


    
 
 
 
        

        