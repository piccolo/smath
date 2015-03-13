# -*- coding: utf8 -*-
from phystricks import *
def FSQMooFDOrkR():
    pspict,fig = SinglePicture("FSQMooFDOrkR")
    pspict.dilatation_X(1.2)
    pspict.dilatation_Y(1)

    mx=-4
    Mx=8

    O=Point(0,0)
    #A=Point(-3,0)
    #B=Point(4,0)

    K=Point(0.5,0)

    O.put_mark(0.2,-90,"\( O\)",automatic_place=(pspict,""))
    #B.put_mark(0.2,-90,"\( B\)",automatic_place=(pspict,""))
    K.put_mark(0.2,90,"\( \\frac{ 1 }{2}\)",automatic_place=(pspict,""))

    for i in range(mx,0):
        A=Point(i,0)
        A.parameters.symbol=""
        if i%2==0 :
            A.put_mark(0.2,-90,"\(  {}\)".format(i),automatic_place=(pspict,""))
        else:
            A.put_mark(0.2,-90,"\( {}\)".format(i),automatic_place=(pspict,""))
        pspict.DrawGraphs(A)
    for i in range(0,floor(Mx)+1):
        A=Point(i,0)
        A.parameters.symbol=""
        A.put_mark(0.2,-90,"\( {}\)".format(i),automatic_place=(pspict,""))
        pspict.DrawGraphs(A)

    axe=SingleAxe(O,Vector(1,0),mx,Mx,pspict=pspict)
    axe.no_numbering()

    pspict.comment="Un axe gradué de -4 à 8. Les nombres sont en-dessous de l'axe, et le 1/2 est au-dessus"
    pspict.DrawGraphs(axe,K)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()