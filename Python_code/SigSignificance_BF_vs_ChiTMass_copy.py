import matplotlib.pyplot as plt
# plt.rcParams['text.usetex'] = True
import numpy as np
from matplotlib import ticker, cm

#The way the array values are arranged (top left value corresponds to 500,0.01, bottom right 2500,0.99, etc.):
#chi_t 500, BF 0.01                   chi_t 2500 BF 0.01
#
#
#chi_t 500, BF 0.99                   chi_t 2500 BF 0.99

#values =np.array([[25.60407913, 8.71877731, 2.52239284, 0.98588960, 0.39159647, 0.19192607, 0.07549218, 0.03271871, 0.02679423],
#[169.50486490, 77.67748700, 33.14208839, 15.40538446, 7.10920249, 3.65843474, 1.60957873, 0.73830251, 0.57779520],
#[241.61901627, 112.42926932, 50.04984544, 24.09798996, 11.63894813, 6.10569305, 2.84090735, 1.35188540, 1.02677797],
#[296.71094363, 138.79950822, 62.78387053, 30.67851972, 15.13881890, 8.02127703, 3.85616963, 1.88133736, 1.39985533],
#[341.33721493, 160.09359921, 73.00665495, 35.95539818, 17.95886110, 9.57183746, 4.69804894, 2.33234721, 1.71053289]])

values =np.array([[25.60407913, 8.71877731, 2.52239284, 0.98588960, 0.39159647, 0.19192607, 0.07549218, 0.03271871, 0.02679423],
[50.00000000, 50.00000000, 33.14208839, 15.40538446, 7.10920249, 3.65843474, 1.60957873, 0.73830251, 0.57779520],
[50.00000000, 50.00000000, 50.00000000, 24.09798996, 11.63894813, 6.10569305, 2.84090735, 1.35188540, 1.02677797],
[50.00000000, 50.00000000, 50.00000000, 30.67851972, 15.13881890, 8.02127703, 3.85616963, 1.88133736, 1.39985533],
[50.00000000, 50.00000000, 50.00000000, 35.95539818, 17.95886110, 9.57183746, 4.69804894, 2.33234721, 1.71053289]])

chi_t_mass = [500,750,1000,1250,1500,1750,2000,2250,2500]
Branching_Fraction = [0.01,0.25,0.5,0.75,0.99]

X, Y = np.meshgrid(chi_t_mass, Branching_Fraction)

t_levels1 = np.linspace(0,50,51)
t_levels2 = np.linspace(0,50,5001)

# for i, enum in enumerate(t_levels):
# 	if enum == 0.9: print(i)

fig, ax = plt.subplots()

im = plt.contourf(X,Y,values, levels=t_levels1, cmap=plt.cm.jet)
im1 = plt.contour(X,Y,values, levels=t_levels2, cmap=plt.cm.jet)

fig.colorbar(im)

#v=[0.9,0.5,0.1]

#manual_locations = [(1800,1.1), (1400,1.3), (1700,1.7)]

#labels = plt.clabel(im, v, fontsize=15, colors='black', inline_spacing=10, manual=manual_locations)

#for l in labels:
#	l.set_rotation(0)

#im1.collections[2].set_color('blue')
#im1.collections[2].set_linestyle('dashed')
#im1.collections[2].set_linewidth(2)

#for indx,elem in enumerate(t_levels):
#	if elem == 1.69:
#		print("1.69 is "+str(indx))
#	if elem == 3.00:
#		print("3.00 is "+str(indx))
#	if elem == 5.00:
#		print("5.00 is "+str(indx))

im1.collections[169].set_color('yellow')
im1.collections[169].set_linestyle('dashed')
im1.collections[169].set_linewidth(4) #linewidth was 2 previously
#im1.collections[169].set_linestyle((0,(5,1))) 
im1.collections[169].set_label('95% CL')

#sigma = 3 contour
im1.collections[300].set_color('red')
im1.collections[300].set_linestyle('dashed')
im1.collections[300].set_linewidth(4) #linewidth was 2 previously
#im1.collections[300].set_linestyle((0,(5,1))) 
im1.collections[300].set_label(r'3$\sigma$')

#sigma = 5 contour
im1.collections[500].set_color('lime')
im1.collections[500].set_linestyle('dashed')
im1.collections[500].set_linewidth(4)
im1.collections[500].set_label(r'5$\sigma$')

#fmt = {}
#strs = [r'$\sigma$ = 3', r'$\sigma$ = 5']
#strs = ['hello','howdy']
#for l, s in zip(im1.levels, strs):
#    fmt[l] = s

#ax.clabel(im1, im1.levels[6], inline=True, fmt='hello', fontsize=10)


plt.xlabel(r'm($T$) [GeV]')
plt.ylabel(r'Br($T\rightarrow Wb$)')
plt.title(r'Signal Significance', loc='right', rotation='90', x=1.3, y=0.25)
plt.legend(loc='upper left')

plt.show()