#Clase 18 de Junio
""""
NÚMEROS
INT (entero) LONG (números más grandes)
LONG= 14652L
FLOAT (números con decimales)
Ej= 0.32 - -33.895
COMPLEX (n. complejos)
EJ= 33.8j

Arimeticos
SUMA +
RESTA -
MULTIPLICACIÓN *
POTENCIA **
DIVISIÓN (COCIENTE) /
DIVISIÓN (PARTE ENTERA) //
PROMEDIO %
Si hay una expresión el operador más grande se debe de poner primero.

PROCEDENCIA DE LOS OPERADORES
1.Términos entre parentesis
2.Potenciación y raices
3.Multi. y divi.
4. Suma y resta
"""
#print(15+8)
#print(80*2)

""""
______STRING = STR (CADENAS DE TEXTOS)_____
Se reperesenta con comillas, es mejor las comillas simples y no dobles (') son datos
'Yazmín'
print('Hola Mundo')
print('string t con tabulación')
print('string n con salto de linea')

_____VARIABLES_____
En ALGUNOS lenguajes son cajas que guardan datos (ya no se usa ese concepto)
En python son etiquetas que hacen referencia a los datos, contiene datos y esos datos van a estar dentro de un objeto
Cada objeto va a tener:
1- Un identificador único (id)
2- Un tipo de dato (entero, decimal, string, etc)
3- Un valor (propio dato del objeto)
Las variable en python no guardan los datos, son simples nombres que se les ponen para hacer referencia de esos objetos
Ej:

dni (nombre de la variblae) = 37350000 (valor de la varible)

a = 2
print(a)

EL NOMBRE DE UNA VARIABLE DEBE DE EMPEZAR CON UNA LETRA O CON UN GUIÓN BAJO (snake_case)
LOS NOMBRES DE LA VARIBLES NO PUEDEN INCLUIR ESPACIOS EN BLANCO
mi_fecha_de_nacimiento = '02 de junio'
print(mi_fecha_de_nacimiento)

METODO DE SALIDA = print()
METODO DE ENTRADA = input() es lo que se ingresa del teclado en la consola (cadena de texto)

nombre = input('Hola! escribí tu nombre:')
print(nombre)

LA FUNCIÓN INPUT POR DEFECTO CONVIERTE LOS DATOS DE ENTRADA EN UN STRING (ES UNA CADENA) AUNQUE ESTEMOS ESCRIBIENDO UN NÚMERO

a = 20
b = 30

resultado = a+b

print(resultado)


c = 100
d = 200

print(c+d)

LOS DATOS DE ESTRADA SE PUEDEN CONVERTIR EN STR (STRING)

e = 30
#f = input(Cuál es tu edad:) #ejemplo de un dato de entrada que lo toma como cadena de texto
f = int(input(Cuál es tu edad:))
"""
#e = 30
#f = int(input(Cuál es tu edad:)) #conversión de tipo: python convierto un str en número

#print(e*f)

cadena_de_texto = 'Python'
anio_del_curso = '2024'
print(cadena_de_texto + anio_del_curso)

#A LA SUMA DE LOS STRING SE LE LLAMA CONCATENACIÓN

print(cadena_de_texto[3]) #indice empieza desde el 0 de izquierda en el ej. de Python es la 3 es la h
#Indice de atrás empieza desde -1 a la derecha
#P Y T H O N
#0 1 2 3 4 5 indice
#-6 -5 -4 -3 -2 -1 indice inverso

#Para el repositorio de github git add .  
# git commit -m  git push