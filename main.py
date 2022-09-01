from Paquete.menu import Menu, gotoxy, cls
import time

class Ejercicio:
    def EjecutarEjercicio(self):
        pass


class HolaMundo(Ejercicio):
    def EjecutarEjercicio(self):
        print("Hey, ya corrió el código!")


class Variables(Ejercicio):
    def EjecutarEjercicio(self):
        nombre = "Joso"
        print(nombre)

        edad = 25
        print(edad)

        edad = True
        print(edad)

        sueldo = 205.10
        print(sueldo)


class Conversiones(Ejercicio):
    def EjecutarEjercicio(self):
        numero1 = "35"
        numero2 = "10"
        print(numero1 + numero2)

        num1 = int(numero1)
        num2 = int(numero2)
        print(num1 + num2)

        sueldo = 1200.43
        sueldoEntero = int(sueldo)
        print(sueldoEntero)

        valor = "4500.89"
        valorDecimal = float(valor)
        print(valorDecimal * 3)

        edad = 100
        print(len(str(edad)))


class NumerosOperaciones(Ejercicio):
    def EjecutarEjercicio(self):
        entero = 23
        decimal = 31.78
        complejo = 12 + 5j
        # booleano = True

        """
        print(entero)
        print(decimal)
        print(complejo)
        print(booleano)
        """

        num1 = 20
        num2 = 4
        print("Suma:", (num1 + num2))
        print("Resta:", (num1 - num2))
        print("Multiplicaión:", (num1 * num2))
        print("División:", (num1 / num2))
        print("División Exacta:", (num1 // num2))
        print("Potencia:", (num1 ** num2))


class TiposDeConcatenacion(Ejercicio):
    def EjecutarEjercicio(self):
        texto1 = "Hola"
        texto2 = "Joso"
        textoFinal = texto1 + " " + texto2
        print(textoFinal)

        print("El saludo es: %s %s" % (texto1, texto2))

        saludoFinal = "Saludo: {0} {1}".format(texto1, texto2)
        print(saludoFinal)

        saludoFinal2 = "Saludo: {x} {y}".format(x=texto1, y=texto2)
        print(saludoFinal2)


class Cadenas(Ejercicio):
    def EjecutarEjercicio(self):
        texto = "Me lleva la que me trajo!"
        print(texto)
        print(texto.lower())
        print(texto.upper())
        print(texto.title())

        print(texto.find("que"))  # Posición donde encuentra la cadena o porción

        print(texto.count("e"))  # CAntidad de ocurrencias de una letra o porción

        textoFinal = texto.replace("e", "3")  # Reemplaza valores, en este caso, el primero se reemplaza por el segundo
        print(textoFinal)

        valor = texto.isnumeric()  # Te dice si es numérico o no(True False), hay varios is...
        print(valor)

        cadenaSeparada = texto.split(" ")  # Separa en una lista por medio de un valor
        print(cadenaSeparada)


class Tuplas(Ejercicio):
    def EjecutarEjercicio(self):
        tupla = (1, 2, 3)
        print(tupla)
        tupla2 = (7, "Oscar", True, 45.1, 16 + 7j)
        print(tupla2)
        tupla3 = (9, 3, (4, 5, 6))
        print(tupla3)
        print(tupla2[1])
        print(tupla2[-1])
        print(tupla2[0:4])
        print(tupla2[-2])

        a, b, c = tupla
        print(a)
        print(b)
        print(c)

        tuplaFinal = tupla + tupla3
        print(tuplaFinal)

        print(tuplaFinal.count(2))  # Cuenta los valores en un array
        print(tuplaFinal.index(9))  # Ubica un valor en un array


class Listas(Ejercicio):
    def EjecutarEjercicio(self):
        lista1 = ["Joso", 25, 98, 3, True, "Flavio", 56.3]
        print(lista1)  # Imprime toda la lista
        print(lista1[:])  # Imprime toda la lista
        print(lista1[2])  # Imprime la posición en una lista
        print(lista1[-1])  # Imprime el último valor de la lista

        print(lista1[
              0:3])  # Imprime un rango, desde la posición dispuesta (primer número = 0) hasta la otra posición(segundo núm = 3) que es hasta el 2
        print(lista1[:2])  # Es lo mismo que arriba solo que la posición inicial se reconoce como nada
        print(lista1[3:])  # Aquí es al revés que arriba, el final se reconoce y empieza desde la posición 3

        lista1.append("Joso")  # Añade un valor más a la lista
        print(lista1)

        lista1.insert(4, "Perú")  # Añade un valor en una posición específica de la lista
        print(lista1)

        lista1.extend(["Ale", 110, False])  # Extiende la lista
        print(lista1)

        print(lista1.index("Flavio"))  # Indica la posición de ese valor

        lista1.remove(56.3)  # Remueve un valor de la lista, pero si no existe da error
        print(lista1)

        lista1.pop()  # Elimina el último valor de la lista
        print(lista1)

        lista2 = ["Chiclayo", "Irma"]
        lista3 = lista1 + lista2
        print(lista3)  # Las listas se pueden sumar

        print(lista2 * 4)

        print("Chiclayo" in lista2)  # Pregunta si el valor está dentro de esa lista y devuelve un booleano


class Diccionarios(Ejercicio):
    def EjecutarEjercicio(self):
        # Estructura de una lista {clave:valor} == {key:values)

        miDiccionario = {"España": "Madrid", "Perú": "Lima", "Alemania": "Berlín"}
        print(miDiccionario)
        print(miDiccionario["Perú"])  # Imprime el valor de la clave

        miDiccionario["Venezuela"] = "Caracas"  # Creación de un nuevo valor en el diccionario
        print(miDiccionario)

        miDiccionario["España"] = "Barcelona"  # Reemplazo de un valor existente
        print(miDiccionario)

        del miDiccionario["España"]  # clausula que borra un elemento
        print(miDiccionario)

        dic2 = {"García": "Oscar", 25: True, "Sueldo": 150.80}
        print(dic2[25])

        llaves = ("España", "Francia", "Inglaterra")
        dicPaises = {llaves[0]: "Madrid", llaves[1]: "Paris", llaves[2]: "Londres"}
        print(dicPaises)

        datosPersonales = {"Apellido": "García", "Anios": {1: 2010, 2: 2011, 3: 2012, 4: 2013, 5: 2014}}
        print(datosPersonales)
        print(datosPersonales["Anios"])

        print(datosPersonales.get("Apellido",
                                  "No se encontró"))  # Devuelve el valor de la clave a buscar y si no se encuentra devuelve lo que está después de la coma

        print(datosPersonales.keys())

        print(datosPersonales.keys())
        valores = list(datosPersonales.values())
        print(valores)


class IngresoDatos(Ejercicio):
    def EjecutarEjercicio(self):
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        sueldo = float(input("Ingrese su sueldo: "))

        print("Hola, " + nombre)
        edadFutura = edad + 20
        print("Tu edad es:", edad)
        print("Tu edad (dentro de 20 años) será:", edadFutura)
        print("Tu sueldo es:", sueldo)


class IfElse(Ejercicio):
    def EjecutarEjercicio(self):
        edad = int(input("Ingrese su edad: "))

        if edad > 18:
            print("Eres mayor de edad.")
        elif edad == 18:
            print("Tienes 18 años!")
        else:
            print("No eres mayor de edad.")


class Funciones(Ejercicio):
    def EjecutarEjercicio(self):
        def saludar():
            print("García")
            print("Oscar")
            print("Joso")

            return "Hola"

        print(saludar())

        def evaluarSueldoMinimo(sueldo):
            if sueldo >= 850:
                print("Cumples con el sueldo")
            else:
                print("Ganas menos que el sueldo minimo")

        evaluarSueldoMinimo(1200)
        evaluarSueldoMinimo(200)


class OperadoresLogicos(Ejercicio):
    def EjecutarEjercicio(self):
        distancia = 400
        numeroHermanos = 3
        salarioPadres = 3000

        tieneBeneficio = False

        if (distancia > 1000 and numeroHermanos > 2) or salarioPadres < 2000:
            tieneBeneficio = True

        print(not tieneBeneficio)

        if (5 > 3) or (8 < 6):
            print("Verdad")
        else:
            print("Es mentira...")


class OperadorTernario(Ejercicio):
    def EjecutarEjercicio(self):
        """
        String sexo;
        sexo = (10 > 20) ? "Masculino" : "Femenino";
        """

        sexos = ("Hombre", "Mujer")

        posicion = True
        sexo = sexos[posicion]  # Mujer
        print(sexo)
        sexo = sexos[not posicion]  # Hombre
        print(sexo)


class Range(Ejercicio):
    def EjecutarEjercicio(self):
        # range(): Crea una lista inmutable de números enteros en sucesión aritmética.

        numeros = range(5)  # [0, 1, 2, 3, 4]

        print(numeros[1])

        numeros1 = range(4, 10)  # [4, 5, 6, 7, 8, 9]
        print(numeros1[5])

        numeros2 = range(10, 100, 8)
        print(numeros2[9])  # [10, 18, 26, 34, 42, 50, 58, 66, 74, 82, 90, 98]


class For(Ejercicio):
    def EjecutarEjercicio(self):
        """
        for num in range(0, 20, 2):
            print("Valor actual: {0}".format(num))
        """

        for i in range(1, 13):
            print("{0} x {1} es: {2}".format(i, i, (i * i)))

        for nom in ["Karen", "Oscar", "Héctor", "Leonardo"]:
            print("Cantidad de letras de {0} es: {1}".format(nom, len(nom)))


class Factorial(Ejercicio):
    def EjecutarEjercicio(self):
        # Factorial: Es el producto de todos los números positivos enteros comprendidos entre 1 y un número.

        # Factorial de 5: 1 * 2 * 3 * 4 * 5 = 120
        # Factorial de 4: 1 * 2 * 3 * 4 = 24

        numero = int(input("Ingrese un número: "))

        factorial = 1
        for n in range(1, (numero + 1)):
            factorial = factorial * n

        print("El factorial de {0} es: {1}".format(numero, factorial))


class While(Ejercicio):
    def EjecutarEjercicio(self):
        """
        indice = 1

        while indice < 10:
            print("Valor actual: {0}".format(indice))
            indice = indice + 1

        print("Hemos terminado el bucle while.")
        # Continua el programa.
        """

        inicio = 2

        while inicio <= 100:
            print("Número par: {0}".format(inicio))
            inicio += 2

        print("Hemos terminado el bucle while.")


class BreakContinuePass(Ejercicio):
    def EjecutarEjercicio(self):
        # Break: Permite salir de un bucle cuando se cumple una condición.
        """
        for numero in range(1, 6):
            if numero == 3:
                break  #Descanso o interrupción en este punto.
            print("El número es: {0}".format(numero))

        print("Bucle terminado.")
        """

        # Continue: Omite una parte del bucle cuando se cumple una condición y
        # continúa con el resto.
        """
        for numero in range(1, 6):
            if numero == 3:
                continue  # Continúa con el resto del bucle, es decir, cuando sea 3, el print se omitirá 
            print("El número es: {0}".format(numero))

        print("Bucle terminado.")
        """

        # Pass: Permite continuar con una sentencia o función que ya no tiene
        # o aún no tiene un bloque de código útil.
        for numero in range(1, 6):
            if numero <= 3:
                # Aquí no pasa nada y el bucle sigue trabajando.
                pass
            else:
                print("El siguiente valor es mayor a 3:")
            print("El número es: {0}".format(numero))

        print("Bucle terminado.")

        def funcionSinImplementar():
            pass


class Generador1(Ejercicio):
    def EjecutarEjercicio(self):
        # Generadores: Permiten extraer valores de una función y almacenarlo
        # (de uno en uno) en objetos iterables (que se pueden recorrer),
        # sin la necesidad de almacenar TODOS A LA VEZ en la memoria RAM.

        """
        def generaMultiplos7(limite):
            numero = 1
            listaNumeros = []

            while numero <= limite:
                listaNumeros.append(numero * 7)
                numero = numero + 1
            return listaNumeros  #Retorna la lista creada

        print(generaMultiplos7(10))
        """

        def generadorMultiplos7(limite):
            numero = 1

            while numero <= limite:
                yield numero * 7  # yield == Ceder. La instrucción "yield" genera un objeto iterable
                numero = numero + 1

        obtieneMultiplos7 = generadorMultiplos7(10)

        """
        # print(obtieneMultiplos7)
        for n in obtieneMultiplos7:
            print(n)
        """

        # next(): Retorna el siguiente elemento de un objeto iterable:
        print(next(obtieneMultiplos7))
        print("Acá hay 300 líneas de código...")
        print(next(obtieneMultiplos7))
        print("Acá hay 1000 líneas de código...")
        print(next(obtieneMultiplos7))
        # Ventajas
        # Son más eficiente que las funciones tradicionales
        # Muy útiles con listas de valores infinitos
        # Entre llamada y llamada, el objeto iterable entra en un estado de pausa (suspensión)


class Generador2(Ejercicio):
    def EjecutarEjercicio(self):
        # Cuando indicamos un * adelante del parámetros de una función,
        # estamos indicado que se va a recibir un número indeterminado
        # de parámetros. Además, esos parámetros se recibirán en forma de tupla.

        """
        def devuelveLenguajes(*lenguajes):
            for leng in lenguajes:
                yield leng
        """

        def devuelveLenguajes(*lenguajes):
            for leng in lenguajes:
                for letra in leng:
                    yield letra

        lenguajesObtenidos = devuelveLenguajes("Python", "Java", "PHP", "Ruby", "JavaScript")

        def devuelveLenguajes(*lenguajes):
            for leng in lenguajes:
                yield from leng

        lenguajesObtenidos = devuelveLenguajes("Python", "Java", "PHP", "Ruby", "JavaScript")

        print(next(lenguajesObtenidos))
        print(next(lenguajesObtenidos))


class Excepción(Ejercicio):
    def EjecutarEjercicio(self):
        # Excepción: Error en tiempo de ejecución (durante la ejecución de un programa).

        numero1 = 20
        numero2 = 2

        # print("La división de {0} entre {1} es: {2}".format(numero1, numero2, (numero1 / numero2)))

        try:
            resultado = numero1 / numero2
        # except:
        except ZeroDivisionError:  # Aquí especificamos una excepción para que salga con un mensaje específico
            print("No se puede dividir entre 0...")
        finally:  # Finally siempre se ejecutará independientemente de si entró a una excepción o no
            print("Yo siempre aparezco.")

        print("Aquí termina mi programa.")


class Raise(Ejercicio):
    def EjecutarEjercicio(self):
        # Raise: Sirve para lanzar (de forma intencional) excepciones en Python.

        def evaluarNota(nota):
            if nota < 0:
                raise ValueError("Valor incorrecto...")
                # raise ZeroDivisionError("Este mensaje es personalizado.")
            elif nota >= 16:
                print("Excelente")
            elif nota >= 11:
                print("Aprobado")
            else:
                print("Desaprobado")

        evaluarNota(-7)

        print("Este es el fin de mi programa.")


class Modulos(Ejercicio):
    def EjecutarEjercicio(self):
        from MODULOS.funciones_matemáticas import sumar, multiplicar
        print(sumar(5, 6))
        print(multiplicar(5, 6))


class PruebaPaquetes(Ejercicio):
    def EjecutarEjercicio(self):
        from Paquete.funcionsCadena import contar_letras
        from Paquete.funcionesNuméricas import multiplicar

        print(multiplicar(5, 6))
        print(contar_letras("Joso"))


class ClasePersona(Ejercicio):
    def EjecutarEjercicio(self):
        class Persona:
            ape = ""
            nom = ""
            edad = 0
            despierta = False

            def despertar(self):
                self.despierta = True
                print("Buen día!")

        persona1 = Persona()
        persona1.ape = "Román"
        persona1.nom = "Felipe"
        print("Tenías un amigo llamado {0} y de appelido {1}".format(persona1.nom, persona1.ape))
        persona1.despertar()
        if persona1.despierta:
            print("La persona {0} {1} de edad {2} ha despertado!".format(persona1.nom, persona1.ape, persona1.edad))
        else:
            print("La persona {0} {1} de edad {2} no ha despertado!".format(persona1.nom, persona1.ape, persona1.edad))


class ClaseCurso(Ejercicio):
    def EjecutarEjercicio(self):
        class Curso():
            """
            nombre = "Matemática"
            creditos = 5
            profesion = "Ingeniería Civil"
            """

            # Estado inicial del objeto:
            def __init__(self, nom, cre, pro):
                self.nombre = nom
                self.creditos = cre
                self.profesion = pro
                self.__imparticion = "Presencial"  # Propiedad encapsulada.

            def mostrarDatos(self):
                dat = "Nombre: {0} / Créditos: {1} / Modo de impartición: {2}"
                print(dat.format(self.nombre, self.creditos, self.__imparticion))
                docenteAsignado = self.__verificarDocente()
                if docenteAsignado:
                    print("Existe docente asignado.")
                else:
                    print("No es necesario asignar un docente...")

            def __verificarDocente(self):
                # print("Verificando si existe docente asignado...")
                if self.__imparticion == "Presencial":
                    return True
                else:
                    return False

            # toString()
            def __str__(self):
                texto = "Nombre: {0} - Créditos: {1}"
                return texto.format(self.nombre, self.creditos)

        curso1 = Curso("Matemática", 5, "Ingeniería Civil")
        print(curso1)
        curso1.mostrarDatos()

        # curso2 = Curso("Lenguaje", 4, "Ingeniería Industrial")
        # print(curso2.nombre)


class ClaseCuenta(Ejercicio):
    def EjecutarEjercicio(self):
        class Cuenta:
            def __init__(self, pro, sal, mon):
                self.__propietario = pro
                self.__saldo = sal
                self.__moneda = mon

            # GETTERS (método GET)
            def get_Saldo(self):
                return self.__saldo

            def get_Propietario(self):
                return self.__propietario

            def get_Moneda(self):
                return self.__moneda

            # SETTERS (método SET)
            def set_Moneda(self, dato):
                self.__moneda = dato

        cuenta1 = Cuenta("Josué", 150, "Dolar")
        print(cuenta1.get_Saldo())
        print(cuenta1.get_Moneda())
        cuenta1.set_Moneda("Yuan")
        print(cuenta1.get_Moneda())


class ClaseHerencia(Ejercicio):
    def EjecutarEjercicio(self):
        class Persona:
            def __init__(self, nom, apePat, apeMat):
                self.apellidoPaterno = apePat
                self.apellidoMaterno = apeMat
                self.nombre = nom

            def mostarNombreCompleto(self):
                txt = "{0} {1} {2}"
                return txt.format(self.nombre, self.apellidoPaterno, self.apellidoMaterno)

            def datos(self):
                print(self.mostarNombreCompleto())

        class Estudiante(Persona):
            def __init__(self, nom, apePat, apeMat, pro):
                super().__init__(nom, apePat, apeMat)
                self.profesion = pro

            def datos(self):
                print("Profesión: {0}".format(self.profesion))

        est1 = Estudiante("Juan", "Torres", "Lopez", "Ingeniero Civil")
        # print(est1.mostarNombreCompleto())
        # print(est1.profesion)
        # est1.datos()

        print(isinstance(est1, Estudiante))


class HerenciaMúltiple(Ejercicio):
    def EjecutarEjercicio(self):
        class ClaseA:
            def __init__(self, par1, par2):
                self.parametro1 = par1
                self.parametro2 = par2

        class ClaseB:
            def __init__(self, par3, par4, par5):
                self.parametro3 = par3
                self.parametro4 = par4
                self.parametro5 = par5

        class ClaseX(ClaseA, ClaseB):

            def __str__(self):
                txt = "Valores de la clase A: {0} y {1}"
                return txt.format(self.parametro1, self.parametro2)

        claseX1 = ClaseX(1, 2)

        print(claseX1.__str__())


class ClasePolimorfismo(Ejercicio):
    def EjecutarEjercicio(self):
        # Polimorfismo (poli => muchas / morfos: formas)

        class Estudiante():

            def describir(self):
                print("Soy un buen estudiante.")

        class Docente():

            def describir(self):
                print("Me dedico a enseñar cursos.")

        class Trabajador():

            def describir(self):
                print("Trabajo dentro de una gran empresa.")

        def describirPersona(persona):
            persona.describir()

        doc1 = Trabajador()
        describirPersona(doc1)


class ClaseRelaciones(Ejercicio):
    def EjecutarEjercicio(self):
        class Pais:
            def __init__(self, nom, pre):
                self.nombre = nom
                self.presidente = pre

            def __str__(self):
                txt = "País: {0} = Presidente: {1}"
                return txt.format(self.nombre, self.presidente)

        class Ciudad():
            def __init__(self, nom, hab, pai):
                self.nombre = nom
                self.habitantes = hab
                self.pais = pai

            def __str__(self):
                txt = "Ciudad: {0} - N° Habitantes: {1} ({2})"
                return txt.format(self.nombre, self.habitantes, self.pais)

        class Urbanizacion():
            def __init__(self, nom, ciud):
                self.nombre = nom
                self.ciudad = ciud

            def __str__(self):
                txt = "Urbanización: {0} ({1})"
                return txt.format(self.nombre, self.ciudad)

        pais1 = Pais("Ecuador", "León Febres-Cordero Ribadeneyra")
        print(pais1)

        ciudad1 = Ciudad("Guayaquil", 2404543, pais1)
        print(ciudad1)

        urba1 = Urbanizacion("9 de Octubre", ciudad1)
        print(urba1)


listaDic = ['Hola Mundo', 'Variables', 'Conversiones', 'Numeros Operaciones', 'Tipos De Concatenacion', 'Cadenas', 'Tuplas',
            'Listas', 'Diccionarios', 'Ingreso Datos', 'If Else', 'Funciones', 'Operadores Logicos', 'Operador Ternario', 'Range',
            'For', 'Factorial', 'While', 'Break Continue Pass', 'Generador 1', 'Generador 2', 'Excepción', 'Raise', 'Modulos',
            'Prueba Paquetes', 'Clase Persona', 'Clase Curso', 'Clase Cuenta', 'Clase Herencia', 'Herencia Múltiple', 'Clase Polimorfismo', 'Clases Relaciones']

men1 = Menu()
ejer1 = HolaMundo()
ejer2 = Variables()
ejer3 = Conversiones()
ejer4 = NumerosOperaciones()
ejer5 = TiposDeConcatenacion()
ejer6 = Cadenas()
ejer7 = Tuplas()
ejer8 = Listas()
ejer9 = Diccionarios()
ejer10 = IngresoDatos()
ejer11 = IfElse()
ejer12 = Funciones()
ejer13 = OperadoresLogicos()
ejer14 = OperadorTernario()
ejer15 = Range()
ejer16 = For()
ejer17 = Factorial()
ejer18 = While()
ejer19 = BreakContinuePass()
ejer20 = Generador1()
ejer21 = Generador2()
ejer22 = Excepción()
ejer23 = Raise()
ejer24 = Modulos()
ejer25 = PruebaPaquetes()
ejer26 = ClasePersona()
ejer27 = ClaseCurso()
ejer28 = ClaseCuenta()
ejer29 = ClaseHerencia()
ejer30 = HerenciaMúltiple()
ejer31 = ClasePolimorfismo()
ejer32 = ClaseRelaciones()

def Execute(Objeto):
    Objeto.EjecutarEjercicio()

listObjetcs = [ejer1, ejer2, ejer3,ejer4,ejer5,ejer6,ejer7,ejer8,ejer9,ejer10,ejer11,ejer12,ejer13,ejer14,ejer15,ejer16,ejer17,
               ejer18,ejer19,ejer20,ejer21,ejer22,ejer23,ejer24,ejer25,ejer26,ejer27,ejer28,ejer29,ejer30,ejer31,ejer32]

ban = True
while ban:
    cls()
    opcion = int(men1.menu(listaDic, "Menú"))
    if opcion in range(0,33):
        cls()
        gotoxy(1,1);print("*"*10, listaDic[opcion-1], "*"*10)
        gotoxy(1,3);Execute(listObjetcs[opcion-1])
    else:
        print("No existe tal opción...")

    if ban:
        resp = input("\nPresiona enter para volver o ingresa 'n'\n")
        if resp.lower() == "n":
            ban = False
            cls()
            print("Saliendo del programa...");time.sleep(1)