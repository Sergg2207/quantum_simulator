[README.md](https://github.com/user-attachments/files/23291906/README.md)
# Quantum Simulator – Observables y Medidas

**Autor:** Sergio Luis González Alba
**Materia:** Ciencias Naturales y Tecnologia
**Entrega:** Observables y Medidas

---

## Descripción General

Este proyecto corresponde a la simulación del primer sistema cuántico descrito en la **sección 4.1**, y al desarrollo de los retos de programación del **capítulo 4**, enfocados en **observables, medidas, valores propios, media, varianza y dinámica del sistema**.

El trabajo se desarrolló en **Python** usando **NumPy** y **Jupyter Notebooks**, y está estructurado para facilitar su ejecución, lectura y validación paso a paso.

---

## Estructura del Proyecto

```
quantum_simulator/
│
├── notebooks/
│ ├── 1_basic_quantum_system.ipynb # Simulación del primer sistema cuántico (sección 4.1)
│ ├── 2_observables_measurements.ipynb # Retos: observables, medidas, media, varianza, autovalores
│ ├── 3_dynamics.ipynb # Dinámica: aplicación de matrices unitarias (Un)
│ ├── 4_problems.ipynb # Ejemplos modelados: 4.3.1, 4.3.2, 4.4.1, 4.4.2
│ └── 5_discussion.ipynb # Discusión de los ejercicios 4.5.2 y 4.5.3
│
├── quantum_simulator/ # Paquete Python con la librería
│ ├── init.py
│ ├── core.py # QuantumSystem: probabilidades, transiciones, etc.
│ ├── observables.py # Observable: hermiticidad, media, varianza, autovalores
│ └── dynamics.py # QuantumDynamics: aplicar secuencia de Unitaries
│
├── requirements.txt # Dependencias (numpy, jupyter, nbformat)
├── pyproject.toml # Configuración para instalación editable
└── README.md # Este archivo
```

---

## Instalación y Ejecución

### 1️ Requisitos

* Python 3.9 o superior
* Bibliotecas:

  ```
  numpy
  nbformat
  ```

### 2️ Instalación

Ejecutar en consola:

```bash
pip install -r requirements.txt
```

### 3️ Ejecución de los notebooks

Abrir Jupyter Notebook o JupyterLab desde la raíz del proyecto:

```bash
jupyter notebook
```

Luego abrir los archivos dentro de la carpeta `notebooks/`.

---

## Contenido y Funcionalidad

### 1. Simulación básica (sección 4.1)

* Define un sistema con **una partícula confinada en posiciones discretas**.
* Calcula la **probabilidad de encontrar la partícula** en una posición dada.
* Permite ajustar el número de posiciones y los estados iniciales (vectores Ket).

### 2. Observables y medidas

* Comprueba si una matriz es **hermitiana**.
* Calcula la **media y la varianza** de un observable.
* Obtiene los **autovalores y autovectores** (posibles resultados de una medida).
* Simula la **dinámica del sistema** aplicando operadores unitarios (como el Hadamard).

### 3. Ejercicios y ejemplos (capítulo 4)

Incluye ejemplos para los ejercicios:

* **4.3.1:** Probabilidad de encontrar la partícula en una posición.
* **4.3.2:** Cálculo de la probabilidad de transición entre dos estados.
* **4.4.1:** Observables, autovalores y probabilidades de medida.
* **4.4.2:** Dinámica del sistema con secuencia de operadores unitarios.

---

## Entregable

Este repositorio contiene:

* Código fuente funcional y probado.
* Ejemplos y explicaciones en cada notebook.
* Estructura limpia y reproducible para evaluación.

---
