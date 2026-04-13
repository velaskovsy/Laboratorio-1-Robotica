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
   - Presionar "Reset" y luego "Play"

# Resultados obtenidos
Luego de haber llevado a cabo los experimentos en el simulador Webots, se dieron a conocer los resultados obtenidos con el modelo cinemático diferencial. A continuación, la resolución de las preguntas de análisis planteadas en la guía del laboratorio:

## 1. ¿Qué ocurre cuando ambas ruedas tienen la misma velocidad?
Lo que ocurre es que el robot toma una trayectoria en línea recta. Eso se debe a que, según el modelo cinemático, la velocidad angular es igual a cero, por lo que no existe rotación.
				
Para obtener este resultado, se modificaron las variables v, colocando el valor de v = 2, y el valor de ω, a ω = 0.

## 2. ¿Cómo cambia la trayectoria cuando las velocidades son diferentes?
Cuando las velocidades de las ruedas son distintas, el robot describe una trayectoria curva. Esto ocurre porque una rueda avanza más rápido que la otra, generando un cambio continuo en la dirección del movimiento.
	
Desde el modelo cinemático, esta diferencia se produce al modificar el valor de la velocidad angular (ω), lo que provoca que las velocidades de ambas ruedas cambien. Además, la magnitud de esta diferencia determina qué tan cerrada o abierta será la curva.

## 3. ¿Qué ocurre cuando una rueda gira en sentido opuesto a la otra?
Cuando una rueda gira en sentido opuesta a la otra, el robot empieza rota sobre su propio eje. En este caso, la velocidad lineal es cero y solo existe movimiento angular.
	
Esto se logra configurando (v = 0), lo que genera velocidades opuestas en cada rueda según el modelo, provocando la rotación en el lugar.

## 4. ¿Qué tipo de movimiento permite dibujar un círculo?
Para que el robot describa un movimiento circular, es necesario que exista una diferencia constante entre las velocidades de ambas ruedas, junto con una velocidad angular constante.
Esto permite que el robot mantenga una trayectoria curva uniforme, formando un círculo.

## Análisis de Encoder
Los encoders miden la posición angular acumulada de cada rueda en radianes, es decir, cuanto ha girado la rueda desde que se encendió el robot. 

* Si el valor aumenta → la rueda gira hacia adelante, 
* Si el valor disminuye → es porque la rueda gira hacia atrás

 Para este análisis, se evaluó el comportamiento del robot en una trayectoria circular, lo que permitió observar diferencias entre ambas ruedas. En este caso, la rueda izquierda presenta valores mayores que la derecha, debido a que gira a mayor velocidad. Los valores que se ocuparon fueron v = 4 y w = 30.

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

En condiciones ideales, el movimiento del robot es fluido, constante y predecible.

A partir de los datos obtenidos, se observa que los valores de los encoders aumentan de forma progresiva. Si se analiza la diferencia entre mediciones consecutivas (valor actual menos el anterior), se obtiene un incremento aproximadamente constante:

* La rueda derecha presenta incrementos cercanos a 0.15 – 0.16
* La rueda izquierda presenta incrementos cercanos a 0.10

Esto indica que ambas ruedas mantienen una velocidad estable en el tiempo. Además, la diferencia constante entre las velocidades de las ruedas explica la trayectoria circular observada.

Este comportamiento es consistente con el modelo cinemático diferencial, ya que velocidades constantes generan un movimiento predecible.

**Con perturbaciones**

Al introducir perturbaciones aleatorias en las velocidades de las ruedas, el comportamiento del robot cambia significativamente.

A diferencia del caso anterior, los valores de los encoders no presentan incrementos constantes. Al analizar las diferencias entre mediciones consecutivas, se observan variaciones irregulares:

* Los incrementos dejan de ser uniformes
* Existen pequeñas fluctuaciones en el avance
* En algunos casos se presentan desaceleraciones momentáneas

Esto provoca que el movimiento del robot sea menos estable, generando desviaciones respecto a la trayectoria esperada.

En este caso, el sistema deja de seguir el modelo cinemático ideal, evidenciando la influencia de perturbaciones en los actuadores.


