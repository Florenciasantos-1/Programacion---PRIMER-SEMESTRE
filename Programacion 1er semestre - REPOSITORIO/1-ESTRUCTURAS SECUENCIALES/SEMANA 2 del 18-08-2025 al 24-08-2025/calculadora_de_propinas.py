#Calculadora de propinas en un restaurante
#Un restaurante quiere ayudar a sus clientes a calcular 
# cuánto dejar de propina según el monto de la cuenta.
#El programa debe:
#✓ Pedir al usuario el monto total de la cuenta.
#✓ Calcular la propina sugerida al 10%.
#✓ Calcular la propina sugerida al 15%.
#✓ Calcular el total a pagar en ambos casos (cuenta + propina).
#✓ Mostrar todos los resultados en pantalla.

#Ejemplo de ejecución
#Ingrese el monto de la cuenta: 3500
#Propina sugerida (10%): 350.0
#Total a pagar (10%): 3850.0
#Propina sugerida (15%): 525.0
#Total a pagar (15%): 4025.0

cuenta = float(input("Ingrese el monto total de la cuenta: "))

propina_1 = "10%"
porcentaje_propina_1 = 0.10
monto_propina_1 = cuenta * porcentaje_propina_1
total_pagar_1 = cuenta + monto_propina_1

propina_2 = "15%"
porcentaje_propina_2 = 0.15
monto_propina_2 = cuenta * porcentaje_propina_2
total_pagar_2 = cuenta + monto_propina_2


print(f"""
      El total de la cuenta es de ${cuenta}
      La propina sugerida del {propina_1} es de {monto_propina_1}, pagando un total de ${total_pagar_1}
      La propina sugerida del {propina_2} es de {monto_propina_2}, pagando un total de ${total_pagar_2}
      """)