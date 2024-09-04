import pytest
from analizador import AnalizadorComposicionCorporal

@pytest.mark.parametrize("peso, altura, expected", [
    (70, 1.89, "Normal"),
    (50, 1.70, "Bajo peso"),
    (90, 1.55, "Obesidad"),
    (110, 1.60, "Obesidad"),
    (80, 1.75, "Sobrepeso")
])

def test_calcular_imc(peso, altura, expected):
    analizador = AnalizadorComposicionCorporal("", "", "", peso, altura, 0, 0)
    assert analizador.calcular_imc() == expected

@pytest.mark.parametrize("grasa, expected", [
    (10, "Porcentaje de grasa bajo"),
    (20, "Porcentaje de grasa normal"),
    (30, "Porcentaje de grasa alto")
])
def test_analizar_composicion(grasa, expected):
    analizador = AnalizadorComposicionCorporal("", "", "", 0, 0, 0, grasa)
    assert analizador.analizar_composicion() == expected

@pytest.mark.parametrize("sexo, peso, altura, edad, expected", [
    ("Hombre", 70, 1.89, 25, 1761),
    ("Mujer", 70, 1.89, 25, 1595)
])
def test_calcular_tbm(sexo, peso, altura, edad, expected):
    analizador = AnalizadorComposicionCorporal("", "", sexo, peso, altura, edad, 0)
    assert analizador.calcular_tbm() == expected

@pytest.mark.parametrize("sexo, peso, expected", [
    ("Hombre", 70, 42),  # 60% de 70 es 42
    ("Mujer", 70, 35)    # 50% de 70 es 35
])
def test_calcular_agua_corporal(sexo, peso, expected):
    analizador = AnalizadorComposicionCorporal("", "", sexo, peso, 0, 0, 0)
    assert analizador.calcular_agua_corporal() == expected

@pytest.mark.parametrize("sexo, peso, expected", [
    ("Hombre", 72, "Nivel de agua corporal adecuado"),
    ("Mujer", 60, "Bajo nivel de agua corporal")
])

def test_analizar_agua_corporal(sexo, peso, expected):
    analizador = AnalizadorComposicionCorporal("", "", sexo, peso, 0, 0, 0)
    assert analizador.analizar_agua_corporal() == expected

