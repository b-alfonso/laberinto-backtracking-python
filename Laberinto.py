import time
import sys

sys.setrecursionlimit(10000)  # Para seguridad en la recursión

# ------------------------------------------------------------
# 1. DEFINICIÓN DEL LABERINTO (9x9)
# ------------------------------------------------------------
laberinto_original = [
    ['F',  1,  1,  0,  1,  1,  1,  1,  1],
    [-2,  0,  0, -1,  0,  1,  0,  1,  0],
    [ 1,  1,  0,  1,  1,  1,  0,  1,  0],
    [ 0,  1,  0, -1,  0,  0,  0, -1,  0],
    [ 1,  1,  1,  1,  1,  1,  1,  1,  0],
    [-1,  0,  0,  0,  0,  0,  0,  1,  1],
    [ 1,  1,  1,  1, -1,  1,  1,  1,  0],
    [ 1,  0,  0,  1,  0,  1,  0,  1,  0],
    ['I',  1, -1,  1,  1,  1,  0,  1,  1]
]

# Posiciones fijas
INICIO = (8, 0)   # fila, columna (esquina inferior izquierda)
FIN    = (0, 0)   # fila, columna (esquina superior izquierda)

# ------------------------------------------------------------
# 2. FUNCIONES AUXILIARES
# ------------------------------------------------------------
def obtener_valor_celda(celda):
    """
    Convierte la celda a su valor numérico para la lógica del juego.
    'I' y 'F' equivalen a 1 (paso normal).
    Los números se devuelven tal cual.
    """
    if celda == 'I' or celda == 'F':
        return 1
    return celda  # ya es int (1, 0, -1, -2)

def mostrar_laberinto(camino, vidas_actuales, pos_actual):
    """
    Imprime el estado actual del laberinto.
    - Las celdas que pertenecen al camino actual (excepto 'I' y 'F') se muestran como '*'.
    - Las posiciones de inicio y fin conservan sus letras.
    - Se muestra la posición actual y las vidas restantes.
    """
    print("\n" + "="*50)
    print(f"VIDAS RESTANTES: {vidas_actuales}   |   POSICIÓN ACTUAL: {pos_actual}")
    print("="*50)
    
    # Convertir el camino a un conjunto para búsqueda rápida
    conjunto_camino = set(camino)
    
    for i in range(len(laberinto_original)):
        fila_str = ""
        for j in range(len(laberinto_original[0])):
            celda = laberinto_original[i][j]
            # Si la celda es parte del camino actual y no es ni inicio ni fin
            if (i, j) in conjunto_camino and celda not in ('I', 'F'):
                fila_str += "  * "   # camino marcado
            else:
                # Formato de impresión: ancho fijo de 3 caracteres
                if isinstance(celda, int):
                    fila_str += f"{celda:3d} "
                else:
                    fila_str += f"  {celda} "
        print(fila_str)
    print("="*50)
    time.sleep(0.3)  # pausa para apreciar el avance

# ------------------------------------------------------------
# 3. BACKTRACKING CON PRIORIDAD DE MOVIMIENTOS
# ------------------------------------------------------------
# Orden estricto de direcciones: Abajo, Derecha, Arriba, Izquierda
DIRECCIONES = [(1, 0), (0, 1), (-1, 0), (0, -1)]
NOMBRES_DIR = ["Abajo", "Derecha", "Arriba", "Izquierda"]

def backtrack(pos_actual, vidas, camino):
    """
    Función recursiva de backtracking.
    Retorna True si encuentra un camino hasta la meta, False en caso contrario.
    """
    i, j = pos_actual
    
    # Si llegamos a la meta
    if pos_actual == FIN:
        return True
    
    # Explorar movimientos según la prioridad establecida
    for (di, dj), nombre_dir in zip(DIRECCIONES, NOMBRES_DIR):
        ni, nj = i + di, j + dj
        nueva_pos = (ni, nj)
        
        # Verificar límites del laberinto
        if 0 <= ni < len(laberinto_original) and 0 <= nj < len(laberinto_original[0]):
            celda_valor = obtener_valor_celda(laberinto_original[ni][nj])
            
            # Condiciones: no es muro (0), no está ya en el camino actual
            if celda_valor != 0 and nueva_pos not in camino:
                # Calcular costo en vidas (0 si es 1, positivo si es -1 o -2)
                costo = 0 if celda_valor == 1 else (-celda_valor) if celda_valor < 0 else 0
                nuevas_vidas = vidas - costo
                
                # Solo se avanza si las vidas se mantienen estrictamente positivas
                if nuevas_vidas > 0:
                    # Realizar el movimiento
                    camino.append(nueva_pos)
                    mostrar_laberinto(camino, nuevas_vidas, nueva_pos)
                    
                    # Llamada recursiva
                    if backtrack(nueva_pos, nuevas_vidas, camino):
                        return True
                    
                    # Backtracking: deshacer el movimiento
                    camino.pop()
                    mostrar_laberinto(camino, vidas, pos_actual)  # mostrar estado al retroceder
    
    # No se encontró una ruta válida desde esta posición
    return False

# ------------------------------------------------------------
# 4. EJECUCIÓN PRINCIPAL Y SALIDA EN PANTALLA
# ------------------------------------------------------------
def main():
    print("="*60)
    print("LABERINTO ORIGINAL")
    print("="*60)
    # Mostrar laberinto original (sin camino)
    mostrar_laberinto(camino=[], vidas_actuales=3, pos_actual=INICIO)
    time.sleep(1)
    
    # Inicializar camino con la posición de inicio
    camino_inicial = [INICIO]
    vidas_iniciales = 3
    
    print("\nINICIANDO BÚSQUEDA DE RUTA...\n")
    mostrar_laberinto(camino_inicial, vidas_iniciales, INICIO)
    
    # Llamar al algoritmo de backtracking
    exito = backtrack(INICIO, vidas_iniciales, camino_inicial)
    
    # Mostrar resultado final
    print("\n" + "="*60)
    if exito:
        print("¡ÉXITO! El ratón ha encontrado una salida con vida.")
        print("Camino completo (marcado con '*'):")
        mostrar_laberinto(camino_inicial, vidas_iniciales, INICIO)
        print(f"Longitud del camino: {len(camino_inicial)} pasos.")
    else:
        print("FRACASO. No se encontró ninguna ruta que mantenga al ratón con vida.")
        print("Se agotaron todas las alternativas.")
    print("="*60)

if __name__ == "__main__":
    main()
