from funciones.auxiliares import calcular_horas_trabajadas

def calcular_monto():
    while True:
        fecha_calcular = input("Ingrese la fecha que quiere calcular: ")
        if fecha_calcular.strip():
            break
        print("Fecha no puede estar vacia")
    
    while True:
        id_input = input("Ingrese el ID del empleado que quiere calcular: ")
        if id_input.isdigit():
            id_empleado_calcular = int(id_input)
            break
        print("ID debe ser numerico")
    
    id_trabajo_empleado = 0
    turno_empleado = ""

    # Verificamos que el empleado exista
    id_existe = False

    # Guardamos los datos del empleado
    datos_empleado = []
    
    with open("estructuras/empleados.txt", "r", -1, "utf-8") as archivo:           
        lineas_empleado = archivo.readlines()
        
        if not lineas_empleado:
            print("El archivo esta vacio.")
        else:    
            for linea_empleado in lineas_empleado:
                empleado = linea_empleado.split(',')

                id = empleado[0]
                id_trabajo_empleado = empleado[1]
                turno_empleado = empleado[2]

                if int(id) != id_empleado_calcular:
                    continue
                
                datos_empleado = empleado
                id_existe = True

    if not id_existe:
        print("El id ingresado no existe.")
        return
    
    # Verificamos que la jornada exista
    clave_jornada_existe = False

    # Creamos una variable para almacenar la jornada
    datos_jornada = []

    with open("estructuras/jornadas.txt", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

        if not lineas:
            print("El archivo esta vacio.")
            return

        for linea in lineas:
            jornada = linea.split(",")

            fecha, id_empleado, horario_entrada, horario_salida = jornada

            if fecha == fecha_calcular and int(id_empleado) == id_empleado_calcular:
                clave_jornada_existe = True
                datos_jornada = jornada
                
    if not clave_jornada_existe:
        print("No existe jornada para esa fecha y empleado")
        return

    # Verificamos que el tipo de trabajo exista
    tipo_trabajo_existe = False

    # Creamos una variable para almacenar el sueldo horario
    sueldo_hora = 0
    
    with open("estructuras/tipo_trabajos.txt", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

        if not lineas:
            print("El archivo esta vacio.")
            return

        for linea in lineas:
            tipo_trabajo = linea.split(",")

            id_trabajo, turno, puesto, sueldo_hora_trabajo, area = tipo_trabajo

            if id_trabajo == id_trabajo_empleado and turno == turno_empleado:
                tipo_trabajo_existe = True
                sueldo_hora = int(sueldo_hora_trabajo)

    if not tipo_trabajo_existe:
        print("No existe configuracion de salario para ese puesto y turno")
        return

    # Calculamos las horas trabajadas
    horario_entrada = datos_jornada[2]
    horario_salida = datos_jornada[3]
    
    horas_trabajadas = calcular_horas_trabajadas(horario_entrada, horario_salida)
    horas_extra = 0

    if horas_trabajadas > 8:
        horas_extra = horas_trabajadas - 8
        horas_normales = 8
    else:
        horas_normales = horas_trabajadas

    monto_dia = horas_normales * sueldo_hora + horas_extra * (sueldo_hora * 1.5)
    
    # Mostramos los datos del empleado y el sueldo
    nombre_empleado = datos_empleado[3]
    apellido_empleado = datos_empleado[4]
    print(f"Empleado: {nombre_empleado} {apellido_empleado}")
    print(f"Horas trabajadas: {horas_trabajadas} (Normales: {horas_normales}, Extra: {horas_extra})")
    print(f"Sueldo por hora: ${sueldo_hora}")
    print(f"Monto del dia: ${monto_dia:.2f}")
    
    periodo = fecha_calcular[3:]

    with open("estructuras/montos.txt", "a+", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

        if not lineas:
            archivo.write(f"{id_empleado_calcular},{periodo},{fecha_calcular},{monto_dia},{horas_trabajadas},{horas_extra}\n")
            return

        for linea in lineas:
            monto = linea.strip().split(',')

            id_empleado, periodo_monto = monto[0], monto[1]

            if id_empleado == id_empleado_calcular and periodo_monto == fecha_calcular[3:]:
                print("Ya hay un monto con el empleado y periodo propuestos.")
                return
            
            nueva_linea = f"{id_empleado_calcular},{periodo},{fecha_calcular},{monto},{horas_trabajadas},{horas_extra}"
            archivo.write(nueva_linea)

def mostrar_montos():
    # Estructura montos_diarios = {(id_empleado, periodo): [fecha, monto, horas_trabajadas, horas_extra]}

    with open("estructuras/montos.txt", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

        if not lineas:
            print("El archivo esta vacio.")
            return

        for linea in lineas:
            monto = linea.strip().split(',')

            id_empleado = int(monto[0])
            periodo, fecha, monto, horas_trabajadas, horas_extra = monto[1:]

            with open("estructuras/empleados.txt", "r", -1, "utf-8") as archivo:           
                lineas_empleado = archivo.readlines()
                
                if not lineas_empleado:
                    print("El archivo esta vacio.")
                    return
                
                for linea_empleado in lineas_empleado:
                    empleado = linea_empleado.split(',')
                    id, nombre, apellido = empleado[0], empleado[3], empleado[4]

                    if int(id) != id_empleado:
                        continue 
                    
                    print(f"Empleado: {nombre} {apellido}")
                    print(f"Periodo: {periodo}")
                    print(f"Dia: {fecha}, monto: {monto}, horas trabajadas: {horas_trabajadas}, horas extra: {horas_extra}")

def actualizar_monto():
    empleado_actualizar = int(input("Ingrese el ID del empleado a actualizar el monto: "))
    periodo_actualizar = input("Ingrese el periodo a actualizar (MM/YYYY): ")
    fecha_actualizar = input("Ingrese la fecha a actualizar (DD/MM/YYYY): ")

    monto_existe = False

    with open("estructuras/montos.txt", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    if not lineas:
        print("No hay montos en la base de datos.")
        return

    for idx, linea in enumerate(lineas):
        partes = linea.strip().split(',')

        if len(partes) < 6:
            continue

        id_empleado, periodo, fecha, monto, horas_trabajadas, horas_extra = partes

        if (
            int(id_empleado) == empleado_actualizar and
            periodo == periodo_actualizar and
            fecha == fecha_actualizar
        ):
            monto_existe = True

            nuevo_monto_input = input("Ingrese el nuevo monto: ")
            try:
                nuevo_monto = int(nuevo_monto_input)
            except:
                print("El monto debe ser un número.")
                return

            lineas[idx] = f"{id_empleado},{periodo},{fecha},{nuevo_monto},{horas_trabajadas},{horas_extra}\n"
            break

    if not monto_existe:
        print("Monto no encontrado.")
        return

    with open("estructuras/montos.txt", "w", encoding="utf-8") as archivo:
        archivo.writelines(lineas)

    print("Monto actualizado correctamente.")

def eliminar_monto():
    empleado_eliminar = int(input("Ingrese el ID del empleado a eliminar el monto: "))
    periodo_eliminar = input("Ingrese el periodo a eliminar (MM/YYYY): ")
    fecha_eliminar = input("Ingrese el periodo a eliminar (DD/MM/YYYY): ")

    with open("estructuras/montos.txt", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    if not lineas:
        print("No hay montos en la base de datos.")
        return

    monto_existe = False

    for idx, linea in enumerate(lineas):
        partes = linea.strip().split(',')
        if len(partes) < 6:
            continue

        id_empleado, periodo, fecha = partes[0], partes[1], partes[2]

        if int(id_empleado) == empleado_eliminar and periodo == periodo_eliminar and fecha == fecha_eliminar:
            monto_existe = True

            confirmacion = input(
                f"¿Está seguro de eliminar el monto del empleado {id_empleado} en el periodo {periodo}? "
                "(1 = Sí, 2 = No): "
            )

            if confirmacion == "1":
                del lineas[idx]

                with open("estructuras/montos.txt", "w", encoding="utf-8") as archivo:
                    archivo.writelines(lineas)

                print("Monto eliminado correctamente.")
            else:
                print("Operación cancelada.")
            break

    if not monto_existe:
        print("Monto no encontrado.")

