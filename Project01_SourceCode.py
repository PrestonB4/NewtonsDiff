#=============================================================================
#  Name        : Project1_SourceCode.py
#  Author      : Preston Brownlee & Ryan White
#  Due Date    : 19.Jan.2025
#  Description : CST-305 -- Dedevelop the mathematical and computer programming solution to perform and visualize Newton's Law of Cooling.
#                Documentation and README provided in the downloaded .zip folder.
#  Packages    : numpy, scipy, matplotlib
#=============================================================================
# Necessary Imports
import math
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the differential equation for Newton's Law of Cooling
def lawOfCooling(temperature, timeElapsed, temperatureSurrounding, k): # (T_s, T_0, k, t)
    temperatureReading = -k*(temperature - temperatureSurrounding) # dT/dt = -k(T - T_s)
    return temperatureReading

# Allow the use to input conditions to solve for k
def solveCoolingConstant():
    while True:
        userResponse = input("Would you like to enter test conditions to solve for the cooling constant [k]? (y/n): ")
        if not (userResponse.lower() == "y" or userResponse.lower() == "n"):
            print(" Please provide valid input.\n")
            continue
        
        if (userResponse.lower() == "n"):
            k = 0.15
            print(f" Using default cooling constant. k = {k:.2f}\n")
            return (k, False)
            
        break

    # Define conditions to solve for cooling constant
    solvingInitial = 0.0
    temperatureSurrounding = 0.0
    solvingRead = 0.0
    solvingTime = 0.0
    while True:
        print("Please enter input values:")

        # Loop until inputs are valid
        try:
            # Assign user input to variables, restart if the input is not 0 or 1.
            solvingInitial = (float)(input("  What is the initial temperature? (in °C): "))
            temperatureSurrounding = (float)(input("  What is the surrounding temperature? (in °C): "))
            solvingRead = (float)(input("  What is the recorded temperature after time has passed? (in °C): "))
            solvingTime = (float)(input("  How much time elapsed? (in sec.): "))
            if solvingTime < 0:
                print(" Please provide valid inputs.\n")
                continue
            
        except:
            print(" Please provide valid inputs.\n")
            continue
            
        k = (-1/solvingTime) * math.log((solvingRead - temperatureSurrounding)/(solvingInitial - temperatureSurrounding))
        print(f" Value for the cooling constant [k]: {k:.2f}\n")
        return (k, True, temperatureSurrounding)

# Create a model of Newton's Law of Cooling
solvingResults = solveCoolingConstant()

# Define program variables
k = solvingResults[0]
solvedK = solvingResults[1]
temperatureInitial = 0.0
temperatureSurrounding = solvingResults[2] if solvedK else 0
timeRangeStart = 0.0
timeRangeEnd = 0.0

while True:
    # Define initial conditions
    print("Please enter input values:")

    # Loop until inputs are valid
    try:
        # Assign user input to variables, restart if the input is not 0 or 1.
        temperatureInitial = (float)(input("  temperatureInitial (in °C): "))
        
        if not solvedK:
            temperatureSurrounding = (float)(input("  temperatureSurrounding (in °C): "))
        else:
            print(f"  temperatureSurrounding (in °C): {temperatureSurrounding}")
        
        
        timeRangeStart = (float)(input("  timeRangeStart (<= 0, in sec.): "))
        if timeRangeStart < 0:
            print(" Please provide valid inputs.\n")
            continue
        
        timeRangeEnd = (float)(input("  timeRangeEnd (<= 0, in sec.): "))
        if timeRangeEnd < 0:
            print(" Please provide valid inputs.\n")
            continue
    except:
        print(" Please provide valid inputs.\n")
        continue
        
    print(" See Output plot.\n")
    break

# Create the time range
timeRange = np.linspace(timeRangeStart,timeRangeEnd)

# Solve the ODE
temperaturePlot = odeint(lawOfCooling,temperatureInitial,timeRange,args=(temperatureSurrounding, k))

# Plot results
plt.plot(timeRange,temperaturePlot,'r:',linewidth=2,label=f"k={k}")
plt.xlabel('time (in sec.)')
plt.ylabel('temperature (in °C)')
plt.legend()
plt.show()
