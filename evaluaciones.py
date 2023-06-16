#diccionario
curso1 = {
    "name" :"curso basico de fotografia" ,
    "instructor": "luis olivares"}
curso2 ={
    "name": "programacion de software",
    "instructor":"william mayorga"
  }

def evaluaciones_curso1():
   
    print("Elementos primordiales para una buena fotografia.\n a=Iluminacion \n b=Composicion. \n c=Perspectiva. \n d=Ninguna de las anteriores.\n e=Todas las anteriores.")
    pregunta1 = input("seleccione una respuesta: ")
    if(pregunta1=="e"):
          print("Respuesta correcta")
    else:
          print("Respuesta incorrecta")
    
def escoger():
    curso1="programacion software"
    curso2="basico de fotografia"
    res= " "
    cursos = input("Que curso desea realizar: ")
    if(cursos=="curso 1"):
        res= input("Iniciar curso: ")
        if(res == "si"):
            res= input("ver video")
            evaluaciones_curso1()
        else:
            escoger()
    elif(cursos=="curso 2"):
        print("ver video curso 2")



escoger()

print("amor")
    