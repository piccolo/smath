# -*- coding: utf8 -*-

from __future__ import division

from phystricks import *

def small_box(n,pc,pspict):
    x0=n*1.1
    rect=Rectangle( Point(x0,1),Point(  x0+1,0 ) )
    if n< floor(pc/10) :
        rect.parameters.filled()
        rect.parameters.fill.color="lightgray"
    pspict.DrawGraphs(rect)
    if n==floor(pc/10):
        print("pour",n)
        reste=(pc-10*n)/10
        x1=x0+reste
        part=Rectangle(  Point(x0,1),Point(x1,0) )
        part.parameters.filled()
        part.parameters.fill.color="lightgray"
        pspict.DrawGraphs(part)

def EISooBQSffk():
    pspict,fig = SinglePicture("EISooBQSffk")
    pspict.dilatation_X(0.7)
    pspict.dilatation_Y(0.5)

    pc=35
    for i in range(0,10):
        small_box(i,pc,pspict)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()