import matplotlib.pyplot as plt
from scipy.integrate import simps
import numpy as np
import pandas as pd
import math

rpm = [i for i in range(0,216,3)]
rpm.append(217)
k = -1
t = 1
for j in range(len(rpm)):
    omega = (2*math.pi*rpm[j])/60
    H = 0.35
    D = 0.2
    g = 9.81
    r = np.linspace(0,0.1,num=26)
    r__ = np.linspace(-0.1,0.1,num=53)
    r_ = np.linspace(-10,10,num=53)
    Z = ((omega*r)**2)/(2*g)
    vol_a = simps(Z,r)*(2*math.pi*D)/2
    vol_i = math.pi*H*((D/2)**2)/2
    zo = (vol_i - vol_a)/(math.pi*((D/2)**2))
    z = []
    for i in range(0,53):
        z_ = (((omega*r__[i])**2)/(2*g) + zo)*100
        if z_ < 0:
            z_ = 0
        z.append(z_)
    c = (omega**2)/(2*g)
    print("Surface profile at RPM",rpm[j],"=",c,"x (r2)")
    
    
    x_left = [-10,-10]
    x_right = [10,10]
    bar = [0,35]
    bottom = [0,0]
    bottom_x = [-10,10]
    plt.plot(bottom, bar,color="#dd0000", dashes=[20, 5, 10, 5],label='Vertical Axis of Rotation')
    plt.plot(r_,z,color="#000080",linewidth = 2, label='Surface Profile')
    plt.plot(x_left,bar,color="black")
    plt.plot(x_right,bar,color="black")
    plt.plot(bottom_x,bottom,color="black")
    plt.stackplot(r_,z,color="#0088ff",alpha=0.65)
    plt.xlabel('Radius (cm)')
    plt.ylabel('Height (cm)')
    plt.legend(loc='upper right')
    plt.title("RPM = {}".format(rpm[j]))
    plt.show()

    if j == 0:
        data_z = pd.DataFrame(z,index=r_)
    elif j!=0:
        data_nz = pd.DataFrame(z,index=r_)
        data_z = data_z.join(data_nz,rsuffix="1")
data_z.set_axis(rpm, axis='columns', inplace=True)
data_z.to_csv('data_file.csv')
print(data_z.head())
    
    
    
    
   
