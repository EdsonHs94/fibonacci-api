# Prueba Fibonacci

Para realizar esta aplicacion se utilizaron las siguientes tecnologias (python).

  - Fhalcon como framework
  - nosetest para los test unitarios
  - Gunicorn como servidor

# Comentarios

  - Para esta aplicacion solo e usado el api de Flacon, queriendo asemejar al enfoque DDD (Diseño guiado por el dominio)
  - Por el tiempo solo realice test unitarios simples
  - Por el tiempo no pude incluirle a este desarrollo un contenedor de docker

### Instalacion

Antes de hacer funcionar este servicio hay que aclarar que los pasos de instalacion estan vistos para el uso de python3 y pip3

Primero crearemos un venv
```sh
$ python3 -m venv api-env
```

Luego activamos este venv
```sh
$ source api-env/bin/activate 
```

Luego instalamos las dependencias
```sh
$ pip3 install -r requeriments.txt
```

Finalmente ponemos a correr la aplicacion
```sh
$ cd app
$ gunicorn wsgi:api
```

For production environments...

```sh
$ npm install --production
$ NODE_ENV=production node app
```

Para verificar entrar a localhost:8000

### Uso

Este servicio solo riene 2 rutas que son las siguientes

  - /: ruta base donde da un mensaje simple
  - /fibonacci/{numero}: Aqui retornaremos lo pedido el n-esimo numero de la sucecion de Fibonacci

