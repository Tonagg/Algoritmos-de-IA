# 📝 Respuestas — 40 Preguntas Opción Múltiple

> **Tema 4: Algoritmos de Aprendizaje — UNAM Facultad de Ciencias**  
> Las respuestas correctas están **subrayadas en el PDF original**. Aquí las repito con justificación breve para que las recuerdes.

---

## Bloque 1: Conceptos generales de Machine Learning (1–10)

| # | Pregunta resumida | ✅ Respuesta | Justificación |
|---|-------------------|-------------|---------------|
| 1 | Cambio de paradigma del ML | **b)** Programar un algoritmo para que aprenda reglas a partir de los datos | El programador no escribe reglas, las aprende el algoritmo |
| 2 | Otro nombre del enfoque ML | **c)** Conexionista | Inspirado en redes neuronales / conexiones |
| 3 | "Combustible" del ML según Taulli (2019) | **b)** Gran cantidad de datos de fácil acceso | Sin datos no hay aprendizaje |
| 4 | Razonamiento del paradigma conexionista | **d)** Inductivo y probabilístico | De ejemplos a reglas, con incertidumbre |
| 5 | Problema de representación según Castelvecchi | **b)** Caja negra (opacidad) | Difícil interpretar lo aprendido |
| 6 | Por qué se llama "autoprogramación" | **c)** Los datos determinan la estructura detallada del modelo | El modelo se construye desde los datos |
| 7 | Objetivo principal de un algoritmo de aprendizaje | **b)** Identificar características en los datos para mejorar la ejecución automáticamente | No es memorizar |
| 8 | Qué es un "Modelo" en ML | **b)** Programa aprendido que mapea entradas a predicciones | Es la salida del entrenamiento |
| 9 | Verdadera medida del éxito | **b)** Capacidad de generalización ante datos nunca vistos | Memorizar ≠ aprender |
| 10 | Qué pasa en Overfitting | **b)** El modelo memoriza los datos en lugar de aprender patrones | Bajo en train, alto en test |

---

## Bloque 2: Tipos de aprendizaje y validación (11–17)

| # | Pregunta resumida | ✅ Respuesta | Justificación |
|---|-------------------|-------------|---------------|
| 11 | Característica del Aprendizaje Supervisado | **b)** Aprende de datos etiquetados | Tenemos las "respuestas correctas" |
| 12 | Función del Aprendizaje No Supervisado | **a)** Encontrar patrones o estructuras ocultas en datos sin etiquetas | Clustering, asociación |
| 13 | Paradigma de "premios y castigos" | **c)** Por refuerzo | Agente, recompensa, estado |
| 14 | Procedimiento Hold-out | **b)** Dividir los datos en conjuntos de entrenamiento y test | Separación simple |
| 15 | Porcentaje habitual de Hold-out | **b)** 80% entrenamiento / 20% test | Es el split estándar |
| 16 | Validación cruzada k-fold | **b)** Dividir los datos en k particiones para estimar el rendimiento | Promedia varios entrenamientos |
| 17 | Valor habitual de k | **b)** k=5 o k=10 | Compromiso entre coste y robustez |

---

## Bloque 3: Métricas y matriz de confusión (18–20)

| # | Pregunta resumida | ✅ Respuesta | Justificación |
|---|-------------------|-------------|---------------|
| 18 | Qué mide Precision | **b)** Proporción de predicciones positivas que fueron realmente correctas | TP / (TP+FP) |
| 19 | Qué es un Falso Negativo | **a)** El modelo predice "Negativo" pero la realidad es "Positivo" | Se "escapa" un positivo |
| 20 | Métrica de error más común en regresión lineal | **b)** Error Cuadrático Medio (MSE) | Penaliza errores grandes |

---

## Bloque 4: Algoritmos supervisados (21–30)

| # | Pregunta resumida | ✅ Respuesta | Justificación |
|---|-------------------|-------------|---------------|
| 21 | Propósito de la Regresión Logística | **b)** Clasificación binaria | A pesar del nombre, no es regresión continua |
| 22 | Objetivo de SVM | **b)** Encontrar el hiperplano que maximice el margen entre dos clases | Margen máximo |
| 23 | Margen en SVM | **b)** Distancia perpendicular desde el hiperplano hasta los vectores de soporte | Es lo que se maximiza |
| 24 | Kernel para relaciones no lineales | **c)** Kernel de Función de Base Radial (RBF / Gaussiano) | El más común |
| 25 | k-NN "no paramétrico" | **b)** No asume una distribución predefinida para los datos | Aprende de los datos directamente |
| 26 | Métrica de distancia común en k-NN | **b)** Distancia Euclidiana | √Σ(xᵢ-yᵢ)² |
| 27 | Regla de decisión en k-NN clasificación | **b)** Voto mayoritario entre los k vecinos más cercanos | Mayoría manda |
| 28 | Estructura matemática de un Árbol | **b)** Grafo acíclico dirigido | Sin ciclos, dirigido |
| 29 | Qué mide la Entropía | **b)** Pureza o mezcla de las etiquetas de clase en un nodo | 0 = puro, 1 = 50/50 |
| 30 | Alta entropía en un nodo | **a)** Las clases están muy mezcladas (alta incertidumbre) | Necesita más splits |

---

## Bloque 5: Ensembles, no supervisado y avanzados (31–40)

| # | Pregunta resumida | ✅ Respuesta | Justificación |
|---|-------------------|-------------|---------------|
| 31 | Feature Bagging en Random Forest | **b)** Seleccionar un subconjunto aleatorio de características en cada nodo | Crea diversidad entre árboles |
| 32 | Diferencia de XGBoost | **b)** Incluye regularización y procesamiento en paralelo | Es el "Gradient Boosting mejorado" |
| 33 | Objetivo de K-Means | **a)** Particionar n observaciones en K grupos donde cada punto pertenece al centroide más cercano | Clustering particional |
| 34 | Característica principal de DBSCAN | **b)** Agrupa puntos basados en la densidad y puede identificar ruido (outliers) | No requiere K predefinido |
| 35 | Clustering Jerárquico Aglomerativo | **c)** Empieza con cada punto como un grupo y los va fusionando por cercanía (bottom-up) | Bottom-up |
| 36 | Principio de Isolation Forest | **b)** Las anomalías son pocas y diferentes, siendo fáciles de aislar | "Pocos y diferentes" |
| 37 | Partes de una red neuronal artificial | **c)** Capas de entrada, capas ocultas y capa de salida | Las 3 capas básicas |
| 38 | Pesos en una red neuronal | **a)** La importancia o fuerza de la conexión entre neuronas | Lo que se aprende |
| 39 | Característica de las RNN | **b)** Tienen "memoria" para manejar secuencias | Recurrencia = bucle temporal |
| 40 | Factor de Descuento γ en RL | **b)** Qué tanto nos importa la recompensa futura | 0=miope, 1=largo plazo |

---

## 🎯 Tips para el examen

- Si dudas entre **Precision y Recall**: pregúntate "¿qué error cuesta más?"
  - **Falso Positivo costoso** (e.g., spam) → maximizar Precision.
  - **Falso Negativo costoso** (e.g., enfermedad) → maximizar Recall.
- **Accuracy NO sirve** cuando las clases están desbalanceadas → usar F1.
- **MSE penaliza más errores grandes** que MAE (porque eleva al cuadrado).
- **K-Means necesita K**, **DBSCAN no** (usa eps y minPts).
- **Random Forest = bagging paralelo**, **Gradient Boosting = secuencial corrigiendo errores**.
