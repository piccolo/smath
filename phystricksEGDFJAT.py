# -*- coding: utf8 -*-

from __future__ import division

from phystricks import *
def EGDFJAT():
    pspict,fig = SinglePicture("EGDFJAT")
    pspict.dilatation(1)

    l=10
    h=5
    rayon=1

    x=var('x')
    I=Point(0,h)
    J=Point(0,0)
    K=Point(l,0)
    L=Point(l,h)
    centre=Point(l/2,h/2)

    terrain=Polygon(I,J,K,L)
    M1=Segment(L,I).center()
    M2=Segment(K,J).center()

    Oy=Segment(J,I).center()
    Oy.put_mark(0.2,180,"\( 25\)",automatic_place=(pspict,"E"))

    I.put_mark(0.2,180,"\( 50\)",automatic_place=pspict)
    J.put_mark(0.2,180,"\( 0\)",automatic_place=pspict)
    K.put_mark(0.2,-90,"\( 100\)",automatic_place=pspict)
    M2.put_mark(0.2,-90,"\( 50\)",automatic_place=pspict)


    mediane=Segment(M1,M2)
    centre=mediane.center()
    cercle=Circle(centre,rayon)

    A=cercle.get_point(90)
    A.put_mark(0.2,45,"\( A\)",automatic_place=pspict)
    Ay=Point(0,A.y)

    B=Point(l/2+l/10,h/10)
    B.put_mark(0.2,90,"\( B\)",automatic_place=pspict)

    Bx=Point(B.x,0)
    By=Point(0,B.y)

    l1=Segment(A,Ay)
    l2=Segment(centre,Oy)
    l3=Segment(B,By)
    l4=Segment(B,Bx)
    l1.parameters.style="dotted"
    l2.parameters.style=l1.parameters.style
    l3.parameters.style=l1.parameters.style
    l4.parameters.style=l1.parameters.style

    pspict.DrawGraphs(terrain,mediane,cercle,A,B,centre,Oy,l1,l2,l3,l4,M2,I,J,K)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()