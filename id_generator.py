from uuid import uuid4


alumnos = [
"Acuña Asenjo, Sebastián Mauricio",
"Álamos Correa, Benjamín",
"Alegría Rojas, Nicolás Felipe",
"Andrade Rodríguez, Francisco Javier",
"Anwandter Gibson, Juan Pablo",
"Araos Alziary, Vicente Luciano",
"Arriagada Jaque, Ignacio Andrés",
"Azócar Aranda, Emilia",
"Baeza Icaza, Ignacia",
"Balart Schlegel, Trinidad Sofia",
"Barra Fuchslocher, Matías Cristian",
"Bianchi Muñiz, Florencia",
"Bihan Velasco, Pedro",
"Bodelón Ciuffardi, Felipe Javier",
"Bravo Sepúlveda, Sebastián Eduardo",
"Cabezas Betancourt, Alejandro",
"Carrasco Falcon, Daniel Roberto",
"Concha Arévalo, Gonzalo Guillermo",
"Concha Martínez, Claudia Isabel",
"Contardo Valdés, Victoria Alejandra",
"Costa Grove, Carlos Andrés",
"Cuevas Franulic, Nicolás Antonio",
"Dawabe Fajardo, Javiera Andrea",
"De La Taille-Tretinville Undurraga, Paulina María",
"De Vidts Errazuriz, Valentina Ignacia",
"Díaz Quappe, Benjamín",
"Donati Lara, Franco Paolo",
"Donoso Guzmán, Uranía Selene",
"Echavarría Schafer, Alfredo",
"Errázuriz Dell'Oro, Antonio José",
"Errázuriz Mc Kay, Joaquín José",
"España Herrera, Josefa Paz",
"Fernández Aburto, Francisca Alejandra",
"Fernández Carrasco, Matías Alejandro",
"Fernández Catalán, Cristóbal Andrés",
"Fernández Julian, Cristóbal",
"Flores Parada, Catalina Fernanda",
"Galdames Llorens, José Andrés",
"Gazmuri Cervantes, José Pedro",
"Giglio Ceruti, Ivanna Belen",
"Goldsack Pérez, Catalina",
"González Aguirre, Vicente",
"González Jones, Benjamín Alfonso",
"Guzmán Salas, Juan Martín",
"Hernández Caldumbide, Sebastián René",
"Hormazábal Pardo, Jessica Yanin",
"Izquierdo Pfingsthorn, Roberto Benjamín",
"Jorquera Roman, Luis Alfonso",
"Jouanne Guzmán, Carlos José",
"Lagos Hurtado, Tomás",
"Leyton Aravena, Benjamin Alberto",
"López Silva, Francisco Javier",
"Luer Sepúlveda, Christian Andrés",
"Marabolí Ayala, Nelson Ignacio",
"Martínez Figueroa, Sergio Ignacio",
"Maturana Álamos, Felipe",
"Meza Aránguiz, Ricardo Benjamín",
"Morales Alcalde, Santiago",
"Muñoz Palma, Martina Paz",
"Navarrete Fernández, Javiera Belén",
"Olguín Valenzuela, Luis Alberto",
"Olivos Inostroza, Carlos Andrés",
"Olivos Poch, Santiago",
"Onetto Hernández, Josemaria",
"Pau Villarino, Santiago",
"Peralta Sarrat, José Ignacio",
"Pérez Bustos, Martín Santiago",
"Plaza Tolosa, Sofia Paz",
"Ramírez Padilla, Juan Pablo",
"Ramos Aspe, Sebastián De Jesús",
"Reyes Zaldívar, Pedro Arturo",
"Riquelme Cepeda, Valeria Sofía",
"Riveros Navarro, Florencia Antonia",
"Rojas Contreras, Javiera Ignacia",
"Russi Brodske, Enrique Alberto",
"Sanchez Elgueta, Felipe Ignacio",
"Sánchez Villar, Martín",
"Sandoval Puebla, Sebastián Ignacio",
"Sepúlveda González, Diego",
"Sfeir Cuevas, Cristóbal Andrés",
"Soto Mutoli, Francisco Andrés",
"Soublette Ruiz De Gamboa, Tomás",
"Stevens Cortés, Amparo Magdalena",
"Struque Barrientos, Ignacio Andrés",
"Uriarte Bravo, Juan José Francisco",
"Uribe Jeria, Alejandra Andrea",
"Urzúa Reyes, Cristóbal",
"Valdés Aspillaga, Mario Jaime",
"Valencia Luttges, Sofía Constanza",
"Valenzuela Torres, José Ricardo",
"Vallejo Ramella, Borja",
"Vargas Besnier, Juan Carlos",
"Vega Ulloa, Vicente Antonio",
"Velasco Gardeweg, Francisca María",
"Venegas Ugarte, Nicolás Agustín",
"Venegas Ugarte, Sebastián Ignacio",
"Vial Díaz, María Josefina Carolina",
"Villalobos Vega, Wladimir Nicolas",
"Zalaquett Mc Kay, Juan Agustín",
]

result = {}

for a in alumnos:
    id_alumno = str(uuid4())
    print(id_alumno)
    result[id_alumno] = a

print(result)