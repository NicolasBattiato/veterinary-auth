# veterinary-auth
VeterinariaApp

_La funcion del microservicio "veterinary-auth" se encarga de **registrar** a un **Usuario** en la que se guardara los datos como **nombre**, **mail**, **contraseña**, y ademas se le asignara un **Token** el cual podra **refrescar** (actualizar token). Este token contener información que verifica la identidad de un usuario y sus permisos, lo que le servira para poder continuar con peticiones a otros microservicios. Por otro lado el Usuario podra **loguearse**, **verificarse** y **eliminarse**._ 

## Instalacion  

## Docker
Realizando los siguientes pasos, instalara todas las dependencias necesarias para el proyecto y tambien podra levantar los contenedores personalizados en el archivo **docker-compose.yml** para levantar todo el microservicio.

Para levantar los contenedores de redis, postgreSQL y de la API personalizados en docker-compose.yml:

- **Via Terminal**

  ```Cmd
  
  docker-compose up --build
  ```
Levantar


Vista del estado los servicios/contenedores:

- **Via Terminal**
    
    ```Cmd
  
    docker ps
    ```

Detener y eliminar los contenedores, redes y volúmenes creados :

- **Via Terminal**
    
    ```Cmd
    docker-compose down
    ```

Stopear los contenedores:

- **Via Terminal**

    ```Cmd
    docker-compose stop
    ```

Si los contenedores aún no existen, los crea; si ya existen, los actualiza y los levanta:

- **Via Terminal**

    ```Cmd
    docker-compose up
    ```

Reiniciar los contenedores:

- **Via Terminal**

    ```Cmd
    docker-compose restart

    ```


## Migraciones
Para Crear una migracion se utilizara el siguiente comando:

- **Via alembic**
    
    ```alembic
    alembic revision --autogenerate -m "init_db"
    ```
Para migrar a la base de datos:

- **Via alembic**

    ```alembic
    alembic upgrade head
    ```

Historial de migraciones:

- **Via alembic**

    ```alembic
    alembic current
    ```

## Uvicorn

Para levantar la aplicacion:

- **Via uvicorn**

    ```uvicorn
    uvicorn app.main:app --port 8000 --reload
    ```
