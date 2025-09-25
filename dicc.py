# empleados = { id_empleado :[id_trabajo, nombre, apellido, dni, telefono, edad]}
# Diccionario empleados
# clave:        identificador del empleado,     INT
# valor:        lista de datos del empleado,    List<6>
# lista
# id_trabajo:   identificador del trabajo,      INT
# nombre:       nombre del empleado,            STR
# apellido:     apellido del empleado,          STR
# dni:          DNI del empleado,               INT
# telefono:     Telefono del empleado,          INT
# edad:         edad del empleado:              INT

# tipo_trabajos = {id_trabajo : [puesto, sueldo_hora, turno, area]}
# Diccionario Tipos de trabajo
# clave:        identificador del trabajo,      INT
# valor:        lista de datos del trabajo,     List<4>
# Lista de datos
# Puesto:       Nombre del cargo,               STR
# Sueldo Hora:  Compesacion horaria,            INT
# turno:        turno del cargo,                STR
# area:         area del cargo,                 STR

# liquidaciones = {id_liquidacion : [id_empleado, sueldo_bruto, sueldo_neto, horas_extra, deducciones, periodo_mes]}
# Diccionario liquidaciones
# clave: identificador de la liquidacion
# valor: lista de informacion
#
#
#
#
#
#
#
# jornada = {id_jornada : [horario_entrada, horario_salida, periodo_mes, id_empleado]}
# sueldos = {id_sueldo : [id_empleado , id_trabajo, id_liquidacion]}

#un empleado tiene varias jornadas en un mes, un empleado tiene un tipo de trabajo, las liquidaciones se hacen mensualmente,
#las liquidaciones se hacen para un solo empleado en un mes especifico, un tipo de trabajo puede tener un area establecida, 


