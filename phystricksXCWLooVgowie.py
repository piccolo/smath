# -*- coding: utf8 -*-
from phystricks import *
def XCWLooVgowie():
    pspict,fig = SinglePicture("XCWLooVgowie")
    pspict.dilatation(0.3)

    A=Point(0,0)
    B=Point(4,0)
    C=Point(0,3)

    A.put_mark(0.2,180+45,"\( A\)",pspict=pspict,position="corner")
    B.put_mark(0.2,-45,"\( B\)",pspict=pspict,position="corner")
    C.put_mark(0.2,90+45,"\( C\)",pspict=pspict,position="corner")

    rh=RightAngle(  Segment(C,A),Segment(A,B),0,1  )

    trig=Polygon(A,B,C)
    trig.edges[0].put_mark(0.2,text="\( 12\)",pspict=pspict,position="N")

    trig.edges[1].put_mark(0.2,trig.edges[1].advised_mark_angle(pspict)*degree,added_angle=180,text="\( ?\)",pspict=pspict,position="corner")
    trig.edges[2].put_mark(0.2,text="\( 9\)",pspict=pspict,position="E")

    no_symbol(trig.vertices)
    pspict.DrawGraphs(A,B,C,trig,rh)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
