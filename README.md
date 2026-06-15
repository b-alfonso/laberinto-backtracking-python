# 🏢 Resolución de Laberinto usando Backtracking en Python

Este proyecto implementa un algoritmo de **Backtracking (Búsqueda con Retroceso)** en Python 3 para resolver de forma automatizada un laberinto matricial de 9x9. El programa simula el recorrido de un ratón que debe navegar desde un punto de inicio hasta la salida de manera segura, gestionando un sistema de vidas limitado.

---

## 🚀 Características del Proyecto

* **Búsqueda Inteligente:** El algoritmo explora las rutas de forma recursiva. Si encuentra un obstáculo o una ruta inviable, retrocede (*backtracking*) para evaluar nuevas alternativas.
* **Prioridad de Movimiento Estricta:** En cada celda, el ratón intenta moverse obligatoriamente en este orden: **Abajo ➡️ Derecha ➡️ Arriba ➡️ Izquierda**.
* **Sistema de Vidas Dinámico:** El ratón inicia con **3 vidas**. Las casillas con valores `-1` o `-2` restan vidas. Si la salud cae a 0 o menos, el camino se declara inválido inmediatamente y la IA retrocede.
* **Visualización en Tiempo Real:** La consola muestra una animación fluida usando el carácter `*` para representar el camino activo, facilitando el análisis del comportamiento del algoritmo.

---

## 🛠️ Requisitos Previos

Antes de ejecutar el script, asegúrate de contar con **Python 3.x** instalado en tu sistema. Puedes comprobarlo abriendo una terminal y escribiendo:

```bash
python --version
```

---

## 💻 Instrucciones de Ejecución

1. **Descargar el repositorio:** Descarga los archivos directamente desde la web de GitHub o clona el proyecto usando Git:
   ```bash
   git clone https://github.com
   ```
2. **Navegar a la carpeta:** Abre la terminal de comandos y accede al directorio del proyecto:
   ```bash
   cd laberinto-backtracking-python
   ```
3. **Ejecutar el programa:** Inicia el script principal de Python:
   ```bash
   python Laberinto.py
   ```

---

## 📊 Resultados Obtenidos

* **Estado Final:** ¡ÉXITO! El ratón localizó la salida manteniendo su supervivencia.
* **Longitud de la Ruta Óptima:** **27 pasos** totales desde el origen hasta el destino.
* **Vidas Finales:** **3 vidas** (el algoritmo logró evadir todas las penalizaciones destructivas).
