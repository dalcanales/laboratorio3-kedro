import cv2
import matplotlib.pyplot as plt

# =========================
# Parte 1: Cargar imágenes
# =========================

img1 = cv2.imread('imagen2.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('imagen3.jpg', cv2.IMREAD_GRAYSCALE)

if img1 is None or img2 is None:
    print("Error: No se pudo cargar alguna imagen.")
    exit()

# =========================
# Parte 2: Mostrar imágenes
# =========================

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.imshow(img1, cmap='gray')
plt.title('Imagen 2')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(img2, cmap='gray')
plt.title('Imagen 3')
plt.axis('off')

plt.show()

# =========================
# Parte 3: Histogramas
# =========================

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.hist(img1.ravel(), bins=256, range=[0,256])
plt.title('Histograma Imagen 1')

plt.subplot(1,2,2)
plt.hist(img2.ravel(), bins=256, range=[0,256])
plt.title('Histograma Imagen 2')

plt.show()

# =========================
# Parte 4: Comparación
# =========================

prom1 = img1.mean()
prom2 = img2.mean()

print("Promedio Imagen 1:", prom1)
print("Promedio Imagen 2:", prom2)

if prom1 > prom2:
    print("La Imagen 2 es más clara")
else:
    print("La Imagen 3 es más clara")