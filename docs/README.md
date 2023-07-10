# Comparativas léxicas 23J 
Visualizaciones comparando la frecuencia de palabras entre los programas políticos de PSOE, PP, Sumar y Vox  las elecciones generales del 23J.

## Visualizaciones
- [PP vs PSOE](https://lirondos.github.io/23j/comparaciones/PPvsPSOE.html).
- [PP vs Sumar](https://lirondos.github.io/23j/comparaciones/PPvsSUMAR.html).
- [PP vs Vox](https://lirondos.github.io/23j/comparaciones/PPvsVOX.html).
- [PSOE vs Sumar](https://lirondos.github.io/23j/comparaciones/PSOEvsSUMAR.html).
- [PSOE vs Vox](https://lirondos.github.io/23j/comparaciones/PSOEvsVOX.html).
- [Sumar vs Vox](https://lirondos.github.io/23j/comparaciones/SUMARvsVOX.html).


## ¿Cómo se lee cada gráfica?
Cada una de las gráficas compara el léxico de dos programas electorales: PSOE vs PP, PSOE vs Vox, PSOE vs Sumar, PP vs Vox, PP vs Sumar, Sumar vs Vox. 

Los ejes x e y de la gráfica reprensentan cada uno de los dos grupos de la comparación. Por ejemplo, cojamos la gráfica que enfrenta [el programa de Sumar y el programa de VOX](https://lirondos.github.io/23j/comparaciones/SUMARvsVOX)). El eje vertical representa aquellas palabras y términos que son más o menos frecuentes en el programa de Sumar, mientras que el eje horizontal representa aquellas palabras y términos que son más o menos frecuentes en el programa de Vox. Las palabras aparecen por tanto ubicadas en el plano según lo frecuentes o infrecuentes que sean en ambos programas. Las palabras muy frecuentes en Sumar pero poco habituales en Vox estarán situadas hacia la esquina superior izquierda (valores altos para el eje y, valores bajos en el eje x: _personas trabajadoras_, _participación_, _sostenible_). Las palabras habituales en Vox pero poco frecuentes en Sumar estarán localizadas hacia la esquina inferior derecha (valores altos para el eje x, valores bajos para el eje y: _iberosfera_, _territorio nacional_, _sánchez_). Aquellas palabras que tengan frecuencias parecidas tanto en la dictadura como en la democracia estarán colocadas hacia la diagonal de la gráfica. 

Si pinchamos en las palabras de la gráfica nos aparecerán más abajo los contextos en los que ha aparecido la palabra en cuestión y las diferencias de frecuencia entre un programa y otro. 

El resto de gráficas comparativas funcionan de la misma manera. A la hora de mirar el gráfico, merece la pena fijarse tanto en las palabras anormalmente frecuentes (esquinas superior izquierda e inferior derecha), pero también aquellas que se mantienen siempre habituales (esquina superior derecha) o las que tienen frecuencias parecidas (eje diagonal).

## ¿Qué información es la que está representada?
Estas gráficas representan la frecuencia de las palabras en los programas de cuatro partidos políticos: PSOE, PP, Sumar, Vox. Sin embargo, ha habido un cierto preprocesamiento y una poderación en la obtención de los valores. En primer lugar, la representación ignora las palabras huecas como preposiciones, artículos, conjunciones, etc. Buena parte de los numerales también han sido eliminados para reducir el ruido.

Además, la frecuencia que se mide no es simplemente un recuento de palabras sin más, sino que el valor representa cuánto de frecuente es una palabra en un programa en relación a lo frecuente que es respecto a los demás programas. Esta medida de la frecuencia se conoce con las siglas [TF-IDF](https://es.wikipedia.org/wiki/Tf-idf).


## ¿Cómo está hecha la visualización?
La visualización está hecha con las librerías de Python [scattertext](https://github.com/JasonKessler/scattertext), y [spaCy](https://spacy.io/). La idea de la visualización así como los textos de los programas parten del [repositorio ProgramasElectorales](https://github.com/fsanchez83/ProgramasElectorales) de [Faustino Sánchez](https://twitter.com/Danielquinn_).
