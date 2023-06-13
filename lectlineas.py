archivo=open("lect.txt", 'r')

for line in archivo.readlines():
    print(line)
archivo.close()