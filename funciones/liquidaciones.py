from estructuras import montos_diarios, liquidaciones

# TODO: crear funcion obtener id liquidacion

def obtener_ultimo_id(): 
    with open("estructuras/liquidaciones.txt", "r", encoding="utf-8") as archivo:
        lineas = [l.strip() for l in archivo.readlines() if l.strip()]

        if not lineas:
            return 1
        
        ultima_linea = lineas[-1]
        ultimo_id = ultima_linea.split(',')[0]
        return int(ultimo_id)

def calcular_liquidacion():
    id_liquidacion = obtener_ultimo_id() + 1
    empleado_liquidar = int(input("Ingrese el ID del empleado a liquidar: "))
    periodo_liquidar = input("Ingrese el periodo a liquidar (MM/YYYY): ")
    
    montos_existe = False
    total = 0
    horas_extra_total = 0

    with open("estructuras/montos.txt", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

        if not lineas:
            print("El archivo esta vacio.")
            return

        for linea in lineas:
            monto = linea.strip().split(',')

            id_empleado = int(monto[0])
            periodo, monto_empleado, horas_extra = monto[1], monto[3], monto[4]

            if id_empleado != empleado_liquidar or periodo != periodo_liquidar:
                continue
            
            montos_existe = True

            total += int(monto_empleado)
            horas_extra_total += int(horas_extra)

    if not montos_existe:
        print("No hay montos para el empleado y/o periodo ingresados.")
        return
    
    jubilacion = total * 0.11
    pensiones = total * 0.03
    obra_social = total * 0.03
    bruto = total
    neto = total - jubilacion - pensiones - obra_social
    deducciones = bruto - neto

    with open("estructuras/liquidaciones.txt", "r+", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

        if not lineas:
            print("El archivo esta vacio.")
            return

        # Estructura liquidaciones = {id_liquidacion: [id_empleado, sueldo_bruto, horas_extra, deducciones, periodo]}
        archivo.write(f"{id_liquidacion},{empleado_liquidar},{bruto},{horas_extra_total},{deducciones},{periodo_liquidar}\n")
        print(f"liquidacion realizada: {id_liquidacion}, {empleado_liquidar}, {bruto}, {horas_extra_total}, {deducciones}, {periodo_liquidar}")

def mostrar_liquidaciones():
    with open("estructuras/liquidaciones.txt", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

        if not lineas:
            print("El archivo esta vacio.")
            return
        
        for linea in lineas:
            liquidacion = linea.strip().split(',')

            id_liquidacion, id_empleado, sueldo_bruto, horas_extra, deducciones, periodo = liquidacion
            print(f"ID Liquidacion: {id_liquidacion}, ID Empleado: {id_empleado}, Sueldo Bruto: {sueldo_bruto}, Horas Extra: {horas_extra}, Deducciones: {deducciones}, Periodo: {periodo}.")


def eliminar_liquidacion():
    while True:
        id_input = input("Ingrese el ID de la liquidacion que quiere eliminar: ")
        if id_input.isdigit():
            id_liquidacion_eliminar = int(id_input)
            break
        print("El ID debe ser un numero")
    
    liquidacion_existe = False

    with open("estructuras/liquidaciones.txt", "r+", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

        if not lineas:
            print("El archivo esta vacio.")
            return
        
        for idx, linea in enumerate(lineas):
            liquidacion = linea.strip().split(',')

            id_liquidacion, id_empleado, sueldo_bruto, horas_extra, deducciones, periodo = liquidacion

            if int(id_liquidacion) != id_liquidacion_eliminar:
                continue

            liquidacion_existe = True

            while True:
                confirmacion = input(f"Esta seguro de eliminar la liquidacion con el ID liquidación: {id_liquidacion_eliminar} y ID empleado: {id_empleado}, 1 = Si, 2 = No: ")
                if confirmacion in ["1","2"]:
                    break
                print("La opcion debe ser 1 o 2")
            if confirmacion == "1":           
                del lineas[idx]

                archivo.seek(0)
                archivo.truncate(0)
                archivo.writelines(lineas)

    if not liquidacion_existe:
        print("No hay una liquidación con el ID ingresado.")
