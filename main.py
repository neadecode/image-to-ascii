from ascii_functs import *

def main():
    ASCII_COLORS = " .`-':,_^~=+*cosLTv)J7ItlueZSEqkph9dVOGUAKXHm8RD#$Bg0MNWQ%&@"
    archivo_imagen = "a.png"
    redux_factor  = 1
    largo_modifier  = 2.5
    dither = False
    save_dithered_image = True

    archivo_output = "ascii.txt"

    image_to_ascii(ASCII_COLORS, archivo_imagen, redux_factor, largo_modifier,
                   dither, save_dithered_image, archivo_output)
    


if __name__ == "__main__":
    main()