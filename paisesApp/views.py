from django.shortcuts import render

def paises(request):
    return render(request, "templatesPaises/paises.html")

def chile(request):
    data = {
        'chile': 'imagenes/bandera_chile.png',
        "titulo_cl": "Chile",
        "información_cl": "Chile es un país largo y angosto que se extiende por el borde occidental de Sudamérica, con más de 6,000 km de costa en el océano Pacífico. Santiago, su capital, se ubica en un valle rodeado de los Andes y la cordillera de la Costa. En la Plaza de Armas de la ciudad, bordeada de palmeras, se encuentra la catedral neoclásica y el Museo de Historia Nacional. El enorme Parque Metropolitano cuenta con piscinas, un jardín botánico y un zoológico.",
       
    }
    return render(request, "templatesPaises/paises.html", data)

def argentina(request):
    data = {
        'argentina':'imagenes/bandera_argentina.png',
        "titulo_arg": "Argentina",
        "información_arg": "Argentina es un país sudamericano de gran envergadura con un terreno que incluye las montañas de los Andes, lagos glaciales y praderas en las Pampas, la tierra tradicional de pastoreo de su famoso ganado. El país es conocido por el baile y la música del tango. Su gran capital cosmopolita, Buenos Aires, se centra en la Plaza de Mayo, rodeada por imponentes edificios del siglo XIX, como la Casa Rosada, el icónico palacio presidencial.",
       
    }
    return render(request, "templatesPaises/paises.html", data)

def brazil(request):
    data = {
        'brazil':'imagenes/bandera_brazil.png',
        "titulo_br": "Brasil",
        "información_br": "Brasil es un vasto país de Sudamérica que se extiende desde la Cuenca del Amazonas en el norte hasta los viñedos y las enormes cataratas del Iguazú en el sur. Río de Janeiro, simbolizado por su estatua de 38 m del Cristo Redentor sobre el cerro del Corcovado, es famoso por sus ajetreadas playas Copacabana e Ipanema, junto con su enorme y estridente festival del Carnaval, que cuenta con carros alegóricos, exuberantes disfraces y danza y música samba.",
       
    }
    return render(request, "templatesPaises/paises.html", data)
