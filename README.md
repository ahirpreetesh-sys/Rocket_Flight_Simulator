# Rocket Trajectory 

## OVERVIEW OF PROJECT
This models contain rocket flight path during and after its powered ascent. It computes position (x,y), velocity, drag forces, and acceleration step-by-step using numerical integration with a time step of 0.1 seconds
## Features
- Customizable Inputs: It user inputs for rocket mass,fuel mass,engine thrust,burn time, and launch angle.
- Realistic Physics Forces: Accounts for gravity (9.8 m/s²),atmospheric density (1.2 kg/m³) ,and aerodynamic drag.
- Dynamic Mass Reduction: Simulates fuel consumption and weight reduction when fuel is burning.
- Real-time Trajectory Table: Prints formatted time-stamped columns for time ,altitude ,downrange and speed.
## Technologies/Tools Used
Python 3.x: Core programming language.
Math Library: Built-in Python math module for trigonometric and square root calculations.
## Steps to Install and Run the Project
Install Python: Ensure Python 3.x is installed on my computer.Save the Code: Copy the simulation code into a file named pthy.py.
Open Terminal/Command Prompt: Navigate to the folder where the file is saved.
Run the Script
Provide Inputs: Enter the requested values in the terminal prompt when asked (e.g., mass, fuel, thrust, burn time, and launch angle).
## Instructions for Testing
                                                      Test Case 1:
Rocket mass: 50
Fuel mass: 20 
Thrust: 2000 
Burn time: 5 
Launch angle: 90 
                                                       Test Case 2:
Rocket mass: 100 
Fuel mass: 40 
Thrust: 4000  
Burn Time: 8 
Launch angle: 60 
## Output Of Simulatino
# Enter rocket mass (kg) 50
# Enter fuel mass (kg) 20
# Enter thrust (N) 5000
# Enter burn time (s) 4
# Enter launch angle (degrees) 85
# Time(s)   Altitude(m)    Downrange(m)   Speed(m/s)  
# ------------------------------------------------------------
# 0.00      0.000          0.000          0.000       
# 2.0       131.71         18.60          119.80      
# 4.0       485.82         75.99          216.28      
# 6.0       812.34         134.34         132.13      
# 8.0       1013.68        176.50         84.73       
# 10.0      1141.60        210.86         54.08       
# 12.0      1216.74        241.06         31.38       
# 14.0      1248.33        269.08         15.49       
# 16.0      1240.10        295.99         18.11       
# 18.0      1194.09        321.67         33.07       
# 20.0      1114.16        345.35         47.83       
# 22.0      1006.05        366.44         60.04       
# 24.0      876.07         384.68         69.37       
# 26.0      729.99         400.12         76.14       
# 28.0      572.52         412.96         80.86       
# 30.0      407.23         423.52         84.09       
# 32.0      236.65         432.15         86.24       
# 34.0      62.56          439.16         87.67       
# **************************************************
Crash! rocket hit the ground at 34.8 seconds
gine thrust curves, structural constraints, guidance, or detailed atmospheric effects. Results are for coursework and software demonstrations only.
