# Leer docu: https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.resize

from PIL import Image
import numpy as np
from numpy.typing import NDArray

def abrir_imagen(archivo_imagen: str, redux_factor: int = 1, largo_modifier: float = 2.5) -> Image.Image:
    """
    Abrir una imagen como un archivo Pillow.
    Docu: https://pillow.readthedocs.io/en/stable/reference/Image.html
    
    Args:
        - archivo_imagen: path de la imagen
        - redux_factor: factor de reescalado de la imagen, sin cambiar su ratio. (Default: 1)
        - largo_modifier: modifica el largo de la imagen, para que el reesultado ASCII
          final no sea demasiado vertical. (Default: 2.5) 

    Return:
        - Objeto Image reescalado y modificado.
    """
    with Image.open(archivo_imagen) as im:
        im = im.reduce(redux_factor)
        largo, alto = im.size
        largo_mod = int(largo * largo_modifier)
        im = im.resize((largo_mod, alto))
    return im

def blanco_negro(im: Image.Image) -> Image.Image:
    """
    Cambiar los valores de color de una imagen Pillow a blanco y negro. 
    """
    return im.convert("L")

def imagen_a_matriz2d(im: Image.Image) -> NDArray:
    """
    Convertir un objeto Image de Pillow a una matriz 2d de numpy.
    
    Args:
        - im: objeto Image de Pillow.
    
    Return:
        Una matriz 2D a partir de los valores de los pixeles del objeto Image
    """
    pixeles = list(im.getdata())
    #Lo siguiente es lo mismo que pixel_matrix = [pixeles[i:i+largo_mod] for i in range(0, largo_mod*alto, largo_mod)]
    return np.array(pixeles, float).reshape((im.height, im.width))

def floyd_steinberg(img: NDArray) -> NDArray:
    """
    Aplicar dithering Floyd-Steinberg dithering a una imagen en escala de grises.
    Docu: https://en.wikipedia.org/wiki/Floyd%E2%80%93Steinberg_dithering
    
    Args:
        img: matriz 2D de los valores de los pixeles en escala de grises (0-255)
    
    Return:
        Imagen como una matriz 2D de numpy (0= negro, 255= blanco)
    """
    img = img.astype(float)
    h, w = img.shape

    for y in range(h):
        for x in range(w):
            old = img[y, x]
            new = 0 if old < 128 else 255
            img[y, x] = new
            err = old - new

            if x + 1 < w:
                img[y, x + 1] += err * 7 / 16

            if y + 1 < h:
                if x - 1 >= 0:
                    img[y + 1, x - 1] += err * 3 / 16
                
                img[y + 1, x] += err * 5 / 16
                
                if x + 1 < w:
                    img[y + 1, x + 1] += err * 1 / 16

    return np.clip(img, 0, 255).astype(np.uint8)

def guardar_imagen_dithered(dithered_matrix: NDArray) -> None:
    Image.fromarray(dithered_matrix).save("b.png")
    return    

def matriz_a_ascii(matrix: NDArray, ASCII_COLORS) -> str:
    max_i = len(ASCII_COLORS) - 1

    return "\n".join(
        "".join(ASCII_COLORS[int(val / 255 * max_i)] for val in fila)
        for fila in matrix
    )

def guardar_texto_ascii(ascii: str, archivo_output: str="ascii.txt") -> None:
    with open(archivo_output, "w") as txt:
        txt.write(ascii)

def image_to_ascii(ASCII_COLORS: str,
                   archivo_imagen: str,
                   redux_factor: int = 1,
                   largo_modifier: float = 1,
                   dither: bool = True,
                   save_dithered_image = True,
                   archivo_output = "ascii.txt") -> None:
    try:
        image = abrir_imagen(archivo_imagen, redux_factor, largo_modifier)
    except FileNotFoundError:
        raise FileNotFoundError(f"No se encontró el archivo: {archivo_imagen}")
    
    imagebn = blanco_negro(image)
    matrix = imagen_a_matriz2d(imagebn)

    dithered_matrix = floyd_steinberg(matrix) if dither else None
    if save_dithered_image and dithered_matrix is not None:
        guardar_imagen_dithered(dithered_matrix)
        
    matriz_final = dithered_matrix if dithered_matrix is not None else matrix

    ascii = matriz_a_ascii(matriz_final, ASCII_COLORS)
    guardar_texto_ascii(ascii, archivo_output)
