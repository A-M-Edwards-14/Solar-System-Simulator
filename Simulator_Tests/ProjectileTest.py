import math
import numpy as np 
from SolarSystem import SolarSystem
from Particle import Particle
import matplotlib.pyplot as plt

"""
By running the simultion for a small delta and a very small range between the Earth and a massless particle,
with the massless particle located at Earth radius with an inital vertical and horizontal componant of velocity,
projectile motion of the particle should be simulated. 

"""

#Pre define all variables with the Earths centre located at the origin
earthMass = 5.97237e24 
earthRadius = 6371*1e3 
Earth = Particle(0.0, np.array([0,0,0]), np.array([0,0,0]), np.array([0,0,0]),'Earth', earthMass, method = 2)

#Define the Projectile as located at the North Pole with a velocity of 10m/s in both the x and y direction
Projectile = Particle(0.0, [0,earthRadius,0], [10,10,0], np.array([0,0,0]), "Projectile", 0, method = 2)

#Define the list of planets as two particles, the Earth and the Satellite
ListOfPlanets=[Earth, Projectile]

#Set the variable newSolarSystem equal to the solar system class acting on the list of planets.
newSolarSystem = SolarSystem(ListOfPlanets)

#Define the detla time step that the simulation will increase by
delta = 0.01
#Create blank lists for the x and y position of the particle as it accelerates towards Earth
Position_x = []
Position_y = []

#State the number of times a which the simulation will be ran and updated for
for i in range (210):
    #Update the time by delta each iteration
    newSolarSystem.update(delta)
    #Append the x and y position of the particle each iteration
    Position_x.append(Projectile.position[0])
    Position_y.append(Projectile.position[1])

#Print the position, accleration and velocity of the massless particle after the stated time range
print("The Projectiles Location after {0:12.3e} seconds is:".format(float(2000*6)))
for particle in [Projectile]:
    print("  Particle: {}".format(particle.Name))
    print("    Mass: {0:12.3e}, ".format(particle.mass))
    for attribute in ["position", "velocity", "acceleration", "time"]:
        print("    {}: {}".format(attribute, particle.__getattribute__(attribute) + 0.0))  # add 0.0 to avoid negative zeros!


#Plot the path the particle moves along, the y axis being vertical displacement and the x being horizontal displacement
x = Position_x
y = Position_y

#plot the Graph
plt.plot(x, y, color="red", linestyle="-", label="Projectile path" )
#Label the x and y axis
plt.xlabel('X displacement')
plt.ylabel('Y displacement')
#Give the graph a title
plt.title('Projectile Path')
#Create a legend
plt.legend()
#Show the graph
plt.show()