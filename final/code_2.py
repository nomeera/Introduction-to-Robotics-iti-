x=[1,3,4,-4,2,3,8,2,5,-7,54,76,789,23,98]
par=[0,0,0,0,0]
impar=[0,0,0,0,0]
counter,counter_par,counter_impar=0,0,0

for i in x:
    if i%2!=0:
        impar[counter_impar]=x[counter]
        if counter_par<5:
            print(f"impar[{counter_impar}] = {impar[counter_impar]}")
            if counter_impar==4: 
               counter_impar=0
               flag_par=False

        counter_impar+=1
        

    elif i%2==0:
        par[counter_par]=x[counter]
        if counter_par<5:
            print(f"par[{counter_par}] = {par[counter_par]}")
            if counter_par==4: 
               counter_par=0
               flag_par=False

        counter_par+=1

    counter+=1
