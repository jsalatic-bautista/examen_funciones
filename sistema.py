from funciones import validador
persona = []
apellido = str(input("Ingrese su apellido: "))
persona.append(apellido)
año = int(input("Ingrese su año de nacimiento: "))
persona.append(año)
altura = int(input("Ingrese su altura en cm: "))
persona.append(altura)
resultado = validador(persona)
if resultado[0]:
    print("Nacido en 2010 o mas")
if resultado[1]:
    print("Cumple con la altura")
