import math
import numpy as np 
from SolarSystem import SolarSystem
from Particle import Particle


#TRY HAVING DEF FORCE IN PARTICLE CLASS

earthMass = 5.97237e24   # https://en.wikipedia.org/wiki/Earth
earthRadius = 63710*1e3  # https://en.wikipedia.org/wiki/Earth
Earth = Particle(0.0, np.array([0,0,0]), np.array([0,10,0]), np.array([0,0,0]),'Earth', earthMass, method = 2)
satPosition = earthRadius+(35786*1e3)
satVelocity = math.sqrt(Particle.G*Earth.mass/(satPosition))
Satellite = Particle(0.0, [satPosition,0,0], [0,satVelocity,0], np.array([0,0,0]), "Satellite", 100, method = 2)

ListOfPlanets=[Earth, Satellite]
newSolarSystem = SolarSystem(ListOfPlanets)

Force = np.array([0,0,0])

delta = 6
for i in range (1000000):

    print((i/1000000)*100)
    #Set the inital potential energy as equal to zero
    newSolarSystem.Force = np.array([0,0,0], dtype=float)
    #Select the first planet in list of planets and assign it an index
    for planet1 in ListOfPlanets:
        #Select a second planet and assign an index to it also
        for planet2 in ListOfPlanets:
            #Only calculate the potential between two planets if the index of 2 is greater than the index of 1, this avoids doubling up on each potential between planets.
            if planet1 != planet2:
                    
                newSolarSystem.Force += planet1.mass*planet1.acceleration

newSolarSystem.update(delta)
               
print(newSolarSystem.Force)