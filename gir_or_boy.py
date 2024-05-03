
#Escribir una funcion que determine el genero de un usuario basandose en su nombre.

def gir_or_boy(nombre_usuario):
  caracteres_distintos = len(nombre_usuario)
  #condicion para determinar si es para o impar
  if caracteres_distintos % 2 == 0:
    return "¡ITS A GIRL!" + " Puedes chatear con:" + nombre_usuario
    
  else:
    return "¡ITS A BOY" + " Mejor ignoralo"
  
print(gir_or_boy("marta"))

