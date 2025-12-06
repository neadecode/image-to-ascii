from PIL import Image
import sys

# Caracteres ASCII ordenados de oscuro a claro
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    """Redimensiona la imagen manteniendo la proporción"""
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio * 0.55)  # 0.55 para compensar altura de caracteres
    return image.resize((new_width, new_height))

def grayscale(image):
    """Convierte la imagen a escala de grises"""
    return image.convert("L")

def pixels_to_ascii(image):
    """Convierte los píxeles a caracteres ASCII"""
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 25]  # 256/10 ≈ 25
    return ascii_str


#Convierte la imagen en un 
def image_to_ascii(image_path, new_width=100):
    """Función principal que convierte imagen a ASCII"""
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Error al abrir la imagen: {e}")
        return None
    
    # Procesar imagen
    image = resize_image(image, new_width)
    image = grayscale(image)
    
    # Convertir a ASCII
    ascii_str = pixels_to_ascii(image)
    
    # Formatear en líneas
    img_width = image.width
    ascii_img = ""
    for i in range(0, len(ascii_str), img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    
    return ascii_img

def save_ascii_to_file(ascii_art, output_file="ascii_art.txt"):
    """Guarda el arte ASCII en un archivo"""
    with open(output_file, "w") as f:
        f.write(ascii_art)
    print(f"Arte ASCII guardado en: {output_file}")

# Ejemplo de uso
if __name__ == "__main__":
    # Cambia esta ruta por la de tu imagen
    image_path = "./2.png"
    
    # Ancho en caracteres (ajusta según tu preferencia)
    width = 100
    
    # Convertir imagen
    ascii_art = image_to_ascii(image_path, width)
    
    if ascii_art:
        # Mostrar en consola
        print(ascii_art)
        
        # Guardar en archivo
        save_ascii_to_file(ascii_art, "output_ascii.txt")