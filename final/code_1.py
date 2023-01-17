x=[ -5, 5, 0, 4, -1, -9, 0, 1, 2, -7, 5]
counter=0 

for i in x:
    if i<=0:
        x[counter]=1
    print(f"x[{counter}] = {x[counter]}")
    counter+=1