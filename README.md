# Laboratorio-1-Robótica
### Integrantes:
* Benjamín Velásquez
* Hector Fuentes
* Diego Escobar
* Fernanda Cádiz

# Descripción del Laboratorio
El laboratorio tiene como objetivo el comprender y simular el comportamiento cinemático de un robot móvil diferencial usando el simulador Webots. La meta es entender cómo las velocidades de las ruedas izquierda y derecha determinan la trayectoria y movimiento del robot.

Para este laboratorio se programó un controlador en el lenguaje Python, respetando el modelo cinemático dado por el laboratorio, donde:

* vr : velocidad de la rueda derecha
* vl: velocidad de la rueda izquierda
* L : distancia entre ruedas
* v : velocidad lineal
* w: velocidad angular

$$v = \frac{v_r + v_l}{2}$$

$$\omega = \frac{v_r - v_l}{L}$$

Para propósitos del laboratorio y llevar la teoría a la práctica, se modificó la fórmula con tal de que se pudiese colocar en el código quedando de la siguiente manera:

* $v_{r} = v + \frac{\omega \cdot L}{2}$
* $v_{l} = v - \frac{\omega \cdot L}{2}$

Así tomamos un modelo de ensayo y error basado en la velocidad lineal y angular.

## Roles
* Programador: Benjamín Velásquez
* Experimentador: Benjamín Velásquez
* Analista: Diego Escobar
* Documentador: Fernanda Cádiz
* Integrador: Hector Fuentes

# Cómo ejecutar la simulación en Webots

1. Abrir el software Webots.

2. Cargar el mundo del robot:
   - Ir a "File" → "Open World"
   - Seleccionar el archivo ubicado en la carpeta /worlds del repositorio.

3. Verificar que el robot e-puck esté presente en el entorno.

4. Seleccionar el controlador del robot:
   - Ir a las propiedades del robot
   - En la sección "Controller", seleccionar "ControladorRobotLab1"

5. Ejecutar la simulación:
   - Presionar el botón "Play"  en Webots.

6. Observar el comportamiento del robot:
   - El robot ejecutará distintos movimientos (recto, curva, rotación y círculo)
   - Dependiendo de las velocidades configuradas en el controlador

7. Para repetir la simulación:
   - Presionar "Reset" y luego "Play" nuevamente

# Resultados obtenidos
Luego de haber llevado a cabo los experimentos en el simulador Webots, se dieron a conocer los datos obtenidos con el modelo cinemático diferencial. Posteriormente se presentan, como resultado de la resolución de las preguntas de análisis presentadas en la guía del laboratorio:

1. ¿Qué ocurre cuando ambas ruedas tienen la misma velocidad?
	- Lo que ocurre cuando ambas ruedas tienen la misma velocidad es que el robot toma 	una trayectoria en línea recta. Eso se explica ya que, según el modelo cinemático, 	cuando las velocidades de la rueda izquierda y derecha son iguales, la velocidad 	angular valdría 0. Así el robot tomaría una trayectoria lineal.
			
    - Para obtener este resultado simplemente se modificaron las variables v, colocando 	el valor de 2, y el valor de w, colocando el valor 0.

2. ¿Cómo cambia la trayectoria cuando las velocidades son diferentes?
	- Al cambiar la velocidad de una rueda del e-puck, este toma una trayectoria curva.	Eso pasa debido a que una rueda va a tener más tracción o en este caso velocidad	que la otra, obligando al robot a desviarse. 
Si lo vemos del lado del modelo cinemático, con las fórmulas modificadas	para el		controlador, al cambiar el valor de w va a ocurrir que ambas velocidades			cambien. Además según la fórmula de la velocidad angular, las velocidades al no ser	iguales se define que tan cerrada va a ser la curva.

3. ¿Qué ocurre cuando una rueda gira en sentido opuesto a la otra?
	- Cuando una rueda gira en sentido opuesta a la otra simplemente el robot empieza a 	girar sobre su propio eje. Eso se explica ya que en el modelo adaptado si colocamos 	el valor de la velocidad lineal en 0, lo que hace que el producto entre w y L sea 		positivo para la rueda izquierda y negativo para la rueda derecha, ocasionando que 	el robot gire sobre su propio eje.

4. ¿Qué tipo de movimiento permite dibujar un círculo?
	- Para dibujar un círculo hay que tener en cuenta que el robot no necesita que las 		velocidades entre las ruedas sean iguales y que exista una velocidad angular 		constante. Entonces necesitamos una diferencia entre la velocidad de las ruedas 	que no varíe, así se podrá formar un movimiento circular constante.

## Info Encoder
Los encoders miden la posición angular acumulada en Radianes, es decir, cuanto ha girado la rueda desde que se encendió el robot. Si el número sube la rueda gira hacia adelante, si baja es porque la rueda gira hacia atrás

Como parte de los resultados obtenidos, para la realización de esta prueba el robot giro en una trayectoria circular, así que la rueda de la izquierda gira más rápido que la derecha, por eso los datos de la rueda izquierda son mayores que los de la derecha. Los valores que se ocuparon fueron v = 4 y w = 30.

Según el modelo, la distancia que recorre cada rueda en cada debe ser siempre la misma.

**Sin perturbaciones**
1. Encoder de la Izquierda: 9820.94 - Encoder de la Derecha: 7657.28
2. Encoder de la Izquierda: 9821.10 - Encoder de la Derecha: 7657.39
3. Encoder de la Izquierda: 9821.25 - Encoder de la Derecha: 7657.49
4. Encoder de la Izquierda: 9821.40 - Encoder de la Derecha: 7657.59
5. Encoder de la Izquierda: 9821.56 - Encoder de la Derecha: 7657.69
6. Encoder de la Izquierda: 9821.71 - Encoder de la Derecha: 7657.79
7. Encoder de la Izquierda: 9821.86 - Encoder de la Derecha: 7657.90
8. Encoder de la Izquierda: 9822.01 - Encoder de la Derecha: 7658.00
9. Encoder de la Izquierda: 9822.16 - Encoder de la Derecha: 7658.10
10. Encoder de la Izquierda: 9822.32 - Encoder de la Derecha: 7658.21

**Con perturbaciones (-5, 5 en ambas ruedas)**
1. Encoder de la Izquierda: 7173.25 - Encoder de la Derecha: 5872.67
2. Encoder de la Izquierda: 7173.34 - Encoder de la Derecha: 5872.87
3. Encoder de la Izquierda: 7173.44 - Encoder de la Derecha: 5872.96
4. Encoder de la Izquierda: 7173.50 - Encoder de la Derecha: 5872.91
5. Encoder de la Izquierda: 7173.63 - Encoder de la Derecha: 5872.96
6. Encoder de la Izquierda: 7173.83 - Encoder de la Derecha: 5872.93
7. Encoder de la Izquierda: 7174.03 - Encoder de la Derecha: 5872.88
8. Encoder de la Izquierda: 7174.23 - Encoder de la Derecha: 5872.89
9. Encoder de la Izquierda: 7174.35 - Encoder de la Derecha: 5872.92
10. Encoder de la Izquierda: 7174.55 - Encoder de la Derecha: 5873.12

### Resultados de perturbaciones

**Sin perturbaciones** 
- El movimiento es fluido, constante y predecible. La diferencia entre la izquierda y la derecha se mantiene estable debido a que no hay ruido ni agentes externos que perturben al robot. Viéndolo del lado del modelo cinemático y según los datos entregados, si restamos los datos dados, tipo el presente menos el dato anterior, daría un paso aproximado de 0.16 o 0.15 para la rueda derecha y de 0.10 aproximadamente para la rueda izquierda. Por lo que podríamos decir que respeta el modelo cinemático, fundamentando con esto y lo dicho el el tercer párrafo del apartado Info Encoder.

**Con perturbaciones**
- El movimiento es turbulento y los datos muestran inconsistencias en el avance. Se observan variaciones que no son lineales como en el otro caso,  donde los encoders incluso registran retrocesos o estancamientos momentáneos. Así podemos concluir que el movimiento con perturbaciones rompe la trayectoria con el robot desviándose un poco.


