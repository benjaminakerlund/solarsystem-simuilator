##Solar system simulator Benjamin Åkerlund 665762

## Introduction
    This is a Solar system Simulator. The user may control the simulation parameters of speed and duration
    as well as loading a satellite into the simulation and seeing how it behaves.

## File and directory structure
  - doc
    Contains the project documentation as well the project plans created in the beginning of the project.
    Also contains the savefile structure plan, which can help the user create scenarios of their own.
    
  - SaveData
    Contains the ready made INIT files that can be used to load a scenario. 
    A file like this must be selected in the loading phase in order to run the simulator.
        
  - src
    Contains all of the actual code the program runs on. 
    The main.py file is the one that needs to be run to start the program.
    

## Installation instructions
  - libraries required are PyQt5
  
  - Astropy is a pythonian astronomical library which can be quite helpful in creating INIT files if one wishes to do so.
    Astropy can give the user initial data of all the planetary objects in our solar system at least.
    From the following link it can be installed https://www.astropy.org/. 
    Here are quite extensive installation guides if one wishes to create their own libraries.
    More about this in /doc/Savefile_structure_plan.txt

## User instructions
  Simulating:
  - Run the main.py file
  - Press the Load button
  - Select a scenario file from one directory up (eg. INIT_8.txt) /solarsystem-simuilator---cs-a1121-y2/Savedata/INIT_8.txt
  - Input the simulation parameters eg. duration: 1000 (simulates for 1000 days)
  - Speed: 100 (simulates 100days in the program for each second elapsed in realtime)
  - Watch and enjoy.
  
  Loading a satellite:
  - input parameters for the satellite:
  - Coordinates: can be taken from INIT file to be similar to planet eg. earth (24887036.79612,-133017159.90135,-57663270.05063)
  - Velocity: Has to be converted manually from the format of the INIT file which is [km/day] to [m/s]
              Conversion factor is 0.1157. Multiply this to eg. earth velocity to get right unit
  - Mass: simple mass in [kg] can eg. be 100100
  - Name: most importantly the name of the satellite!
  
  - Click "Load Sat" button
  - Check that simulation parameters are correct.
  - Press "Run" button and enjoy
   
   
   
## Extra notes etc.
  It is assumed that the environment has the latest version of python installed.
  To run this program in a linux (debian) terminal follow the steps below:
  1. Clone the git repository at 
  2. Make sure to install the required developer tools for pyqt
     This can be done with 
     "sudo apt-get install qtcreator" and
     "sudo apt-get install qtcreator pyqt5-dev-tools"
     "sudo apt-get install qttools5-dev-tools"
     "sudo apt-get isntall python3-pip"
  3. Navigate in the directory the git repo was installed, to the src dir
     Here simply run the main.py file
     "python3 main.py"