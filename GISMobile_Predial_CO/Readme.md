## GIS Mobile Predial - CO

<div align="center">
  <img alt="GISMobile" src="graph/QField_MapView.png" width="300px">
  <img alt="GISMobile" src="graph/QField_Layers.png" width="300px">
  <img alt="GISMobile" src="graph/QField_Atributes.png" width="300px">
</div>

Sistema de información geográfico móvil a partir de datos públicos https://www.colombiaenmapas.gov.co/ - Colombia y otras fuentes.

En Colombia la Ley de Transparencia y Acceso a la Información, define los datos abiertos como “todos aquellos datos primarios o sin procesar, que se encuentran en formatos estándar e interoperables que facilitan su acceso y reutilización, los cuales están bajo la custodia de las entidades públicas o privadas que cumplen con funciones públicas y que son puestos a disposición de cualquier ciudadano, de forma libre y sin restricciones, con el fin de que terceros puedan reutilizarlos y crear servicios derivados de los mismos” (Ley 1712 de 2014. Literal J, artículo 6. Definiciones.)

> Mapa publicado en release como: [GISMobile_Predial_CO_v2020](https://github.com/rcfdtools/R.GISMobile/releases/tag/GISMobile)


### Sistema de proyección de coordenadas - CRS

Origen nacional único Colombia EPSG: 9377 o ESRI: 103599 [^1]

El establecimiento de las condiciones técnicas mínimas que deben tener los productos básicos de cartografía oficial, serán los definidos de conformidad con lo dispuesto por la Resolución 471 del 14 de mayo de 2020 y la posterior Resolución 529 del 05 de junio de 2020, emitidas por el Instituto Geográfico Agustín Codazzi - IGAC, o la norma que la modifique y sustituya, para ello y para garantizar la homogeneidad y continuidad en la representación de los elementos del territorio, así como facilitar los trabajos relacionados con la gestión de coordenadas en el país. En tal sentido, los proyectos, obras o actividades, sujetos al licenciamiento ambiental, deben ajustar su información geográfica a los lineamientos establecidos en la referida normatividad, para la evaluación y seguimiento de los estudios ambientales y/o presentación de los Informes de Cumplimiento Ambiental.

El sistema de proyección cartográfico para Colombia, con un único origen, consiste en una proyección cartográfica Transversa de Mercator Secante, cuyos parámetros están establecidos en el literal i Sistema de Referencia del artículo 4 de la resolución 471 de 2020, los cuales pueden configurarse en software especializado para procesamiento de información geográfica.

```
MAGNA_Colombia_Origen_Unico
Authority: Custom

Projection: Transverse_Mercator
False_Easting: 5000000.0
False_Northing: 2000000.0
Central_Meridian: -73.0
Scale_Factor: 0.9992
Latitude_Of_Origin: 4.0
Linear Unit: Meter (1.0)

Geographic Coordinate System: GCS_MAGNA
Angular Unit: Degree (0.0174532925199433)
Prime Meridian: Greenwich (0.0)
Datum: D_MAGNA
  Spheroid: GRS_1980
    Semimajor Axis: 6378137.0
    Semiminor Axis: 6356752.314140356
    Inverse Flattening: 298.257222101
```

### Datasets & Feature Class

| Feature class  | Descripción            | Fuente                                                                                                           | Licencia                                                         |
|:---------------|:-----------------------|:-----------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------|
| Municipios2022 | Municipios de Colombia | www.colombiaenmapas.gov.co <br>Base de datos vectorial básica de Colombia. Escala 1:100.000<br>Fecha: 01-04-2022 | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.es) |

[^1]: Tomado o adaptado de: https://www.anla.gov.co/01_anla/entidad/subdirecciones-y-oficinas/instrumentos-permisos-y-tramites-ambientales/sistema-de-informacion-geografica