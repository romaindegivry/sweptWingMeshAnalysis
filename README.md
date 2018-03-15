# sweptWingMeshAnalysis
Python and shell scripts used to perform a mesh convergence analysis on swept wing 3D panel codes

## Required software
The code requires the user to submit two fFORTRAN files a mesh generator (geowing.f) that reads the mesh parametres from Panel_code/meshParam.dat. And combo.f a solver that outputs at least 3 sectionnal files sect_001 sect_002 and sect_003 and reads stream definition data from Panel_code/stream.dat.

The folowing python3 packages are required:
  numpy
  matplotlib
  
## Running the program
A linux enviroment is required, for this manipulation:
- cd into the main directory
- Run meshConv.sh with bash
- Simulation may take up to an hour to run (tested on intel i5)

## Future improvements
The code needs to be 
