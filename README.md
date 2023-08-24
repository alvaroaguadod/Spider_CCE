# Concanaco scraper project

Scrapy project for data extraction in https://cce.org.mx/


## Spider Parameters

|   Params   |        Type        | Description                                                                                                                                  | Mandatory |
| :--------: | :-----------------: | :------------------------------------------------------------------------------------------------------------------------------------------- | :-------- |
| search |        string        | Accepts any search keyword                                                                                 | YES       |   

The parameter field search only accepts a string, more than one spider is not supported
## Local development

### Setting Up the environment

Install dependencies.

```bash
pip install -r requirements
```

### How run the spider

- By scrapy command

```bash
scrapy crawl CCESpider -a search= gobierno

```

- By python command

````bash
python main.py
````
##  Manual Deployment

Login zyte cloud

```bash
shub login #Then add zyte cloud credencial
```

Upload the project to zyte cloud:

- Deploy in dev

```bash
shub deploy 
```

- Deploy in pro

```bash
shub deploy pro
```

Set ZYTE_SMARTPROXY_APIKEY variable in zyte cloud project in settings section.

Set SMTP_SERVER, USER_EMAIL, USER_EMAIL_PASSWORD, RECIPIENT_LIST, EMAIL_SUBJECT and ENABLE_ERROR_EMAIL variables to enable the email error notification.



## Run spider in zyte cloud by postman
### Url

> https://app.scrapinghub.com/api/run.json

### Body parameters

|               Params               |  Type  | Description                                                        | Mandatory |
| :--------------------------------: | :----: | :----------------------------------------------------------------: | :-------: |
|              project               |  int   | Id project (default: 648571 / pro: 648574).                        | YES       |
|              spider                | string | CCESpider                                                          | YES       |
| [More parameters](#spider-parameters) |        |                                                                 |           |


## Example of returned item

## Example of returned item

```
[
{"title": "El sector privado participó en reunión con el Gobierno Federal y el sector laboral para un acuerdo sobre subcontratación y reparto de utilidades", "author": "LUIS MEDEL", "date": "abril 5, 2021", "text": "Download File"},
{"title": "EL CCE ENCABEZA MISIÓN EMPRESARIAL DE ALTO NIVEL EN ESPAÑA", "author": "CCE", "date": "enero 16, 2023", "text": "Ciudad de México, 16 de enero de 2023. El día de hoy, el Presidente del Consejo Coordinador Empresarial (CCE), Francisco Cervantes Díaz encabezó el primero de tres días de la misión empresarial de alto nivel en Madrid, España, acompañado por el Presidente de la Confederación de Cámaras Industriales (CONCAMIN), José Abugaber Andonie; el Presidente de la Cámara de Comercio de la Ciudad de México (CANACO CDMX), José Rodríguez Cárdenas; el Presidente de la Industria Nacional de Autopartes (INA), Francisco González Díaz; el Subsecretario de la Confederación Patronal de la República Mexicana (COPARMEX), José Loret de Mola Gomory; el Secretario General de la Confederación de Cámaras Nacionales de Comercio, Servicios y Turismo (CONCANACO SERVYTUR), Guillermo Romero Rodríguez; y el Vicepresidente Ejecutivo del Consejo Empresarial Mexicano de Comercio Exterior, Inversión y Tecnología (COMCE), Sergio Contreras Pérez. Como parte de las actividades de su gira de trabajo por el país europeo, el Presidente Cervantes se reunió con el Ministro de Asuntos Exteriores, Unión Europea y Cooperación de España y Secretario de Estado para Iberoamérica y el Caribe y el Español en el Mundo, Juan Fernández Trigo, con quien conversó sobre los retos y oportunidades que enfrentan ambos países, en un contexto de reactivación económica post pandemia. Posteriormente, en el marco del foro “México y España, una apuesta empresarial de futuro” organizado por la Confederación Española de Organizaciones Empresariales -y que contó con la participación de la Secretaria de Estado de Comercio de España, Xiana Méndez; el presidente de la Confederación Española de Organizaciones Empresariales (CEOE), Antonio Garamendi; y el presidente de la Cámara de Comercio de España, José Luis Bonet-, el Presidente del CCE agradeció la asistencia de los líderes del sector privado de ambos países y de los funcionarios públicos, destacó las similitudes en los sectores manufacturero, comercio, turismo, agrícola, así como en el desarrollo permanente de infraestructuras, y resaltó que España es el segundo inversionista más importante de México con 80 mil millones de dólares invertidos en los últimos 24 años. En el acto, Xiana Méndez resaltó la importancia que el Acuerdo Global entre México y la Unión Europea ha tenido como “vía para mantener unas relaciones comerciales abiertas y estables y expresamos la confianza en que las autoridades mexicanas y la Comisión Europea puedan encontrar una solución pronta y adecuada para su modernización”. Asimismo, Méndez abordó también el compromiso y la colaboración para favorecer la inversión española en México y viceversa, la inversión mexicana en nuestro país. A su vez, el presidente de CEOE, Antonio Garamendi, abogó por seguir fortaleciendo la relación con México durante estos días, para alcanzar sociedades más unidas y prósperas, siempre mediante el diálogo y el bienestar de los países y de sus ciudadanos, haciendo uso del mejor instrumento de inclusión social que existe: la creación de empleo. Garamendi informó de que México es el sexto país inversor en España con 7,000 empresas instaladas, y el tercero en la Unión Europea. Apostó además por realizar un trabajo conjunto para que logremos entre todos un futuro de economía circular y digital, de cambio y, sobre todo, de renovación. Posteriormente, durante su reunión con el Gobernador del Banco de España, Pablo Hernández de Cos, Francisco Cervantes y la delegación empresarial mexicana intercambiaron sus puntos de vista sobre el ámbito monetario y financiero de ambas naciones, en el ánimo de continuar abonando a una relación cada vez más estrecha y con mayores oportunidades para la inversión. Finalmente, el líder empresarial mexicano y las respectivas delegaciones se dieron cita en La Casa de México en España, un esfuerzo conjunto de la sociedad civil y del gobierno para promover a nuestro país. En este acto se destacó una vez más la prioridad de explorar oportunidades para desarrollar conjuntamente la agenda en temas culturales, de negocios, de emprendimiento, turísticos, gastronómicos y de desarrollo comunitario, entre otros. Así finalizó el primero de tres días de la gira que encabeza el Presidente del Consejo Coordinador Empresarial, durante los cuales se reunirá con representantes de la Secretaría de Estado de Iberoamérica; con la Secretaría de Estado de Comercio; con el Club Español de Energía; con la Comisión de Asuntos Exteriores del Congreso de los Diputados; con la Alcaldía del Ayuntamiento de Madrid; entre otras instituciones y empresas, con el firme objetivo de hermanar a la iniciativa privada de ambas naciones. VF-Comunicado-No.-01-Mision-Empresarial-Espana"},
{"title": "El CCE exhorta al Senado a que la iniciativa de reforma electoral sea analizada privilegiando el diálogo y el acuerdo entre las fuerzas políticas. ", "author": "CCE", "date": "febrero 7, 2023", "text": "Ciudad de México, 7 de febrero de 2023.  El Consejo Coordinador Empresarial (CCE) y los 14 organismos que lo integran hacen un respetuoso exhorto al Senado de la República para que el proceso legislativo de la iniciativa de reforma en materia electoral, que se analiza y discute actualmente, se lleve a cabo a partir del consenso de los grupos parlamentarios ahí representados.  La relevancia de la elección federal en el año 2024 en la que se elegirá presidente de la República, y de los procesos locales que se llevarán a cabo este año, precisa de un marco electoral que otorgue certidumbre y, sobre todo, que sea producto del diálogo y el acuerdo entre las fuerzas políticas.  Durante el 2024 también se efectuarán comicios de suma importancia, como la renovación de la totalidad de los integrantes del Congreso Federal, ocho gubernaturas y el Gobierno de la Ciudad de México, así como 1,580 ayuntamientos y 30 congresos locales.  Los tiempos que vivimos requieren de instituciones fuertes y de un marco de convivencia política que privilegie los acuerdos y la construcción de consensos, a fin de consolidar los avances democráticos logrados en las últimas décadas, que han permitido la organización de elecciones libres y transparentes en México.  El sector empresarial reitera su compromiso con la democracia y con un diálogo permanente y respetuoso con los distintos órganos de representación política en nuestro país. "},
{"title": "Firma de convenio de colaboración entre el CCE y la Asociación Internacional para la Economía Sostenible (IASE®) ", "author": "CCE", "date": "febrero 17, 2023", "text": "-Esta alianza es parte de una estrategia de fortalecimiento de los lazos entre la comunidad empresarial de México con el desarrollo sostenible de las organizaciones a través de la implementación y la integración de los criterios ESG en el día a día de las empresas, no sólo en la alta dirección sino en todos los integrantes de los corporativos.  Ciudad de México, 16 de febrero de 2023.  El día de hoy se llevó a cabo la firma del convenio de colaboración entre el Consejo Coordinador Empresarial (CCE), así como de la Asociación Internacional para la Economía Sostenible (IASE®) en México, el cual busca el fortalecimiento de la estrategia de promoción, educación, divulgación y desarrollo de la implementación de los criterios medioambientales, sociales y corporativos (ESG, por sus siglas en inglés) en el ámbito empresarial de México.  Entre las múltiples finalidades de esta alianza, el acuerdo hace hincapié en el trabajo conjunto en actividades para incluir los factores ESG en el modelo de negocio de empresas, tanto grandes como pequeñas y medianas (PyMEs), a través de la creación y ejecución de programas que eleven la conciencia en el desarrollo sostenible y sus beneficios para la economía local y global, así como alentar al espectro empresarial hacia la transformación financiera, la innovación y el desarrollo tecnológico enfocados en sostenibilidad.  La IASE® busca cerrar la brecha que existe entre los organismos especializados en sostenibilidad basada en los criterios ESG y los profesionales de todos los sectores financieros y empresariales, reguladores, gobierno e iniciativa privada, teniendo un lenguaje común de competencias y conocimientos que fortalezcan los modelos de desarrollo sostenible. Los criterios ESG los tenemos que promover e implementar todos los integrantes del sector empresarial, sin importar el tamaño de la empresa o el puesto en la organización.  Como parte de la estrategia derivada de la colaboración entre ambos organismos, también se dieron a conocer los medios para lograr sus objetivos, como el posicionamiento de los criterios ESG en la agenda del sector empresarial, programas de difusión, desarrollo y publicación de contenido educativo, artículos periodísticos y/o académicos, así como la participación activa de IASE® México en la redacción de Anexos y Contenido sobre Desarrollo Sostenible del Código de Principios y Mejores Prácticas de Gobierno Corporativo del CCE. Todo ello, con la finalidad de participar y enriquecer el entorno de la opinión pública en la pertinencia y urgencia de estos temas. Durante su participación, el presidente de la Comisión de Gobierno Corporativo del CCE, Bernardo Rivadeneyra, destacó que “es de vital importancia posicionar los criterios ASG en la agenda del sector empresarial y en toda clase de empresas, giros y tamaños. Su inclusión en el Código de Gobierno Corporativo mexicano materializará dicha prioridad. El reto subsiguiente será su promoción, implementación y medición de resultados. Sin duda será también de mucha utilidad la colaboración del IASE, pues urge que las empresas en México conozcan y apliquen en sus modelos de negocio estos nuevos conceptos de gestión y sostenibilidad empresarial”.  En tanto, Rodrigo Manrique Gómez Pimienta, Director Ejecutivo de IASE® México, aseguró que “el desarrollo económico de México está comprometido con que cuidemos el medio ambiente, tengamos mejores relaciones labores (por ejemplo, con principios de seguridad, salud y equidad de género) y que las empresas impacten positivamente en el entorno donde operan. Sin duda, la alianza que hoy estamos oficializando nos ayudará a lograrlo”.  En la firma estuvieron presentes Bernardo Rivadeneyra, Presidente de la Comisión de Gobierno Corporativo del CCE; Rodrigo Manrique Gómez Pimienta, Director Ejecutivo de IASE® México; Carmen Micu, Presidenta de IASE® Internacional; y Silvia Dávalos de la Rosa, Directora General de Políticas Públicas y Comisiones del CCE.   "},
(...)
]
```

