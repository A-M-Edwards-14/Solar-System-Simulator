import math
import numpy as np 
from SolarSystem import SolarSystem
from Particle import Particle
import copy
import matplotlib.pyplot as plt

"""
This simulation calls upon both the Particle and SolorSystem class to calculate the position,
velocity and acceleration of the planets at every given time step, delta.
This data will be saved to a file called "nbodysimulation".
This data will now be used to see how well the system conserves total energy by plotting the
total energy of the system aganist time.

"""

#Define inital conditions for all N bodies, the coordinates taken with the suns centre set as the origin.
#Sun
sunMass = 1.989e30
Sun = Particle(0, np.array([0,0,0]), np.array([0,0,0]), np.array([0,0,0]),'Sun', sunMass, method = 2)

#Mercury
mercuryMass = 3.302e23
Mercury = Particle(0, np.array([-3.930046702152635e10, 3.162551442307564e10, 6.189497562862767e9]), np.array([-4.046795974292945e4, -3.595140717176649e4, 7.745950908430377e2]), np.array([0,0,0]),'Mercury', mercuryMass, method = 2)

#Earth
earthMass = 5.97237e24
Earth = Particle(0, np.array([6.435351701129258e10,1.328720924669925e11,-6.455927257947624e6]), np.array([-2.730774728652689e4,1.287730703357347e4,4.566335445082004e-1]), np.array([0,0,0]),'Earth', earthMass, method = 2)

#Moon
moonMass = 7.349e22
Moon = Particle(0, np.array([6.421919781899114e10,1.325231003945380e11,1.027209870419651e7]), np.array([-2.634544813442052e4,1.245288576371886e4,-8.031653195062916e1]), np.array([0,0,0]),'Moon', moonMass, method = 2)

#Jupiter
jupiterMass = 1898.13e24
Jupiter = Particle(0, np.array([3.975398507855213e10,-7.829216264725822e11,2.362472502021730e9]), np.array([1.290352850609894e4,1.280336564705750e3,-2.940703401553226e2]), np.array([0,0,0]),'Jupiter', jupiterMass, method = 2)

#Define the List of Planets as a list of all the defined planets above
ListOfPlanets=[Sun, Mercury, Earth, Moon, Jupiter]

#Set the variable newSolarSystem equal to the solar system class acting on the list of planets.
newSolarSystem = SolarSystem(ListOfPlanets)

#Define the time step of which the simulation will be interated over.
delta = 100
#Create a blank Data list
Data=[]
#Create a blank list for energy and time
Energy=[]
time=[]

#The for loop will calculate the total potential energy between all the planets.
for i in range (1000000):

    print((i/1000000)*100)
    #Set the inital potential energy as equal to zero
    newSolarSystem.TotalPotentialEnergy = 0
    #Select the first planet in list of planets and assign it an index
    for index1, planet1 in enumerate(ListOfPlanets):
        #Select a second planet and assign an index to it also
        for index2, planet2 in enumerate(ListOfPlanets):
            #Only calculate the potential between two planets if the index of 2 is greater than the index of 1, this avoids doubling up on each potential between planets.
            if planet1 != planet2 and index2 > index1:
                #Calculate the distance between the two planets
                distance = np.linalg.norm(planet2.position - planet1.position)
                #Update the Potential by minusing it from the total amount each time    
                newSolarSystem.TotalPotentialEnergy -= (Particle.G*planet2.mass*planet1.mass)/(distance)
                
#Calculate the total kinetic energy of the solar system        
TotalKineticEnergy = Sun.KineticEnergy()+Mercury.KineticEnergy()+Earth.KineticEnergy()+Moon.KineticEnergy()+Jupiter.KineticEnergy()
#Calculate the total of kinetic and potential energy in the system
TotalEnergy = TotalKineticEnergy + newSolarSystem.TotalPotentialEnergy

#Append the total energy to the blank Energy list
Energy.append(TotalEnergy)
#Append the time at which this energy occurs to the blank energy list
time.append(Earth.time)

#Update the time in the SolarSystem class by delta and recalculate the variables 
newSolarSystem.update(delta)
  
#Every time the time can be divided by 100 with no remained, append the planets data to the blank data list.
if i % 100 == 0:
    item = copy.deepcopy(newSolarSystem.ListOfPlanets)
    Data.append(item)

#Save the data list into a file called nbodysimulation
np.save("nbodysimulation",Data, allow_pickle=True)
DataIn = np.load("nbodysimulation.npy", allow_pickle=True)


#Plot a graph of total energy against time
y = Energy
x = time
plt.plot(x, y, color="red", linestyle="-", label = "Conservation of ennergy" )
#Label the x and y axis
plt.xlabel('$Time$')
plt.ylabel('$Total Energy$')
#Create a graph title
plt.title('Conservation of Total Energy')
#Create a legend
plt.legend()
#Show the graph
plt.show()






                


