from typing import Any
from pygame.draw import rect
from pygame.display import set_mode, flip, set_caption, set_icon, update
from pygame.image import load
from pygame.font import Font
from pygame import init
from pygame.transform import scale
init()

__Ratio_ecran = 3 #facteur d'agrandissement par rapport à l'écran d'une Numworks.
__fonte_kandinsky = Font("ter-u18b.bdf")
__screen = set_mode((320 * __Ratio_ecran, 222 * __Ratio_ecran))
__screen.fill("white")
set_caption("Numworks Calculator")
set_icon(load("icon_Numworks.bmp"))
flip()


def __check_int_type(*args: Any) -> None:
    for i in args:
        if not isinstance(i, int):
            raise TypeError(f"can't convert {type(i).__name__} to int")


def color(r: int|bool|float, g:int|float|bool, b: int|float|bool) -> tuple[int, int, int]:
    """
    Définit une couleur rvb

    Génère la valeur de la couleur r,g,b.
    Vous pouvez aussi simplement utiliser un tuple pour définir une couleur : (r,g,b).
    """
    for i in r,g,b:
        if not isinstance(i, (float, int)):
            raise TypeError(f"can't convert {type(i).__name__} to float")
    return (r, g, b)


def get_pixel(x: int, y: int) -> tuple[int, int, int]:
    """
    Renvoie la couleur du pixel (x,y)

    Renvoie la couleur du pixel aux coordonnées x,y sous forme de tuple (r,g,b).
    """
    __check_int_type(x,y)
    return __screen.get_at((x * __Ratio_ecran, y * __Ratio_ecran))[:3]


def set_pixel(x: int, y: int, color: tuple[int, int, int]|str) -> None:
    """
    Colore le pixel (x,y)

    Allume le pixel x,y de la couleur color.
    """
    __check_int_type(x, y)
    update(rect(__screen, color,
                (x * __Ratio_ecran, y * __Ratio_ecran, __Ratio_ecran, __Ratio_ecran)))


def draw_string(text: str, x: int, y: int, color: tuple[int, int, int]|str = "black", background: tuple[int]|str = "white") -> None:
    """
    Affiche un texte au pixel (x,y)

    Affiche le texte text aux coordonnées x,y.
    Les arguments color (couleur du texte) et background (couleur de l’arrière plan du texte) sont optionnels.
    """
    __check_int_type(x,y)
    if not isinstance(text, str):
        raise TypeError(f"can't convert '{type(text).__name__}' object to str implicitly")
    __screen.blit(scale(__fonte_kandinsky.render(text, False, color, background),
                        (__Ratio_ecran * 10 * (len(text)-text.count("\u0301")),
                         18 * __Ratio_ecran)),
                  (x * __Ratio_ecran, y * __Ratio_ecran))
    flip()


def fill_rect(x: int, y: int, w: int, h: int, col: tuple[int, int, int]|str) -> None:
    """
    Remplit un rectangle

    Remplit un rectangle de largeur w et de hauteur h avec la couleur col au point de coordonnées x et y.
    """
    __check_int_type(x, y, w, h)
    update(rect(__screen, col, (x * __Ratio_ecran, y * __Ratio_ecran,
                                w * __Ratio_ecran, h * __Ratio_ecran)))