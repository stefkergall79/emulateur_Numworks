from python_mieux import *
from kandinsky import *
from time import sleep

cm44 = (0,113,70)

def fill(c):
  fill_rect(0,0,320,222,c)

def fill_circle(x,y,r,c):
    r2 = r*r
    for dy in range(-r,r+1):
        dx = int((r2 - dy*dy)**0.5)
        fill_rect(x - dx, y + dy, 2 * dx + 1, 1, c)

def draw_line(x1,y1,x2,y2,c):
  width=x2-x1
  height=y2-y1
  if abs(width)>=abs(height):
    div=height/width
    for i in range(0,width,(width>0)*2-1):
      set_pixel(x1+i,y1+int(div*i+0.5),c)
  else:
    div=width/height
    for i in range(0,height,(height>0)*2-1):
      set_pixel(x1+int(div*i+0.5),y1+i,c)

def draw_multilines_string(string, x, y, w = 32, c = "black", b = "white"):
  liste_strings = chaine_divisee(string, w)
  
  for s in range(len(liste_strings)):
    draw_string(liste_strings[s], x, y + 20*s, c, b)
  return len(liste_strings)

def draw_selection_string(list_string, x, y, c, b, ind_sel):
  for s in range(len(list_string)):
    col = (b,c) if s == ind_sel else (c,b)
    draw_string(list_string[s], x, y + 30*s, *col)

def changed_selected(ind_sel, max):
  if keydown(KEY_UP) and ind_sel != 0:
    return -1
  elif keydown(KEY_DOWN) and ind_sel != max:
    return 1
  return 0