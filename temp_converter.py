def temperature_converter():
    # Pedir ao usuário para inserir a temperatura
    temperature = float(input("Insira a temperatura: "))
    # Pedir ao usuário para inserir a unidade de medida da temperatura (C, F ou K)
    unit = input("Insira a unidade de medida (C, F ou K): ").upper()

    # Verificar qual unidade de medida foi inserida e converter para as outras unidades
    if unit == "C":
        fahrenheit = (temperature * 9/5) + 32
        kelvin = temperature + 273.15
        print("%.2f graus Celsius é igual a %.2f graus Fahrenheit e %.2f Kelvin" % (temperature, fahrenheit, kelvin))
    elif unit == "F":
        celsius = (temperature - 32) * 5/9
        kelvin = (temperature + 459.67) * 5/9
        print("%.2f graus Fahrenheit é igual a %.2f graus Celsius e %.2f Kelvin" % (temperature, celsius, kelvin))
    elif unit == "K":
        celsius = temperature - 273.15
        fahrenheit = (temperature * 9/5) - 459.67
        print("%.2f Kelvin é igual a %.2f graus Celsius e %.2f graus Fahrenheit" % (temperature, celsius, fahrenheit))
    else:
        print("Unidade de medida inválida. Por favor, insira C, F ou K.")

# Chamar a função para iniciar o conversor de temperaturac
temperature_converter()
