#Rakshak Adhikari 03-14-21
#Plots Maximum Velocity Profiles from fof output


import h5py
import numpy as np
import matplotlib.pyplot as plt


file = h5py.File('fof_subhalo_tab_005.hdf5', 'r')

#print((file.keys()))



Subhalo=file.get('Subhalo') #Subhalo is the group, SubhaloVMas is the dataset inside the group
SubhaloVMax=np.array(Subhalo['SubhaloVmax']) #km/s

#for naming the plot properly
name=str(file)
snap_num=name[28:31]
#Get Redshift, boxsize, n_particle
Redshift="{:.2e}".format(file['Header'].attrs['Redshift'])
Boxsize=int((file['Header'].attrs['BoxSize']))


#Take Absolute Values of the velocities

MaxVel=[]
AbsVel=0
for i in range(0,len(SubhaloVMax)):
    AbsVel=np.absolute(SubhaloVMax[i])
    MaxVel.append(AbsVel)





#Gotta Create a maximum velocity bin

a=0.5*min(MaxVel)
MaxVel_Bin=[]
while a<max(MaxVel):
    MaxVel_Bin.append(a)
    a=np.power(a,1.01)+a/5
    print(a)

print('Maximum Velocity_cdm bin created sucessfully')
print(MaxVel_Bin)
print('Its length is')
print(len(MaxVel_Bin))

#Doing the magic here

N_halo=[]
i=0
k=0
for i in range(0,len(MaxVel_Bin)):
    TempArray=[]
    for k in range(0,len(MaxVel)):
            if MaxVel[k]> MaxVel_Bin[i]:
                TempArray.append(MaxVel)

    N_halo.append(len(TempArray))
        
                




#plot Stuff
       
fig,ax=plt.subplots()
ax.plot(MaxVel_Bin, N_halo)


plt.yscale("log")
plt.xscale("log")

plt.grid(True, which="both", ls="-")



plt.title("Max Velocity Distribution for snap "+snap_num+' z= '+Redshift)
plt.xlabel("Maximum Velocity (Km/s)")
plt.ylabel("Halo Number")
#plt.legend()
plt.show()
output_filename = 'MaxVelocityProfile_L'+str(Boxsize)+snap_num + '.png'

plt.savefig(output_filename)


















