# -*- coding: utf8 -*-
from phystricks import *
def GSfDCyx():
    pspict,fig = SinglePicture("GSfDCyx")
    pspict.dilatation_X(0.8)
    pspict.dilatation_Y(1)

    moustaches=[]

    # Le delta_y n'a pas d'importance parce qu'il est recalculé plus bas.
    moustaches.append(Moustache(2.0,6.0,8.5,10.5,17.5,h=0.5,delta_y=0.75))  # DS8
    moustaches.append(Moustache(2.0,9.45,12.5,14.775,19.0,h=0.5,delta_y=0.75))   # DS7
    moustaches.append(Moustache(2.0,7.0,10.25,13.0,16.0,h=0.5,delta_y=0.75))    # DS6
    moustaches.append(Moustache(0.0,6.225,10.0,13.5,17.5,h=0.5,delta_y=0.75))       #DS5
    moustaches.append(Moustache(5.5,11.0,12.5,14.32,18.5,h=0.5,delta_y=0.75))      #DS4
    moustaches.append(Moustache(0.0,8.1,11.0,14.0,17.5,h=0.5,delta_y=0.75))        #DS3
    moustaches.append(Moustache(1.0,8.5,12.0,14.5,19.0,h=0.5,delta_y=1.75))        #DS2
    moustaches.append(Moustache(1.5,6.5,9.75,14.025,17.0,h=0.5,delta_y=2.75))      #DS1

    for i,m in enumerate(moustaches) :
        m.delta_y=0.75+i
        m.put_mark(0.2,text="DS {}".format( len(moustaches)-i ),pspict=pspict,position="W")

    pspict.DrawGraphs(moustaches)
    pspict.grid.draw_horizontal_grid=False
    pspict.axes.draw_single_axeY=False
    pspict.axes.single_axeY.no_graduation()
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def PEoyeQt():

    pspict,fig = SinglePicture("PEoyeQt")
    pspict.dilatation_X(0.8)
    pspict.dilatation_Y(1)

    moustaches=[]

#    # Le delta_y n'a pas d'importance parce qu'il est recalculé plus bas.
    moustaches.append(Moustache(0.0,1.8499999999999996,5.5,9.450000000000001,16.5,h=0.5,delta_y=0.75))
    moustaches.append(Moustache(0.0,4.0,8.0,11.4,19.5,h=0.5,delta_y=0.75))     #DS7
    moustaches.append(Moustache(0.5,5.0,7.5,10.5,19.5,h=0.5,delta_y=0.75))      #DS6
    moustaches.append(Moustache(1.5,5.0,8.5,11.5,19.0,h=0.5,delta_y=0.75))      #DS5
    moustaches.append(Moustache(2.0,7.5,10.0,12.0,19.5,h=0.5,delta_y=0.75))     #DS4
    moustaches.append(Moustache(3.0,5.6,7.5,10.9,15.5,h=0.5,delta_y=0.75))      #DS3
    moustaches.append(Moustache(1.0,5.5,7,11.4,19.0,h=0.5,delta_y=0.75))        #DS2
    moustaches.append(Moustache(2.5,6.5,8.5,11.5,17.0,h=0.5,delta_y=0.75))      #DS1

    for i,m in enumerate(moustaches) :
        m.delta_y=0.75+i
        m.put_mark(0.2,text="DS {}".format( len(moustaches)-i ),pspict=pspict,position="W")

    pspict.DrawGraphs(moustaches)
    pspict.grid.draw_horizontal_grid=False
    pspict.axes.draw_single_axeY=False
    pspict.axes.single_axeY.no_graduation()
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
