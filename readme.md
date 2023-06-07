# Test ORBIDI

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

# API REST

Esta es una API REST creada con el propósito de proporcionar acceso a dos endpoints para realizar  funcionalidades descritas en el archivo de prueba tecnica.

## Endpoints

La API REST tiene los siguientes endpoints disponibles:

### user/

Este endpoint permite realizar una determinada funcionalidad relacionada con la creacion de usuario en la plataforma de Hubspot. A continuación se detallan los detalles de uso:

- **URL:** `/user`
- **Método:** POST
- **Parámetros de entrada:**
  - `email`: (str) 
  - `firstname":`: (str)
  - `lastname`: (str) 
  - `phone":`: (str)
  - `website":`: (str)
- **Cuerpo de la solicitud (payload):**
  ```json
  {
    "email": "test@orbidi.com",
    "firstname": "Test",
    "lastname": "Orbidi",
    "phone": "(322) 123-4567",
    "website": "orbidi.com"
}

### sync/

Este endpoint permite realizar una determinada funcionalidad relacionada con la creacion y sincronizacion de usuarios en la plataforma de clickUp. A continuación se detallan los detalles de uso:

- **URL:** `/sync`
- **Método:** GET


## Instalacion

Requiere python en la version 3.7 +

Instalar paquetes y levantar servidor de desarrollo

```sh
python -m venv ven
cd venv/Scrits/
en windows
activate.bat
```

Instalar requeriments.txt
```sh
pip install -r requeriments.txt
```

Levantar servidor de desarrollo

```sh
uvicorn main:app --reload 
```

Visitar url 
```sh
http://127.0.0.1:8000/
```

## License

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>