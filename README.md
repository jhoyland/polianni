# PoliAnni

A simple command line program to draw animated or static arrow diagrams to represent the polarization of light. Draw linear, elliptic of circular polarized light with any combination of amplitudes and phases.


usage: polianni.py [-h] [-a POLARIZATION_ANGLE] [-p PHASE_DIFFERENCE]
                   [-u {radians,pi-radians,degrees}]
                   [-t {none,static,animated}] [-q {x,y,xy,xe,ye,xye,e}]
                   [-s STEPS]
                   filename

positional arguments:
  filename              Output file name. Do not include extension. Two files are generated, an animated gif and a static png

optional arguments:
  -h, --help            show this help message and exit
  -a POLARIZATION_ANGLE, --polarization-angle POLARIZATION_ANGLE
                        This is the angle between the x-axis and the resultant electric field amplitudes. Default is 45 degrees to give equal amplitudes.
  -p PHASE_DIFFERENCE, --phase-difference PHASE_DIFFERENCE
                        This is the phase difference between the x and y components of the field. Positive is leading x.
  -u {radians,pi-radians,degrees}, --unit {radians,pi-radians,degrees}
                        The unit to use for angle measurements. Default is pi * radians. i.e. entering 0.5 means pi/2.
  -t {none,static,animated}, --tip-plot {none,static,animated}
                        You can optionally produce a plot of the tip of the field vector to illustrate circular and elliptic polarization. The plot can either be animated or static.
  -q {x,y,xy,xe,ye,xye,e}, --arrows {x,y,xy,xe,ye,xye,e}
                        Which arrows to draw. The default is to draw the E-vector and the x and y components, but any combination of them is possible.
  -s STEPS, --steps STEPS
                        Number of animation steps to calculate