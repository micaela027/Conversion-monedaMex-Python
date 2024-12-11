# Paso 1: Definir valor actual del Euro y Dolar respecto al Peso
tipo_cambio_eur_a_mex = 23.70
tipo_cambio_usd_a_mex = 20.75

# Paso 2: Solicitar al usuario el tipo de conversión (Euro a Mex o Dolar a Mex)
tipo_conversion = input("Por favor ingrese la moneda origen para la conversion (EUR/USD) ").lower()

# Paso 3: Solicitar al usuario el monto a convertir
monto_a_convertir = float(input("Por favor ingrese la cantidad a convertir: "))

# Paso 4 y 5: Realizar la conversion usando el tipo de cambio correspondiente, mostrar resultado
if tipo_conversion.upper() == "EUR":
    resultado = monto_a_convertir * tipo_cambio_eur_a_mex
    print("El resultado de la conversion de EUR a Mex es: ",resultado)

elif tipo_conversion.upper() == "USD":
    resultado_usd = monto_a_convertir * tipo_cambio_usd_a_mex
    print("El resultado de la conversion de USD a Mex es: ",resultado_usd)

else:
    print("Lo sentimos, no podemos realizar esta conversion") 