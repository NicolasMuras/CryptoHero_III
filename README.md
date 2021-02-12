# CryptoHero_III_Leyends_Of_Bitcoin
RESTful API con Django REST Framework, unit testing con pytest, y diseño y desarrollo de bases de datos con MySQL. Limite de tiempo: 7 Días.

La tecnologia avanza. Estamos en el año 2078.
El sistema monetario de billetes y monedas se deja de utilizar, ahora los pagos se realizan de forma electronica.
Artistas independientes de todas partes del mundo buscan una manera de poder seguir siedo remunerados actuando en las calles.
Buscan un programador, se contactan conmigo y les ofrezco una solución, un sistema de pago electronico.
Para esto se construye un pedal de guitarra, tiene delay pero tambien funciona como wallet de criptomonedas.
Despues, el artista solo tiene que descargar una aplicación en su dispositivo movil.
Ahora los artistas en su gorra tendran un codigo QR que servira para aceptar pagos criptográficos.

Caracteristicas de la app:
* El usuario puede visualizar mediante un gps cuales son los lugares en los que recibe mejor remuneración.
* Puede visualizar las horas donde la remuneración es mas alta.
* Puede registrar sus canciones y ver cual es su cancion mas exitosa.
* Podra ver el monto total ganado en bitcoins
* Oyentes podran adjuntar con su pago un comentario y otorgar una puntuación.

Endpoints:
* Recibir datos de gps. (x, y)
* Recibir horario / fecha (mes, dia, hora, min)
* Recibir feedback. (puntuacion, comentario)
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
