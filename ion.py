from pygame import init
from pygame.locals import *
from pygame.key import get_pressed
from pygame.event import get
init()

KEY_LEFT, KEY_UP, KEY_DOWN, KEY_RIGHT = 0, 1, 2, 3
KEY_OK, KEY_BACK, KEY_HOME, KEY_ONOFF = 4, 5, 6, 8
KEY_SHIFT, KEY_ALPHA, KEY_XNT = 12, 13, 14
KEY_VAR, KEY_TOOLBOX, KEY_BACKSPACE = 15, 16, 17
KEY_EXP, KEY_LN, KEY_LOG = 18, 19, 20
KEY_IMAGINARY, KEY_COMMA, KEY_POWER = 21, 22, 23
KEY_SINE, KEY_COSINE, KEY_TANGENT = 24, 25, 26
KEY_PI, KEY_SQRT, KEY_SQUARE = 27, 28, 29

KEY_SEVEN, KEY_EIGHT, KEY_NINE = 30, 31, 32
KEY_LEFTPARENTHESIS, KEY_RIGHTPARENTHESIS = 33, 34
KEY_FOUR, KEY_FIVE, KEY_SIX = 36, 37, 38
KEY_MULTIPLICATION, KEY_DIVISION = 39, 40
KEY_ONE, KEY_TWO, KEY_THREE = 42, 43, 44
KEY_PLUS, KEY_MINUS = 45, 46
KEY_ZERO, KEY_DOT, KEY_EE = 48, 49, 50
KEY_ANS, KEY_EXE = 51, 52


liste_touches_convertisseur = (
    K_LEFT, K_UP, K_DOWN, K_RIGHT,
    K_RETURN, K_ESCAPE, *(None,)*6,
    K_r, K_t, K_y,
    K_u, K_i, K_BACKSPACE,
    K_f, K_g, K_h,
    K_j, K_k, K_l,
    K_c, K_v, K_b,
    K_n, K_COMMA, K_SEMICOLON,
    
    K_KP7, K_KP8, K_KP9,
    K_LEFTPAREN, K_RIGHTPAREN, None,
    K_KP4, K_KP5, K_KP6,
    K_KP_MULTIPLY, K_KP_DIVIDE, None,
    K_KP1, K_KP2, K_KP3,
    K_KP_PLUS, K_KP_MINUS, None,
    K_KP0, K_KP_PERIOD, K_COLON,
    K_EXCLAIM, K_KP_ENTER
    )

def keydown(k):
    for ev in get():
        if ev.type == QUIT:
            quit()
    return get_pressed()[liste_touches_convertisseur[k]]
