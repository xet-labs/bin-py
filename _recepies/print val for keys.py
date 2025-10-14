# Python3 Program to check whether a
# given key already exists in a dictionary.
 
def checkKey(dic, key):
    if key in dic:
        print("Present, ", end =" ")
        print("value =", dic[key])
    else:
        print("Not present")
         
# Driver Code
dic = {'a': 100, 'b':200, 'c':300}
key = 'b'
checkKey(dic, key)
 
key = 100
checkKey(dic, key)
#------------------same----------------------
def checkKey(dic, key):
     
    if key in dic:
        print("--Present, ", end =" ")
        print("-value =", dic[key])
    else:
        print("--Not present")
 
# Driver Code
dic = {'a': 100, 'b':200, 'c':300}
key = 'b'
checkKey(dic, key)
 
key = 'w'
checkKey(dic, key)


#-----------------------------------------------------------------------

# creating a new dictionary
my_dict ={"java":100, "python":112, "c":11}
 
# list out keys and values separately
key_list = list(my_dict.keys())
val_list = list(my_dict.values())
print(key_list,val_list)
 
# print key with val 100
position = val_list.index(100)
print(position)
print(key_list[position])
