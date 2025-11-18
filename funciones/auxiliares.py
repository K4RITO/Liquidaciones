def calcular_horas_trabajadas(hora_entrada, hora_salida):
    hora_entrada = int(hora_entrada)
    hora_salida = int(hora_salida)

    if hora_salida < hora_entrada:
        return (24 - hora_entrada) + hora_salida
    else:
        return hora_salida - hora_entrada