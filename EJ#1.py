print("***********************")
print("|  Calcula tu compra  |")
print("***********************\n")
 #creo la funcion promocion para en caso tal de existir un descuento sea aplicado y me muestre el valor completo
def hasPromotion(name, price, quantity, percentage):
    price = float(price)
    percentage = float(percentage)
    quantity = float(quantity)
    subtotal = price * quantity
    discount = (subtotal * percentage) / 100
    total = (subtotal - discount)
    print(f"Nombre del producto: {name}")
    print(f"El valor unitario del producto es: {price}")
    print(f"La cantidad del producto es: {quantity}")
    print(f"El subtotal a pagar sin descuento: {subtotal}")
    print(f"El {percentage}% de descuento equivale a: {discount}$")
    print(f"El total a pagar es {total}")

def notPromotion(name, price, quantity):
    price = float(price)
    quantity = float(quantity)
    total = (price * quantity)
    print(f"El nombre del producto es: {name}")
    print(f"El valor unitario del producto es: {price}")
    print(f"La cantidad del producto es: {quantity}")
    print(f"El total a pagar es de: {total}$")

products = ["leche","arroz","papas","jabon","pollo","queso", "pan","azucar","huevos","carne"] #creo un array o lista para validar la existencia del producto que de ingresara
    
#validacion del nombre, se valida con replace() que si no hay texto o si se ingresa un espacio lo remplace por no texto y asi llevar al usuario a un error para interlarlo nuevamente.
while True: #tenemos while para repetir el preceso hasta que el dato solicitado se ingrese de forma correcta
    productName = input("Ingrese el nombre del producto: \n").strip().lower()
    if productName.replace(" ", "").isalpha(): #isalpha me garantiza que todo se ingrese unicamente en texto
       if productName in products:
            break
    print("ERROR: Nombre ingresado inválido, verificar que no tenga números ni caracteres especiales o que si tenga texto.")

#validamos que el precio del producto sea ingreado unicamente en numero 
while True:
    productPrice = input("ingrese el precio del producto: ").strip() #Usamos strip para elimiar cualquier espacion ingresado de forma involunaria sea al inicio o al final
    try: #tenemos el try para garantizar que al ingresar str permita cambiarlo a float sin tener bug en el codigo y de asi ser poner una alerta de error.
        productPriceValid = float(productPrice)
        if productPriceValid > 0:
            break
        else:
            print("ERROR: el numero ingresado debe ser mayor a cero y positivo")
    except:
        print("ERROR: el numero ingresado no debe tener texto ni caracteres especiales, intenta nuevamente")

#validamos que la cantidad del producto sea ingreada unicamente en numero 
while True: 
    productQty = input("ingrese la cantidad del producto: ").strip()
    try:
        productQtyVald = float(productQty)
        if productQtyVald > 0:
            break
        else:
            print("ERROR: el numero ingresado debe ser mayor a cero y positivo")
    except:
        print("ERROR: el numero ingresado no debe tener texto ni caracteres especiales, intenta nuevamente")

while True: #buscamos validar si aplica promocion o no
    hasDiscount = input("¿Aplica descuento?: (Si/No)\n").strip().lower() 
    if hasDiscount.replace(" ", "").isalpha() and hasDiscount == "si" or hasDiscount == "no": 
       break
    print("ERROR: respuesta no espesificada")

#si aplica primosion se valida que se ingrece un porcentaje en el rango aceptable solicitado y que se ingrese unicamente un dato numerico
while hasDiscount == "si":
    discountPercentage = input("Ingrese el porcentaje de descuento, rango aceptable entre (0% y 100): ")
    try:
        discountPercentValid = float(discountPercentage)
        if 0 < discountPercentValid < 100:
            hasPromotion(productName,productPriceValid, productQtyVald, discountPercentValid) #si hay descuento se llama la funcion creada promocion para calcular el descuento segun lo valores ya ingresados anteriormente
            break
        else:
            print("ERROR: porcentaje ingresado esta fuera del rango aceptable, intenta nuevamente")
    except:
        print("ERROR: el numero ingresado no debe tener texto ni caracteres especiales, intenta nuevamente")
else:
    notPromotion(productName,productPriceValid, productQtyVald) # no hay descuento llamamos la funcion creada sin descuento para mostrar el total de la compra

