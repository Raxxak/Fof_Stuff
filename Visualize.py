import os
from numpy import *

from pylab import *
import matplotlib.pyplot as plt

from matplotlib.colors import LogNorm

import h5py
snap = h5py.File('snap_022121_2CDM_005.hdf5', 'r')

#Get Redshift, boxsize, n_particle


DM1=snap.get('PartType1')
Gas=snap.get('PartType0')
DMpos1=np.array(DM1['Coordinates'])
Gaspos=np.array(Gas['Coordinates'])

x1 = DMpos1[:,0]
y1 = DMpos1[:,1]
z1 = DMpos1[:,2]

x0 = Gaspos[:,0]
y0 = Gaspos[:,1]
z0 = Gaspos[:,2]

#plotting
fig = plt.figure(figsize=(10,10))
plt.style.use('dark_background')


ax = plt.axes(projection='3d')



fig.patch.set_facecolor('white')

ax.set_xlabel(r'$x$',fontsize=20)
ax.set_ylabel(r'$y$',fontsize=23)

ax.plot3D(x1,y1,z1,'o', color='crimson',markersize=0.2 ,alpha=0.4)
ax.plot3D(x0,y0,z0,'o', color='green',markersize=0.2 ,alpha=0.1)

print(dir)
print(snap)




plt.show()



