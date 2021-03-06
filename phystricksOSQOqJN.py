# -*- coding: utf8 -*-
from phystricks import *
def OSQOqJN():
    pspict,fig = SinglePicture("OSQOqJN")
    pspict.dilatation(1)

    pspict.dilatation_X(0.7)
    pspict.dilatation_Y(0.7)

    x=var('x')
    f=phyFunction(-x-2).graph(-4,2)

    B=f.get_point(0)
    B.put_mark(0.2,B.advised_mark_angle(pspict),"\( p\)",pspict=pspict)
        
    x0=solve(f(x)==0,x)[0].rhs()
    A=f.get_point(x0)
    A.put_mark(0.2,A.advised_mark_angle(pspict),"\( -p/m\)",pspict=pspict)
        
    pspict.DrawGraphs(f,A,B)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
