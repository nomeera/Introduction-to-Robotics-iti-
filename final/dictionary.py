lst = [1,1.3,7,4.4,"hi",[0,1],'45']
dictionary = {}
element_int=[]
element_float=[]
element_str=[]
element_list=[]

for i in lst:
    if isinstance(i,int):
        element_int.append(i)
        dictionary[type(i)] = element_int
    if isinstance(i,float):
        element_float.append(i)
        dictionary[type(i)] = element_float
    if isinstance(i,str):
        element_str.append(i)
        dictionary[type(i)] = element_str
    if isinstance(i,list):
        element_list.append(i)
        dictionary[type(i)] = element_list

print(dictionary)
    

     











