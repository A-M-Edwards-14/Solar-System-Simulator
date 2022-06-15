import math
import numpy as np 
from SolarSystem import SolarSystem
from Particle import Particle

"""
By running the simultion for a small delta and a very small range between the Earth and a massless particle
located at the Earths radius we should get a value for acceleration of Earth to be zero and the acceleration
of the particle to be -9.81 m/s^2 within a given tolerance

"""

#Pre define all the variable with the Earths centre set as the origin
earthMass = 5.97237e24   # https://en.wikipedia.org/wiki/Earth
earthRadius = 6371*1e3  # https://en.wikipedia.org/wiki/Earth
Earth = Particle(0.0, np.array([0,0,0]), np.array([0,0,0]), np.array([0,0,0]),'Earth', earthMass, method = 2)

#Create a massless particle that it located at the Earths radius in the positive y direciton.
Mass = Particle(0.0, np.array([earthRadius,0,0]), np.array([0,0,0]), np.array([0,0,0]), "Mass", 0, method = 2)

#Define the list of planets as two particles, the Earth and the Satellite
ListOfPlanets=[Earth, Mass]

#Set the variable newSolarSystem equal to the solar system class acting on the list of planets.
newSolarSystem = SolarSystem(ListOfPlanets)

#Define a small delta time step
delta = 1

#Set the range of iteration as something small so the position of the particle doesnt change by much
for i in range (1):
    #Update the time for which the acceleration in calculated for by delta
    newSolarSystem.update(delta)


print("The Masses accleration at Earth radius is:")
#Print the Earth and particles Name and mass
for particle in [Earth, Mass]:
    print("  Particle: {}".format(particle.Name))
    print("    Mass: {0:12.3e}, ".format(particle.mass))
    #Create loop that will print the acceleration of the massless particle
    for attribute in ["acceleration"]:
        #Add 0.0 to the print statement to avoid negative zeros
        print("    {}: {}".format(attribute, particle.__getattribute__(attribute) + 0.0))  

