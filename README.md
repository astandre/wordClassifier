# Clasificador de palabras

## Instalacion
Para instalar las dependencias necesarias usar el comando:

``
pip install -r requirements.txt
``
## Configuracion

Debemos configurar la base de datos que vayamos a usar, en el archivo .env (Este archivo puede estar invisible en entornos linux). Gracias al ORM utiliza las tablas se generaran automaticamente.

``
DATA_BASE='mysql+pymysql://user:pass@localhost/db_name'
``



## Uso

Para usar la aplicacion debemos ejecutarla de la siguiente manera:
``
python Main.py -f archivo.txt
``
 



