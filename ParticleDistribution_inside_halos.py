#Rakshak Adhikari 03-19-21
#Plots particle Distributions inside halos
#needs fof file as well as the snapshot
#specify the halo you want to look into(0 being the largest)

import h5py
import numpy as np
import matplotlib.pyplot as plt


fof = h5py.File('fof_subhalo_tab_005.hdf5', 'r')
snap = h5py.File('snap_030821_2CDM_005.hdf5', 'r')

#Get Redshift, boxsize, n_particle
Redshift="{:.2e}".format(fof['Header'].attrs['Redshift'])
Boxsize=int((fof['Header'].attrs['BoxSize']))

Subhalo=fof.get('Subhalo')

Subhalo_CM=np.array(Subhalo['SubhaloCM'])
Subhalo_Radius=np.array(Subhalo['SubhaloHalfmassRad'])

DM=snap.get('PartType1')
DMpos=np.array(DM['Coordinates'])
DMvel=np.array(DM['Velocities'])

vx = DMvel[:,0]
vy = DMvel[:,1]
vz = DMvel[:,2]


x = DMpos[:,0]
y = DMpos[:,1]
z = DMpos[:,2]

COM_x_array=Subhalo_CM[:,0]
COM_y_array=Subhalo_CM[:,1]
COM_z_array=Subhalo_CM[:,2]

halos=[0,1,2,3,5,8,9,15]
halo_size=0
for halo_size in halos:

    Radius=Subhalo_Radius[halo_size]
    COM_x=COM_x_array[halo_size]
    COM_y=COM_y_array[halo_size]
    COM_z=COM_z_array[halo_size]

    
    distance=0
    Velocity=[]  #This Will be the list of all the (absolute) velocity values
    Absolutevelocity=0
    print('lenght of dmpos',len(DMpos))
    i=0
    for i in range(0,len(x)):
        distance=((COM_x-x[i])**2+(COM_y-y[i])**2+(COM_z-z[i])**2)**0.5
        if distance<Radius:
                Absolutevelocity=(vx[i]**2+vy[i]**2+vz[i]**2)**0.5
                #print('absvel=',Absolutevelocity)
                Velocity.append(Absolutevelocity)

    numberofparticles=len(Velocity)


    #make a bin for the velocity
    v_min=0.5*min(Velocity)
    v_max=max(Velocity)
    Bin1=[]
    v=0
    i=0
    while v<v_max:
        v=np.power(1.08,i)*v_min
        i=i+1
        #print(v)
        Bin1.append(v)


    #print('Bin',Bin1)



    #############Here we calculate the velocity distribution


    Vdistribution1=[]        #This the the thing that we shall plot along the bin
    i=0
    for i in range(0, len(Bin1)):
        j=0
        Temp=[] #This is the temporary array the length of which will give us the number of particles with velocities in the range
        for j in range(0,len(Velocity)):
            if Velocity[j]>Bin1[i]:
                if Velocity[j]<Bin1[i+1]:
                    Temp.append(Velocity[j])
                    #print(Velocity[j], 'is greater than',Bin1[i],'and less than',Bin1[i+1])
                    #print('Secondary iteration, j=',j)
                           
                           
        Vdistribution1.append(len(Temp))
        

    #print(Vdistribution1)
          
    fig,ax=plt.subplots()
    ax.plot(Bin1, Vdistribution1)

    fig.suptitle('Distribution inside Halo 2CDM L'+str(Boxsize)+' z='+str(Redshift) , fontsize=14, fontweight='bold')



    plt.yscale("log")
    plt.xscale("log")

    plt.grid(True, which="both", ls="-")

    #ax.set_xticks([10,20,30,40,50])
    #ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())


    plt.title("Radius ="+str(round(Radius, 3))+"#particles="+str(numberofparticles)+'COMx= '+str(round(COM_x,3)),fontsize=8)
    plt.xlabel("Velocity (km/sec)")
    plt.ylabel("Halo Number")
    plt.legend()
    #plt.show()
    output_filename = 'Particle_distribution_inside_halo_L'+str(Boxsize)+'#'+str(numberofparticles) + '.png'

    print(output_filename)
    plt.savefig(output_filename)
    #plt.show()
