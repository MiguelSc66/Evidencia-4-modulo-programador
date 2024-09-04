class AnalizadorComposicionCorporal:
    def __init__(self, nombre, apellido, sexo, peso, altura, edad, grasa):
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.edad = edad
        self.grasa = grasa

    # El imc es el indice de masa coroporal el cual se basa en el peso y altura del usuario
    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2) # Con este calculo podemos saber que IMC de la persona
        if imc < 18.5:
            return "Bajo peso"
        elif imc < 24.9:
            return "Normal"
        elif imc < 29.9:
            return "Sobrepeso"
        else:
            return "Obesidad"

    # El metodo lo que hace es analizar la composicion del usuario y devuelve la interpretacion basandose en su porcentaje de grasa
    def analizar_composicion(self):
        if self.grasa < 15: 
            return "Porcentaje de grasa bajo"
        elif self.grasa < 25:
            return "Porcentaje de grasa normal"
        else:
            return "Porcentaje de grasa alto"
        
    # El TBM es la cantidad mínima de energía que una persona necesita para mantener las funciones vitales básicas del cuerpo en reposo. Dependiendo del genero de la persona el calculo recibe una pequeña diferencia    
    def calcular_tbm(self):
        altura_cm = self.altura * 100  # Hacemos la conversion de metros a centimetros ya que los cualculos estan planteados usando centimetros.
        if self.sexo == "Hombre":
            bmr = 10 * self.peso + 6.25 * altura_cm - 5 * self.edad + 5
        else:
            bmr = 10 * self.peso + 6.25 * altura_cm - 5 * self.edad - 161
        return round(bmr)

    # Calcula el porcentaje de agua corporal total (siglas en ingles: TBW) basado en el sexo y peso de la persona
    def calcular_agua_corporal(self):
        if self.sexo == "Hombre":
            tbw = 0.6 * self.peso
        else:
            tbw = 0.5 * self.peso 
        return round(tbw)

    # Analiza el nivel de agua corporal basándose en el TBW calculado
    def analizar_agua_corporal(self):
        tbw = self.calcular_agua_corporal()
        if tbw < 40:
            return "Bajo nivel de agua corporal"
        elif tbw <= 50:
            return "Nivel de agua corporal adecuado"
        else:
            return "Alto nivel de agua corporal"


    # La funcion devuelve un texto con los valores de los resultado de las anteriores funciones para que el usuario pueda ver todos sus datos
    def __str__(self):
        return (f"IMC: {self.calcular_imc()} \nTBM: {self.calcular_tbm()} \nComposición: {self.analizar_composicion()} \nAgua Corporal: {self.analizar_agua_corporal()}")

    
# Esta funcion es la principal del programa la cual va a realizar la interaccion con el usuario
def main():
    print("Bienvenido al Analizador de Composición Corporal")
    
    # Se le solicitan los datos al usuario
    nombre = input("Introduce tu nombre: ")
    apellido = input("Introduce tu apellido: ")
    sexo = input("Introduce tu sexo (Hombre/Mujer): ")
    peso = float(input("Introduce tu peso en kg: "))
    altura = float(input("Introduce tu altura en metros: "))
    edad = int(input("Introduce tu edad: "))
    grasa = float(input("Introduce tu porcentaje de grasa corporal: "))
    

    analizador = AnalizadorComposicionCorporal(nombre, apellido, sexo, peso, altura, edad, grasa)
    
    while True:
        print("\n¿Qué te gustaría saber?")
        print("1. Calcular IMC")
        print("2. Analizar composición corporal")
        print("3. Calcular TMB")
        print("4. Calcular agua corporal")
        print("5. Ver todo")
        print("6. Salir")

        opcion = input("Elige una opción (1-5): ")

        if opcion == "1":
            print(f"Tu IMC es: {analizador.calcular_imc()}")
        elif opcion == "2":
            print(f"Tu composición corporal es: {analizador.analizar_composicion()}")
        elif opcion == "3":
            print(f"Tu BMR es: {analizador.calcular_tbm()}")
        elif opcion == "4":
            print(f"Tu agua corporal es: {analizador.calcular_agua_corporal()}")
        elif opcion == "5":
            print(analizador)
        elif opcion == "6":
            print("¡Adiós!")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__":
    main()