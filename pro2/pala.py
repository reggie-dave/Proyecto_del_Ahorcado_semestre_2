import random
def palabras(dificultad, tema):
    try:
        match dificultad.lower():
            case "facil":
                match tema.lower():
                    case "animales":
                        lista=[
    "perro",
    "gato",
    "pez",
    "loro",
    "vaca",
    "pato",
    "rana",
    "raton",
    "cebra",
    "oveja"
]
                        res=random.choice(lista)
                        return res

                    case "tecnologia":
                        lista=[
    "mouse",
    "teclado",
    "pantalla",
    "cable",
    "cpu",
    "router",
    "tablet",
    "laptop",
    "usb",
    "wifi"
]
                        res=random.choice(lista)
                        return res

                    case "frutas":
                        lista=[
    "pera",
    "uva",
    "melon",
    "mango",
    "kiwi",
    "limon",
    "coco",
    "guaba",
    "papaya",
    "piña"
]
                        res=random.choice(lista)
                        return res

                    case _:
                        return print("Ingrese un valor valido.")

            case "medio":
                match tema.lower():
                    case "animales":
                        lista=[
    "caballo",
    "elefante",
    "cocodrilo",
    "tortuga",
    "murcielago",
    "jirafa",
    "camello",
    "delfin",
    "ardilla",
    "iguana"
]
                        res=random.choice(lista)
                        return res

                    case "tecnologia":
                        lista=[
    "internet",
    "servidor",
    "software",
    "hardware",
    "programa",
    "monitor",
    "impresora",
    "aplicacion",
    "navegador",
    "memoria"
]
                        res=random.choice(lista)
                        return res

                    case "frutas":
                        lista=[
    "manzana",
    "banana",
    "naranja",
    "sandia",
    "mandarina",
    "granada",
    "cereza",
    "ciruela",
    "guanabana",
    "maracuya"
]
                        res=random.choice(lista)
                        return res

                    case _:
                        return print("Ingrese un valor valido.")

            case "dificil":
                match tema.lower():
                    case "animales":
                        lista=[
    "ornitorrinco",
    "chimpance",
    "rinoceronte",
    "hipopotamo",
    "ajolote",
    "cacatua",
    "suricata",
    "escarabajo",
    "armadillo",
    "murcielago"
]
                        res=random.choice(lista)
                        return res

                    case "tecnologia":
                        lista=[
    "microprocesador",
    "ciberseguridad",
    "inteligenciaartificial",
    "criptografia",
    "virtualizacion",
    "desarrollador",
    "base_de_datos",
    "programacion",
    "automatizacion",
    "telecomunicaciones"
]
                        res=random.choice(lista)
                        return res

                    case "frutas":
                        lista=[
    "carambola",
    "frambuesa",
    "pitahaya",
    "tamarindo",
    "lichi",
    "toronja",
    "mangostan",
    "arándano",
    "zapote",
    "rambutan"
]
                        res=random.choice(lista)
                        return res

                    case _:
                        return print("Ingrese un valor valido.")

            case _:
                return print("Ingrese un valor valido.")

    except IndexError or TypeError:
        print("Error!!! Ingrese un valor valido.")
