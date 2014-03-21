# -*- coding: utf8 -*-
from phystricks import *

# Attention : cette figure est recodéer en dur dans la correction, figure SUCoowlFdp


def GJbvyTt():
    pspict,fig = SinglePicture("GJbvyTt")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    O=Point(0,0)
    A=Point(3,1)
    B=Point(-1,1)
    C=Point(-3,2)
    F=B+(-1,0)

    O.put_mark(0.2,-45,"\( O\)",automatic_place=(pspict,"corner"))
    A.put_mark(0.2,45,"\( A\)",automatic_place=(pspict,"corner"))
    B.put_mark(0.2,180+45,"\( B\)",automatic_place=(pspict,"corner"))
    C.put_mark(0.2,90+45,"\( C\)",automatic_place=(pspict,"corner"))
    F.put_mark(0.2,180+45,"\( F\)",automatic_place=(pspict,"corner"))

    pspict.force_math_bounding_box( C+(-1,1) )
    pspict.force_math_bounding_box( A+(1,0) )

    pspict.DrawGraphs(O,A,C,B,F)
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
