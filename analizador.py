class AnalizadorComposicionCorporal:
    def __init__(self, nombre, apellido, sexo, peso, altura, edad, grasa):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura
        self.__edad = edad
        self.__grasa = grasa

    # El IMC es el índice de masa corporal basado en el peso y altura del usuario
    def calcular_imc(self):
        imc = self.__peso / (self.__altura ** 2) 
        if imc < 18.5:
            return "Bajo peso"
        elif imc < 24.9:
            return "Normal"
        elif imc < 29.9:
            return "Sobrepeso"
        else:
            return "Obesidad"

    # El método analiza la composición del usuario y devuelve la interpretación basada en su porcentaje de grasa
    def analizar_composicion(self):
        if self.__grasa < 15:
            return "Porcentaje de grasa bajo"
        elif self.__grasa < 25:
            return "Porcentaje de grasa normal"
        else:
            return "Porcentaje de grasa alto"
        
    # El TBM es la cantidad mínima de energía que una persona necesita para mantener las funciones vitales básicas del cuerpo en reposo. Dependiendo del género de la persona el cálculo recibe una pequeña diferencia    
    def calcular_tbm(self):
        altura_cm = self.__altura * 100  # Hacemos la conversión de metros a centímetros ya que los cálculos están planteados usando centímetros.
        if self.__sexo == "Hombre":
            bmr = 10 * self.__peso + 6.25 * altura_cm - 5 * self.__edad + 5
        else:
            bmr = 10 * self.__peso + 6.25 * altura_cm - 5 * self.__edad - 161
        return round(bmr)

    # Calcula el porcentaje de agua corporal total (siglas en inglés: TBW) basado en el sexo y peso de la persona
    def calcular_agua_corporal(self):
        if self.__sexo == "Hombre":
            tbw = 0.6 * self.__peso
        else:
            tbw = 0.5 * self.__peso 
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

    # La función devuelve un texto con los valores de los resultados de las anteriores funciones
    def __str__(self):
        return (f"Nombre: {self.__nombre} {self.__apellido}\n"
                f"IMC: {self.calcular_imc()}\n"
                f"TBM: {self.calcular_tbm()}\n"
                f"Composición: {self.analizar_composicion()}\n"
                f"Agua Corporal: {self.analizar_agua_corporal()}")
