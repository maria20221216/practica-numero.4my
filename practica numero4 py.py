# este es un comentario realizado en el codigo presionar Ctrl + S

"""
consigna: 
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
PREGUNTE al usuario la nota que ha sacado en cada asignatura y ELIMINE de la lista las asignaturas aprobadas. 
Al final el programa debe MOSTRAR por pantalla las asignaturas que el usuario tiene que repetir.
"""
materias = ["matwmatica", "fisica", "Quimica", "historica", "lengua"]

aprobadas= []

for materia in  materias: 
    nota = float(input("¿que nota has sacado en " + materia + " ? " ))
    
    if nota >= 5: 
        aprobadas.append(materia)

for materia in aprobadas: 
     materias.remove(materia)

print("tiene que repetir" + str (materia))



        
           
