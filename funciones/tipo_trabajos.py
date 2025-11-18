def agregar_tipo_trabajo():
    while True:
        id_input = input("Ingrese el ID del puesto: ")
        if id_input.isdigit():
            id_trabajo = int(id_input)
            break
        print("La ID debe ser numero.")
    
    while True:
        turno_trabajo = input("Ingrese el turno del puesto (Mañana o Tarde): ").lower()
        if turno_trabajo in ["mañana","tarde"]:
            break
        print("Turno debe ser mañana o tarde")
    
    tipo_trabajo_existe = False

    with open("estructuras/tipo_trabajos.txt", "r", encoding="utf-8") as archivo:
        lineas = [l for l in archivo.readlines() if l.strip()]

        if lineas:
            for linea in lineas:
                tipo_trabajo = linea.split(",")

                id_trabajo_existente, turno, puesto, sueldo_hora, area = tipo_trabajo

                if int(id_trabajo_existente) == id_trabajo and turno.lower() == turno_trabajo:
                    tipo_trabajo_existe = True

    if tipo_trabajo_existe:
        print("Ya hay un puesto con esa ID y turno")
        return

    while True:
        puesto = input("Ingrese el nombre del puesto: ")
        if puesto.strip():
            break
        print("Puesto no puede estar vacio")
    
    while True:
        sueldo_input = input("Ingrese el sueldo por hora del puesto: ")
        if sueldo_input.isdigit() and int(sueldo_input) > 0:
            sueldo_hora = int(sueldo_input)
            break
        print("Sueldo debe ser numero positivo")
    
    while True:
        area = input("Ingrese el area del puesto: ")
        if area.strip():
            break
        print("Area no puede estar vacia")

    with open("estructuras/tipo_trabajos.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{id_trabajo},{turno_trabajo.lower()},{puesto.lower()},{sueldo_hora},{area.lower()}\n")
    print("Tipo de trabajo agregado correctamente")

def mostrar_tipos_trabajos():

    with open("estructuras/tipo_trabajos.txt", "r", encoding="utf-8") as archivo:
        lineas = [l for l in archivo.readlines() if l.strip()]

        if not lineas:
            print("El archivo esta vacio.")
            return

        for linea in lineas:
            tipo_trabajo = linea.split(",")

            id_trabajo, turno, puesto, sueldo_hora, area = tipo_trabajo
            print(f"ID Puesto: {id_trabajo}, Turno: {turno}, Puesto: {puesto}, Sueldo por hora: {sueldo_hora}, Area: {area[:-1]}.")

def modificar_tipo_trabajo():

    while True:
        id_input = input("Ingrese el ID del puesto que quiere modificar: ")
        if id_input.isdigit():
            id_trabajo_modificar = int(id_input)
            break
        print("ID debe ser numero")
    
    while True:
        turno_modificar = input("Ingrese el turno del puesto que quiere modificar (Mañana o Tarde): ").lower()
        if turno_modificar in ["mañana","tarde"]:
            break
        print("Turno debe ser manana o tarde")

    tipo_trabajo_existe = False
    
    with open("estructuras/tipo_trabajos.txt", "r", encoding="utf-8") as archivo:
        lineas = [l for l in archivo.readlines() if l.strip()]

        if not lineas:
            print("El archivo esta vacio.")
        else:
            for linea in lineas:
                tipo_trabajo = linea.strip().split(",")

                id_trabajo, turno = tipo_trabajo[0], tipo_trabajo[1]

                if int(id_trabajo) == id_trabajo_modificar and turno == turno_modificar:
                    tipo_trabajo_existe = True

    if not tipo_trabajo_existe:
        print("El tipo de trabajo no existe.")
        return

    with open("estructuras/tipo_trabajos.txt", "r+", encoding="utf-8") as archivo:
        lineas = [l for l in archivo.readlines() if l.strip()]

        if not lineas:
            print("El archivo esta vacio.")
            return

        tipo_trabajo_encontrada = False

        for idx, linea in enumerate(lineas):
            tipo_trabajo = linea.split(",")
            id_trabajo, turno, puesto, sueldo_hora, area = tipo_trabajo
            
            if int(id_trabajo) != id_trabajo_modificar:
                continue
            tipo_trabajo_encontrada = True
            datos_tipo_trabajo = [turno, puesto, sueldo_hora, area]
            etiquetas = ["turno", "puesto", "sueldo hora", "area"]

            for i in range(len(datos_tipo_trabajo)):
                while True:
                    modificar = input(f"Desea modificar {etiquetas[i]}? 1 = Si, 2 = No: ")
                    if modificar in ["1","2"]:
                        break
                    print("Opcion debe ser 1 o 2")
                if modificar != "1":
                    continue
                
                while True:
                    nuevo_valor = input(f"Ingrese el nuevo valor de {etiquetas[i]}: ")
                    if etiquetas[i] == "sueldo_hora":
                        if nuevo_valor.isdigit() and int(nuevo_valor) > 0:
                            datos_tipo_trabajo[i] = int(nuevo_valor)
                            break
                        print("Sueldo debe ser numero positivo")
                    else:
                        if nuevo_valor.strip():
                            datos_tipo_trabajo[i] = nuevo_valor
                            break
                        print("El campo no puede estar vacio")

            nueva_linea = f"{id_trabajo},{datos_tipo_trabajo[0].lower()},{datos_tipo_trabajo[1].lower()},{datos_tipo_trabajo[2]},{datos_tipo_trabajo[3].lower()}\n"

            lineas[idx] = nueva_linea

            break

        if not tipo_trabajo_encontrada:
            print("Tipo trabajo no encontrado.")
            return

        archivo.seek(0)
        archivo.truncate(0)
        archivo.writelines(lineas)
    
def eliminar_tipo_trabajo():
    while True:
        id_input = input("Ingrese el ID del puesto que quiere eliminar: ")
        if id_input.isdigit():
            id_trabajo_eliminar = int(id_input)
            break
        print("ID debe ser numero")
    
    while True:
        turno_eliminar = input("Ingrese el turno del puesto que quiere eliminar (Mañana o Tarde): ").lower()
        if turno_eliminar in ["mañana","tarde"]:
            break
        print("Turno debe ser manana o tarde")
    
    with open("estructuras/tipo_trabajos.txt", "r+", encoding="utf-8") as archivo:
        lineas = [l for l in archivo.readlines() if l.strip()]

        if not lineas:
            print("El archivo esta vacio.")
            return

        tipo_trabajo_encontrada = False

        for idx, linea in enumerate(lineas):
            tipo_trabajo = linea.split(",")

            id_trabajo, turno = tipo_trabajo[0], tipo_trabajo[1]

            if int(id_trabajo) != id_trabajo_eliminar or turno != turno_eliminar:
                continue
        
            tipo_trabajo_encontrada = True
                
            while True:
                confirmacion = input(f"Esta seguro de eliminar el tipo de trabajo con ID {id_trabajo_eliminar} y turno {turno_eliminar}, 1 = Si, 2 = No: ")
                if confirmacion in ["1","2"]:
                    break
                print("Opcion debe ser 1 o 2")
            if confirmacion == "1":
                del lineas[idx]
                print("Tipo de trabajo eliminado correctamente")

        if not tipo_trabajo_encontrada:
            print("Jornada no encontrada.")
            return

        archivo.seek(0)
        archivo.truncate(0)
        archivo.writelines(lineas)

