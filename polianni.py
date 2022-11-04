# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 12:36:28 2022

@author: jhoyland

PolarPlot

Makes animated plots of polarization vectors of EM-waves. Shows variation in E-field and its components during propagation.


"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-a','--polarization-angle',type=float,default=0,help="Polarization angle")
parser.add_argument('-p','--phase-difference',type=float,default=0,help="Phase differnce for x-component of polarization")
parser.add_argument('-u','--unit',choices=['radians','pi-radians','degrees'],default='pi-radians',help="Unit for angles")
parser.add_argument('-t','--tip-plot',choices=['none','static','animated'],default='none',help="Trace of the tip of the E-vector. Can be animated or not")
parser.add_argument('-q','--arrows',choices=['x','y','xy','xe','ye','xye','e'],default='xye',help="Which arrows to draw")
parser.add_argument('-s','--steps',type=int,default=120,help="Animation steps to calculate")
parser.add_argument('filename',help="Output file name")

args = parser.parse_args()



def wave(E,w,t,phi=0):
    
    return E * math.cos(w*t+phi)

#Wave period
T = 30.0

#Angular frequency
w0 = 2.0 * math.pi / T

#Polarization angle (For linear polarization)
#For circular polarized light set this to pi/4 to give equal amplitudes for components


unit = 1
    
if args.unit == 'pi-radians':
    
    unit = math.pi
    
if args.unit == 'degrees':

    unit = math.pi / 180
    
ang = args.polarization_angle * unit

#Overall amplitude
E0 = 1.0

#Component amplitudes
E0x = E0 * math.cos(ang)
E0y = E0 * math.sin(ang)

#Fixed phase factors for x and y components
#phix= 0.3 * math.pi
phix = args.phase_difference * unit
phiy = 0

#Intitial x and y component magitudes
Ex = wave(E0x,w0,0,phix)
Ey = wave(E0y,w0,0,phiy)

#Time steps for one period
tarray = np.linspace(0,T,args.steps)

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

arrow_colors = []
arrow_x = []
arrow_y = []

if 'x' in args.arrows:
    
    arrow_x.append(1)
    arrow_y.append(0)
    arrow_colors.append('orange')
    
if 'y' in args.arrows:
    
    arrow_x.append(0)
    arrow_y.append(1)
    arrow_colors.append('orange')

if 'e' in args.arrows:
    
    arrow_x.append(1)
    arrow_y.append(1)
    arrow_colors.append('darkred')
    
org_coords = [0] * len(arrow_x)    
arrow_x_coords = np.array([arrow_x])
arrow_y_coords = np.array([arrow_y])
    

#The "quiver" for the vector arrows
qr = ax.quiver(org_coords,org_coords, arrow_x_coords * Ex, arrow_y_coords * Ey, color=arrow_colors, width=0.0125, angles='xy', scale=1, scale_units='xy')

#Draw the line plot for the tip trace - comment this out for no tip trace
if args.tip_plot in 'staticanimated':
    line, = ax.plot(xtip,ytip,color='lightblue')


plt.savefig(args.filename+".png")

def animate(num):
    
    
    #Update tip trace data
    if args.tip_plot == 'animated':
        line.set_data(xtip[:num],ytip[:num])
    
    #Update arrows
    u = arrow_x_coords*xtip[num]
    v = arrow_y_coords*ytip[num]
    
    qr.set_UVC(u,v)
    
    return qr
    
    
anim = animation.FuncAnimation(fig, animate, frames=len(tarray), blit=False)


#Save animation
writergif = animation.PillowWriter(fps=15) 
anim.save(args.filename+".gif", writer=writergif)

plt.show()
