import h5py
import numpy as np
import matplotlib.pyplot as plt


file = h5py.File('fof_subhalo_tab_005.hdf5', 'r')

#print((file.keys()))

Subhalo=file.get('Subhalo')
SubhaloMass=np.array(Subhalo['SubhaloMass'])
SubhaloMass=10**10*SubhaloMass #converting to solar masses

#Get Redshift, boxsize, n_particle
Redshift="{:.2e}".format(file['Header'].attrs['Redshift'])
Boxsize=int((file['Header'].attrs['BoxSize']))





a=min(SubhaloMass)/2
Mass_Bins=[]
i=1
while a<max(SubhaloMass):
    Mass_Bins.append(a)
    a=np.power(2,i/2)*min(SubhaloMass)
    i=i+1

print('MassBins Created Sucesfully')
print(Mass_Bins)


i=0
j=0
N_halo=[]
for i in range(0,len(Mass_Bins)):
    array=[]
    for j in range(0,len(SubhaloMass)):
            if SubhaloMass[j]>Mass_Bins[i]:
                array.append(SubhaloMass[j])
    N_halo.append(len(array))        
    #MassBins.pop(0)


print('Here is the Number-of-halo Array:')
print(N_halo)


    #fig,ax=plt.subplots()
plt.rcParams["figure.figsize"] = (6,6)
plt.plot(Mass_Bins, N_halo)




plt.yscale("log")
plt.xscale("log")
plt.legend();


plt.grid(True, which="both", ls="-")




plt.title('Halo Mass Distribution L'+str(Boxsize)+', z= '+Redshift)
plt.xlabel("HaloMass ($M_{\odot}$)")
plt.ylabel("Halo Number")


output_filename=('Halo_Mass_Distribution_L'+str(Boxsize)+'_z_'+Redshift+'.png')
plt.savefig(output_filename)
plt.show()
file.close()

















