"""
@name rendu monnaie.py
@author Aélion
@version 0.0.1
A poor coins counter
Use // to get an integer division
Use % to get rest of int div
Use input () function to get a user entry 
print ("la machine vous donne",billet100, "les billets de 100",billet50, "les billets de 50", billet20, "les billets de 20", billet10 "les billets de 10", billet5,"les billets de 5", piece2, "les pieces de 2")
"""
# Accept an amount entry
somme = 2000
billet100 = somme // 100
reste100 = somme % 100
billet50 = reste100 // 50
reste50 = reste100 % 50
billet20 = reste50 // 20
reste20 = reste50 % 20
billet10 = reste20 // 10
reste10 = reste20 % 10
billet5 = reste10 // 5
reste5 = reste10 % 5
piece2 = reste5 // 2
reste2 = piece2 % 2

if reste100 > 0:
    print ("La machine vous donne", billet100, "les billets de 100")
else:
    print ()
if reste50 > 0:
    print ("La machine vous donne", billet50, "les billets de 50")
else:
    print()
if reste20 > 0:
    print ("La machine vous donne", billet20, "les billets de 20")
else:
    print ()
if reste10 > 0:
    print ("La machine vous donne", billet10, "les billets de 10")
else:
    print ()
if reste10 > 0:
    print ("La machine vous donne", billet5, "Les billets de 5")
else:
    print ()
if reste5 > 0:
    print ("La machine vous donne",billet5, "les billets de 5")
else:
    print ()
if reste2 > 0:
    print ("La machine vous donne",piece2, "les pieces de 2")
else:
    print ()
