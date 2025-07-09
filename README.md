# ProyectoEstudiantes
1. Clonar el proyecto usando: git clone git@github.com:juan071201-dev/ProyectoEstudiantes.git
2. Activar virtualenv .venv
3. Abrir el editor con code.
3. Usar source .venv/Scripts/activate
4. Instalar los requerimientos usando: pip install -r requirements.txt
5. Ejecutar el app con: ptyhon main.py

PARTE TEÓRICA

1. ¿Para qué se puede usar Python en lo que respecta a datos? (5 casos)
    1.	Análisis de datos: usando pandas y numpy para limpiar y analizar grandes volúmenes de información.
    2.	Visualización: con matplotlib o seaborn para crear gráficos y entender tendencias.
    3.	Machine Learning: con scikit-learn o TensorFlow para entrenar modelos predictivos.
    4.	Web scraping: con BeautifulSoup o Scrapy para extraer datos de páginas web.
    5.	Bases de datos: conexión y consultas a bases de datos SQL o NoSQL con SQLite, MySQL o MongoDB.
--------------------------------------------------------------------------------------------------------------------
2. ¿Cómo se diferencian Flask de Django?
•	Flask es minimalista. Tú decides qué herramientas agregar. Ideal para proyectos pequeños.
•	Django viene con todo incluido: autenticación, ORM, panel de admin, etc. Mejor para proyectos grandes.

--------------------------------------------------------------------------------------------------------------------
3. ¿Qué es un API? (en palabras propias)
Es una forma de comunicación entre programas. Es como un menú de tú pides un dato y el servidor te responde con eso, sin saber como funciona internamente.

--------------------------------------------------------------------------------------------------------------------
4. ¿Principal diferencia entre REST y WebSockets?
•	REST es comunicación de una sola dirección por llamada (petición-respuesta).
•	WebSockets mantiene una conexión constante y bidireccional (cliente y servidor se comunican en tiempo real).

--------------------------------------------------------------------------------------------------------------------
5. Ejemplo de API comercial y cómo funciona (no visto en clase)
API de Spotify
Permite a los desarrolladores acceder a canciones, artistas, playlists, historial de escucha, etc.
•	Un frontend puede usarla para mostrar el reproductor y estadísticas del usuario.
•	Tú haces una petición con tu token de acceso (GET /v1/me/player), y te devuelve qué canción estás escuchando.
