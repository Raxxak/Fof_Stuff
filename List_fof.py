import numpy as np
import h5py



file = 'fof_subhalo_tab_005.hdf5'


##################
def visitor_func(name, node):
    if isinstance(node, h5py.Group):
        print(node.name, 'is a Group')
    elif isinstance(node, h5py.Dataset):
       if (node.dtype == 'object') :
            print (node.name, 'is an object Dataset')
       else:
            print(node.name, 'is a Dataset')   
    else:
        print(node.name, 'is an unknown type')         
#################
        

h5f = h5py.File(file,'r')

h5f.visititems(visitor_func)   

h5f.close()




