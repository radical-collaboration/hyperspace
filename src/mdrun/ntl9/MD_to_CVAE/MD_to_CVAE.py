import h5py, warnings 
import argparse, os
import numpy as np 
from glob import glob
from utils import cm_to_cvae, read_h5py_file

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--sim_path", dest='f', help="Input: OpenMM simulation path") 
parser.add_argument("-o", help="Output: CVAE 2D contact map h5 input file")

# Let's say I have a list of h5 file names 
args = parser.parse_args() 

if args.f: 
    cm_filepath = os.path.abspath(os.path.join(args.f, 'omm*/*_cm.h5')) 
else: 
    warnings.warn("No input dirname given, using current directory...") 
    cm_filepath = os.path.abspath(os.path.join('.', 'omm*/*_cm.h5'))

cm_files = sorted(glob(cm_filepath)) 
if cm_files == []: 
    raise IOError("No h5 file found, recheck your input filepath") 
# Get a list of opened h5 files 
cm_data_lists = [read_h5py_file(cm_file) for cm_file in cm_files] 

# Compress all .h5 files into one in cvae format 
cvae_input = cm_to_cvae(cm_data_lists)


# Create .h5 as cvae input
cvae_input_file = 'cvae_input.h5'
cvae_input_save = h5py.File(cvae_input_file, 'w')
cvae_input_save.create_dataset('contact_maps', data=cvae_input)
cvae_input_save.close()
