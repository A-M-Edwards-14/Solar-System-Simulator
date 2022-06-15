import math
import numpy as np 
from Particle import Particle
import copy


class SolarSystem:
    """
    This is a class uses Newtons law of gravity to approximate the acceleration of a given
    planet at any given time.

    Parameters
    ----------
    Planets: List
        A variable which will later be set equal to a list of particles in a simulation,
        it is these particles within this list that we are calculating the gravitational 
        attraction between. 

    """


    def __init__(self, Planets):

        #had to remove copy.deepcopy(Planets) and replace with just Planets
        self.ListOfPlanets = Planets
        self.TotalPotentialEnergy = 0
 
    def __repr__( self ):
        return ("{}".format(self.ListOfPlanets, self.TotalPotentialEnergy))

    #Create acceleration function that will calculate the accleration of each planet due to each other planet.
    def PlanetAcceleration(self):

        #Select one specific planet in the list of planets.
        for planet1 in self.ListOfPlanets:
            #Per-set all acclerations as equal to zero in all directions.
            acceleration=np.array([0,0,0], dtype=float)
            #Iterate through the list of planets again and select another planet
            for planet2 in self.ListOfPlanets:
                #Eliminate the possibility of calculating the gravitational affect of a planet on itself
                if planet1 != planet2:
                    #Calculate the distance between the planet and another
                    distance = np.linalg.norm(planet2.position - planet1.position)
                    #Add the acceleration affect of this one planet to the pre defined zero
                    acceleration += np.array((Particle.G*planet2.mass)/(distance)**3)*(planet2.position - planet1.position)

            #set the accleration of planet1 calculated equal to its acceleration initally defined as zero.    
            planet1.acceleration = acceleration
        


    #Changed name from update to Euler for when i create euler croomer
    def update(self, delta):
        self.PlanetAcceleration()

        for planet1 in self.ListOfPlanets:
            planet1.update(delta)

