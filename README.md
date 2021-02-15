<h1> CryptoHero III: Leyends Of Bitcoin </h1>

![alt text](https://github.com/NicolasMuras/CryptoHero_III_Leyends_Of_Bitcoin/blob/main/images/example_ui.jpg?raw=true)

<h2><a id="user-content-tabla-de-contenido" class="anchor" aria-hidden="true" href="#tabla-de-contenido"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Tabla de contenido
</h2>
<ul>
  <li><a href="#introduccion-al-proyecto">Introducción al proyecto</a></li>
  <li><a href="#implementaci%C3%B3n-del-proyecto">Implementacion del proyecto</a></li>
  <li><a href="#modelos">Modelos</a></li>
</ul>

<h2><a id="user-content-introduccion-al-proyecto" class="anchor" aria-hidden="true" href="#introduccion-al-proyecto"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Introduccion al proyecto</h2>

La tecnología avanza. Estamos en el año 2078.
El sistema monetario de billetes y monedas se deja de utilizar, ahora los pagos se realizan de forma electrónica.
Artistas callejeros de todas partes del mundo buscan una manera de poder seguir siendo remunerados actuando en las calles.
Buscan un programador, se contactan conmigo y les ofrezco una solución, un sistema de pago electrónico.
Para esto se construye un pedal de guitarra, tiene delay pero también android y pantalla tactil.
Después, el artista solo tiene que descargar la aplicación, esta proveera una wallet y algunas funcionalidades.
Ahora los artistas en su gorra tendrán un código QR que servirá para aceptar pagos en criptomonedas.

<h3>Características de la applicación:</h3>
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
<li><strong>Django REST</strong>: Es una aplicación de django que nos permitira contruir el proyecto bajo la arquitectura REST.</li>
<li><strong>django-simple-history</strong>: Guarda el estado del modelo Django en cada create/update/delete.</li>
<li><strong>Insomnia</strong>: Utilizo insomnia para ir testeando la aplicación mediante requests a medida que avanzo.</li>
<li><strong>virtualenv</strong>: Recomiendo utilizar entornos virtuales, nos hace la vida mas facil :D.</li>
</ul>

Utilizo una estructura escalable desde el comienzo, se me hace mas organizado y facil de manejar, me gusta separar bien los archivos y carpetas.

<h3>Estructura del proyecto:</h3>

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

<h2><a id="user-content-modelos" class="anchor" aria-hidden="true" href="#modelos"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Modelos</h2>

<h3>Artist</h3>

<table>
  <tbody><tr>
   <td><strong>Dato</strong>
   </td>
   <td><strong>Valor</strong>
   </td>
  </tr>
  <tr>
   <td><strong>name</strong>
   </td>
   <td>CharField('Nombre', max_length=100, unique = False, blank = False, null = False)
   </td>
  </tr>
  <tr>
   <td><strong>last_name</strong>
   </td>
   <td>CharField('Apellido', max_length=100, unique = False, blank = False, null = False)
   </td>
  </tr>
  <tr>
   <td><strong>artist_name</strong>
   </td>
   <td>CharField('Nombre Artistico', max_length=100, unique = True, blank = False, null = False)
   </td>
  </tr>
</tbody></table>

<h3>Album</h3>

<table>
  <tbody><tr>
   <td><strong>Dato</strong>
   </td>
   <td><strong>Valor</strong>
   </td>
  </tr>
  <tr>
   <td><strong>name</strong>
   </td>
   <td>CharField('Nombre', max_length=100, unique = False, null = False, blank = False)
   </td>
  </tr>
  <tr>
   <td><strong>release_date</strong>
   </td>
   <td>DateField()
   </td>
  </tr>
  <tr>
   <td><strong>genre</strong>
   </td>
   <td>CharField('Genero', max_length=50, unique = False, null = True, blank = True)
   </td>
  </tr>
  <tr>
   <td><strong>image</strong>
   </td>
   <td>ImageField('Tapa', upload_to='artistas/', blank = True, null = True)
   </td>
  </tr>
  <tr>
   <td><strong>belongs_to_artist</strong>
   </td>
   <td>ForeignKey(Artist, on_delete=models.CASCADE, verbose_name = 'Autor', null = True)
   </td>
  </tr>
</tbody></table>

<h3>Song</h3>

<table>
  <tbody><tr>
   <td><strong>Dato</strong>
   </td>
   <td><strong>Valor</strong>
   </td>
  </tr>
  <tr>
   <td><strong>track_id</strong>
   </td>
   <td>SmallIntegerField()
   </td>
  </tr>
  <tr>
   <td><strong>name</strong>
   </td>
   <td>CharField('Nombre', max_length=100, unique = False, null = False, blank = False)
   </td>
  </tr>
  <tr>
   <td><strong>minutes</strong>
   </td>
   <td>SmallIntegerField()
   </td>
  </tr>
  <tr>
   <td><strong>seconds</strong>
   </td>
   <td>SmallIntegerField()
   </td>
  </tr>
  <tr>
   <td><strong>belongs_to_album</strong>
   </td>
   <td>ForeignKey(Album, on_delete=models.CASCADE, verbose_name = 'Album', null = True)
   </td>
  </tr>
</tbody></table>

