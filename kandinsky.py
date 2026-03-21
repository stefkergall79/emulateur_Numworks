from pygame.draw import rect
from pygame.display import set_mode, flip, set_caption, set_icon, update
from pygame.image import load
from pygame.font import Font
from pygame import init
from pygame.transform import scale
init()

__Ratio_ecran = 3 #facteur d'agrandissement par rapport à l'écran d'une Numworks.

__screen = set_mode((320 * __Ratio_ecran, 222 * __Ratio_ecran))
__screen.fill("white")
set_caption("Numworks Calculator")
set_icon(load("icon_Numworks.bmp"))
flip()

def __check_int_type(args):
    for i in args:
        if not isinstance(i, int):
            raise TypeError(f"can't convert {type(i).__name__} to int")

def set_pixel(x, y, col):
    """
    Colore le pixel (x,y)
    """
    __check_int_type((x, y))
    update(rect(__screen, col,
                (x * __Ratio_ecran, y * __Ratio_ecran, __Ratio_ecran, __Ratio_ecran)))


def get_pixel(x, y):
    """
    Renvoie la couleur du pixel (x,y)
    """
    __check_int_type((x,y))
    return __screen.get_at((x * __Ratio_ecran, y * __Ratio_ecran))[:3]


def fill_rect(x, y, w, h, col):
    """
    Remplit un rectangle
    """
    __check_int_type((x, y, w, h))
    update(rect(__screen, col, (x * __Ratio_ecran, y * __Ratio_ecran,
                                w * __Ratio_ecran, h * __Ratio_ecran)))

__fonte_kandinsky = Font("ter-u18b.bdf")
def draw_string(text, x, y, color = "black", background = "white"):
    """
    Affiche un texte au pixel (x,y)
    """
    __check_int_type((x,y))
    if not isinstance(text, str):
        raise TypeError(f"can't convert '{type(text).__name__}' object to str implicitly")
    __screen.blit(scale(__fonte_kandinsky.render(text, False, color, background),
                        (__Ratio_ecran * 10 * (len(text)-text.count("\u0301")),
                         18 * __Ratio_ecran)),
                  (x * __Ratio_ecran, y * __Ratio_ecran))
    flip()

def color(r, g, b):
    """
    Définit une couleur rvb
    """
    for i in r,g,b:
        if not isinstance(i, (float, int)):
            raise TypeError(f"can't convert {type(i).__name__} to float")
    return (r, g, b)