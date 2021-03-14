import h5py
import numpy as np
import matplotlib.pyplot as plt

filename = "fof_subhalo_tab_005.hdf5"



def dump_info(name, obj):
    print ("{0} :".format(name))
    try:
        print ("   .value: {0}".format(obj.value))

        for key in obj.attrs.keys():
            print ("     .attrs[{0}]:  {1}".format(key, obj.attrs[key]))
    except:
        pass

file = h5py.File(filename)
file.visititems(dump_info)






file.close()











