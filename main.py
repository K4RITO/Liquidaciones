# TODO: añadir error handler y sentencias TRY EXCEPT FINALLY
# TODO: anañir funciones para modificar el diccionario tipo_trabajos
# estructura empleados = {id_empleado: [id_trabajo, turno, nombre, apellido, dni, telefono, edad]}
empleados = {1: [1, "mañana", "Juan", "Perez", "12345678", "555-1234", 30],
             2: [2, "tarde", "Maria", "Gomez", "87654321", "555-5678", 40],
             3: [1, "mañana", "Carlos", "Lopez", "11223344", "555-8765", 25],
             4: [2, "tarde", "Ana", "Martinez", "44332211", "555-4321", 35]}

# estructura tipo_trabajos = {(id_trabajo, turno): [puesto, sueldo_hora, area]}
# Actualmente tenemos id 1: obrero, id 2: gerente
tipo_trabajos = {(1, "mañana"): ["Obrero", 1000, "Produccion"],
                 (1, "tarde"): ["Obrero", 1200, "Produccion"],
                 (2, "mañana"): ["Gerente", 3000, "Administracion"],
                 (2, "tarde"): ["Gerente", 3000, "Administracion"]}

# estructura liquidaciones = {id_liquidacion: [id_empleado, sueldo_bruto, horas_extra, deducciones, periodo, id_jornada, premios]}
liquidaciones = {}

# estructura jornada = {(fecha, id_empleado): [horario_entrada, horario_salida]}
jornada = {("10/10/2025", 1): [8, 17],
           ("11/10/2025", 2): [8, 18],
           ("12/10/2025", 3): [8, 16],
           ("13/10/2025", 4): [9, 17]}

contador_empleado = 5


mensaje = "Que operacion quiere realizar: 1 = Agregar Empleado, 2 = Eliminar empleado, 3 = mostrar empleados, 4 = modificar empleado, 5 = Agregar jornada, 6 = Mostrar jornadas, 7 = Modificar horarios jornada, 8 = Eliminar Jornada, 9 = calcular monto del dia, 10 = salir: "
operacion = input(mensaje)

while int(operacion) not in range(1, 11):
    print("Opcion incorrecta, seleccione una opcion valida!")
    operacion = input(mensaje)
    
while operacion != "10":
    if operacion == "1":
        bandera = True
        #modificar esta funcion para que agregue el id del trabajo y el turno
        while bandera:
            id_trabajo = int(input("Ingrese el id del puesto: 1 = Obrero, 2 = Gerente: "))
            turno = input("Ingrese el turno del empleado: ")
            nombre = input("Ingrese el nombre del empleado: ")
            apellido = input("Ingrese el apellido del empleado: ")
            dni = input("Ingrese el DNI del empleado: ")
            telefono = input("Ingrese el telefono del empleado: ")
            edad = input("Ingrese la edad del empleado: ")

            empleados[contador_empleado] = [id_trabajo, turno, nombre, apellido, dni, telefono, edad]
            contador_empleado += 1
            
            continuar = input("Desea ingresar otro empleado: 1 = Si, 2 = No: ")
            if (continuar == "2"):
                bandera = False
    
    elif operacion == "2":
        empleado_a_eliminar = int(input("Ingrese el ID del empleado que quiere eliminar: "))

        if empleado_a_eliminar not in empleados.keys():
            print("El ID propusto no existe en la base de datos, pruebe con otro ID o revise los existentes.")
        else :
            confirmacion = int(input(f"Esta seguro de eliminar el empleado {empleados[empleado_a_eliminar]}, 1 = Si, 2 = No: "))
            if confirmacion == 1:
                empleados.pop(id)
    
    elif operacion == "3":
        for id, datos in empleados.items():
            id_trabajo, turno, nombre, apellido, dni, telefono, edad = datos
            print(f"ID: {id}, nombre: {nombre}, apellido: {apellido}, DNI: {dni}, telefono: {telefono}, ID trabajo: {id_trabajo}, edad: {edad}, turno: {turno}.")
    
    elif operacion == "4":
        id_empleado_modificar = int(input("Ingrese el ID del empleado que quiere modificar: "))
        
        for id, empleado in empleados.items():
            if id_empleado_modificar != id:
                continue

            etiquetas = ["id_trabajo", "turno", "nombre", "apellido", "dni", "telefono", "edad"]
            id_trabajo, turno, nombre, apellido, dni, telefono, edad = empleado

            for i in range(len(empleado)):
                modificar = input(f"Desea modificar {etiquetas[i]} de {nombre}, {apellido}? 1 = Si, 2 = No: ")
                if modificar != "1":
                    continue
                nuevo_valor = input(f"Ingrese el nuevo valor de {etiquetas[i]}: ")
                empleado[i] = nuevo_valor

    elif operacion == "5":
        fecha = input("Ingrese la fecha de la jornada (DD/MM/AAAA): ")
        id_empleado = input("Ingrese el ID del empleado: ")
        horario_entrada = int(input("Ingrese la hora de entrada (formato 24hs): "))
        horario_salida = int(input("Ingrese la hora de salida (formato 24hs): "))
        jornada [(fecha, id_empleado)] = [horario_entrada, horario_salida]
    
    elif operacion == "6":
        for id_jornada, datos_jornada in jornada.items():
            fecha, id_empleado = id_jornada
            horario_entrada, horario_salida = datos_jornada
            print(f"Fecha: {fecha}, ID Empleado: {id_empleado}, Hora Entrada: {horario_entrada}, Hora Salida: {horario_salida}.")
    
    elif operacion == "7":
        fecha_modificar = input("Ingrese la fecha de la jornada que quiere modificar (DD/MM/AAAA): ")
        id_empleado_modificar = int(input("Ingrese el ID del empleado de la jornada que quiere modificar: "))

        for id_jornada, datos_jornada in jornada.items():

            etiquetas = ["Horario de entrada", "Horario de Salida"]
            if fecha_modificar != id_jornada[0] or id_empleado_modificar != id_jornada[1]:
                continue

            for i in range(len(datos_jornada)):
                modificar = input(f"Desea modificar {etiquetas[i]}? 1 = Si, 2 = No: ")
                if modificar != "1":
                    continue
                nuevo_valor = input(f"Ingrese el nuevo valor de {etiquetas[i]}: ")
                datos_jornada[i] = int(nuevo_valor)

    elif operacion == "9":
        fecha_calcular = input("Ingrese la fecha que quiere calcular: ")
        id_empleado_calcular = int(input("Ingrese el ID del empleado que quiere calcular: "))
        turno_calcular = input("Ingrese el turno del empleado que quiere calcular (Mañana o Tarde): ").lower()

        for id_jornada, datos_jornada in jornada.items():
            horario_entrada = datos_jornada[0]
            horario_salida = datos_jornada[1]

            if fecha_calcular == id_jornada[0] and id_empleado_calcular == id_jornada[1]:
                horas_trabajadas = horario_salida - horario_entrada

                if horas_trabajadas > 8:
                    horas_extra = horas_trabajadas - 8
                    horas_trabajadas -= horas_extra

                for id_tipo_trabajo, datos_tipo_trabajo in tipo_trabajos.items():
                    id_puesto = id_tipo_trabajo[0]
                    turno_puesto = id_tipo_trabajo[1]
                    sueldo_hora = datos_tipo_trabajo[1]
                    if id_puesto == id_empleado_calcular and turno_calcular == turno_puesto:
                        monto_dia = horas_trabajadas * sueldo_hora + horas_extra * (sueldo_hora * 1.5)
                        print("El monto del dia es: ", monto_dia)

    operacion = input(mensaje)
