# data-science-comunidad-anillo

## Datos
Primero antes de ejecutar cualquier script deben descomprimir los zip que hemos descargado del servidor de GEO. Cada zip va a generar una carpeta con los datos necesarios de la base de datos. Ojo que los zip no se encuentran adjuntados en el repo.

En la carpeta stream se encuentra en script de python para procesar los datos. Antes de ejecutar dicho script, es necesario preprocesar los datos de las carpetas usando el siguiente bashscript (a su vez al termina de procesar los datos ejecutará el código de python). Solo usar este script de bash la primera vez (a menos que agreguen mas archivos a procesar).
```bash
./start.sh
```

## Observacion
- Cuando vayan a ejecutar un script haganlo desde la misma carpeta del código.
- Los archivos de la carpeta GEO son los códigos que se ejecutan para realizar los trabajos de extracción en el servidor GEO.

## Despliegue
Si poseen el plugin de VSCode de DevContainer, entonces pueden ejecutar automáticamente todo el ambiente de python ya dockerizado con la opción F1 -> Reopen in container.