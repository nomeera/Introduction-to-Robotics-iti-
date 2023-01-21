String = input("Enter Your String: ")
String=String.lower()
counter = 0

for i in String:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        counter+=1

print("Number of vowels =  ",counter)