'''
Created on Oct 13, 2014

@author: AndrewSpiteri
'''
from pylab import *

def main():
    figure()
    hold(True)
    z = -50
    #use the function 2z^3+3
    for i in range(100):
        y = 2*(z**3)+5*(z**2)-8*z+3
        plot(z,y,'o')
        z = z+1
    z = -50
    show()

main()
