CREATE DATABASE Inmobiliaria;

USE Inmobiliaria;

CREATE TABLE Tipo
(
Id_Tipo INT NOT NULL AUTO_INCREMENT,
Nombre_Tipo VARCHAR(25),
CONSTRAINT tipo_idtipo_pk PRIMARY KEY(Id_Tipo)
);
    
CREATE TABLE Estado 
(
Id_Estado INT NOT NULL AUTO_INCREMENT,
Nombre_Estado VARCHAR(20),
CONSTRAINT est_idest_pk PRIMARY KEY(Id_Estado)
);
    
CREATE TABLE OperatoriaComercial
(
Id_Operatoria_Comercial INT NOT NULL AUTO_INCREMENT,
Nombre_Operatoria_Comercial VARCHAR(25),
CONSTRAINT ope_idope_pk PRIMARY KEY(Id_Operatoria_Comercial)
);

CREATE TABLE Propietario
(
Id_Propietario INT NOT NULL AUTO_INCREMENT,
Nombre VARCHAR(50),
Direccion VARCHAR(35),
Contacto INT,
CONSTRAINT pro_idpro_pk PRIMARY KEY(Id_Propietario)
);

CREATE TABLE Propiedad
(
Id_Propiedad INT NOT NULL AUTO_INCREMENT,
Id_Tipo INT,
Id_Estado INT,
Id_Operacion_Comercial INT,
Id_Propietario INT,
Nombre VARCHAR(25),
Direccion VARCHAR(30),
Contacto INT,
CONSTRAINT prop_idprop_pk PRIMARY KEY(Id_Propiedad),
CONSTRAINT id_tip_fk FOREIGN KEY (Id_Tipo) REFERENCES Tipo(Id_Tipo),
CONSTRAINT id_est_fk FOREIGN KEY (Id_Estado) REFERENCES Estado(Id_Estado),
CONSTRAINT id_ope_fk FOREIGN KEY (Id_Operacion_Comercial) REFERENCES OperatoriaComercial(Id_Operatoria_Comercial),
CONSTRAINT id_prop_fk FOREIGN KEY (Id_Propietario) REFERENCES Propietario (Id_Propietario)
);

INSERT INTO Tipo VALUES (null, 'Casa'), (null, 'Departamento'), (null, 'PH'), (null, 'Country'), (null, 'Local Comercial');

INSERT INTO Estado VALUES (null, 'Disponible'), (null, 'No Disponible');

INSERT INTO OperatoriaComercial VALUES (null, 'Venta'), (null, 'Alquiler');

INSERT INTO Propietario VALUES 
(null, 'Acosta Juan', 'Alberdi 123', 456789456), 
(null, 'González María', 'Sarmiento 412', 456769966), 
(null, 'Centurión Sebastián', 'Moreno 632', 454839458),
(null, 'Ojeda Mariana', 'Castelli 456', 456456451),
(null, 'Ruiz Matías', 'San Mrtín 828', 456754752);

INSERT INTO Propiedad (Nombre, Direccion, Contacto) VALUES 
('Alvarez Carlos', 'Azcuénaga 636', '478778965'),
('Oviedo Leandro', 'Mitre 661', '487877855'),
('Gaona Andrea', 'Rivadavia 144', '478333969'), 
('Segovia Martín', 'España 363', '418778641'),
('Ocampos Ana', '25 de Mayo 777', '437788967');