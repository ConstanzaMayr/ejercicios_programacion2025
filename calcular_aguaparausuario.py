 #

peso_kg = int (input("Ingrese su peso en números, sin letras: "))
nivel_actividad = (input("Ingrese su nivel de actividad (bajo, medio, alto): "))

def calcular_objetivo_ml (peso_kg, nivel_actividad):
        base = peso_kg * 35

        if nivel_actividad == "bajo":
          return base * 0.90
        elif nivel_actividad == "alto":
            return base * 1.10
        else:  #nivel_actividad == "medio"
            return base


objetivo_ml = calcular_objetivo_ml(peso_kg, nivel_actividad)

consumo_ml = int(input("Ingrese su consumo de agua en ml: "))

def estado_hidratacion(consumo_ml, objetivo_ml):
    porcentaje = (consumo_ml / objetivo_ml) * 100

    if porcentaje == 100:
        return "Has alcanzado tu objetivo"
    elif porcentaje < 100:
        falta = 100 - porcentaje
        return f"Te falta un {falta:.1f}% para llegar al objetivo"
    else:
        exceso = porcentaje - 100
        return f"Has excedido tu objetivo en un {exceso:.1f}%"


estado = estado_hidratacion(consumo_ml, objetivo_ml)

print(f"\nObjetivo diario de hidratación: {objetivo_ml:.0f} ml")
print(estado)