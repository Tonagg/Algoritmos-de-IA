# 📖 Preguntas Abiertas + Resumen Teórico

> Material para los **2 puntos** de "Pregunta abierta" y los **2 puntos** de "Algoritmo y código de teoría".  
> Cada respuesta es directa, lista para copiar/parafrasear en el examen.

---

## 📋 Las 15 preguntas abiertas (respuestas listas)

### 1. Aprendizaje Automático vs Programación Tradicional
> En la **programación tradicional** el desarrollador escribe reglas explícitas (`if x then y`) que la computadora ejecuta. En el **aprendizaje automático**, en cambio, se programa un **algoritmo capaz de aprender esas reglas a partir de los datos**: en lugar de codificar la lógica, le mostramos ejemplos y el algoritmo infiere los patrones. Es un cambio de paradigma de "instrucciones" a "datos + aprendizaje".

### 2. Paradigma conexionista vs simbólico (representación)
> El **paradigma simbólico** representa el conocimiento mediante **reglas lógicas explícitas** y símbolos manipulables; es transparente y explicable porque cada paso del razonamiento es legible. El **conexionista** representa el conocimiento como **pesos numéricos distribuidos** en una red de unidades simples; es muy potente para tareas perceptuales, pero a menudo es una **caja negra** difícil de descifrar.

### 3. ¿Por qué ML es mejor en percepción sensorial?
> Tareas como ver, oír o reconocer voz las realizamos los humanos de forma **inconsciente y automática**: no podríamos escribir las reglas explícitas para identificar un gato en una imagen. ML aprovecha que aunque sea **difícil codificar las reglas, es fácil dar muchos ejemplos**, y los algoritmos modernos (sobre todo deep learning) son excelentes extrayendo patrones a partir de esos ejemplos.

### 4. Generalización (analogía del examen)
> Aprender no es **memorizar**. Si un alumno solo memoriza las respuestas de exámenes pasados pero no entiende el tema, fallará en una pregunta nueva. La **generalización** es la capacidad del modelo (o estudiante) de **responder correctamente sobre datos que no vio durante el entrenamiento**: es la verdadera medida de aprendizaje.

### 5. Supervisado vs No Supervisado
> En **supervisado** los datos vienen con **etiquetas** (la respuesta correcta) que guían el aprendizaje; el modelo aprende a mapear entradas a esa etiqueta (clasificación o regresión). En **no supervisado** **no hay etiquetas**: el algoritmo busca por sí solo estructuras o patrones ocultos en los datos (clustering, reducción de dimensionalidad, detección de anomalías).

### 6. Ciclo del Aprendizaje por Refuerzo
> Un **agente** observa el **estado** del entorno, toma una **acción**, recibe una **recompensa** (positiva o negativa) y pasa a un nuevo estado. Este ciclo se repite y el agente ajusta su política de decisión con el objetivo de **maximizar la recompensa acumulada a largo plazo**.

### 7. Por qué la aleatoriedad al elegir el test
> Para **evitar sesgos sistemáticos** entre el conjunto de entrenamiento y el de test. Si separamos por orden temporal o por categoría, el test podría no representar correctamente la distribución real. La aleatoriedad garantiza que ambos conjuntos provienen de la **misma distribución** y la evaluación es justa.

### 8. ¿Qué es un "fold" en validación cruzada?
> Un fold es una de las **k particiones disjuntas** en las que se divide el dataset. Si k=10, cada fold contiene aproximadamente el 10% de los datos. En cada iteración un fold actúa como conjunto de prueba y los k-1 restantes como entrenamiento; el rendimiento final es el **promedio sobre los k folds**.

### 9. Métricas con sus fórmulas (RESPUESTA EXTENSA)

#### Métricas para CLASIFICACIÓN

| Métrica | Fórmula | Cuándo usarla |
|---------|---------|---------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Clases balanceadas |
| **Precision** | TP / (TP + FP) | Falso positivo es costoso (spam) |
| **Recall** (Sensibilidad) | TP / (TP + FN) | Falso negativo es costoso (medicina) |
| **F1-score** | 2 · (P · R) / (P + R) | Clases desbalanceadas |
| **Specificity** | TN / (TN + FP) | Capacidad de descartar negativos |

#### Métricas para REGRESIÓN

| Métrica | Fórmula | Característica |
|---------|---------|----------------|
| **MAE** | (1/n) · Σ \|yᵢ − ŷᵢ\| | Robusto a outliers |
| **MSE** | (1/n) · Σ (yᵢ − ŷᵢ)² | Penaliza errores grandes |
| **RMSE** | √MSE | En unidades originales |
| **R²** | 1 − (SS_res / SS_tot) | Proporción de varianza explicada (0–1) |

### 10. ¿Cómo decide k-NN la etiqueta?
> 1) Calcula la **distancia** (euclidiana habitualmente) del nuevo punto a **todos los puntos del entrenamiento**.  
> 2) Selecciona los **k más cercanos**.  
> 3) Hace **voto mayoritario** entre las etiquetas de esos k vecinos.  
> 4) En regresión, en lugar de votar, **promedia** los valores de los k vecinos.

### 11. Kernel Lineal vs Polinomial
> El **kernel lineal** busca una **línea recta** (o hiperplano plano en más dimensiones) para separar clases; es rápido y suficiente cuando los datos son linealmente separables. El **kernel polinomial** transforma los datos elevando a potencias y permite **fronteras curvas**, útiles cuando las clases tienen relaciones no lineales (e.g., separadas por una parábola).

### 12. Desventaja de SVM con datasets grandes
> El tiempo de entrenamiento y el uso de memoria de una SVM crece **al cuadrado o cubo** con el número de muestras (complejidad O(n²) a O(n³)), porque debe calcular y almacenar la matriz kernel entre todos los pares de puntos. Con millones de registros se vuelve **inviable**, frente a algoritmos como Random Forest o Gradient Boosting que escalan mucho mejor.

### 13. Nodo raíz, interno y hoja en un árbol
> - **Nodo raíz**: el primero del árbol; contiene todo el dataset y aplica la primera división.  
> - **Nodo interno**: nodos intermedios que evalúan un atributo y dividen los datos en sub-conjuntos.  
> - **Nodo hoja**: nodo terminal que **emite la decisión final** (clase o valor); ya no se subdivide.

### 14. Aprendizaje en una red neuronal por ajuste de pesos
> La red **propaga hacia adelante** una entrada y produce una predicción. Esa predicción se compara con el valor real mediante una **función de pérdida**. Por **retropropagación** se calcula el gradiente de la pérdida respecto a cada peso y se ajustan los pesos en dirección contraria al gradiente (descenso de gradiente). Tras muchas iteraciones, la red minimiza el error y mejora su precisión.

### 15. Transformers vs RNN
> Las **RNN tradicionales** procesan secuencias **palabra por palabra** y sufren de "memoria a corto plazo" (problema del gradiente que desaparece) en secuencias largas. Los **Transformers** usan el mecanismo de **atención** para procesar **todas las palabras en paralelo** y aprender qué partes del texto son relevantes entre sí, sin importar la distancia. Resultado: entrenan más rápido y manejan dependencias largas mucho mejor.

---

## 🧠 Algoritmo + código de teoría — PLANTILLAS LISTAS

> Para el bloque de **2 puntos** te van a pedir explicar un algoritmo con: fundamentos matemáticos, descripción narrativa, **pseudocódigo**, **código** y **buenas prácticas**.  
> Aquí tienes las plantillas más probables. Copia/pega la que toque.

### Plantilla A — K-NN (la más probable)

#### 1. Fundamentos matemáticos
- **Distancia euclidiana** entre dos puntos `x` y `y` en R^d:  
  `d(x, y) = √( Σᵢ (xᵢ − yᵢ)² )`
- **Regla de decisión**: la clase del nuevo punto es el modo (clasificación) o la media (regresión) de las etiquetas de los k vecinos más cercanos.

#### 2. Descripción narrativa
> K-NN es un algoritmo **basado en instancias**, **perezoso** (no entrena, solo memoriza el dataset) y **no paramétrico** (no asume una distribución). Para predecir una nueva muestra mide su distancia a todas las muestras conocidas, selecciona las k más cercanas y devuelve la clase mayoritaria.

#### 3. Pseudocódigo
```
ENTRADA: dataset D = {(x₁,y₁), …, (xₙ,yₙ)}, punto nuevo x*, número k
SALIDA : etiqueta predicha para x*

1. Para cada (xᵢ, yᵢ) en D:
       calcular dᵢ = distancia(x*, xᵢ)
2. Ordenar las dᵢ de menor a mayor
3. Tomar las k primeras → vecinos N
4. Devolver el voto mayoritario de las etiquetas de N
```

#### 4. Código en Python con buenas prácticas
```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix

# 1. Carga de datos (reemplazar con el dataset del examen)
# df = pd.read_csv('datos.csv')
# X = df.drop('target', axis=1).values
# y = df['target'].values

# 2. Split estratificado
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

# 3. ESCALADO (crítico para K-NN)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

# 4. Entrenamiento
modelo = KNeighborsClassifier(n_neighbors=5, metric='euclidean')
modelo.fit(X_train, y_train)

# 5. Evaluación
y_pred = modelo.predict(X_test)
print('Matriz de confusión:\n', confusion_matrix(y_test, y_pred))
print('\nReporte:\n', classification_report(y_test, y_pred))
```

#### 5. Buenas prácticas aplicadas
- Semilla fija (`random_state=42`) → reproducibilidad.
- **Escalado** antes de calcular distancias (k-NN es sensible a escalas).
- `stratify=y` mantiene la proporción de clases.
- Reporte con métricas múltiples (no solo accuracy).
- Variables descriptivas (`modelo`, `scaler`).

---

### Plantilla B — K-Means

#### 1. Fundamentos matemáticos
- Función objetivo:  
  `J = Σⱼ Σ_{x∈Cⱼ} ||x − μⱼ||²`  (suma de distancias al cuadrado dentro de cada cluster).
- Centroide: `μⱼ = (1/|Cⱼ|) · Σ_{x∈Cⱼ} x`.

#### 2. Descripción narrativa
> Algoritmo de clustering particional. Divide los datos en K grupos minimizando la varianza intra-cluster. Asume forma esférica y requiere fijar K.

#### 3. Pseudocódigo
```
ENTRADA: dataset X, número K
SALIDA : asignación de cluster para cada punto, centroides

1. Inicializar K centroides aleatoriamente (o con K-means++)
2. Repetir hasta convergencia:
     a. Asignar cada punto al centroide más cercano
     b. Recalcular cada centroide como la media de sus puntos
3. Devolver asignación y centroides
```

#### 4. Código
```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 1. Datos (reemplazar)
# X = ...

# 2. Escalado
X_esc = StandardScaler().fit_transform(X)

# 3. Elegir K con elbow method
inercias = []
for k in range(1, 11):
    km = KMeans(n_clusters=k, n_init=10, random_state=42).fit(X_esc)
    inercias.append(km.inertia_)
plt.plot(range(1,11), inercias, 'bo-'); plt.show()

# 4. Modelo final
modelo = KMeans(n_clusters=3, n_init=10, random_state=42)
etiquetas = modelo.fit_predict(X_esc)
print('Centroides:\n', modelo.cluster_centers_)
```

---

### Plantilla C — Árbol de Decisión

#### 1. Fundamentos matemáticos
- **Entropía**: `H(S) = − Σᵢ pᵢ log₂(pᵢ)`
- **Ganancia de información**: `IG(S,A) = H(S) − Σᵥ (|Sᵥ|/|S|) · H(Sᵥ)`
- En cada nodo se elige el atributo con **mayor IG**.

#### 2. Descripción narrativa
> Modelo basado en una serie de preguntas if-then organizadas como árbol. La raíz contiene todos los datos; cada nodo divide por el atributo que mejor reduce la incertidumbre; las hojas dan la decisión final. Es **interpretable** y **no requiere escalado**.

#### 3. Pseudocódigo
```
FUNCION construir_arbol(D):
  si todos los y en D son iguales → devolver hoja con esa clase
  si no quedan atributos          → devolver hoja con clase mayoritaria
  A* = atributo con mayor ganancia de información en D
  crear nodo con A*
  para cada valor v de A*:
      D_v = subconjunto de D con A* = v
      hijo_v = construir_arbol(D_v)
  devolver nodo
```

#### 4. Código
```python
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

modelo = DecisionTreeClassifier(criterion='entropy', max_depth=5, random_state=42)
modelo.fit(X_train, y_train)

plt.figure(figsize=(15, 8))
plot_tree(modelo, filled=True, rounded=True, fontsize=8)
plt.show()

y_pred = modelo.predict(X_test)
print(classification_report(y_test, y_pred))
```

---

## ✅ Buenas prácticas que SIEMPRE debes incluir

1. **Semilla fija** (`random_state=42`) — reproducibilidad.
2. **División train/test** con `stratify` cuando es clasificación.
3. **Escalado** con `StandardScaler` para K-NN, SVM, redes neuronales y K-Means.
4. **No fugar datos**: ajustar el scaler solo con `X_train`, no con todo X.
5. **Reportar varias métricas**: matriz de confusión + accuracy + precision + recall + F1.
6. **Comentar el código** brevemente.
7. **Visualizar** cuando aporte (matriz de confusión, árbol, frontera).
8. **Conclusión** breve interpretando los resultados.
