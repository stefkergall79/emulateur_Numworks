# Jouer au jeu de société Mémoire44 sur Numworks
# contre un ami est désormais possible !
# Développeur : Stéphane Kergall, 02/03/2026

D = {"Pegasus Bridge":     "b01_pegasus",
     "Sainte-Mère-ᴇ́glise": "b02_stemere",
     "Sword Beach":        "b03_swordbeach",
     "Pointe-du-Hoc":      "b04_pointe_hoc",
     "Omaha Beach":        "b05_omahabeach",
     "Mont Mouchet":       "b06_montmouchet",
     "Vassieux, Vercors":  "b07_vassieux",
     "Opération Cobra":    "b08_cobra",
     "Opération Lüttich":  "b09_luttich",
     "Toulon":             "b10_toulon",
     "Libération de Paris":"b11_paris",
     "Montélimar":         "b12_montelimar",
     "Arnhem Bridge":      "b13_arnhem",
     "Arracourt":          "b14_arracourt",
     "Saint-Vith":         "b15_stvith",
     "Trouée de Saverne":  "b16_saverne",
     
}

L = sorted(D, key=D.get)

from kandinsky2 import *

ch = True
ind_scen = 0
mx = 8
fill(cm44)
fill_rect(114,9,71,20,"white")
fill_rect(185,9,21,20,"red")
draw_string("Mᴇ́MOIRE",115,10,"white",cm44)
draw_string("44",185,10,"red","white")    
draw_string("Choisissez votre scénario :", 15, 30, "black", cm44)

while not O():
  if ch:
    st = (ind_scen//mx)*mx + mx
    if ind_scen >= ((len(L)-1)//mx)*mx:
      st = len(L)
    fill_rect(15, 60, 305, 182, cm44)
    draw_selection_string(L[(ind_scen//mx)*mx:st],
                          15, 60, "black", cm44, ind_scen%mx)
    ch = 0
    sleep(0.2)
  
  ch = changed_selected(ind_scen, len(L)-1)
  ind_scen += ch

try:
  aff_tuto = keydown(4)
  from a2_tutoriel import *
except:
  aff_tuto = False

exec("from " + D[L[ind_scen]] + " import *")

for ii in range(9):
  for ji in range(13 - ii%2):
    if not tabl_terr[ii][ji]:
      if cote == "plage":
        if ii < 4: tabl_terr[ii][ji] = h
        elif ii > 6: tabl_terr[ii][ji] = m
        else: tabl_terr[ii][ji] = s
      else:
        tabl_terr[ii][ji] = h

def x_in(po):
  return X_dep + 11*(po[0]%2) + 22*po[1]
def y_in(po):
  return Y_dep + 20*po[0] + 7
def pos(po):
  return x_in(po), y_in(po)

pio=["Embuscade", "Action héroïque", "Combat rapproché", "Fusillade", "Infiltration",
     "Tir d'artillerie", "Médecins et mécaniciens", "Tir de barrage", "Encerclement(2)",
     "Attaque aérienne", "Consolidation de position", "Attaque frontale(2)", "Accrochage centre(2)"]
pio+=["Contre-attaque", "Ordre du QG", "Assaut de blindés", "Assaut d'infanterie",
      "À l'assaut", "Reconnaissance gauche(1)", "Reconnaissance droite(1)", "Assaut centre(tout)",
      "Reconnaissance centre(1)", "Assaut gauche(tout)", "Assaut droite(tout)"]*2
pio+=["Reconnaissance en force(1)", "Attaque gauche(3)", "Attaque droite(3)"]*3
pio+=["Attaque centre(3)", "Accrochage gauche(2)", "Accrochage droite(2)", "Accrochage centre(2)"]*4
defausse=[]

def put_card(ch):
    ca = choice(pio)
    ch.append(ca)
    pio.remove(ca)

def is_reco(ca):
  return ca[0] == 'R' and len(ca) == 24

class P:
    def __init__(self, col, nom, nbc, key, yd, ym):
        self.col = col
        self.nom = nom
        self.nbc = nbc
        self.key = key
        self.y_dep, self.y_med = yd, ym
        self.med = 0
        self.jeu = []
        for i in range(self.nbc):
          put_card(self.jeu)


    def jouer_carte(self):
      fill("white")
      nb_spaces = 16 - len(self.nom)//2
      name_plr = " "*nb_spaces + self.nom + " "*nb_spaces
      draw_string(name_plr, -5* (len(self.nom)%2), 5,
                  "white", self.col)
      
      ind_card = 0
      ch = True
      
      while not S():
        if ch:
          cur_card = self.jeu[ind_card]
          draw_selection_string(self.jeu, 15, 35,
                                "black", "white", ind_card)
          ch = 0
          sleep(0.1)

        ch = changed_selected(ind_card, self.nbc - 1)
        ind_card += ch
      
      if O():
        self.jeu.remove(cur_card)
        defausse.append(cur_card)
        
        if is_reco(cur_card) or (is_reco(cajo) and cur_card == "Contre-attaque"):
          choix = []
          for ii in range(2):
            put_card(choix)
          ind_card = 0
          ch = True
          while O(): pass
          fill("white")
          draw_string("Choisissez la nouvelle carte :", 10, 20)
          
          while not O():
            if ch:
              draw_selection_string(choix, 15, 70,
                                    "black", "white", ind_card)
              ch = 0

            ch = changed_selected(ind_card, 1)
            ind_card += ch

          self.jeu.append(choix[ind_card])
          defausse.append(choix[not ind_card])
          
        else:
          put_card(self.jeu)
        return C(self, cur_card)
      
      return cajo


D = {
  'l': P((0, 60, 0), "Alliés", nb_l, 15, 11, 192),
  'x': P((80, 80, 200), "Allemands", nb_x, 14, 24, -6)
}

class C:
  def __init__(self, plr, nom = None):
    self.text = nom if nom else plr.nom
    self.plr = plr
    self.y = 205*(self.plr is D['l'])
    self.y_dep = plr.y_dep
  
  def __str__(self): return self.text
  def __eq__(self, other): return self.text == other
  def __getitem__(self, key): return self.text[key]
  def __len__(self): return len(self.text)
  
  def aff(self):
    if aff_tuto:
      draw_string("Tuto →", 218, self.y)
      draw_string("Ans", 285, self.y, "white", cm44)
    draw_string(self.text, 0, self.y, self.plr.col)

cajo = C(D[first])
X_dep, Y_dep = 1, cajo.y_dep
sel = [4, 6]

def un_cur(se = sel):
  return tabl_unit[se[0]][se[1]]
def ter_cur(se = sel):
  return tabl_terr[se[0]][se[1]]

def aff_medailles():
  for plr in D.values():
    for ii in range(med_vic):
      for ee in ((5, "black"),
                 (4, plr.col if plr.med > ii else "white")):
        fill_circle(X_dep + 10 + 30*ii, Y_dep + plr.y_med, *ee)

def draw_hex(xx,yy,col):
  fill_rect(xx, yy, 1, 13, col)
  draw_line(xx, yy-1, xx+13, yy-9, col)
  draw_line(xx+11, yy-7, xx+23, yy, col)
  fill_rect(xx+22, yy, 1, 14, col)
  draw_line(xx+10, yy+19, xx+23, yy+11, col)
  draw_line(xx, yy+13, xx+10, yy+19, col)

def plateau():
  for yy in range(5):
    for xx in range(13):
      draw_hex(22*xx+X_dep, 40*yy+Y_dep+7, "black")
  for yy in range(4):
    for xx in range(13):
      fill_rect(x_in((0, xx)) + 11, Y_dep + 40*yy + 27,
                1, 13, "black")

def fill_hex(xx,yy,col):
  fill_rect(xx+1 , yy, 21, 14, col)
  for ii in (
    (2, -1, 19),
    (4, -2, 16),
    (4, -3, 14),
    (6, -4, 10),
    (8, -5, 6),
    (10, -6, 2),
    (3, 14, 17),
    (5, 15, 14),
    (6, 16, 11),
    (8, 17, 8),
    (10, 18, 4)):
    fill_rect(xx + ii[0], yy + ii[1],
              ii[2], 1, col)


def terrains():
  if cote == "plage":
    for ii in (0,84,h), (84,59,s), (143,44,m):
      fill_rect(X_dep, Y_dep+ii[0], 287, *ii[1:])
  else:
    fill_rect(X_dep,Y_dep,287,187,h)

  for ii in range(9):
    li = tabl_terr[ii]
    yy = y_in([ii])
    for ji in range(len(li)):
      if li[ji] not in [h, s , m]:
        fill_hex(x_in([ii, ji]), yy, li[ji])
  for bu in bunkers:
    fill_rect(x_in(bu) + 1, y_in(bu),
              21, 13, v)

def sacasable(sa):
  dir = (sa[2] == 'x')*2 - 1
  pts = ((2, 6 + 6*dir, 10, 6 + 11*dir),
         (10, 6 + 11*dir, 21, 6 + 5*dir))
  xx, yy = pos(sa)
  
  for ii in pts:
    for jj in range(2):
      draw_line(xx + ii[0], yy + ii[1] - jj*dir,
                xx + ii[2], yy + ii[3] - jj*dir,
                D[sa[2]].col)

def barble(ba):
  xx, yy = pos(ba)
  for ji in range(3,19,5):
    fill_rect(xx + ji, yy, 1, 13, D['x'].col)

def antich(an):
  xx, yy = pos(an)
  fill_rect(xx+9, yy, 2, 13, D['x'].col)
  draw_line(xx+5, yy+1, xx+18, yy+11, D['x'].col)
  draw_line(xx+3, yy+10, xx+15, yy+3, D['x'].col)

def objectif(ob):
  fill_circle(x_in(ob) + 11,
              y_in(ob) + 13 - (ob[2] == 'x')*12,
              3, D[ob[2]].col)

def obstacles():
  for sa in sbl: sacasable(sa)
  try:
    for an in ant : antich(an)
  except: pass
  for ba in brb: barble(ba)
  for ob in obj: objectif(ob)

def draw_unit(ii,jj):
  col_place = tabl_terr[ii][jj]
  for bu in bunkers:
    if bu == [ii, jj]: col_place = v
  
  un = tabl_unit[ii][jj]
  draw_string(un[:2], x_in((ii, jj)) + 1, y_in([ii]) -2,
              D[un[2]].col, col_place)

def unites():
  for ii in range(9):
    li = tabl_unit[ii]
    for ji in range(len(li)):
      if li[ji] != False:
        draw_unit(ii,ji)
  obstacles()
  aff_medailles()

def draw_hex2(xx,yy,col):
  fill_rect(xx+1, yy, 1, 14, col)
  fill_rect(xx+21, yy+1, 1, 12, col)
  draw_line(xx+1, yy, xx+13, yy-8, col)
  draw_line(xx+11, yy-6, xx+22, yy+1, col)
  draw_line(xx+10, yy+18, xx+22, yy+10, col)
  draw_line(xx+1, yy+12, xx+10, yy+18, col)

def select(aj, po, col):
  for co in [[ter_cur(), "black"],
              [col]*2]:
    xx, yy = pos(sel)
    draw_hex2(xx, yy, co[0])
    draw_hex(xx, yy, co[1])
    if co != [col]*2: sel[po] += aj
  for ii in (88, 198):
    fill_rect(X_dep+ii, Y_dep, 1, 187, "red")

def move(col):
  for ii in [1,0,-1],[2,8,1]:
    if keydown(ii[0]) and sel[0] != ii[1]:
      if sel[1] == 12: select(-1,1,col)
      select(ii[2],0,col)
      sleep(0.1)
  
  for ii in [[3, 1, 12 - sel[0]%2],
             [0, -1, 0]]:
    if keydown(ii[0]) and sel[1] != ii[2]:
      select(ii[1],1,col)
      sleep(0.1)

def affichage():
  fill("white")
  terrains()
  cajo.aff()
  unites()
  plateau()
  select(0,0,"blue")
affichage()

def press_a_number(lst_k):
  prs = -1
  while not keydown(17) and prs < 0:
    for ki in range(len(lst_k)):
      if keydown(lst_k[ki]):
        prs = ki
  while any(map(keydown, [17]+lst_k)): pass
  return prs if prs >= 0 else 0

def tirer_des():
  fill_rect(X_dep+298, 0, 20, 160, "white")
  nbd = press_a_number([48,42,43,44,36,37,38])
  for ii in range(nbd):
    fill_rect(X_dep+298, Y_dep+3+ii*25, 15, 15,
              choice(["blue"]*2 + ["black","orange","green",'purple']))


#Programme principal.
while all(D[p].med < med_vic for p in D):
  if L[ind_scen] == "Sainte-Mère-ᴇ́glise" and len(pio) < 2:
    D['x'].med = med_vic
  
  if (len(pio) < 2 or cajo == "Action héroïque") and L[ind_scen] != "Sainte-Mère-ᴇ́glise":
    pio.extend(defausse)
    defausse.clear()
  
  for plr in D.values():
    if keydown(plr.key):
      cajo = plr.jouer_carte()
      Y_dep = cajo.y_dep
      affichage()
  
  move("blue")
  
  if keydown(39) and aff_tuto:
    aff_tuto = False
    fill_rect(218, cajo.y, 102, 18, "white")
    cajo.aff()
    aff_medailles()
  
  elif keydown(51):
    try:
      ans_pressed()
      affichage()
    except: pass
  
  elif keydown(22) and un_cur() != 0:
    ini = sel.copy()
    select(0,0, (0,250,0))
    while keydown(22): pass
    while not keydown(22) and not keydown(17):
      move((0, 250, 0))
    if keydown(22) and ini != sel and un_cur() == False:
      tabl_unit[sel[0]][sel[1]] = un_cur(ini)
      tabl_unit[ini[0]][ini[1]] = False
      xx, yy = pos(ini)
      fill_hex(xx,yy,ter_cur(ini))
      draw_hex(xx,yy,"black")
      
      for bu in bunkers:
        if bu == ini:
          fill_rect(xx+1,yy,21,13,v)
      draw_unit(*sel)
      
      for sa in sbl:
        if sa[:2] == ini:
          sbl.remove(sa)
    obstacles()
    select(0,0,"blue")
    while keydown(22): pass
  
  elif keydown(19) and un_cur():
    select(0,0,"red")
    tirer_des()
    
    if not keydown(17):
      rest_unit = int(un_cur()[0]) - press_a_number([48,42,43,44,36])
      
      if rest_unit > 0:
        tabl_unit[sel[0]][sel[1]] = str(rest_unit) + un_cur()[1:]
        draw_unit(*sel)
      
      else:
        unit = un_cur()
        tabl_unit[sel[0]][sel[1]] = False
        xx, yy = pos(sel)
        fill_hex(xx, yy, ter_cur())
        
        for sa in sbl:
          if sa[:2] == sel:
            sbl.remove(sa)
        for bu in bunkers:
          if sel == bu:
            fill_rect(xx+1,yy,21,13,v)
        
        if unit[2] == 'x':
          D['l'].med += 1 + (unit[1] == 't' and ind_scen == 5)
        else:
          D['x'].med += 1
        aff_medailles()
      
      obstacles()
    select(0,0,"blue")
  
  elif keydown(21) and un_cur() and int(un_cur()[0]) < 4:
    select(0,0,"white")
    tirer_des()
    
    if not keydown(17):
      add_unit = press_a_number([48,42,43,44])
      tabl_unit[sel[0]][sel[1]] = str(int(un_cur()[0]) + add_unit) + un_cur()[1:]
      draw_unit(*sel)
      obstacles()
    select(0,0,"blue")
  
  elif keydown(20):
    tirer_des()
  
  elif keydown(25):
    ba = list(sel)
    if ba in brb:
      brb.remove(ba)
      fill_hex(x_in(sel), y_in(sel), ter_cur())
      if un_cur(): draw_unit(*sel)
      select(0,0,"blue")
    else:
      brb.append(ba)
    obstacles()
    while keydown(25): pass
  
  elif keydown(26):
    suppr = False
    for char in D:
      sa = sel + [char]
      if sa in sbl:
        sbl.remove(sa)
        fill_hex(x_in(sel), y_in(sel), ter_cur())
        if un_cur(): draw_unit(*sel)
        select(0,0,"blue")
        suppr = True

    if not suppr:
      sa = sel + ['l' if Y_dep == 11 else 'x']
      sbl.append(sa)
    
    obstacles()
    while keydown(26): pass
  
  if keydown(27):
    fill("white")
    draw_string("Règles Spéciales", 80, 5, "white",cm44)
    draw_multilines_string(regles_spe, 5, 30, 31)
    while not S(): pass
    affichage()
  
  elif keydown(28):
    add_med = True
    for plr in D:
      ob = sel + [plr]
      
      if ob in obj:
        obj.remove(ob)
        D[plr].med += 1
        xx, yy = pos(ob)
        fill_hex(xx, yy, ter_cur(ob))
        draw_hex(xx, yy, "black")
        for bu in bunkers:
          if ob[:2] == bu:
            fill_rect(xx+1, yy, 21, 13, v)
        if un_cur(ob):
          draw_unit(*ob[:2])
        select(0,0,"blue")
        add_med = False
    
    if add_med:
      while not any(map(keydown, (14, 15, 17))): pass
      for plr in D:
        if keydown(D[plr].key) and D[plr].med > 0 :
          D[plr].med -= 1
          obj.append(sel + [plr])
    
    obstacles()
    aff_medailles()
    while any(map(keydown, (28, 14, 15))): pass

  elif keydown(29):
    fill("white")
    draw_string("Des commentaires ?",10,10)
    draw_string("écrivez-nous à l'adresse",10,40)
    draw_string("smkq@gmail.com",10,70,cm44)
    fill_rect(10, 86, 140, 1, cm44)
    draw_string("et suivez-nous sur",10,100)
    draw_string("les réseaux sociaux :",10,130)
    for ii in ("f", 10),("in", 50):
      draw_string(ii[0], ii[1], 160,"white","blue")
    while not S(): pass
    affichage()


for plr in D.values():
  if plr.med >= med_vic:
    fill(plr.col)
    w = "VICTOIRE DES " + plr.nom + " !"
    draw_string(w, 160 - 5*len(w), 105,
                'white', plr.col)