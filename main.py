# -*- coding:utf-8 -*-


# estructura empleados = {id_empleado: [id_trabajo, turno, nombre, apellido, dni, telefono, edad]}
empleados = {}
# estructura tipo_trabajos = {(id_trabajo, turno):[puesto, sueldo_hora, entrada, salida, area]}
tipo_trabajos = {}
# estructura liquidaciones = {id_liquidacion: [id_empleado, sueldo_bruto, horas_extra, deducciones, periodo, id_jornada, premios]}
liquidaciones = {}
# estructura jornada = {(fecha, id_empleado): [horario_entrada, horario_salida]}
jornada = {}
contador_empleado = 1
empleado = []


mensaje = "Que operacion quiere realizar: 1 = Agregar Empleado, 2 = Eliminar empleado, 3 = mostrar empleados, 4 = modificar puesto, 5 = calcular monto del dia, 10 = salir "
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

            empleados[contador_empleado] = [id_trabajo, turno, nombre, apellido, dni, telefono]
            contador_empleado =+ 1
            
            continuar = input("Desea ingresar otro empleado: 1 = Si, 2 = No: ")
            if (continuar == "2"):
                bandera = False
    
    elif operacion == "2":
        empleado_a_eliminar = input ("Ingrese el ID del empleado que que quiere eliminar: ")
        for id, datos in empleados:
            if empleado_a_eliminar == id:
                empleados.pop(id)
    
    elif operacion == "3":
        indice = 0
        for id,datos in empleados.items():
            nombre = datos[0]
            apellido = datos[1]
            dni = datos[2]
            telefono = datos[3]
            id_puesto = datos[4]
            empleado.append(nombre)
            empleado.append(apellido)
            empleado.append(dni)
            empleado.append(telefono)
            empleado.append(id_puesto)
            indice =+1
            print(indice,"-nombre: ", empleado[0],"apellido: ", empleado[1], "dni: ", empleado [2],"telefono: ", empleado[3], "ID puesto: ", empleado[4])
    
    elif operacion == "4":
        id_puesto_modificar = input("Ingrese el ID del puesto que quiere modificar: ")
        turno_modificar = input("Ingrese el turno que quiere modificar: ")
        valor = input("Ingrese el nuevo sueldo por hora: ")
        
        for id, datos in tipo_trabajos.items():
            sueldo_hora = datos[id][1]
            if id_puesto_modificar == id and turno_modificar == id[1]:
                sueldo_hora = valor
    
    elif operacion == "5":
        fecha_calcular = input("Ingrese la fecha que quiere calcular: ")
        id_empleado_calcular = input("Ingrese el ID del empleado que quiere calcular: ")
        for id, datos in jornada.items():
            horario_entrada = datos[0]
            horario_salida = datos[1]
            if fecha_calcular == id[0] and id_empleado_calcular == id[1]:
                horas_trabajadas = horario_salida - horario_entrada
                if horas_trabajadas > 8:
                    horas_extra = horas_trabajadas - 8
                for id, datos in empleados.items():
                    id_puesto = datos[0]
                    for id, datos in tipo_trabajos.items():
                        sueldo_hora = datos[1]
                        if id_puesto == id[0]:
                            monto_dia = horas_trabajadas * sueldo_hora + horas_extra * (sueldo_hora * 1.5)
                            print("El monto del dia es: ", monto_dia)

    operacion = input("Que operacion quiere realizar: 1=Agregar Empleado, 2=Eliminar empleado,3=modificar puesto,4=mostrar sueldo, 5=Calcular monto del dia, 10=salir ")
