# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 12:36:28 2022

@author: jhoyland

PolarPlot

Makes animated plots of polarization vectors of 


"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math


def wave(E,w,t,phi=0):
    
    return E * math.cos(w*t+phi)

#Wave period
T = 30.0

#Angular frequency
w0 = 2.0 * math.pi / T

#Polarization angle (For linear polarization)
#For circular polarized light set this to pi/4 to give equal amplitudes for components
ang = 0.25 * math.pi

#Overall amplitude
E0 = 1.0

#Component amplitudes
E0x = E0 * math.cos(ang)
E0y = E0 * math.sin(ang)

#Fixed phase factors for x and y components
#phix= 0.3 * math.pi
phix = 0
phiy= 0.5 * math.pi

#Intitial x and y component magitudes
Ex = wave(E0x,w0,0,phix)
Ey = wave(E0y,w0,0,phiy)

#Time steps for one period
tarray = np.linspace(0,T,120)

#Calculate component amplitudes over time array
xtip = np.array([wave(E0x,w0,tm,phix) for tm in tarray])
ytip = np.array([wave(E0y,w0,tm,phiy) for tm in tarray])

#Set up figure
fig, ax = plt.subplots(1, 1)

#Set up the axes
ax.set(xlim=(-E0,E0),ylim=(-E0,E0))
ax.axes.xaxis.set_ticklabels([])
ax.axes.yaxis.set_ticklabels([])
ax.tick_params(axis="x", direction="inout")
ax.tick_params(axis="y", direction="inout")
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.set_aspect('equal')


#The "quiver" for the vector arrows
qr = ax.quiver([0,0,0], [0,0,0], [Ex,0,Ex], [0,Ey,Ey], color=['orange','orange','darkred'], width=0.0125, angles='xy', scale=1, scale_units='xy')
#Draw the line plot for the tip trace - comment this out for no tip trace
line, = ax.plot(xtip,ytip,color='lightblue')


plt.savefig("circRight.png")

def animate(num):
    
    
    #Update tip trace data - comment out for no animation of tip trace
    #line.set_data(xtip[:num],ytip[:num])
    
    #Update arrows
    u = [xtip[num],0,xtip[num]]
    v = [0,ytip[num],ytip[num]]
    
    qr.set_UVC(u,v)
    
    return qr
    
    
anim = animation.FuncAnimation(fig, animate, frames=len(tarray), blit=False)


#Save animation
writergif = animation.PillowWriter(fps=15) 
anim.save("circRight.gif", writer=writergif)

plt.show()
