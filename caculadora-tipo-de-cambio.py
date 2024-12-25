#1 qué moneda queres cambiar
#2 ingresar tipo de cambio de la moneda
#3 ingresar pesos a cambiar

pesos= float(input("Cuántos pesos tenés disponibles para cambiar? "))
moneda= input("Qué moneda querés cambiar? eur o usd? ")

if moneda == "eur":
    tc_eur= float(input("Cuál es el tipo de cambio euro peso? "))
    resultado_eur= pesos/tc_eur
    print("Con",pesos,"pesos, podés comprar:",resultado_eur,"euros")
elif moneda == "usd":
    tc_usd= float(input("Cuál es el tipo de cambio dolar peso? "))
    resultado_usd= pesos/tc_usd
    print("Con",pesos,"pesos, podés comprar:",resultado_usd,"dólares")
else:
    print("Lo siento. Tipo de cambio no disponible. Ingresa eur o usd")
