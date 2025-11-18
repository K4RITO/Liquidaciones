def agregar_jornada():
    while True:
        fecha = input("Ingrese la fecha de la jornada (DD/MM/AAAA): ")
        if fecha.strip():
            break
        print("La fecha no puede estar vacia")
    
    while True:
        id_input = input("Ingrese el ID del empleado: ")
        if id_input.isdigit():
            id_empleado = int(id_input)
            break
        print("La ID debe ser numero")
    
    id_existe = False

    with open("estructuras/empleados.txt", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

        if not lineas:
            print("El archivo esta vacio.")
        else:    
            for linea in lineas:
                jornada = linea.split(',')
                
                id = int(jornada[0])
                
                if id != id_empleado:
                    continue
                
                id_existe = True
    
    if not id_existe:
        print("El empleado no existe")
        return
    
    while True:
        entrada_input = input("Ingrese la hora de entrada (formato 24hs): ")
        if entrada_input.isdigit() and 00 <= int(entrada_input) <= 23:
            horario_entrada = int(entrada_input)
            break
        print("La hora debe ser entre 00 y 23")
    
    while True:
        salida_input = input("Ingrese la hora de salida (formato 24hs): ")
        if salida_input.isdigit() and 00 <= int(salida_input) <= 23:
            horario_salida = int(salida_input)
            break
        print("La hora debe ser entre 00 y 23")

    with open("estructuras/jornadas.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{fecha},{id_empleado},{horario_entrada},{horario_salida}\n")
    print("Jornada agregada correctamente")

def mostrar_jornadas():
    with open("estructuras/jornadas.txt", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

        if not lineas:
            print("El archivo esta vacio.")
            return

        for linea in lineas:
            jornada = linea.split(",")

            fecha, id_empleado, horario_entrada, horario_salida = jornada
            print(f"Fecha: {fecha}, ID Empleado: {id_empleado}, Hora Entrada: {horario_entrada}, Hora Salida: {horario_salida[:-1] if horario_salida.endswith("\n") else horario_salida}.")

def modificar_jornada():
    while True:
        fecha_modificar = input("Ingrese la fecha de la jornada que quiere modificar (DD/MM/AAAA): ")
        if fecha_modificar.strip():
            break
        print("La fecha no puede estar vacia")
    
    while True:
        id_input = input("Ingrese el ID del empleado de la jornada que quiere modificar: ")
        if id_input.isdigit():
            id_empleado_modificar = int(id_input)
            break
        print("La ID debe ser numero")

    with open("estructuras/jornadas.txt", "r+", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

        if not lineas:
            print("El archivo esta vacio.")
            return

        # para validar que exista la jornada
        jornada_existe = False

        for idx, linea in enumerate(lineas):
            jornada = linea.strip().split(",")

            if jornada == "":
                continue

            fecha, id_empleado, horario_entrada, horario_salida = jornada

            if int(id_empleado) != id_empleado_modificar or fecha != fecha_modificar:
                continue
            
            jornada_existe = True
            etiquetas = ["Horario de entrada", "Horario de Salida"]
            
            datos_jornada = [horario_entrada, horario_salida]
            
            for i in range(0, len(datos_jornada)):
                while True:
                    modificar = input(f"Desea modificar {etiquetas[i]}? 1 = Si, 2 = No: ")
                    if modificar in ["1","2"]:
                        break
                    print("La opcion debe ser 1 o 2")
                if modificar != "1":
                    continue
                
                while True:
                    nuevo_valor = input(f"Ingrese el nuevo valor de {etiquetas[i]}: ")
                    if nuevo_valor.isdigit() and 00 <= int(nuevo_valor) <= 23:
                        datos_jornada[i] = int(nuevo_valor)
                        break
                    print("La hora debe ser entre 00 y 23")
            
            nueva_linea = f"{fecha},{id_empleado},{datos_jornada[0]},{datos_jornada[1]}\n"

            lineas[idx] = nueva_linea

            break

        if not jornada_existe:
            print("Jornada no encontrada.")
            return

        archivo.seek(0)
        archivo.truncate(0)
        archivo.writelines(lineas)

def eliminar_jornada():
    while True:
        fecha_eliminar = input("Ingrese la fecha de la jornada que quiere eliminar (DD/MM/AAAA): ")
        if fecha_eliminar.strip():
            break
        print("La fecha no puede estar vacia")
    
    while True:
        id_input = input("Ingrese el ID del empleado de la jornada que quiere eliminar: ")
        if id_input.isdigit():
            id_empleado_eliminar = int(id_input)
            break
        print("La ID debe ser numero")
    
    with open("estructuras/jornadas.txt", "r+", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

        if not lineas:
            print("El archivo esta vacio.")
            return

        # para validar que exista la jornada
        jornada_existe = False

        for idx, linea in enumerate(lineas):
            jornada = linea.split(",")

            fecha, id_empleado = jornada[0], int(jornada[1])

            if id_empleado != id_empleado_eliminar or fecha != fecha_eliminar:
                continue
            
            jornada_existe = True
            
            while True:
                confirmacion = input(f"Esta seguro de eliminar la jornada del empleado con ID {id_empleado_eliminar} en la fecha {fecha_eliminar}, 1 = Si, 2 = No: ")
                if confirmacion in ["1","2"]:
                    break
                print("La opcion debe ser 1 o 2")
            
            if confirmacion == "1":
                lineas.pop(idx)
                print("Jornada eliminada correctamente")
                break


        if not jornada_existe:
            print("Jornada no encontrada.")
            return

        archivo.seek(0)
        archivo.truncate(0)
        archivo.writelines(lineas)