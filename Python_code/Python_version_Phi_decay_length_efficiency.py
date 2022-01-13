import matplotlib.pyplot as plt
# plt.rcParams['text.usetex'] = True
import numpy as np

values =np.array([[0.0023,0.0010,0.0004,0.0005,0.0006,0.0009,0.0003],
[0.0810,0.0313,0.0139,0.0084,0.0064,0.0060,0.0047],
[0.6883,0.3415,0.1717,0.1082,0.0714,0.0518,0.0454],
[0.9923,0.9335,0.8016,0.6490,0.4878,0.3676,0.2806],
[0.9999,0.9993,0.9952,0.9855,0.9659,0.9323,0.8833],
[1.0,1.0,1.0,1.0,1.0,1.0,1.0]])

chi_t_mass = [500,750,1000,1250,1500,1750,2000]
phi_mass = [0.5,0.75,1.0,1.25,1.5,2.0]

X, Y = np.meshgrid(chi_t_mass, phi_mass)

t_levels = np.linspace(0,1,101)

# for i, enum in enumerate(t_levels):
# 	if enum == 0.9: print(i)

fig, ax = plt.subplots()
im = plt.contourf(X,Y,values, levels=t_levels)
im1 = plt.contour(X,Y,values, levels=t_levels)
fig.colorbar(im)

v=[0.9,0.5,0.1]

manual_locations = [(1800,1.1), (1400,1.3), (1700,1.7)]

labels = plt.clabel(im, v, fontsize=15, colors='black', inline_spacing=10, manual=manual_locations)

for l in labels:
	l.set_rotation(0)

im1.collections[10].set_color('red')
im1.collections[10].set_linestyle('dashed')
im1.collections[10].set_linewidth(2)
# im1.collections[10].set_rotation(0)
im1.collections[50].set_color('red')
im1.collections[50].set_linestyle('dashed')
im1.collections[50].set_linewidth(2)
im1.collections[90].set_color('red')
im1.collections[90].set_linestyle('dashed')
im1.collections[90].set_linewidth(2)

plt.xlabel(r'$\chi_{t}$ Mass (GeV)')
plt.ylabel(r'$\phi$ Mass (MeV)')
plt.title(r'$\phi$ Decay Length Efficiency')


plt.show()