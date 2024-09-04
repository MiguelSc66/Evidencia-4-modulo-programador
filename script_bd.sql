-- Creamos la tabla de la persona con sus datos básicos
CREATE TABLE persona (
  id_persona INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(45) NOT NULL,
  apellido VARCHAR(45) NOT NULL,
  sexo VARCHAR(45) NOT NULL
) ENGINE=InnoDB;
-- Elegi esos datos para la tabla porque creo que son aquellos que son basicos de una persona y sirve para los requerimientos del sistema, 
-- hice que los datos no pudieran ser nulos ya que son importantes a la hora de registrar al usuario.
-- El ENGINE lo agregue porque habia un error en la compatibilidad de claves foranes lo cual investigue y 
-- para resolverlo debo especificar el motor a utilizar el cual soluciona dicho error, opte por usar InnoDB ya que era el mas recomednado en estas situaciones.

-- Creamos la tabla de la información de la persona
CREATE TABLE info_persona (
  id_info INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  id_persona INT NOT NULL UNIQUE, -- El UNIQUE lo agregue para que unicamente para que cada informacion corporal este relacionada con una sola persona. 
  altura FLOAT NOT NULL, -- La altura la defini como un FLOAT ya que me voy a manejar con metros y 
  peso FLOAT NOT NULL, -- El peso de la persona, lo defini como FLOAT ya que se maneja en kilogramos y puede llegar a tener decimales.
  grasa INT NOT NULL, -- La grasa la defini como un INT porque se utiliza el porcentaje y creo que es mas conveniente el uso de un INT antes que un FLOAT.
  FOREIGN KEY (id_persona) REFERENCES persona (id_persona) -- La FK la utilizamos para establece una relacion entre las tablas la cual nos permite asociar la informacion corporal con la persona.
) ENGINE=InnoDB;
-- Los valores son NOT NULL porque son fundamentales esos datos a la hora de recopilar informacion de la persona y no permitiria el uso de las funciones del programa.


-- INSERT de la tabla persona
-- Insertamos un nuevo registro de un individuo a la tabla en la cual nos permite almacenar y gestionar su informacion. Lo mismo sucede en los INSERT de la misma tabla
INSERT INTO persona (nombre, apellido, sexo)
VALUES ('Juan', 'Pérez', 'Masculino');

INSERT INTO persona (nombre, apellido, sexo)
VALUES ('María', 'Gómez', 'Femenino');

INSERT INTO persona (nombre, apellido, sexo)
VALUES ('Carlos', 'López', 'Masculino');

INSERT INTO persona (nombre, apellido, sexo)
VALUES ('Ana', 'Martínez', 'Femenino');

INSERT INTO persona (nombre, apellido, sexo)
VALUES ('Luis', 'Rodríguez', 'Masculino');

-- INSERT de la tabla info_persona
-- Insertamos la informacio corporal del individuo a esta tabla, esto nos permite realizar un analisis de la composicion corporal de la persona que tiene asociada estos datos. 
-- Lo mismo sucede en los INSERT de la misma tabla
INSERT INTO info_persona (id_persona, altura, peso, grasa)
VALUES (1, 175, 70, 15);

INSERT INTO info_persona (id_persona, altura, peso, grasa)
VALUES (2, 165, 65, 22);

INSERT INTO info_persona (id_persona, altura, peso, grasa)
VALUES (3, 180, 85, 18);

INSERT INTO info_persona (id_persona, altura, peso, grasa)
VALUES (4, 160, 55, 25);

INSERT INTO info_persona (id_persona, altura, peso, grasa)
VALUES (5, 170, 78, 20);


-- Consultas de datos

-- Muestra todos los datos de la tabla persona
SELECT * FROM persona;

-- Muestra el nombre y apellido de todas las personas que sean de género Femenino
SELECT nombre, apellido FROM persona WHERE sexo = 'Femenino';

-- Muestra las personas que tengan una grasa mayor a 20
SELECT id_info, altura, grasa FROM info_persona WHERE grasa > 20;

-- Muestra las personas cuyo nombre termine con la letra 'a'
SELECT nombre, apellido FROM persona WHERE nombre LIKE '%a';

-- Muestra las personas que tengan un porcentaje de grasa igual a 20
SELECT id_persona, altura, grasa FROM info_persona WHERE grasa = 20;
