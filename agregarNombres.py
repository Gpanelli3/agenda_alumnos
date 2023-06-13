archivo=open('agregar.txt','w')

cantidad=int(input('ingresar la cantidad de nombres de los alumnos'))
lista=[]
notas=[]
lista_alumnos={}

archivo.write('NOTAS DE LOS ALUMNOS')
archivo.write('\n')
archivo.write('\n')

for i in range(0,cantidad):
    alumno=input('Ingresar nombre de alumno')
    nota=input('ingresar su nota')

    archivo.write('nombre: ')
    archivo.write(alumno)
    archivo.write(', ')
    archivo.write('su nota es: ')
    archivo.write(nota)
    archivo.write('\n')

    lista_alumnos[alumno]=nota
#print(lista_alumnos)


archivo.close()
