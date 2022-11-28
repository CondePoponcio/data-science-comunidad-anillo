# data-science-comunidad-anillo
En este repositorio se guardan los avances correspondientes a la entrega, entre los cuales se destacan 3 en particular correspodientes a la arquitectura de solución, el código para procesar y modelar la solución, y la implementación del sistema de visualización. Adicionalmente en la raíz de esta carpeta se puede encontrar el informe correspondiente a la entrega oficial del avance del proyecto.

## Datos
Los datos de la base de datos citylog pueden encontrarse en formato CSV en la carpeta datos, los cuales corresponden a la tabla buses y paraderosrutas. También es posible encontrar el archivo paraderos2.csv para rellenar la tabla paraderos2 la cual es una creación nuestra a partir de ...

## Modelo Solución
En la carpeta model pueden encontrar un archivo python donde se está escribiendo el código con el cual se han realizado los cálculos de las métricas, cuyos datos de entrada (generados a partir de la creación de una vista en la base de datos) y datos de salida (usados posteriormente para en las pruebas del visualizador) se pueden encontrar en la misma carpeta model.

## Visualizador
En la carpeta DockerConQGisDesktop se pueden encontrar las configuraciones para desplegar las herramientas de QGis necesarias para este proyecto. Dentro de esta también se encuentra una carpeta llamada imagenes donde se muestra el avance o progreso con la herramienta. Al igual que algunas muestras de los resultados obtenidos.

## Arquitectura solución
En la raíz de la carpeta se encuentro un archivo yaml de docker compose, al igual que la carpeta build un archivo build.sh para construir toda la arquitectura e instalar las dependencias con la cual se montrá toda la solución. Una vez instaladas, es posible ejecutar el archivo yaml ubicado en la carpeta raíz de este proyecto, el cual montará un clúster de spark, una base de datos y un laboratorio web de jupyter donde poder realizar las pruebas de los modelos utilizados con python desde cualquier navegador en el puerto 8888. El objetivo de esta implementación es poder generar el flujo de procesamiento de datos de manera automática desde la base de datos, pasando a través del clúster de Spark para procesar los modelos solución y finalizar con la visualización de estos resultados en QGis.

## Autores ✒️

* **Felipe Condore** [CondePoponcio]()
* **Pamela Saldías** [pame17]()
* **Lucas Almonacid** [Natez]()
* **Benjamín Fernández** [Platypunk2]()