<!-- #region -->
# Método computacional basado en el análisis de noticias para caracterizar problemáticas territoriales

## Tabla de contenidos


## Resumen

El presente proyecto se enmarca en conjunto al proyecto Fondecyt “Sophia2: métodos basados en lingüística computacional y machine learning para analizar el pluralismo en los medios de prensa” desarrollado en la Facultad de Ciencias de la Ingeniería (FCI) de la UACh entre diciembre 2019 y marzo 2023. Proyecto en el cual colaboran un grupo de investigadores y estudiantes de la FCI y de la Facultad de Filosofía y Humanidades de la UACh. El trabajo realizado en este proyecto Fondecyt ha permitido, entre otras cosas, desarrollar primeras
colaboraciones con instituciones públicas y privadas (por ejemplo el GORE Los Lagos). La tecnología desarrollada por Sophia2 permite a las instituciones públicas y privadas monitorear problemáticas territoriales a través de informes PDF.


El proyecto “Método computacional basado en el análisis de noticias para caracterizar problemáticas territoriales” consiste en generar un método computacional que permita caracterizar las problemáticas presentes en las noticias de Chile, y para ello utilizará distintos modelos y técnicas del procesamiento del lenguaje natural. En concreto, utilizará el modelo Latent dirichlet allocation para descubrir los tópicos abstractos que están presentes en la colección de documentos. También, utilizará transformers, una técnica basada en redes neuronales profundas para la realización de un análisis de sentimientos que permita identificar el grado de polaridad (positiva o negativa) de cada una de las noticias. Asimismo, mediante un análisis de grafos, se geolocalizarán y contextualizarán en el tiempo las problemáticas identificadas. En último lugar, se realizará un caso de estudio que comprenda el análisis de al menos dos regiones del país.


El desarrollo del proyecto contempla periodos de investigación y una metodología secuencial de etapas que comprende desde la adquisición de noticias, filtrado y limpieza de datos, diseño e implementación de modelos
de procesamiento y evaluación de resultados mediante un caso de estudio.


El objetivo principal del proyecto es ser de ayuda tanto a la clase política como a los distintos entes gubernamentales y municipios, que mediante su uso podrán identificar de primera fuente las problemáticas que perturban a la población y así, facilitarles el camino para diseñar soluciones precisas. En este sentido, el método computacional servirá de apoyo a Sophia2 en la generación de informes PDF, entregando información útil en la
caracterización de problemáticas territoriales.   

## Descripción de la innovador (mérito innovador)

#### **¿Qué desarrollaremos? ¿Cómo lo desarrollaremos?**

Desarrollaremos un método computacional que nos permita caracterizar las problemáticas y oportunidades presentes en las noticias de los distintos medios de información de Chile. Para esto, hemos pensado en el diseño de una arquitectura que comprende los siguientes modelos del procesamiento del lenguaje natural: **Latent dirichlet allocation** para el modelado de tópicos y **transformers** para el análisis de sentimiento. Además, representaremos la información extraída de la implementación de los dos métodos anteriormente mencionados y los datos crudos (date, region, media_outlet, content, etc.) en **grafos**, puesto que consideramos que entregan una ventaja cuando se busca implementar heurísticas que comprendan la caracterización geoespacial y en el tiempo de las noticias.

Estrictamente, el mérito innovador de este proyecto se focaliza en la integración de distintas tecnologías: LDA y transformers, pero también, en el diseño e implementación de grafos para la caracterización de territorial de noticias.
Además, este proyecto, bajo el contexto de la lingüística computacional, busca ser un aporte en la gestación de soluciones por parte de Sophia2, las que permitirán a distintas organizaciones públicas y privadas tomar
decisiones estratégicas.

El proyecto utilizará un pipeline de procesamiento compuesto por las siguientes fases: _adquisición de datos, extracción y limpieza de textos, preprocesamiento, implementación de diferentes modelos para el modelado de tópicos, análisis de sentimiento y análisis de grafos._

En primer lugar, se va a recopilar las noticias de los sitios web de los medios información de interés utilizando técnicas de web scraping. Las noticias se almacenarán en una base de datos. Luego, se realizarán distintos procedimientos para limpiar y filtrar las noticias de posibles perturbaciones (caracteres especiales o símbolos). También se busca convertir las noticias en una forma canónica que permitirá trabajar con las noticias en un único formato.

Terminado el preprocesamiento de los datos, se implementará el modelo Latent Dirichlet Allocation (LDA), puesto que permite identificar las relaciones (tópicos) presentes entre noticias. Este procedimiento se piensa implementar en dos ocasiones, con tal de extraer los subtópicos de los tópicos encontrados.

Finalmente, a cada noticia se le realizará un análisis de sentimiento que permita clasificarla como positiva o negativa. Para esto implementaremos algún modelo de transformers que responda bien al problema puntual.

Finalizada la clasificación de la noticia puntual, implementaremos distintos algoritmos para analizar los datos representados en grafos, puesto que buscamos encontrar una conexión entre la noticia, una problemática y su entorno (comunas y regiones aledañas), también buscamos caracterizar la noticia en el tiempo, con tal de identificar si es una problemática local, está esparcida o se está esparciendo. 

#### **¿Cuál es el problema o necesidad del cliente que no está siendo cubierta satisfactoriamente por el mercado y que buscamos resolver?**

La falta de información confiable y oportuna sobre las problemáticas de un territorio es un problema clave para instituciones públicas y privadas. Por ejemplo, los Gobiernos Regionales (GORE) deben analizar cuáles son las problemáticas territoriales emergentes, elaborar una estrategia con distintos actores y distribuir recursos públicos para apoyar iniciativas. Este trabajo se acompaña por una exigencia de transparencia y de rendición de cuenta al Ministerio del Interior quien establece los presupuestos anuales de los GORE. Escuchar lo que está pasando en un territorio requiere datos y herramientas de análisis. Nuestro proyecto participa en el desarrollo de una solución tecnológica innovadora que ayuda a la decisión monitoreando problemáticas territoriales para instituciones públicas y privadas.

#### **Nivel de relevancia que tiene el problema o necesidad que buscamos resolver:**

El problema de no contar con información confiable y oportuna para caracterizar las problemáticas de un territorio afecta a una gran cantidad de instituciones públicas y privadas, tanto en Chile como en el extranjero.
Sin una adecuada solución, los actores territoriales podrían fallar o atrasarse en resolver correctamente problemáticas territoriales (brechas socioeconómicas, cambio climático, etc.). Este es un problema crítico a
resolver por la cantidad de información que procesar, por los indicadores que diseñar y las exigencias de transparencia. Sin el apoyo de herramientas informáticas para automatizar ciertos procesos de recopilación de
datos y análisis, se generan sobre-gastos innecesarios para las instituciones y un mal uso de recursos.

#### **Principales competidores o soluciones existentes en el mercado indicando sus atributos y debilidades en relación al problema detectado**

Los competidores se dividen en actores tradicionales y nuevos actores tecnológicos. En la primera categoría, los servicios nacionales de información (ine.cl, sni.gob.cl/estudios), las consultoras y las empresas de
investigación de mercado (por ejemplo, Cadem) publican estudios anuales y entregan servicios generales de consejos y encuestas. Sin embargo, nuevos actores tecnológicos se posicionan, más ágiles para integrar nuevos
tipos de datos y responder a necesidades específicas. En Chile y en la región de Los Ríos, podemos citar la empresa Spike que se especializa en Inteligencia Artificial y analítica avanzada para empresas de retail y que fue recién adquirida por la empresa consultora [Bain & Company](https://tinyurl.com/3cb3wmru), pero no abarca problemáticas territoriales.

                                                                                
## Objetivos específicos
 
1. Diseñar un método capaz de identificar, geolocalizar y contextualizar en el tiempo problemáticas territoriales.
2. Diseñar un método capaz de evaluar la problemática territorial según una polaridad positiva o negativa.
3. Implementar y validar el método a partir de un caso de estudio en Chile.


## Referencias

- Ruiz, Fabian (2020). Evolution of the gender biases in the news media: a computational method using dynamic topic model. Tesis de magíster en Informática, Universidad Austral de Chile.

- Ghahramani, M., Galle, N, Ratti, C. (2021). Tales of a city: Sentiment analysis of urban green space in Dublin. Cities, Vol. 119 (2021).

- Chen Lin-Chih (2017). An effective LDA-based time topic model to improve blog search
performance. Department of Information Management, National Dong Hwa University, Taiwan.

- Dias, F., Baptista de Oliveira, J., (2022) BERT for Sentiment Analysis: Pre-trained and Fine-Tuned
Alternatives. Electrical Engineering Department, Federal University of Rio de Janeiro, Brazil.
https://arxiv.org/pdf/2201.03382.pdf

- Grenager, T., Finkel, R., Manning C. (2005) Incorporating non-local information into information extraction systems. Proceedings of the 43nd Annual Meeting of the Association for Computational Linguistics (ACL 2005), pp. 363-370.

- S. N. Lehman-Wilzig, M. Seletzky, Hard news, soft news, ‘general’ news: The necessity and utility of an intermediate classification, Journalism 11 (2010) 37–56. doi:10.1177/1464884909350642.

- Devlin, J., Chang, M., Lee, K., Toutanova, K.: BERT: Pre-training of deep bidirectional transformers for language understanding. Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers). pp. 4171–4186. Association for Computational Linguistics, Minneapolis, Minnesota (Jun 2019). https://doi.org/10.18653/v1/N19-1423, https://aclanthology.org/N19-1423
<!-- #endregion -->
