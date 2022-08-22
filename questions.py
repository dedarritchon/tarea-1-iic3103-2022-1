SAMPLE_QUESTIONS = [
    
    {
        "type": "text",
        "title": "Quién es el creador de Javascript?",
        "options": {},
        "answer": "Brendan Eich",
        "wait": 20,
        "points": 10
    },
    {
        "type": "chat",
        "title": "Quién es el creador de Python?",
        "options": {},
        "answer": "Guido van Rossum",
        "wait": 20,
        "points": 10
    },
    {
        "type": "text",
        "title": "Quién es el creador de Linux?",
        "options": {},
        "answer": "Linus Torvalds",
        "wait": 10,
        "points": 10
    },
    {
        "type": "chat",
        "title": "Quién es el creador de Microsoft?",
        "options": {},
        "answer": "Bill Gates",
        "wait": 10,
        "points": 5
    },
    {
        "type": "chat",
        "title": "Quién es el creador de Macintosh?",
        "options": {},
        "answer": "Steve Jobs",
        "wait": 10,
        "points": 5
    },
    {
        "type": "text",
        "title": "Quién es el creador de WebSocket?",
        "options": {},
        "answer": "Michael Carter",
        "wait": 15,
        "points": 15
    },
    {
        "type": "chat",
        "title": "Quién es el CEO de Google?",
        "options": {},
        "answer": "Sundar Pichai",
        "wait": 20,
        "points": 5
    },
    {
        "type": "text",
        "title": "Quién es el CEO de Apple?",
        "options": {},
        "answer": "Tim Cook",
        "wait": 15,
        "points": 5
    },
    {
        "type": "chat",
        "title": "Quién es el CEO de Amazon?",
        "options": {},
        "answer": "Jeff Bezos",
        "wait": 15,
        "points": 5
    },
    {
        "type": "text",
        "title": "Quién es el CEO de Tesla?",
        "options": {},
        "answer": "Elon Musk",
        "wait": 15,
        "points": 5
    },
    {
        "type": "chat",
        "title": "Qué año se inventó la World Wide Web?",
        "options": {},
        "answer": "1990",
        "wait": 20,
        "points": 10
    },
    {
        "type": "button",
        "title": "Cuál de las siguientes afirmaciones es FALSA respecto a los servicios:",
        "options": {
            1: "Es deseoso que el servicio tenga bajo acoplamiento", 
            2: "La comunicación solo tiene dos mensajes: solicitud y respuesta",
            3: "La comunicación es punto a punto",
            4: "La comunicación es iniciada por el servidor"
        },
        "answer": 4,
        "wait": 20,
        "points": 5
    },
    {
        "type": "button",
        "title": "Cuál de las siguientes afirmaciones es verdadera:",
        "options": {
            1: "Si bien son pocos, existen casos en los que el servidor inicia la comunicación", 
            2: "La comunicación termina cuando el cliente deja de hacer solicitudes al servidor",
            3: "La comunicación se inicia cuando el cliente envia un request al servidor y este último entrega la información solicitada",
            4: "El servidor está esperando recibir una solicitud por parte de un cliente"
        },
        "answer": 4,
        "wait": 20,
        "points": 15
    },
    {
        "type": "button",
        "title": "Cuál de las siguientes NO es un método del protocolo http:",
        "options": {
            1: "Get", 
            2: "Delete",
            3: "Post",
            4: "Push"
        },
        "answer": 4,
        "wait": 20,
        "points": 5
    },
    {
        "type": "button",
        "title": "Cuál de los siguientes códigos se refiere a un error en el servidor:",
        "options": {
            1: "300", 
            2: "404",
            3: "400",
            4: "500"
        },
        "answer": 4,
        "wait": 20,
        "points": 10
    },
    {
        "type": "button",
        "title": "Cuál de la siguiente información NO va en el header de un determinado request de tipo POST.",
        "options": {
            1: "Credenciales de autorización para realizar un request de tipo POST", 
            2: "Id del elemento creado en un request de tipo POST",
            3: "Formato del body en un request de tipo POST",
            4: "El envío de cookies por parte del cliente al servidor en un request de tipo POST"
        },
        "answer": 2,
        "wait": 20,
        "points": 5
    },
    {
        "type": "button",
        "title": "REST significa:",
        "options": {
            1: "Representational State Transfer", 
            2: "Representational State Transform",
            3: "Representational Station Transform",
            4: "Representational Statement Topic"
        },
        "answer": 1,
        "wait": 20,
        "points": 5
    },
    {
        "type": "button",
        "title": "Cuál de las siguientes afirmaciones respecto al estilo de arquitectura REST es verdadera:",
        "options": {
            1: "REST impone un estándar formal", 
            2: "REST permite saber si un servicio es Restful o no",
            3: "REST define un set de restricciones con objetivos específicos",
            4: "REST no conversa con el protocolo HTTP"
        },
        "answer": 3,
        "wait": 20,
        "points": 10
    },
    {
        "type": "button",
        "title": "Cual de los siguientes principios NO corresponde a un princpio clave en el diseño de servicios REST",
        "options": {
            1: "Deben ser simples e intuitivos", 
            2: "Deben ser eficientes",
            3: "Deben ser baratos de mantener",
            4: "Deben estar bien documentados"
        },
        "answer": 3,
        "wait": 20,
        "points": 5
    },
    {
        "type": "button",
        "title": "Cuál de los siguientes métodos realiza consultas read-only",
        "options": {
            1: "POST", 
            2: "HEAD",
            3: "PATCH",
            4: "DELETE"
        },
        "answer": 2,
        "wait": 15,
        "points": 5
    },
    {
        "type": "button",
        "title": "Cuál de las siguientes características NO corresponde a una limitación de los servicios REST:",
        "options": {
            1: "El cliente no tiene la capacidad  de usar respuestas anteriores por lo que no se evita duplicar llamadas", 
            2: "Los servicios REST son ineficientes para ir a buscar información de muchos objetos a la vez",
            3: "Solo opera sobre HTTP",
            4: "El cliente no tiene la capacidad de ser notificado de cambios en los datos por parte del servidor"
        },
        "answer": 1,
        "wait": 20,
        "points": 10
    },
    {
        "type": "text",
        "title": "Qué status code lleva la respuesta: Created ?",
        "options": {},
        "answer": "201",
        "wait": 10,
        "points": 2
    },
    {
        "type": "text",
        "title": "Qué status code lleva la respuesta: Partial Content ?",
        "options": {},
        "answer": "206",
        "wait": 10,
        "points": 3
    },
    {
        "type": "text",
        "title": "Qué status code lleva la respuesta: Bad Request ?",
        "options": {},
        "answer": "400",
        "wait": 10,
        "points": 2
    },
    {
        "type": "chat",
        "title": "Qué status code lleva la respuesta: Payment Required ?",
        "options": {},
        "answer": "402",
        "wait": 10,
        "points": 5
    },
    {
        "type": "chat",
        "title": "Qué status code lleva la respuesta: Forbidden ?",
        "options": {},
        "answer": "403",
        "wait": 10,
        "points": 2
    },
    {
        "type": "chat",
        "title": "Qué status code lleva la respuesta: Not Found ?",
        "options": {},
        "answer": "404",
        "wait": 10,
        "points": 2
    },
    {
        "type": "chat",
        "title": "Qué status code lleva la respuesta: Method Not Allowed ?",
        "options": {},
        "answer": "405",
        "wait": 10,
        "points": 2
    },
    {
        "type": "chat",
        "title": "Qué status code lleva la respuesta: Too Many Requests ?",
        "options": {},
        "answer": "429",
        "wait": 10,
        "points": 4
    },
    {
        "type": "chat",
        "title": "Qué status code lleva la respuesta: Internal Server Error ?",
        "options": {},
        "answer": "500",
        "wait": 10,
        "points": 2
    },
    {
        "type": "chat",
        "title": "Qué status code lleva la respuesta: Bad Gateway ?",
        "options": {},
        "answer": "502",
        "wait": 10,
        "points": 4
    },
    {
        "type": "text",
        "title": "Qué status code lleva la respuesta: Service Unavailable ?",
        "options": {},
        "answer": "503",
        "wait": 10,
        "points": 4
    },
    {
        "type": "chat",
        "title": "Qué status code lleva la respuesta: Accepted ?",
        "options": {},
        "answer": "202",
        "wait": 10,
        "points": 3
    },
    {
        "type": "chat",
        "title": "Qué status code lleva la respuesta: OK ?",
        "options": {},
        "answer": "200",
        "wait": 10,
        "points": 1
    },
    {
        "type": "chat",
        "title": "Qué status code lleva la respuesta: Switching Protocols ?",
        "options": {},
        "answer": "101",
        "wait": 10,
        "points": 5
    },
    {
        "type": "chat",
        "title": "¿Quién inicia la conexión en un servicio? El...",
        "options": {},
        "answer": "Cliente",
        "wait": 10,
        "points": 20
    },
    {
        "type": "text",
        "title": "La siguiente característica de uso, corresponde a un evento o un servicio?: Basta con conocer el contrato de comunicación para realizar un request",
        "options": {},
        "answer": "Servicio",
        "wait": 15,
        "points": 2
    },
    {
        "type": "chat",
        "title": "¿Cómo se denomina al tiempo de demora entre una transmisión y recepción de datos en una red?",
        "options": {},
        "answer": "Latencia",
        "wait": 20,
        "points": 3
    },
    {
        "type": "chat",
        "title": "¿Qué significa la H en HTTP?",
        "options": {},
        "answer": "Hypertext",
        "wait": 20,
        "points": 5
    },
    {
        "type": "chat",
        "title": "¿Cuál es la llave de cabecera (header) usada para indicar el media type (en-US) de un recurso?",
        "options": {},
        "answer": "Content-Type",
        "wait": 15,
        "points": 5
    },
    {
        "type": "chat",
        "title": "¿A qué corresponde la siguiente definición?: una pequeña pieza de datos que un servidor envía al navegador. El navegador puede guardar estos datos para, por ejemplo, mantener la sesión de un usuario abierta.",
        "options": {},
        "answer": "Cookie",
        "wait": 20,
        "points": 4
    },
    {
        "type": "chat",
        "title": "¿A qué corresponde la siguiente definición?Almacenamiento intermedio que permite reducir la latencia, tráfico de red y procesamiento, reduciendo el tiempo necesario para obtener algún recurso.",
        "options": {},
        "answer": "Cache",
        "wait": 20,
        "points": 4
    },
    {
        "type": "text",
        "title": "¿Quién es el creador de Temple OS? ",
        "options": {},
        "answer": "Terry Davis",
        "wait": 20,
        "points": 50
    },
    {
        "type": "chat",
        "title": "Complete la oración: Se dice que una llamada HTTP con el método _____ es idempotente y segura.",
        "options": {},
        "answer": "GET",
        "wait": 20,
        "points": 5
    },
    {
        "type": "chat",
        "title": "Complete la oración: ________ Zuckerberg",
        "options": {},
        "answer": "Mark",
        "wait": 10,
        "points": 5
    },
    {
        "type": "text",
        "title": "Complete la oración: _______ Stark",
        "options": {},
        "answer": "Tony",
        "wait": 10,
        "points": 5
    },
    {
        "type": "text",
        "title": "Complete la oración: _______ Tagle",
        "options": {},
        "answer": "Arturo",
        "wait": 10,
        "points": 20
    },
    {
        "type": "text",
        "title": "Complete la oración: Vanilla __________",
        "options": {},
        "answer": "Javascript",
        "wait": 10,
        "points": 5
    },
    {
        "type": "chat",
        "title": "Complete la oración: _____ Atlas",
        "options": {},
        "answer": "MongoDB",
        "wait": 10,
        "points": 5
    },
    {
        "type": "text",
        "title": "Complete la oración: ______ Cloud Platform",
        "options": {},
        "answer": "Google",
        "wait": 10,
        "points": 5
    },
    {
        "type": "text",
        "title": "Complete la oración: Amazon _____ Services",
        "options": {},
        "answer": "Web",
        "wait": 10,
        "points": 5
    },
    {
        "type": "button",
        "title": "Las URLs se construyen a partir de secciones que identifican distintas características de esta. En la siguiente URL: http://www.google.com/search?q=facebook#result a que corresponde q=facebook?",
        "options": {
            1: "fragment", 
            2: "domain",
            3: "path",
            4: "query parameters"
        },
        "answer": 4,
        "wait": 20,
        "points": 5
    },
    {
        "type": "button",
        "title": "Qué significa el status code 418 ?",
        "options": {
            1: "Internal Server Error", 
            2: "I'm a teapot",
            3: "Bad Request",
            4: "Not Found"
        },
        "answer": 2,
        "wait": 20,
        "points": 10
    },
    {
        "type": "button",
        "title": "¿Cuál es la fecha conocida como Unix Epoch?",
        "options": {
            1: "1 de enero de 1970 a las 00:00:00", 
            2: "4 de marzo de 1992 a las 12:00:00",
            3: "1 de junio de 2000 a las 00:00:00",
            4: "1 de diciembre de 1995 a las 23:59:59"
        },
        "answer": 1,
        "wait": 20,
        "points": 5
    },
    {
        "type": "button",
        "title": "¿Cuál de estos no es una forma de integrar servicios?",
        "options": {
            1: "Base de datos compartidas", 
            2: "RPC (Remote Procedure Call)",
            3: "Telekinesis",
            4: "Eventos"
        },
        "answer": 3,
        "wait": 20,
        "points": 5
    },
    {
        "type": "button",
        "title": "En el contexto de eventos, ¿Quiénes son los participantes?",
        "options": {
            1: "Cliente y servidor", 
            2: "Un emisor",
            3: "Un emisor y multiples suscriptores",
            4: "Servidor"
        },
        "answer": 3,
        "wait": 20,
        "points": 5
    },
    {
        "type": "button",
        "title": "En el contexto de eventos, ¿Qué es un suscriptor?",
        "options": {
            1: "Todos los clientes que no quieren recibir notificaciones", 
            2: "Todos los clientes que quieren recibir notificaciones",
            3: "El servidor",
            4: "Un usuario de Netflix"
        },
        "answer": 2,
        "wait": 20,
        "points": 5
    },
    {
        "type": "button",
        "title": "¿Cuál es el sistema operativo más usado en el mundo?",
        "options": {
            1: "Windows", 
            2: "Macintosh",
            3: "Linux",
            4: "Temple OS"
        },
        "answer": 3,
        "wait": 20,
        "points": 5
    },
    {
        "type": "button",
        "title": "¿Qué es una API?",
        "options": {
            1: "Es un estándar de desarrollo de servicios web", 
            2: "Es una interfaz que entrega un software para ser usado",
            3: "Sistema de suscripción de eventos",
            4: "Un framework"
        },
        "answer": 2,
        "wait": 20,
        "points": 5
    },
    {
        "type": "button",
        "title": "¿Cuál de los siguientes es un framework de JavaScript?",
        "options": {
            1: "Django", 
            2: "Ruby on Rails",
            3: "Vue",
            4: "Blazor"
        },
        "answer": 3,
        "wait": 20,
        "points": 5
    },
    {
        "type": "button",
        "title": "¿Qué lenguaje es de más bajo nivel?",
        "options": {
            1: "Python", 
            2: "C",
            3: "Assembly",
            4: "Javascript"
        },
        "answer": 3,
        "wait": 20,
        "points": 5
    },
    {
        "type": "button",
        "title": "¿Cuál de estas no es una línea de comandos real?",
        "options": {
            1: "bash", 
            2: "cmd",
            3: "powershell",
            4: "shelly"
        },
        "answer": 4,
        "wait": 20,
        "points": 5
    }
]