H = 1.00784
He = 4.2026
Li = 6.9410
Be = 9.0121
B = 10.811
C = 12.0107
N = 14.0067
O = 15.9994
F = 18.9984
Ne = 20.1797
Na = 22.9897
Mg = 24.3050
Al = 26.9815
Si = 28.0855
P = 30.9737
S = 32.065
Cl = 35.453
Ar = 39.948
K = 39.0983
Ca = 40.078
Sc = 44.9559
Ti = 47.867
V = 50.9415
Cr = 51.9961
Mn = 54.9380
Fe = 55.845
Co = 58.9331
Ni = 58.6934
Cu = 63.546
Zn = 65.38
Ga = 69.723
Ge = 72.64
As = 74.9216
Se = 78.96
Br = 79.904
Kr = 83.798
Rb = 85.467
Sr = 87.62
Y = 88.905
Zr = 91.224
Nb = 92.906
Mo = 95.94
Tc = 98.906
Ru = 101.07
Rh = 102.905
Pd = 106.42
Ag = 107.868
Cd = 112.411
In = 114.818
Sn = 118.710
Sb = 121.760
Te = 127.60
I = 126.904
Xe = 131.293
Cs = 132.905
Ba = 137.327
La = 138.905
Ce = 140.116
Pr = 140.904
Nd = 144.242
Pm = 144.912
Sm = 150.36
Eu = 151.964
Gd = 157.25
Tb = 158.925
Dy = 162.500
Ho = 164.93
Er = 167.259
Tm = 168.934
Yb = 173.04
Lu = 174.967
Hf = 178.49
Ta = 180.947
W  = 83.84
Re = 186.207
Os = 190.23
Ir = 192.217
Pt = 195.084
Au = 196.966
Hg = 200.59
Tl = 204.383
Pb = 207.2
Bi = 208.9804
Po = 208.9824
At = 209.9871
Rn = 222.0176
Fr = 223.0197
Ra = 226.0254
Ac = 227.0278
Th = 232.0380
Pa = 231.0358
U  = 238.0289
Np = 237.0482
Pu = 244.0642
Am = 243.0614
Cm = 247.0703
Bk = 247.0703
Cf = 251.0796
Es = 252.0829
Fm = 257.0951
Md = 258.0951
No = 259.1009
Lr = 266.1193
Rf = 261.1087
Db = 262.1138
Sg = 263.1182
Bh = 262.1229
Hs = 269
Mt = 278
Ds = 281.1620
Rg = 281.1684
Cn = 285.1744
Nh = 286.1810
Fl = 287.1904
Mc = 288.1943
Lv = 291.2045
Ts = 294.2104
Og = 294.2139
Uue = 316
Ubn = 320
Ubu = 320
Ubb = 321
Ubt = 325
Ubq = 330
Ubp = 332
Ubh = 334
Ubs = 335






"""
elementoUm = input('Digite o primeiro elemento: ')


vezesUm = input('Digite quantas vezes ele aparece na fórmula molecular: ')


numero_2 = input('Digite o segundo elemento: ')


vezes_2 = input('Digite quantas vezes ele aparece na fórmula molecular: ')


continuar = input('Tem mais algum elemento: ')


if continuar: "Não"


resultado_conta1 = (float(elementoUm)*float(vezesUm)+float(numero_2)*float(vezes_2))


print("Massa molar:") 


input(float(resultado_conta1))


print ('g/mol')


imput("Pressione ENTER para continuar")
"""
"""
numero_1= input('Digite o primeiro elemento: ')
vezes_1= input('Digite quantas vezes ele aparece na fórmula molecular: ')
numero_2= input('Digite o segundo elemento: ')
vezes_2= input('Digite quantas vezes ele aparece na fórmula molecular: ')
continuar = input('Tem mais algum elemento: ')
if continuar: "Não"
resultado_conta1= float("numero_1")*float("vezes_1")+float("numero_2")*float("vezes_2")
print("Massa molar:") 
input(float(resultado_conta1))
print ('g/mol')

if continuar: "Sim"
numero_3= input('Digite o terceiro elemento: ')
vezes_3= input('Digite quantas vezes ele aparece na fórmula molecular: ')
continuar = input('Tem mais algum elemento: ')
if continuar: "Não"
resultado_conta2 = (numero_1*vezes_1+numero_2*vezes_2+numero_3*vezes_3)
print("Massa molar:") 
input(resultado_conta2)
print ('g/mol')

if continuar: "Sim"
numero_4= input('Digite o quarto elemento: ')
vezes_4= input('Digite quantas vezes ele aparece na fórmula molecular: ')
continuar = input('Tem mais algum elemento(Sim/Não): ')
if continuar: "Não"
resultado_conta3= numero_1*vezes_1+numero_2*vezes_2+numero_3*vezes_3+numero_4*vezes_4
print("Massa molar:") 
input(resultado_conta3)
print ('g/mol')

if continuar: "Sim"
numero_5= input('Digite o quinto elemento: ')
vezes_5= input('Digite quantas vezes ele aparece na fórmula molecular: ')
continuar = input('Tem mais algum elemento: ')
if continuar: "Não"
resultado_conta4 = numero_1*vezes_1+numero_2*vezes_2+numero_3*vezes_3+numero_4*vezes_4+numero_5*vezes_5
print("Massa molar:") 
input(resultado_conta4)
print ('g/mol')
"""
