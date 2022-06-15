import math
import numpy as np 
from SolarSystem import SolarSystem
from Particle import Particle
import matplotlib.pyplot as plt
import copy

"""
    This simulation will run for 2000 times with a delta time step of 6 seconds. Using know results between
    a satellite and Earth the accuracy of the simulation can be tested.

"""

#Pre define all variables for the Earth and Satellite
earthMass = 5.97237e24
earthRadius = 63710*1e3 
#Define the Earths centre as the origin and give the Earth an inital velocity of 10m/s in the y direction.
Earth = Particle(0.0, np.array([0,0,0]), np.array([0,10,0]), np.array([0,0,0]),'Earth', earthMass, method = 1)
satPosition = earthRadius+(35786*1e3)
satVelocity = math.sqrt(Particle.G*Earth.mass/(satPosition))
Satellite = Particle(0.0, [satPosition,0,0], [0,satVelocity,0], np.array([0,0,0]), "Satellite", 100, method = 1)

#Define the list of planets as two particles, the Earth and the Satellite
ListOfPlanets=[Earth, Satellite]

#Set the variable newSolarSystem equal to the solar system class acting on the list of planets.
newSolarSystem = SolarSystem(ListOfPlanets)

#Define the delta time step as 6 seconds
delta = 6

#Set how many times the position, velocity and accleration will be calculated with an increase in time of delta 
for i in range (2000):
    #Update the time at which the acceleration should be calculated for by delta
    newSolarSystem.update(delta)


print("The Earth and Satellites Location after {0:12.3e} seconds is:".format(float(2000*6)))
#Print the Earth and Satellites name and mass
for particle in [Earth, Satellite]:
    print("  Particle: {}".format(particle.Name))
    print("    Mass: {0:12.3e}, ".format(particle.mass))
    #Print all the attributes of the Earth and satellite 
    for attribute in ["position", "velocity", "acceleration", "time"]:
        print("    {}: {}".format(attribute, particle.__getattribute__(attribute) + 0.0))  # add 0.0 to avoid negative zeros!


#EXPECTED OUTPUT

#The Earth and Satellites Location after    1.200e+04 seconds is:
  #Particle: Earth
    #Mass:    5.972e+24,
    #position: [4.82888242e-17 1.20000000e+05 0.00000000e+00]
    #velocity: [8.01412732e-21 1.00000000e+01 0.00000000e+00]
    #acceleration: [6.55202176e-25 1.60424090e-25 0.00000000e+00]
  #Particle: Satellite
    #Mass:    1.000e+02,
    #position: [96612012.75033642 23787438.38973474        0.        ]
    #velocity: [-478.6333356  1943.80629604    0.        ]
    #acceleration: [-0.0391311  -0.00958112  0.        ]