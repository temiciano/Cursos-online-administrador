EL planteamineto inicial para este pryecto sera depender de 3 tablas, una correspondiente a los cursos, otra tabla para los estudiantes, y una correspondiente a "inscripciones", donde se asociaran las ID de los estudiantes a sus ID de cursos respectivos. 

La base de datos se creara en sqlite mediante sql Browser

Mediante codigo vamos a querer, leer y modificar nuestras tablas


## Funcionalidades conseguidas:

- Creacion de nuevos cursos
- Inscripcion de estudiantes a estos cursos
- Candidato no se puede inscribir al mismo curso mas de una vez
- Correo electronico debe tener formato valido
- Asignacion de codigo unico a cada inscripcion


## No incluye:
- Búsqueda de participantes. 
- Filtros por curso. 
- Filtros por estado. 
- Ordenamiento de la información. 

- Total de cursos registrados. 
- Total de participantes inscritos. 
- Total de cupos disponibles. 
- Cantidad de cursos completos. 
- Porcentaje de ocupación de los cursos.
- exportar listado en formato CSV


#Ejecutar comando "python ./app.py"

Pagina Principal
<p align="center">
  <img src="/Screenshots/cap_1.png" width="500" alt="Pagina principal"/>
</p>

Pagina de creacion de cursos
<p align="center">
  <img src="/Screenshots/cap_2.png" width="500" alt="Creacion cursos"/>
</p>

Pagina de inscripcion de participantes
<p align="center">
  <img src="/Screenshots/cap_3.png" width="500" alt="Inscripcion particitapntes"/>
</p>