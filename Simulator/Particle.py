import math
import numpy as np


class Particle:
    """
    This is a class used to calculated the velocity and position of a particle with given
    acceleration after some time deltaT.

    Parameters
    ----------
    method: integer
        An integer defining the approximation method used to calculate the new 
        position and velocity: 1 is the Euler method and 2 is the Euler Cromer method. 
        The method used must be defined within the Particle.

    Velocity, Acceleration, Position: float
        The velocity, accleration and position of a given particle defined as a vector 
        by having the 3 different componants in a numpy array.

    Name: string
        The assigned name given to a specific particle.

    Mass: float
        The assigned mass given to a specific particle.
    """

    G=6.67408E-11

    #The initalize function
    def __init__(self, time=0.0, Position=np.array([0,0,0], dtype=float), Velocity=np.array([0,0,0], dtype=float), Acceleration=np.array([0,-10,0], dtype=float), Name='Ball', Mass=1.0, method = 2):

        self.position = np.array(Position, dtype=float)
        self.velocity = np.array(Velocity, dtype=float)
        self.acceleration = np.array(Acceleration, dtype=float)
        self.mass = Mass
        self.Name = Name
        self.time = time
        self.setMethod(method)
        
        

    #STring was too long if i included self.CalculationMethod.__name__
    def __repr__( self ):
        return ( 'Particle: {0}, Mass: {1:12.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}, Time: {5}'.format(self.Name, self.mass, self.position, self.velocity, self.acceleration, self.time ))

    #setMethod determines the method used for calculating velocity and position.
    def setMethod(self, method):
        #If the method is set as equal to 1 the Euler method is used.
        if method == 1:
            self.CalculationMethod = self.Euler
        #If the method is set as equal to 2 the Euler Cromer method is used. 
        elif method == 2:
            self.CalculationMethod = self.EulerCromer
        #If neither 1 nor 2 is assigned to a particle a value error will be rasied as no method will have been assigned.
        else:
            raise ValueError("Unrecognised method called to calculate position and velocity. Method must be 1 (Euler) or 2 (Euler Cromer).")


    #The Euler Cromer method, this calculates a new velocity first and then uses this new inital velocity to caluclate position.
    def EulerCromer(self, deltaT):
        self.velocity = self.velocity + self.acceleration * deltaT
        self.position = self.position + self.velocity * deltaT
        self.time += deltaT

    #Euler method calculates a new position first and the uses this new intial position to calculate a new velocity.    
    def Euler(self, deltaT):
        self.position = self.position + self.velocity * deltaT
        self.velocity = self.velocity + self.acceleration * deltaT
        self.time += deltaT
        
    #This update function updates the time by deltaT and then calls the calculation method to assign the given method defined.
    def update(self,deltaT):
        self.CalculationMethod(deltaT)

    #This function returns a value for the kinetic energy of a given particle. 
    def KineticEnergy(self):
        return 0.5*self.mass*np.dot(self.velocity, self.velocity)

    #This function returns the value for the linear momentum of a given particle.
    def Momentum(self):
        return self.mass*self.velocity





    


