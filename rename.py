import os

i = 1
for file in os.listdir():
    print(file)
    if not file.endswith('.py') and not file.endswith('.gif'):
        os.rename(file, "bread.{}.".format(i)+file.split('.')[-1])
        i +=1
