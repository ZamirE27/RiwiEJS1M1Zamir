print("***********************")
print("|  Calcula tu compra  |")
print("***********************\n")
 #creo la funcion promocion para en caso tal de existir un descuento sea aplicado y me muestre el valor completo
def promocion(nombre, precio, cantidad, porcentaje):
    precio = float(precio)
    porcentaje = float(porcentaje)
    cantidad = float(cantidad)
    subtotal = precio * cantidad
    descuento = (subtotal * porcentaje) / 100
    total = (subtotal - descuento)
    print(f"Nombre del producto: {nombre}")
    print(f"El valor unitario del producto es: {precio}")
    print(f"La cantidad del producto es: {cantidad}")
    print(f"El subtotal a pagar sin descuento: {subtotal}")
    print(f"El {porcentaje}% de descuento equivale a: {descuento}$")
    print(f"El total a pagar es {total}")

def sinpromocion(nombre, precio, cantidad):
    precio = float(precio)
    cantidad = float(cantidad)
    total = (precio * cantidad)
    print(f"El nombre del producto es: {nombre}")
    print(f"El valor unitario del producto es: {precio}")
    print(f"La cantidad del producto es: {cantidad}")
    print(f"El total a pagar es de: {total}$")

productos = ["leche","arroz","papas","jabon","pollo","queso", "pan","azucar","huevos","carne"] #creo un array o lista para validar la existencia del producto que de ingresara
    
#validacion del nombre, se valida con replace() que si no hay texto o si se ingresa un espacio lo remplace por no texto y asi llevar al usuario a un error para interlarlo nuevamente.
while True: #tenemos while para repetir el preceso hasta que el dato solicitado se ingrese de forma correcta
    nomprod = input("Ingrese el nombre del producto: \n").strip().lower()
    if nomprod.replace(" ", "").isalpha(): #isalpha me garantiza que todo se ingrese unicamente en texto
       if nomprod in productos:
            break
    print("ERROR: Nombre ingresado inválido, verificar que no tenga números ni caracteres especiales o que si tenga texto.")

#validamos que el precio del producto sea ingreado unicamente en numero 
while True:
    precioPro = input("ingrese el precio del producto: ").strip() #Usamos strip para elimiar cualquier espacion ingresado de forma involunaria sea al inicio o al final
    try: #tenemos el try para garantizar que al ingresar str permita cambiarlo a float sin tener bug en el codigo y de asi ser poner una alerta de error.
        valPrecioPro = float(precioPro)
        if valPrecioPro > 0:
            break
        else:
            print("ERROR: el numero ingresado debe ser mayor a cero y positivo")
    except:
        print("ERROR: el numero ingresado no debe tener texto ni caracteres especiales, intenta nuevamente")

#validamos que la cantidad del producto sea ingreada unicamente en numero 
while True: 
    cantPro = input("ingrese la cantidad del producto: ").strip()
    try:
        valCantPro = float(cantPro)
        if valCantPro > 0:
            break
        else:
            print("ERROR: el numero ingresado debe ser mayor a cero y positivo")
    except:
        print("ERROR: el numero ingresado no debe tener texto ni caracteres especiales, intenta nuevamente")

while True: #buscamos validar si aplica promocion o no
    aplPromPro = input("¿Aplica descuento?: (Si/No)\n").strip().lower() 
    if aplPromPro.replace(" ", "").isalpha() and aplPromPro == "si" or aplPromPro == "no": 
       break
    print("ERROR: respuesta no espesificada")

#si aplica primosion se valida que se ingrece un porcentaje en el rango aceptable solicitado y que se ingrese unicamente un dato numerico
while aplPromPro == "si":
    porProm = input("Ingrese el porcentaje de descuento, rango aceptable entre (0% y 100): ")
    try:
        valPorProm = float(porProm)
        if 0 < valPorProm < 100:
            promocion(nomprod,valPrecioPro, valCantPro, valPorProm) #si hay descuento se llama la funcion creada promocion para calcular el descuento segun lo valores ya ingresados anteriormente
            break
        else:
            print("ERROR: porcentaje ingresado esta fuera del rango aceptable, intenta nuevamente")
    except:
        print("ERROR: el numero ingresado no debe tener texto ni caracteres especiales, intenta nuevamente")
else:
    sinpromocion(nomprod,valPrecioPro, valCantPro) # no hay descuento llamamos la funcion creada sin descuento para mostrar el total de la compra

