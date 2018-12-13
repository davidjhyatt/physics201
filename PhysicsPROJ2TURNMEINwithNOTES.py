import math
from matplotlib import pyplot as plt

item = 0        #
mass = 0        #
diameter = 0    #
height = 0      #
dataInt = 0     #  Creating Variables and lists to store results and interations of results
vel = []        #
time = []       #
dist = []       #
refSpd = []     #
refDist = []    #


#####################
#####################
##This section is what the user interacts with to input data and the pre inputed example's data is converted to metric.

unit = 0
if unit == 0:
    unitn = "meters"
    unitw = "kg"

dObj = int(input("What object do you want to drop? \n0. Custom \n1. 16Lb Bowling Ball \n2. Basket Ball \n3. Baseball \n"))
if dObj == 0:
    item = str(input("What's the name of the object? \n"))
    if unit == 0:
        mass = float(input("How much does the " + item + " weigh in " + unitw + " ? \n"))
        diameter = float(input("What is the diameter of the " + item + " in " + unitn + "? \n"))

elif dObj == 1:
    item = "16 Lb Bowling Ball"
    mass = float(16 / 2.2)#lbs to kg
    diameter = float(8.5 * 0.0254)#inch to meters
elif dObj == 2:
    item = "Basket Ball"
    mass = float(1.4 / 2.2)#lbs to kg
    diameter = float(9.55 * 0.0254)#inch to meters
elif dObj == 3:
    item = "Baseball"
    mass = float(0.328 / 2.2)#lbs to kg
    diameter = float(2.94 * 0.0254)#inch to meters
else:
    print("Enter a 0 - 3 and press the Enter key. ")

h = int(input("How high would you like it to fall from? \n0. Custom \n1. Willis (Sears) Tower \n2. Burj Khalifa \n3. Mount Everest \n"))
if h == 0:
    height = float(input("How many " + unit + " would you like the " + item + " to fall from? "))
elif h == 1:
    height = float(440.0)#already in meters
elif h == 2:
    height = float(2717 * 0.305)#feet to meters
elif h == 3:
    height = float(29029 * 0.305)#feet to meters
else:
    print("Enter a 0 - 3 and press the Enter key. ")

dI = int(input("How many seconds between data points? \n0. Custom \n1. 0.001 \n2. 0.01 \n3. 0.1 \n"))
if dI == 0:
    dataInt = float(input("Enter the amount of a second between data points you want in decimal form. \n"))
elif dI == 1:
    dataInt = float(0.001)
elif dI == 2:
    dataInt = float(0.01)
elif dI == 3:
    dataInt = float(0.1)
else:
    print("Enter a 0 - 3 and press the Enter key. ")

########################
########################
##This section we calculate surface area, allowing for custom entries as well as create the vartiables for our formulas.

    
surfArea = float(4.0 * math.pi * (diameter/2) ** 2.0)
a = float(9.8)
Vi = 0
d = 0
itr = 1
itr2 = 0
Xi = 0
Xf = 0
Xx = 0

#############################
#############################

while height > Xf: ## Fall until terminal velocity is reached
    Vf = Vi + (a - d) * dataInt ## Velocity formula
    d = (1.225 * 0.5 * surfArea * (Vf ** 2)) / (2 * mass) ##Air resistance formula
    Xf = Xi + (Vi * dataInt) + ((a - d) * dataInt ** 2) / 2 ##Distance formula
    VyT = ((2*mass*a)/(1.225*0.5*surfArea))**(1/2)*math.tanh(((0.5*1.225*surfArea*a)/(2*mass))**(1/2)*(itr*dataInt)) ##Exact velocity formula
    XfT = ((2*mass)/(1.225*0.5*surfArea)*math.log(math.cosh(((1.225*0.5*surfArea*a)/(2*mass))**(1/2)*(itr*dataInt)))) ##Exact distance formula
    vel.append(Vf)              #
    time.append(itr * dataInt)  #
    dist.append(Xf)             #
    refSpd.append(VyT)          #Add resulst for this iteration to the corresponding lists
    refDist.append(XfT)         #
    Vi = Vf                     #
    Xi = Xf                     #
    itr += 1                    ##Add 1 to iteration count

    if Xf >= height and Xx == 0:##This is written funky because I want to calculate terminal velocity if that point were beyond the ground, but displays final results.
        if unit == 1:
            print("The " + item + " hit the ground at a velocity of " + str(vel[-1] * 3.281) + " " + unitn + " per second. ")
            print("The " + item + " fell " + str(Xf) + unitn + " for " + str(time[-1]) + " seconds \n")
            Xx = 1
        else:
            print("The " + item + " hit the ground at a velocity of " + str(vel[-1]) + " " + unitn + " per second. ")
            print("The " + item + " fell for " + str(time[-1]) + " seconds \n")
            Xx = 1

########################
########################
##Graphs that auto populate the fields

plt.plot(time, vel, label="Euler's Method")
plt.plot(time, refSpd, label='Exact Result')
plt.ylabel('Velocity')
plt.xlabel('Time')
plt.title(item + " Velocity vs Time Falling " + str(height) + " " + unitn)
plt.legend()
plt.show()

plt.plot(time, dist, label="Euler's Method")
plt.plot(time, refDist, label="Exact Result")
plt.ylabel('Distance')
plt.xlabel('Time')
plt.title(item + " Distance vs Time Falling " + str(height) + " " + unitn)
plt.legend()
plt.show()
