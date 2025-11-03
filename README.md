## ¿Qué es el Modelo Serverless?

**Serverless** (o "sin servidor") es un modelo de computación en el que el **proveedor de servicios** (AWS, Google Cloud, Azure, etc.) gestiona completamente la infraestructura (servidores, hardware, sistema operativo).

Se sube el código y el prestador de servicios es quien corre este programa automáticamente cuando se solicite. Cuando no se está utilizando, el servidor se apaga.

## Funciones Lambda

Una **Función Lambda** es el código que se ejecuta en el entorno Serverless de AWS cuando se activa por un **evento** (una solicitud HTTP, un *streaming* de datos, procesamiento de archivos, etc.).

| ✅ Ventajas | ❌ Desventajas |
| :--- | :--- |
| **Escala Automática:** La asignación de recursos es dinámica según la demanda. | **Arranque en Frío:** Puede ser un poco lento si no se ha utilizado en un tiempo. |
| **Pago por Uso Real:** Solo se cobra por el uso real (tiempo de ejecución y memoria). | **Poco Control:** La administración del servidor la realiza completamente AWS. |
| **Sin Mantenimiento:** AWS se encarga de todo el mantenimiento de la infraestructura. | **Tiempo Máximo de Uso:** Generalmente limitado (ej. 15 minutos), no ideal para uso prolongado. |

##Lenguajes Soportados

Soporta una gran variedad de lenguajes de forma nativa:
* `java`
* `nodejs`
* `python`
* `c++`
* `go`
* `ruby`
* `bash`

También incluye una API para crear ambientes personalizados de ejecución.

## Modelo de Pago

Generalmente se incluye un plan en en el que se ofrece una **cantidad gratuita de ejecuciones**, por lo que el cobró se determina en base a la cantidad de memoria y tiempo necesario por cada ejecución. 


## 🔄 Ciclo de Vida de Ejecución

El proceso desde la activación hasta la finalización es el siguiente:

1.  **Evento:** Se realiza una solicitud (ej. solicitud HTTP).
2.  **Creación:** Se crea el contenedor (si no hay uno disponible).
3.  **Ejecución:** Se ejecuta el código.
4.  **Reciclaje:** Se desecha el contenedor o puede ser **reutilizado** si la siguiente ejecución ocurre pronto.

> **Nota de Diseño:** AWS asegura que la función se ejecutará correctamente al menos una vez. Si ocurre un error de confirmación, el código podría volver a ejecutarse (**reintentos**). Por ello, es crucial diseñar funciones que sean robustas ante ejecuciones duplicadas.
