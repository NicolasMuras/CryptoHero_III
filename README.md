<h1> CryptoHero III </h1>

![alt text](https://github.com/NicolasMuras/CryptoHero_III_Leyends_Of_Bitcoin/blob/main/images/example_ui.jpg?raw=true)

<h2><a id="user-content-tabla-de-contenido" class="anchor" aria-hidden="true" href="#tabla-de-contenido"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Tabla de contenido
</h2>
<ul>
  <li><a href="#introduccion-al-proyecto">Introducción al proyecto</a></li>
  <li><a href="#implementaci%C3%B3n-del-proyecto">Implementacion del proyecto</a></li>
  <li><a href="#instalaci%C3%B3n-de-dependencias">Instalacion de dependencias</a></li>
  <li><a href="#iniciar-la-aplicacion">Iniciar la aplicación</a></li>
  <li><a href="#resultados">Resultados</a></li>
</ul>

<h2><a id="user-content-introduccion-al-proyecto" class="anchor" aria-hidden="true" href="#introduccion-al-proyecto"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Introduccion al proyecto</h2>

La tecnología avanza. Estamos en el año 2078.
El sistema monetario de billetes y monedas se deja de utilizar, ahora los pagos se realizan de forma electrónica.
Artistas callejeros de todas partes del mundo buscan una manera de poder seguir siendo remunerados actuando en las calles.
Buscan un programador, se contactan conmigo y les ofrezco una solución, un sistema de pago electrónico.
Para esto se construye un pedal de guitarra, tiene delay pero también android y pantalla tactil.
Después, el artista solo tiene que descargar la aplicación, esta proveera una wallet y algunas funcionalidades.
Ahora los artistas en su gorra tendrán un código QR que servirá para aceptar pagos en criptomonedas.

<h3>Características de la aplicación:</h3>
<ul>
<li><strong>Funcion basica: El usuario deberia poder enviar sus datos para registrarse, luego registrar sus canciones, poder ver un listado de sus canciones y elegir cual va a tocar. Cuando una persona le page, junto al pago, se adjuntarian datos de coordenadas, tiempo, fecha y la canción que esta sonando. Internamente se añadiria ese monto modelo que gestione el dinero recaudado para esa canción. Inmediatamente se puede visualizar en el historial de pagos (pantalla) el pago realizado.</strong></li>
<li><strong>Mapa: El mapa solicitaria a la API los pagos almacenados, el monto se transformaria en un rango de colores, del rojo al verde, las coordenadas servirian para pintar puntos en el mapa, el verde nos indicaria las zonas en las que el artista recibe mejor remuneración y el rojo lo contrario.</strong></li>
<li><strong>Registro: En el area del registro se solicitara el listado de albumes asociados a dicho artista, y cada album contendra sus canciónes, al lado de cada canción se podra visualizar la cantidad de dinero ganada por cada una de ellas.</strong></li>
<li><strong>Grafico: El grafico solicitara el dato de fecha dentro del modulo 'payments', como asi tambien el mismo monto de cada dia, en base a esto se construira un grafico que permitira al artista visualizar su crecimiento economico a lo largo del tiempo.</strong></li>
</ul>

<h2><a id="user-content-implementación-del-proyecto" class="anchor" aria-hidden="true" href="#implementación-del-proyecto"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Implementación del proyecto</h2>
<ul>
<li><strong>Python</strong>: El lenguaje utilizado para la elaboracion del codigo.</li>
<li><strong>Django</strong>: Framework open-source utilizado para la elaboración del proyecto.</li>
<li><strong>Django REST Framework</strong>: Es una aplicación de django que nos permitira contruir el proyecto bajo la arquitectura REST.</li>
<li><strong>Ecosistema Docker (docker, Dockerfile, Docker-Compose)</strong>:  A partir del Dockerfile en el raíz del proyecto se puede compilar la imagen que corre la REST API hecha en Django REST Framework, con todas sus dependencias y código fuente dentro. Con Docker-Compose se puede ejecutar la aplicación con un único comando, creando además un servidor de base de datos PostgreSQL.</li>
<li><strong>PostgreSQL</strong>: Sistema de gestion de base de datos elegido.</li>
<li><strong>django-simple-history</strong>: Guarda el estado del modelo Django en cada create/update/delete.</li>
<li><strong>Insomnia</strong>: Utilizo insomnia para ir testeando la aplicación mediante requests a medida que avanzo.</li>
<li><strong>virtualenv</strong>: Recomiendo utilizar entornos virtuales, nos hace la vida mas facil :D.</li>
</ul>

Empecé tomando el lugar del cliente, establecí mis requerimientos sin pensar en 'programación', en base a eso, pase a escribir un pequeño backlog (sección introducción), este serviría para destacar objetos que podrían ser nuestros 'modelos' a la hora de programar además de ayudarnos a diferenciar los distintos usos que el usuario podría darle a dichos objetos (datos). Hice un boceto con las relaciones que estos objetos podrían tener entre si. Ya tenia mi diseño, es sencillo, y creo que es ideal para exponer.
Procedí a escribir el código del programa, busco que sea prolijo y funcional al principio, luego se hace un refactoring con el objetivo de optimizar y simplificar el código.
Una vez que una característica esta lista, pusheamos a Git. Hacemos rebuild a nuestro contenedor en Docker y seguimos trabajando. Al final, se documenta el código.

Me propuse un desafío personal, si bien me dijeron que la entrevista seria casual y relajada, no quería ir con las manos vacías, la pregunta es la siguiente: 

<h3>¿ Como uno puede demostrar su capacidad de adaptación y aprendizaje?.</h3>

La respuesta a esto es utilizar una medida estándar como es el tiempo, para aprender una nueva tecnología en tiempo record e implementarla en un proyecto real !
Me anime a implementar el ecosistema de Docker por primera vez en un proyecto que quizás si, quizás no, me tocaría exponer.
Sigo los mismos principios que utilizo para mis proyectos con DRF anteriores, pero en este utilizo diversos métodos para los diferentes modelos que se incluyen en la api, 
quiero dejar claro, lo ideal es seguir un mismo patrón y ser consistente en cuanto a código se refiere, pero teniendo un framework tan grande y flexible como lo es "Django REST Framework" en este proyecto en especifico busque destacar mi flexibilidad, conozco diferentes maneras de trabajar, y puedo hacer uso de ellas cuando la situación lo requiera.
Esto se traduce en mostrar una mejor adaptación al trabajo de otro desarrollador y comprensión de distintos patrones de desarrollo.

Que aprendi con Docker: <br>
Es una buena practica utilizar esta tecnologia a la hora de comenzar un proyecto, pero tambien es adaptable a un proyecto en curso.
Es el presente y futuro de los microservicios.

<h3>Estructura del proyecto:</h3>

Utilizo una estructura escalable desde el comienzo, se me hace mas organizado y facil de manejar, me gusta separar bien los archivos y carpetas.

<pre>
PROYECT
│   manage.py
│
├───apps
│   │   
│   │
│   ├───base
│   │   │   admin.py
│   │   │   api.py
│   │   │   apps.py
│   │   │   models.py
│   │   │   tests.py
│   │   │   views.py
│   │   │   
│   │   │
│   │   └───migrations
│   │          
│   │
│   ├───payments
│   │   │   admin.py
│   │   │   apps.py
│   │   │   models.py
│   │   │   
│   │   │
│   │   ├───api
│   │   │   │   urls.py
│   │   │   │   
│   │   │   │
│   │   │   ├───serializers
│   │   │   │       general_serializers.py
│   │   │   │       payment_serializers.py
│   │   │   │       
│   │   │   │
│   │   │   └───views
│   │   │           general_views.py
│   │   │           payment_views.py
│   │   │           
│   │   │
│   │   ├───migrations
│   │   │       0001_initial.py
│   │   │       
│   │   │
│   │   └───tests
│   │           test_api.py
│   │           test_common.py
│   │           test_ui.py
│   │          
│   │
│   └───songs
│       │   admin.py
│       │   apps.py
│       │   models.py
│       │   
│       │
│       ├───api
│       │   │   urls.py
│       │   │   
│       │   │
│       │   ├───serializers
│       │   │       general_serializers.py
│       │   │       song_serializers.py
│       │   │       
│       │   │
│       │   └───views
│       │           general_views.py
│       │           song_views.py
│       │           
│       │
│       ├───migrations
│       │       0001_initial.py
│       │       0002_auto_20210213_1527.py
│       │       
│       │
│       └───tests
│               test_api.py
│               test_common.py
│               test_ui.py
│               
│
└───PROYECT
    │   asgi.py
    │   db.sqlite3
    │   urls.py
    │   wsgi.py
    │   
    │
    └───settings
            base.py
            local.py
            production.py
            
</pre>

<h2><a id="user-content-instalación-de-dependencias" class="anchor" aria-hidden="true" href="#instalación-de-dependencias"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Instalación de dependencias</h2>

<p>Para correr este proyecto se necesitan las siguientes dependencias:</p>
<ul>
<li><a href="https://www.python.org/" rel="nofollow">Python 3+</a> (sólo necesario para modo desarrollo o testing).</li>
<li><a href="https://docs.docker.com/get-docker/" rel="nofollow">Docker</a>.</li>
<li><a href="https://docs.docker.com/compose/install/" rel="nofollow">Docker compose</a>.</li>
</ul>
<p>Una vez instaladas las dependencias se puede correr la aplicación.</p>

<h2><a id="user-content-iniciar-la-aplicacion" class="anchor" aria-hidden="true" href="#iniciar-la-aplicacion"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Iniciar la aplicación</h2>

La aplicación funciona sobre Docker-Compose, de esta manera se puede correr la misma en cualquier sistema operativo.

El primer paso es ejecutar la aplicación con el comando a continuación.

<pre><code>docker-compose up
</code></pre>
<em>
  Nota: Si es la primera vez que se ejecuta la aplicación, puede haber errores con respecto a existencia de la base de datos 'app', usted puede ejecutar primero el servicio PostgreSQL y crearla con los siguientes comandos.
</em><br>
<br>
<pre>
<code># su postgres
</code>
</pre>

<pre>
<code># psql
</code>
</pre>

<pre>
<code>postgres-# create database app;
</code>
</pre>

Es necesario notar que esto sólo ocurrirá la primera vez que se ejecute la aplicación.

<h2><a id="user-content-resultados" class="anchor" aria-hidden="true" href="#resultados"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Resultados</h2>

El resultado son los siguientes endpoints:<br>
En 'user' tenemos un endpoint para crear usuario, proporcionando nombre, email y contraseña, luego tenemos un endpoint para logearnos y recibir un token de acceso.
El token de acceso nos permitirá acceder a información relacionada a los pagos (pay / location). Cada pago tiene adjunto un 'location' único. No se implementa un endpoint para actualizar pagos o localizaciones ya que no es un valor que se necesite modificar.

![alt text](https://github.com/NicolasMuras/CryptoHero_III_Leyends_Of_Bitcoin/blob/main/images/endpoints_1.bmp?raw=true)

CRUD completo para Song, Album y Artist. La relación funciona así, una canción puede o no pertenecer a un álbum, pero es obligatorio que pertenezca a un artista.
Por otro lado, un álbum debe pertenecer a un artista obligatoriamente.

![alt text](https://github.com/NicolasMuras/CryptoHero_III_Leyends_Of_Bitcoin/blob/main/images/endpoints_2.bmp?raw=true)

