from vehicules.velo import Velo
from vehicules.trottinette import Trottinette

v1 = Velo("Bleu", False)
v1.accelerer()
v1.accelerer()
print(v1)
v1.ralentir()
print(v1)

print("\n" + "-"*50 + "\n")

v2 = Velo("Vert", True)
v2.installer_porte_bagage()
print(v2)

print("\n" + "-"*50 + "\n")

t1 = Trottinette("Orange", True)
print(t1.est_arrete())

print(t1)
