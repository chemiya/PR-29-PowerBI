<h1>Documento resumen del proyecto para crear dashboards con Power BI</h1>




<ol>
    <h2>
        <li>Resumen del proyecto</li>
    </h2>
    <p>En este proyecto se realizarán diferentes dashboards para analizar los datos de diferentes datasets. En primer
        lugar, se describirán los diferentes datasets definiendo sus atributos. En segundo lugar, se definirán preguntas
        que se deben de responder con el dashboard.</p>







<h2><li>Análisis de cada dataset</li></h2>
    <ol>
        <h3>
            <li>Videogames sales</li>
        </h3>
        El dashboard sobre este dataset y el archivo con los datos del dataset se encuentran en la carpeta "videogames
        sales dashboard"

<ul>
            <h4><li>Descripción del dataset</li></h4>
            Este conjunto de datos contiene los datos de ventas de videojuegos con más de 100.000 ventas.

<h4>
                <li>Atributos del dataset</li>
            </h4>
            <ul>
                <li>Rank: clasificación en el ranking de ventas</li>
                <li>Name: nombre del videojuego</li>
                <li>Platform: plataforma del videojuego</li>
                <li>Year: año en el que se publicó</li>
                <li>Genre: género del videojuego</li>
                <li>Publisher: creador del videojuego</li>
                <li>NaSales: ventas en Norte América (millones)</li>
                <li>EuSales: ventas en Europa (millones)</li>
                <li>JpSales: ventas en Japón (millones)</li>
                <li>OtherSales: ventas en el resto del mundo (millones)</li>
                <li>GlobalSales: ventas globales (millones)</li>

</ul>

<h4>
                <li>Preguntas a responder</li>
            </h4>
            <ul>
                <li>¿Cuál fue la región en la que más videojuegos vendió Activision en 2009?</li>
                <li>¿Cuál es la plataforma que más videojuegos ha vendido en Norte América?</li>
                <li>¿Cuál es el género que más videojuegos vende para la plataforma Xbox360? ¿y wii?</li>
                <li>¿Cuál es el creador de videojuegos que más vendió en el año 2000 en Norte América?</li>
                <li>¿Cuál fue el año en Europa en el que más videojuegos se vendieron para la plataforma
                    PS3?</li>
                <li>¿Cuál ha sido el número de ventas de videojuegos en Europa para el género de deportes para la
                    plataforma PS4?</li>

</ul>

</ul>























<h3>
            <li>Supermarket sales</li>
        </h3>
El dashboard sobre este dataset y el archivo con los datos del dataset se encuentran en la carpeta "Supermarket
        sales dashboard"


<ul>
            <h4>
                <li>Descripción del dataset</li>
            </h4>
            Este conjunto de datos contiene las ventas de los productos de un supermercado

<h4>
                <li>Atributos del dataset</li>
            </h4>

<ul>
                <li>Invoice id: id de la factura</li>
                <li>Branch: rama del supermercado</li>
                <li>City: localización del supermercado</li>
                <li>Customer type: tipo de consumidor</li>
                <li>Gender: género del consumidor</li>
                <li>Producto line: tipo de producto vendido</li>
                <li>Unit price: precio por unidad del producto</li>
                <li>Quantity: cantidad de productos comprados</li>
                <li>Tax 5%: impuesto del 5%</li>
                <li>Total: precio total del producto</li>
                <li>Date: fecha de la compra</li>
                <li>Time: hora de la compra</li>
                <li>Payment: método de pago</li>
                <li>COGS: coste de los productos vendidos</li>
                <li>Gross margin percentaje: porcentaje de margen bruto</li>
                <li>Gross income: ingresos brutos por la venta</li>
                <li>Rating: puntuación del cliente</li>



</ul>

<h4>
                <li>Preguntas a responder</li>
            </h4>

<ul>
                <li>¿Cuál han sido los ingresos brutos de todos los productos vendidos en la ciudad de Yangon?</li>
                <li>¿Cuál son los ingresos brutos obtenidos por los productos comprados por los consumidores que son de
                    tipo miembro y pagan con cash?</li>
                <li>¿Cuál es el tipo de producto que más ingresos brutos proporciona en la rama A?</li>
                <li>¿Cuál es el rating medio de los productos vendidos de tipo comida y bebidas?</li>
                <li>¿Cuáles son los ingresos brutos se han obtenido con los productos vendidos de tipo accesorios
                    electrónicos antes del 10 de febrero de 2019 comprados por los clientes que no son miembros? </li>
                <li>¿Cuál fue el dia que más ingresos brutos se obtuvieron en la ciudad de Yangon? </li>


</ul>

</ul>










<h3>
            <li>Formula 1 World Championship (1950 - 2023)</li>
        </h3>
        El dashboard sobre este dataset y los archivos con los datos del dataset se encuentran en la carpeta "F1
        dashboard"
        <ul>
            <h4>
                <li>Descripción del dataset</li>
            </h4>
            Este conjunto de datos contiene todos los datos de las temporadas entre 1950 y 2023 de la
            Formula 1. Este dataset agrupa diferentes dataset. A continuación, se describe cada uno de ellos.

<h4>
                <li>Atributos del dataset: Circuitos</li>
            </h4>
            <ul>
                <li>CircuitId</li>
                <li>Name: nombre del circuito</li>
                <li>Location: localización donde se encuentra</li>
                <li>Country: pais donde se encuentra</li>
                
</ul>


<h4>
                <li>Atributos del dataset: Constructores</li>
            </h4>
            <ul>
                <li>ConstructorId</li>
                <li>Name: nombre del constructor</li>
                
</ul>


<h4>
                <li>Atributos del dataset: Pilotos</li>
            </h4>
            <ul>
                <li>DriverId</li>
                <li>Name: nombre del piloto</li>
                <li>Nacionality: nacionalidad del piloto</li>
                
</ul>

<h4>
                <li>Atributos del dataset: Carrera</li>
            </h4>
            <ul>
                <li>RaceId</li>
                <li>Year: año de la carrera</li>
                <li>CircuitId: id del circuito donde se celebra</li>
                <li>Name: nombre de la carrera</li>
                
</ul>

<h4>
                <li>Atributos del dataset: Resultado</li>
            </h4>
            <ul>
                <li>ResultId</li>
                <li>RaceId: id de la carrera</li>
                <li>DriverId: id del piloto</li>
                <li>ConstructorId: id del constructor del piloto</li>
                <li>Position: posición del piloto en la carrera</li>
                <li>Points: puntos obtenidos por el piloto</li>
                
</ul>


<h4>
                <li>Preguntas a responder</li>
            </h4>
            <ul>
                <li>¿Qué piloto obtuvo más puntos en el año 2018?</li>
                <li>¿Qué piloto ha ganado más veces en el circuito de Spa?</li>
                <li>¿Qué constructor ha obtenido mas puntos en las carreras realizadas en circuitos de Italia?</li>
                <li>¿Qué piloto británico ha obtenido más puntos en la historia?</li>
                <li>¿En qué circuito el piloto Hamilton obtuvo más puntos entre las años 2013 a 2017?</li>
                <li>¿En qué circuito los pilotos alemanes corriendo para el constructor Mercedes han obtenido más
                    puntos? </li>


</ul>
        </ul>
















<h3>
            <li>European Soccer Database</li>
        </h3>
        El dashboard sobre este dataset y los archivos con los datos del dataset se encuentran en la carpeta "Futbol
        dashboard".

<ul>
            <h4>
                <li>Descripción del dataset</li>
            </h4>
            Contiene datos de partidos de fútbol, equipos y ligas entre 2009 y 2016. Este dataset agrupa diferentes
            dataset. A continuación, se describe cada uno de ellos.



<h4>
                <li>Atributos del dataset: Equipo</li>
            </h4>
            <ul>
                <li>TeamId</li>
                <li>Name: nombre del equipo</li>
                
</ul>

<h4>
                <li>Atributos del dataset: Equipo_atributos</li>
            </h4>
            <ul>
                <li>Id</li>
                <li>TeamId: id del equipo al que pertenecen los atributos</li>
                <li>buildUpPlaySpeed: velocidad de juego</li>
                <li>buildUpPlayPassing: velocidad de pase</li>
                <li>chanceCreationPassing: creacion de oportunidades pasando</li>
                <li>chanceCreationShooting: creacion de oportunidades tirando</li>
                <li>defencePressure: presion defensiva</li>
                <li>defenceAggression: agresividad defensiva</li>
            </ul>


<h4>
                <li>Atributos del dataset: Jugador</li>
            </h4>
            <ul>
                <li>PlayerId</li>
                <li>Name: nombre del jugador</li>
                <li>Birthday: fecha de nacimiento del jugador</li>
</ul>

<h4>
                <li>Atributos del dataset: Jugador_atributos</li>
            </h4>
            <ul>
                <li>Id</li>
                <li>PlayerId: id del jugador al que pertenecen los atributos</li>
                <li>OverallRating: puntuacion total del jugador</li>
                <li>PreferredFoot: prierna preferida</li>
                <li>AttackingWorkRate: ratio de trabajo en ataque</li>
                <li>DefensiveWorkRate: ratio de trabajo en defensa</li>
                <li>Finishing: finalizacion</li>
                <li>HeadingAccuracy: precision con la cabeza</li>
                <li>ShortPassing: pases cortos</li>
                <li>Dribbling: dribbling</li>
                <li>FreeKickAccuracy: precision en los tiros libres</li>
                <li>LongPassing: pases en largo</li>
                <li>BallControl: control del balon</li>
                <li>Acceleration: aceleracion</li>
                <li>SprintSpeed: velocidad en sprint</li>
                <li>Agility: agilidad</li>
                <li>ShotPower: potencia de disparo</li>
                <li>Stamina: resistencia</li>
                <li>Strength: fuerza</li>
                <li>LongShot: disparo desde lejos</li>
                <li>Aggression: agresividad</li>
                <li>Interceptions: intercepciones</li>
                <li>Positioning: posicionamiento</li>
                <li>Vision: vision</li>
                <li>GkDiving: capaciodad como portero para lanzarse</li>
                <li>GkHandling: capacidad como portero para atrapar</li>
                <li>GkPositioning: capacidad como portero para posicionarse</li>
                <li>GkReflexes: reflejos como portero</li>

</ul>




<h4>
                <li>Preguntas a responder</li>
            </h4>
            <ul>
                <li>Comparar los principales atributos de dos jugadores. ¿Entre Cristiano Ronaldo y Messi, quién tiene
                    más aceleración agilidad, dribbling, finalización y velocidad al sprint?</li>
                <li>Mostrar los atributos de un equipo. ¿Que equipos tienen un valor superior a 60 en velocidad de juego
                    y de pase?</li>


</ul>
</ul>






<h3>
            <li>Product sales dataset</li>
        </h3>
        El dashboard sobre este dataset y los archivos con los datos del dataset se encuentran en la carpeta
        "product sales dashboard".
        <ul>
            <h4>
                <li>Descripción del dataset</li>
            </h4>
            Este dataset contiene los datos de los productos vendidos por una compañía

<h4>
                <li>Atributos del dataset</li>
            </h4>
            <ul>
                <li>Trimestre: trimestre del año en que se vendió el producto</li>
                <li>Año: año en el que se vendió el producto</li>
                <li>Tipo producto: qué tipo de producto se vendió</li>
                <li>Region: continente en el que se vendió el producto</li>
                <li>Pais: pais en el que se vendió el producto</li>
                <li>Ingresos: ingresos obtenidos por la venta del producto</li>
                <li>Gastos: gastos generados por el producto</li>


</ul>





<h4>
                <li>Preguntas a responder</li>
            </h4>
            <ul>
                <li>¿En 2020, que beneficios se obtuvieron en Estados Unidos, India y China?</li>
                <li>¿Cuál fue el pais donde se obtuvo un mayor margen en 2021?</li>
                <li>¿Qué margen se ha obtenido en Europa con los productos de tipo PC en cada año?</li>
                <li>¿Qué beneficios se obtuvieron en 2019 en América por la venta de productos del tipo celulares?
                </li>
                <li>¿En qué trimestre de 2021 se obtuvieron más beneficios por los productos de tipo musica en
                    Europa?</li>
                <li>¿Qué beneficios y margen se obtuvo en 2020 por la venta de productos de tipo TV en Asia?</li>

</ul>


</ul>




<h3>
            <li>Product sales second dataset</li>
        </h3>
        El dashboard sobre este dataset y los archivos con los datos del dataset se encuentran en la carpeta "product
        sales
        second dashboard".
        <ul>
            <h4>
                <li>Descripción del dataset</li>
            </h4>
            Este dataset contiene los datos de los productos vendidos por una compañía

<h4>
                <li>Atributos del dataset</li>
            </h4>
            <ul>
                <li>Fecha: fecha en la que se vendió el producto</li>
                <li>Marca: marca del producto que se vendió</li>
                <li>Cliente: tipo de cliente que compró el producto</li>
                <li>Pais: pais en el que se vendió el producto</li>
                <li>Ingresos: ingresos obtenidos por la venta del producto</li>
                <li>Gastos: gastos generados por el producto</li>


</ul>





<h4>
                <li>Preguntas a responder</li>
            </h4>
            <ul>
                <li>¿En 2020, en Argentina que margen obtuvieron los productos vendidos de la marca Innovatech?</li>
                <li>¿En 2021 en qué pais se obtuvo mayor margen con los productos vendidos a clientes del tipo sector
                    público ?</li>
                <li>¿En 2020, cuál fue el tipo de cliente que beneficios reportó en Mexico?</li>
                <li>¿Cuál fue el margen medio en el año 2020?</li>
                <li>¿Cuál fue el mes de 2021 en que mayor margen se obtuvo?¿Y en 2020 cuál fue el mes con menor margen?
                </li>
                <li>¿Cuáles han sido los ingresos, gastos, beneficios y margen por los productos vendidos por de la
                    marca
                    Nextec en Chile en el año 2022?</li>

</ul>

</ul>




<h3>
            <li>World population dataset</li>
        </h3>
        El dashboard sobre este dataset y los archivos con los datos del dataset se encuentran en la carpeta "Population
        dashboard".
        <ul>
            <h4>
                <li>Descripción del dataset</li>
            </h4>
            Este dataset contiene los datos de la población en diferentes paises

<h4>
                <li>Atributos del dataset</li>
            </h4>
            <ul>
                <li>Rank: ranking por población</li>
                <li>Country/Territory: nombre del pais o territorio</li>
                <li>Capital: nombre de la capital</li>
                <li>Continent: nombre del continente</li>
                <li>Year population: población en cada de unos años marcados</li>
                <li>Area: área del pais en km2</li>
                <li>Density: densidad de la población por km2</li>
                <li>Growth rate: ratio de crecimiento de la población</li>
                <li>World population porcentage: porcentaje de la población mundial</li>

</ul>


<h4>
                <li>Preguntas a responder</li>
            </h4>
            <ul>
                <li>¿Qué continente en 2010 tenía más población?¿Y en 2020?¿ Y en el 2000?</li>
                <li>¿Qué porcentaje de la población mundial pertenece a Europa?</li>
                <li>¿Qué densidad de población tiene el pais con más habitantes de Asia?</li>
                <li>¿Qué ratio de crecimiento tiene el pais que más porcentaje de la población mundial representa?</li>
                <li>¿Cuál es la suma de los áreas de los 3 paises que más porcentaje de la población mundial
                    representan?</li>
                <li>¿Qué paises tienen una poblacion en 2022 superior a los 50 millones y una densidad de poblacion
                    superior a
                    los 300 habitantes por km2?</li>

</ul>

</ul>

</ol>









<h2>
        <li>Tiempo empleado</li>
    </h2>

<img src="./tiempo empleado.png">



<h2>
        <li>Resultado final: vídeo youtube y repositorio</li>
    </h2>
    Repositorio Github:

Video Youtube:

<h2>
        <li>Conclusiones</li>
    </h2>
    He comprendido diferentes dataset y he podido obtener datos valiosos sobre ellos mediante PowerBI. Con esta
    herramienta
    he podido extraer información muy útil sobre los dataset que puede ser de gran ayuda. Además he podido responder a
    las
    diferentes preguntas planteadas sobre los datos almacenados en los dataset que pueden ayudar a analizar, comprender
    y
    sacar conclusiones de los datos.


</ol>