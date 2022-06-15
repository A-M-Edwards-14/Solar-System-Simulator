import math
import numpy as np 
from SolarSystem import SolarSystem
from Particle import Particle
import copy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""
This simulation calls upon both the Particle and SolorSystem class to calculate the position,
velocity and acceleration of the planets at every given time step, delta.
This data will be saved to a file called "nbodysimulation" and will also be plotted onto a 3D
graph to show how the planets orbit one another.

"""

#Define inital conditions for all N bodies, Coordinates taken with the suns centre as origin
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

#Define the time step of the simulation
delta = 10

#Create a blank list of which all the data on the planets calculated in the solar system class will be appended to.
Data=[]

#Set how many times the position, velocity and accleration will be calculated with an increase in time of delta.
for i in range (10000):
    #Update the time in the solar system and particle class by delta
    newSolarSystem.update(delta)
   
    #Every time the time can be divided by 100 with no remained, append the planets data to the blank data list.
    if i % 100 == 0:
        item = copy.deepcopy(newSolarSystem.ListOfPlanets)
        Data.append(item)
        print('Have not crashed')

#Save the data list into a file called nbodysimulation
np.save("nbodysimulation",Data, allow_pickle=True)
DataIn = np.load("nbodysimulation.npy", allow_pickle=True)

#Creating a 3D plot of how the planets position changes over time.
#Create blank list for all the planets vector positions
Sun_Position=[]
Mercury_Position=[]
Earth_Position=[]
Moon_Position=[]
Jupiter_Position=[]

#Create a for loop that will append the position of each planet from the Data list, into the new planet position list.
for row in Data:

    #Append zero element, the position, of Data list to the planet list.
    Sun_Position.append(row[0].position)
    Mercury_Position.append(row[1].position)
    Earth_Position.append(row[2].position)
    Moon_Position.append(row[3].position)
    Jupiter_Position.append(row[4].position)

#Convert the position lists into numoy arrays
a = np.asarray(Sun_Position)
b = np.asarray(Mercury_Position)
c = np.asarray(Earth_Position)
d = np.asarray(Moon_Position)
e = np.asarray(Jupiter_Position)

fig = plt.figure()

#Label the planet positons with there corrosponding name
Sun_Name=[row[0].Name]
Mercury_Name=[row[1].Name]
Earth_Name=[row[2].Name]
Moon_Name=[row[3].Name]
Jupiter_Name=[row[4].Name]

#Create a 3D axis of which the x, y and z componant of the planet position will be plotted.
ax = fig.add_subplot(111, projection='3d')
ax.plot(a[:,0], a[:,1], a[:,2], label = Sun_Name)
ax.plot(b[:,0], b[:,1], b[:,2], label = Mercury_Name)
ax.plot(c[:,0], c[:,1], c[:,2], label = Earth_Name)
ax.plot(d[:,0], d[:,1], d[:,2], label = Moon_Name)
ax.plot(e[:,0], e[:,1], e[:,2], label = Jupiter_Name)

#Create legend
plt.legend()
#Show the plotted graph
plt.show()