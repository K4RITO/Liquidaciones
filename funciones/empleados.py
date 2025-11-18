def obtener_dni_empleados():
    lista_dni = []

    with open("estructuras/empleados.txt", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

        if not lineas:
            return []
        
        for linea in lineas:
            empleado = linea.split(',')

            dni = empleado[4]

            lista_dni.append(dni)

    return lista_dni    

def obtener_ultimo_id(): 
    with open("estructuras/empleados.txt", "r", encoding="utf-8") as archivo:
        lineas = [l.strip() for l in archivo.readlines() if l.strip()]

        if not lineas:
            return 1
        
        ultima_linea = lineas[-1]
        ultimo_id = ultima_linea.split(',')[0]
        return int(ultimo_id)

def agregar_empleado():
    archivo = open("estructuras/empleados.txt", "a", encoding="utf-8")
    contador_empleado = obtener_ultimo_id() + 1

    bandera = True
    while bandera:
        while True:
            id_input = input("Ingrese el id del puesto: 1 = Obrero, 2 = Gerente: ")
            if id_input in ["1","2"]:
                id_trabajo = int(id_input)
                break
            print("El ID debe ser 1 o 2")
        
        while True:
            turno = input("Ingrese el turno del empleado: ")
            if turno.lower() in ["mañana", "tarde"]:
                break
            print("el Turno debe ser mañana o tarde")
        
        while True:
            nombre = input("Ingrese el nombre del empleado: ")
            if nombre.strip():
                break
            print("El nombre no puede estar vacio")
        
        while True:
            apellido = input("Ingrese el apellido del empleado: ")
            if apellido.strip():
                break
            print("El apellido no puede estar vacio")
        
        while True:
            dni = input("Ingrese el DNI del empleado: ")
            if dni.isdigit() and len(dni) == 8:
                lista_dni = obtener_dni_empleados()
                dni_existe = False
                for dni_existente in lista_dni:
                    if dni_existente == dni:
                        dni_existe = True
                        break

                if dni_existe:
                    print("Ya existe un empleado con ese DNI")
                else:
                    break
            else:
                print("El DNI debe ser de 8 digitos numericos")
        
        while True:
            telefono = input("Ingrese el telefono del empleado: ")
            if telefono.strip() and telefono.isdigit():
                telefono = int(telefono)
                break
            print("El numero de telefono debe ser un numero")
        
        while True:
            edad_input = input("Ingrese la edad del empleado: ")
            if edad_input.isdigit() and 18 <= int(edad_input) <= 65:
                edad = int(edad_input)
                break
            print("La edad debe ser un numero entre 18 y 65")

        archivo.write(f"{contador_empleado},{id_trabajo},{turno.capitalize()},{nombre.capitalize()},{apellido.capitalize()},{dni},{telefono},{edad}\n")
        
        while True:
            continuar = input("Desea ingresar otro empleado: 1 = Si, 2 = No: ")
            if continuar in ["1","2"]:
                break
            print("Opcion debe ser 1 o 2")
        if continuar == "2":
            bandera = False
            archivo.close()

def eliminar_empleado():
    while True:
        id_input = input("Ingrese el ID del empleado que quiere eliminar: ")
        if id_input.isdigit():
            empleado_a_eliminar = int(id_input)
            break
        print("El ID debe ser un numero")
    
    with open("estructuras/empleados.txt", "r+", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
        archivo.seek(0)
            
        if empleado_a_eliminar not in range(1, obtener_ultimo_id() + 1):
            print("Id fuera de rango.")
            return

        if not lineas:
            print("El archivo esta vacio.")
            return
        
        id_existe = False

        for idx, linea in enumerate(lineas):
            empleado = linea.split(',')

            id, nombre, apellido = empleado[0], empleado[3], empleado[4]

            if int(id) == empleado_a_eliminar:  
                id_existe = True
                while True:
                    confirmacion = input(f"Esta seguro de eliminar el empleado {nombre} {apellido}, 1 = Si, 2 = No: ")
                    if confirmacion in ["1","2"]:
                        break
                    print("La opcion debe ser 1 o 2")
                if confirmacion == "1":
                    del lineas[idx]          

                    archivo.truncate(0)
                    archivo.writelines(lineas)
        
        if not id_existe:
            print("El id dado no existe.")

def mostrar_empleados():
    archivo = open("estructuras/empleados.txt", "r", -1, "utf-8")
     
    lineas = archivo.readlines()
    
    if not lineas:
        print("El archivo esta vacio.")
    else:
        for linea in lineas:
            datos = linea.split(',')
            id, id_trabajo, turno, nombre, apellido, dni, telefono, edad = datos 
            
            print(f"ID: {id}, nombre: {nombre}, apellido: {apellido}, DNI: {dni}, telefono: {telefono}, ID trabajo: {id_trabajo}, edad: {edad[:-1]}, turno: {turno.capitalize()}.")
    
    archivo.close()

def modificar_empleado():
    while True:
        id_input = input("Ingrese el ID del empleado que quiere modificar: ")
        if id_input.isdigit():
            id_empleado_modificar = int(id_input)
            break
        print("El ID debe ser un numero")
    
    with open("estructuras/empleados.txt", "r+", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

        if not lineas:
            print("El archivo esta vacio.")
            return
        
        if id_empleado_modificar not in range(0, len(lineas) + 1):
            print("El id dado no corresponde a ningun id de la base de datos.")
            return
        
        for idx, linea in enumerate(lineas):
            empleado = linea.strip().split(',')
            
            id_empleado = int(empleado[0])

            if id_empleado != id_empleado_modificar:
                continue

            etiquetas = ["id_trabajo", "turno", "nombre", "apellido", "dni", "telefono", "edad"]

            for i in range(0, len(empleado) - 1):
                while True:
                    modificar = input(f"Desea modificar {etiquetas[i]} de {empleado[3]} {empleado[4]}? 1 = Si, 2 = No: ")
                    if modificar in ["1","2"]:
                        break
                    print("La opcion debe ser 1 o 2")
                if modificar != "1":
                    continue
                
                while True:
                    nuevo_valor = input(f"Ingrese el nuevo valor de {etiquetas[i]}: ")

                    if etiquetas[i] == "id_trabajo":
                        if nuevo_valor in ["1","2"]:
                            empleado[i + 1] = int(nuevo_valor)
                            break
                        print("La ID trabajo debe ser 1 o 2")
                    
                    elif etiquetas[i] == "turno":
                        if nuevo_valor.lower() in ["mañana","tarde"]:
                            empleado[i + 1] = nuevo_valor
                            break
                        print("El turno debe ser mañana o tarde")
                    
                    elif etiquetas[i] == "edad":
                        if nuevo_valor.isdigit() and 18 <= int(nuevo_valor) <= 65:
                            empleado[i + 1] = int(nuevo_valor)
                            break
                        print("la Edad debe ser un numero entre 18 y 65")
                    
                    elif etiquetas[i] == "dni":
                        if nuevo_valor.isdigit() and len(nuevo_valor) == 8:
                            dni_existe = False
                            lista_dni = obtener_dni_empleados()

                            for dni in lista_dni:
                                if dni == nuevo_valor:
                                    dni_existe = True
                                    break
                            
                            if dni_existe:
                                print("Ya existe un empleado con ese DNI")
                            else:
                                empleado[i + 1] = nuevo_valor
                                break
                        else:
                            print("El DNI debe ser 8 digitos")        
                    elif etiquetas[i] == "nombre" or etiquetas[i] == "apellido":
                        empleado[i + 1] = nuevo_valor.capitalize()
                        break
                    elif etiquetas[i] == "telefono":
                        if nuevo_valor.isdigit():
                            empleado[i + 1] = nuevo_valor
                            break
                        print("El telefono tiene que ser un numero")
            
            lineas[idx] = ",".join(map(str, empleado)) + "\n"

        archivo.seek(0)
        archivo.truncate(0)
        archivo.writelines(lineas)