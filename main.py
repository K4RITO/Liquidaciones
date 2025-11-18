from funciones.empleados import agregar_empleado, modificar_empleado, mostrar_empleados, eliminar_empleado
from funciones.jornadas import agregar_jornada, modificar_jornada, mostrar_jornadas, eliminar_jornada
from funciones.tipo_trabajos import agregar_tipo_trabajo, modificar_tipo_trabajo, mostrar_tipos_trabajos, eliminar_tipo_trabajo
from funciones.montos import actualizar_monto, calcular_monto, mostrar_montos, eliminar_monto
from funciones.liquidaciones import calcular_liquidacion, mostrar_liquidaciones, eliminar_liquidacion

def main():
    mensaje = """------------------------------
Que operacion quiere realizar: 
Empleado:           1 = Agregar Empleado, 2 = Eliminar empleado, 3 = mostrar empleados, 4 = modificar empleado.
Jornadas:           5 = Agregar jornada, 6 = Mostrar jornadas, 7 = Modificar horarios jornada, 8 = Eliminar Jornada.
Cargos laborales:   9 = Agregar tipo trabajos, 10 = Mostrar tipos de trabajos, 11 = Modificar Tipo trabajo, 12 = Eliminar tipo trabajo.
Montos diarios:     13 = Calcular monto, 14 = Mostrar montos, 15 = Actualizar monto, 16 = Eliminar monto.
Liquidaciones:      17 = Calcular liquidacion de empleado, 18 = Mostrar liquidaciones, 19 = eliminar liquidacion.
Para salir de la aplicacion = Ingrese "20".
------------------------------
Ingrese la operacion a realizar: """

    operacion = input(mensaje)

    while operacion not in ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]:
        print("Opcion incorrecta, seleccione una opcion valida!")
        operacion = input(mensaje)
        
    while operacion != "20":
        if operacion == "1":
            agregar_empleado()
        elif operacion == "2":
            eliminar_empleado()
        elif operacion == "3":
            mostrar_empleados()
        elif operacion == "4":
            modificar_empleado()
        elif operacion == "5":
            agregar_jornada()
        elif operacion == "6":
            mostrar_jornadas()
        elif operacion == "7":
            modificar_jornada()
        elif operacion == "8":
            eliminar_jornada()
        elif operacion == "9":
            agregar_tipo_trabajo()
        elif operacion == "10":
            mostrar_tipos_trabajos()
        elif operacion == "11":
            modificar_tipo_trabajo()
        elif operacion == "12":
            eliminar_tipo_trabajo()
        elif operacion == "13":
            calcular_monto()
        elif operacion == "14":
            mostrar_montos()
        elif operacion == "15":
            actualizar_monto()
        elif operacion == "16":
            eliminar_monto()
        elif operacion == "17":
            calcular_liquidacion()
        elif operacion == "18":
            mostrar_liquidaciones()
        elif operacion == "19":
            eliminar_liquidacion()

        operacion = input(mensaje)
        
if __name__ == "__main__":
    main()
