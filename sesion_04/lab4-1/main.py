import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar imagen en escala de grises
imagen = cv2.imread('img1.jpg', cv2.IMREAD_GRAYSCALE)

# Mostrar imagen original
plt.imshow(imagen, cmap='gray')
plt.title('Imagen Original')
plt.axis('off')
plt.show()

# Aplicar filtro gausiano
imagen_suavizada = cv2.GaussianBlur(imagen, (5, 5), 0)

plt.imshow(imagen_suavizada, cmap='gray')
plt.title('Imagen Suavizada (Filtro Gaussiano)')
plt.axis('off')
plt.show()

# Detección de bordes (Canny)
bordes = cv2.Canny(imagen_suavizada, 50, 150)

plt.imshow(bordes, cmap='gray')
plt.title('Detección de Bordes (Canny)')
plt.axis('off')
plt.show()

# Detección de esquinas (Harris)
imagen_color = cv2.imread('img1.jpg')
imagen_color = cv2.cvtColor(imagen_color, cv2.COLOR_BGR2RGB)

esquinas = cv2.cornerHarris(np.float32(imagen), 2, 3, 0.04)
imagen_color[esquinas > 0.01 * esquinas.max()] = [255, 0, 0]

plt.imshow(imagen_color)
plt.title('Detección de Esquinas (Harris)')
plt.axis('off')
plt.show()

# Detección de líneas (Hough)
lineas = cv2.HoughLinesP(
    bordes,
    1,
    np.pi / 180,
    threshold=100,
    minLineLength=50,
    maxLineGap=10
)

if lineas is not None:
    for linea in lineas:
        x1, y1, x2, y2 = linea[0]
        cv2.line(imagen_color, (x1, y1), (x2, y2), (0, 255, 0), 2)

plt.imshow(imagen_color)
plt.title('Detección de Líneas (Hough)')
plt.axis('off')
plt.show()