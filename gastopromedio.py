#Define la función calcular_gasto_promedio(total_gastado, numero_dias) que reciba
#el total gastado en un viaje y la duración en días, y devuelva el gasto promedio diario.
print ("୨♡୧ Este es mi sistema para calcular el gasto promedio en un viaje, para ello necesitare que ingreses el presupuesto total del viaje, el total gastado hasta ahora y el número de días que llevas de viaje ୨♡୧")

print ("ʚ♡ɞ")

presupuesto = float(input("✎ Ingresa el presupuesto total del viaje: "))

print ("ʚ♡ɞ")

total_gastado = float(input("✎ Ingresa el total gastado en el viaje: "))

print ("ʚ♡ɞ")

numero_dias = int(input("✎ Ingresa el número de días que duró el viaje: "))

print ("ʚ♡ɞ")

def calcular_gasto_promedio(total_gastado, numero_dias):
    return total_gastado / numero_dias

def calcular_balance(presupuesto, gasto_promedio):
    return (presupuesto / numero_dias) - gasto_promedio

gasto_promedio = calcular_gasto_promedio(total_gastado, numero_dias)
balance_diario = calcular_balance(presupuesto, gasto_promedio)

print(f"✧ Gasto promedio diario: ${gasto_promedio:.2f}")
print(f"✧ Balance disponible por día: ${balance_diario:.2f}")