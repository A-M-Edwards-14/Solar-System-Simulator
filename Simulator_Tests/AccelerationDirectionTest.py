import math
import numpy as np 
from SolarSystem import SolarSystem
from Particle import Particle

"""
This simulation will test if the accleration calculated in the SolarSystem class is pointing in the right direction. By
having two planets initally at rest with one located at the origin and the other at some position along the x axis we should
get an acceleration directed towards one another 

"""
#Pre define all the variables with one planet at origin and the other at some position along the x axis, both initally at rest
sunMass = 1.989e30
Sun = Particle(0, np.array([0,0,0]), np.array([0,0,0]), np.array([0,0,0]),'Sun', sunMass, method = 1)

#Mercury
mercuryMass = 3.302e23
Mercury = Particle(0, np.array([57.91e9,0,0]), np.array([0,0,0]), np.array([0,0,0]),'Mercury', mercuryMass, method = 1)

#Define the list of planets as two particles, the sun and mercury.
ListOfPlanets=[Sun, Mercury]

#Set the variable newSolarSystem equal to the solar system class acting on the list of planets.
newSolarSystem = SolarSystem(ListOfPlanets)

#Define the delta time step of which the SolarSystem class will be updated by each time
delta = 6

#State the number of times a which the simulation will be ran and updated for
for i in range (2000):

    #Update the time by delta each iteration
    newSolarSystem.update(delta)

#Print out all the attributes of the Sun and Mercury
print("The Sun and Mercury Location after {0:12.3e} seconds is:".format(float(2000*6)))
for particle in [Sun, Mercury]:
    print("  Particle: {}".format(particle.Name))
    print("    Mass: {0:12.3e}, ".format(particle.mass))
    for attribute in ["position", "velocity", "acceleration", "time"]:
        #Add 0.0 to avoid negative zeros
        print("    {}: {}".format(attribute, particle.__getattribute__(attribute) + 0.0)) 