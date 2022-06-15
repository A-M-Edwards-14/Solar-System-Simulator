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
This data will now be used to see how well the system conserves linear momentum by plotting the
total momentum of the system aganist time.

"""

#Define inital conditions for all N bodies, taking the coordinates with the suns centre taken as the origin.
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

#Set the time step of the simulation.
delta = 10

#Create a blank list of data for which all the planetary data will be appended to
Data=[]

#Create a blank list of momentum and time
Momentum = []
time = []

#Create a for loop for how many times the simulation will be iterated for.
for i in range (10000):
    #Append the total momentum at a given time to the momentum list 
    Momentum.append(np.linalg.norm(Sun.Momentum()+Mercury.Momentum()+Earth.Momentum()+Moon.Momentum()+Jupiter.Momentum()))
    #Append the time at which this total momentum is from and append it to the time list
    time.append(Earth.time)

    #Update the time by adding delta to it and recalculate all the variables once again.
    newSolarSystem.update(delta)

    #Every time the time can be divided by 100 with no remained, append the planets data to the blank data list.
    if i % 100 == 0:
        item = copy.deepcopy(newSolarSystem.ListOfPlanets)
        Data.append(item)

#Save the data list to a file called nbodysimulation
np.save("nbodysimulation",Data, allow_pickle=True)
DataIn = np.load("nbodysimulation.npy", allow_pickle=True)


#Plot the graph of total momentum against time
#Create a new blank list for relative momentum
relativemomentum = []

#Divide each entry in the Momentum list by the momentum at time = 0 and append these values to the relative momentum list.
for x in Momentum:
  relativemomentum.append(x/Momentum[0])

#Plot relative momentum against time
y = relativemomentum
x = time
plt.plot(x, y, color="red", linestyle="-", label="Total Momentum of N body system" )

#Show the graph
plt.show()

