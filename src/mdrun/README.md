# ntl9 with EnTK

see the [ntl9](ntl9) sub directory

# MD Simulation

The 100-ns MD simulation of GPCR can be run with the follow code. 
Check `python run_openmm.py --help` for more information.  

```bash 
python run_openmm.py --pdb_file pdb/3pbl.pdb --topol pdb/topol.top --length 100
```

## Dependencies 
1. OpenMM 
2. Parmed 
3. MDAnalysis 
4. Numpy 

