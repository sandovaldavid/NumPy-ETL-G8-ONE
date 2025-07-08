<div align="center">

# 🔢 NumPy: análisis numérico eficiente con Python

[![Status](https://img.shields.io/badge/Status-Finalizado-green?style=for-the-badge)]()
[![ONE](https://img.shields.io/badge/ONE%20Education-G8-blue?style=for-the-badge)](https://www.oracle.com/lad/education/oracle-next-education/)
[![Alura](https://img.shields.io/badge/Alura-Data%20Science-orange?style=for-the-badge)](https://www.alura.com.br/)

</div>

<p align="center">Este repositorio documenta mi aprendizaje del curso <strong>NumPy: análisis numérico eficiente con Python</strong>, parte de la formación <strong>Aprendiendo a hacer ETL G8 - ONE</strong> de Alura.</p>

## 🎯 Descripción del Curso

<div align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeHZhbXoxbzM4aW9wYnJ2Y3R6ZXd6anp2b3l3eW1mcmcwb2YwcDYybiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oKIPEqDGUULpEU0aQ/giphy.gif" width="400">
</div>

Este curso está enfocado en el aprendizaje de NumPy, una biblioteca fundamental para el análisis numérico en Python, que proporciona soporte para arrays y matrices multidimensionales, junto con una amplia colección de funciones matemáticas de alto nivel para operar con estos objetos.

## 📚 Lo que aprenderás en este curso

<details>
<summary><h3>1. Lectura y escritura de datos con NumPy &nbsp; <img src="https://img.shields.io/badge/NumPy-%23013243.svg?style=flat&logo=numpy&logoColor=white" /></h3></summary>
<br>

- 📥 Importar y exportar datos con NumPy
- 📤 Funciones para guardar y cargar arrays
- 🔄 Interacción con diferentes formatos de datos
- 📊 Lectura eficiente de conjuntos de datos grandes

```python
import numpy as np

# Ejemplo de guardado y carga
data = np.array([[1, 2, 3], [4, 5, 6]])
np.savetxt('data.txt', data)
loaded_data = np.loadtxt('data.txt')
```

</details>

<details>
<summary><h3>2. Creación y manipulación de matrices multidimensionales &nbsp; <img src="https://img.shields.io/badge/NumPy-%23013243.svg?style=flat&logo=numpy&logoColor=white" /></h3></summary>
<br>

- 🔢 Creación de arrays de diferentes dimensiones
- 🧮 Indexación y slicing avanzado
- 🔄 Reshaping y reorganización de datos
- 🔍 Operaciones de broadcast

```python
import numpy as np

# Creación y manipulación de matrices
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
reshaped = arr_2d.reshape(3, 2)
slice_example = arr_2d[:, 1:3]  # Selecciona todas las filas, columnas 1 y 2
```

</details>

<details>
<summary><h3>3. Generación de números aleatorios &nbsp; <img src="https://img.shields.io/badge/NumPy-%23013243.svg?style=flat&logo=numpy&logoColor=white" /></h3></summary>
<br>

- 🎲 Funciones para generación de números aleatorios
- 📊 Distribuciones probabilísticas disponibles
- 🔄 Muestreo y permutaciones aleatorias
- 🧩 Creación de datasets sintéticos

```python
import numpy as np

# Generación de números aleatorios
np.random.seed(42)  # Para reproducibilidad
random_array = np.random.rand(3, 3)  # Array 3x3 con valores entre 0 y 1
random_ints = np.random.randint(1, 100, size=10)  # 10 enteros entre 1 y 99
```

</details>

<details>
<summary><h3>4. Uso de Seeds para controlar la aleatoriedad &nbsp; <img src="https://img.shields.io/badge/NumPy-%23013243.svg?style=flat&logo=numpy&logoColor=white" /></h3></summary>
<br>

- 🔒 Concepto de semilla (seed) en generación pseudoaleatoria
- 🔄 Reproducibilidad de resultados
- 🧪 Experimentación controlada
- 🔬 Casos de uso para investigación científica

```python
import numpy as np

# Demostrando reproducibilidad con seeds
np.random.seed(42)
result1 = np.random.rand(5)

np.random.seed(42)  # Misma semilla
result2 = np.random.rand(5)

print("¿Son iguales?", np.array_equal(result1, result2))  # True
```

</details>

<details>
<summary><h3>5. Regresión lineal con NumPy &nbsp; <img src="https://img.shields.io/badge/NumPy-%23013243.svg?style=flat&logo=numpy&logoColor=white" /></h3></summary>
<br>

- 📈 Implementación de regresión lineal desde cero
- 🧮 Cálculo de coeficientes con álgebra lineal
- 📊 Evaluación de modelos de regresión
- 🔍 Predicción con modelos entrenados

```python
import numpy as np

# Ejemplo simple de regresión lineal
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Calcular coeficientes (pendiente y ordenada al origen)
A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]

print(f"Ecuación de regresión: y = {m:.2f}x + {c:.2f}")
```

</details>

<details>
<summary><h3>6. Funciones de agregación en NumPy &nbsp; <img src="https://img.shields.io/badge/NumPy-%23013243.svg?style=flat&logo=numpy&logoColor=white" /></h3></summary>
<br>

- 📊 Cálculo de estadísticas descriptivas
- 🔢 Operaciones de reducción (sum, mean, max, min)
- 🧮 Funciones de agregación por ejes
- 📈 Análisis de datos multidimensionales

```python
import numpy as np

# Funciones de agregación
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(f"Suma total: {data.sum()}")
print(f"Media por columna: {data.mean(axis=0)}")
print(f"Máximo por fila: {data.max(axis=1)}")
print(f"Desviación estándar: {data.std()}")
```

</details>

## 🛠️ Herramientas y Tecnologías

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12.7-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white" />
  <img src="https://img.shields.io/badge/Jupyter-F37626.svg?style=for-the-badge&logo=Jupyter&logoColor=white" />
  <img src="https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black" />
</p>

Este curso forma parte del programa ONE Education G8 de Alura, dentro de la formación "Aprendiendo a hacer ETL G8 - ONE", enfocado en el dominio de NumPy como herramienta fundamental para el análisis numérico y científico en Python.

## 🎓 Beneficios del curso

> Al completar este curso de NumPy, obtendré habilidades fundamentales para el análisis numérico eficiente en Python, lo que me permitirá:
> - Procesar grandes volúmenes de datos numéricos con alto rendimiento
> - Implementar algoritmos matemáticos y estadísticos desde cero
> - Crear simulaciones y modelos predictivos básicos
> - Construir una base sólida para avanzar en el campo de la ciencia de datos

---

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-David_Sandoval-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/devsandoval)
[![GitHub](https://img.shields.io/badge/GitHub-@sandovaldavid-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sandovaldavid)

Programa ONE Education G8 - Alura

</div>