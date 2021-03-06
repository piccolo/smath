from __future__ import division


from phystricks import *
def EvZZys():
    pspict,fig = SinglePicture("EvZZys")
    pspict.dilatation(1.5)

    x=var('x')
    X=Point(4,3)
    Y=Point(-5,0)
    Z=Point(-1,-1/2)

    X.put_mark(0.1,X.angle(),"$X$",pspict=pspict)
    Y.put_mark(0.1,135,"$Y$",pspict=pspict)
    Z.put_mark(0.1,Z.angle(),"$Z$",pspict=pspict)

    pspict.DrawGraphs(X,Y,Z)
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
