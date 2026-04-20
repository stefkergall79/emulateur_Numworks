# Émulateur Numworks
Émuler n'importe quel script Python prévu pour [Numworks](https://www.numworks.com/fr/) sur votre PC, directement via l'application python.

**ATTENTION ! Vous avez besoin du module `pygame` sur votre PC pour faire fonctionner ce dépôt !**

Clonez ce dépôt sur votre PC (`git clone https://github.com/stefkergall79/emulateur_Numworks.git`) et ajoutez-y votre script Python prévu pour Numworks. Vous aurez une Numworks en grand écran et avec un clavier qui fonctionne, bien que peu intuitif.

Dans ce projet  :
 - deux scripts Python `kandinsky.py` et `ion.py`, qui permettent d'émuler les modules du même nom sur les calculatrices Numworks.
   - `kandinsky` est (beaucoup) plus lent que sur Numworks.
   - `ion` est assez complexe à utiliser, voir les correspondances entre les touches Numworks et celles de votre PC dans le code source.
 - une icône `.bmp` de Numworks pour l'image d'application.
 - une fonte `.bdf` monospacée 10×18, comme celle de Numworks. Elle est très moche, faîtes un ticket si vous en avez une autre avec les même spécifications.

Grâce à ce projet, j'ai pu coder sur mon PC le [Mémoire44 pour Numworks](https://my.numworks.com/python/memoire44) !
