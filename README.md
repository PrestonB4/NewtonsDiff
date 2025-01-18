# README | CST-305: Project 1 - Visualize ODE With SciPy
> Preston Brownlee & Ryan White
---

*__Instructions:__ Identify a performance metric associated with a computer system that would necessitate the use of ODE to calculate. Your task is to develop the mathematical and computer programming solution to perform and visualize this calculation. The program processes an ODE as input from the user. Using the appropriate scientific computing package, write the appropriate code to solve the ODE. Based on the readings and class activities, choose the most appropriate visualization paradigm and style for the solution. When the program displays the solution, the language, terminology, units, and error estimates should be descriptive in the context of the problem you are solving. Write a computer program that solves an ODE and generates a visual representation of a solutions*

## Setup
This project was developed in Python3 using Thonny with the installed numpy, SciPy, and Matplotlib packages.
This program will not function if your Python IDE cannot access numpy, SciPy, and Matplotlib.

## Functionality
The program takes input values from the user to simulate and model temperature change that behaves according to the differential equation of Newton's Law of Cooling. Given an initial temperature, surrounding environment temperature, and time range, the output is a curve which demonstrates how the initial temperature will adjust to the surrounding temperature.

The cooling constant, k, is given a default value of 0.15 -- a value determined in the testing conditions of a study on CPU cooling by [JETIR](https://www.jetir.org/papers/JETIRBU06044.pdf). However, the user is initally prompted if they would like to enter tested conditions to solve for the cooling constant.

If they choose "yes", they must enter an initial temperature, a surrounding temperature, a recorded temperature, and the time that passed between the initial and recorded temperature. The cooling constant is now input into the program and the program continues as usual. The decided surrounding temperature will carry over into further input to maintain the simulated environment.

## Usage
Run the program in a Python IDE and the Shell will display prompts for user input. Any invalid input will not be accepted by the program and the user will be prompted to retry.

Once the user gives the appropriate input the program will create the output chart and demonstrate the change in temperature in the conditions given.
