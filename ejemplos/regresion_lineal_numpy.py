# Ejemplo de regresión lineal con NumPy
import numpy as np
import matplotlib.pyplot as plt

# Generar datos de ejemplo
np.random.seed(42)  # Para reproducibilidad
x = np.linspace(0, 10, 100)  # 100 puntos entre 0 y 10
y_true = 2.5 * x + 5  # Función lineal (pendiente 2.5, intercepto 5)
y = y_true + np.random.normal(0, 2, size=len(x))  # Añadir ruido gaussiano

# Implementar regresión lineal usando NumPy
X = np.vstack([x, np.ones(len(x))]).T  # Matriz de diseño
coefs, residuals, rank, s = np.linalg.lstsq(X, y, rcond=None)  # Mínimos cuadrados
pendiente, intercepto = coefs

# Calcular predicciones
y_pred = pendiente * x + intercepto

# Calcular error cuadrático medio
mse = np.mean((y - y_pred) ** 2)

# Visualizar resultados
plt.figure(figsize=(10, 6))
plt.scatter(x, y, alpha=0.7, label='Datos con ruido')
plt.plot(x, y_true, 'r-', linewidth=2, label='Función real')
plt.plot(x, y_pred, 'g--', linewidth=2, label='Regresión estimada')
plt.title(f'Regresión Lineal con NumPy\nPendiente={pendiente:.4f}, Intercepto={intercepto:.4f}, MSE={mse:.4f}')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('regresion_lineal.png')
plt.show()

print(f"Ecuación estimada: y = {pendiente:.4f}x + {intercepto:.4f}")
print(f"Error cuadrático medio: {mse:.4f}")

# Guardar los resultados
resultados = np.column_stack((x, y, y_pred))
np.savetxt('resultados_regresion.csv', resultados, delimiter=',', header='x,y_observado,y_predicho', comments='')

print("\nResultados guardados en 'resultados_regresion.csv'")
