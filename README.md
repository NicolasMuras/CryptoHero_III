<h1> CryptoHero III: Leyends Of Bitcoin </h1>

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
Artistas independientes de todas partes del mundo buscan una manera de poder seguir siendo remunerados actuando en las calles.
Buscan un programador, se contactan conmigo y les ofrezco una solución, un sistema de pago electrónico.
Para esto se construye un pedal de guitarra, tiene delay pero también funciona como wallet de criptomonedas.
Después, el artista solo tiene que descargar una aplicación en su dispositivo móvil.
Ahora los artistas en su gorra tendrán un código QR que servirá para aceptar pagos criptográficos.

Características de la app:
* El usuario puede visualizar mediante un gps cuales son los lugares en los que recibe mejor remuneración.
* Puede visualizar las horas donde la remuneración es mas alta.
* Puede registrar sus canciones y ver cual es su canción mas exitosa.
* Podrá ver el monto total ganado en bitcoins
* Oyentes podrán adjuntar con su pago un comentario y otorgar una puntuación.

Endpoints:
* Recibir datos de gps. (x, y)
* Recibir horario / fecha (mes, dia, hora, min)
* Recibir feedback. (puntuación, comentario)
* Recibir pagos. (cantidad, tipo de criptomoneda)
* Recibir registro de canciones: (id, nombre_genero), (id, nombre_cancion), (nombre_artistico, nombre, apellido), (nombre_album, cantidad_canciones).

* Enviar rango de colores (rojo - verde) entre mas verde, mejor es la remuneración en dicho lugar u horario.
* Enviar monto total ganado en dolares.

Modelos:<br>
* Artista --> Album --> Cancion

* Pay
* Wallet

Abstracto:<br>
Album --> Genero<br>
Pay --> Location, DateTime, Feedback.
