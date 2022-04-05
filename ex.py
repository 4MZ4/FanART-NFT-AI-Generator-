# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 11:52:19 2022

@author: Hamza
"""


import time
start_time = time.time()

from svg_turtle import SvgTurtle


def draw_spiral(t):
    # t.fillcolor('blue')
    # t.begin_fill()
    # for i in range(20):
    #     d = 50 + i*i*1.5
    #     t.pencolor(0, 0.05*i, 0)
    #     t.width(i)
    #     t.forward(d)
    #     t.right(144)
    # t.end_fill()
    sides = 3 #Try change from 2 - 9
    colors=['red','purple','blue','green','orange','yellow']

    for i in range(350):
        t.fillcolor('black')
        t.pencolor(colors[i%6])
        t.forward(i * 2 / sides + i)
        t.left(360/ sides + 1.5)
        t.pensize(1) #change it as you want

def write_file(draw_func, filename, width, height):
    t = SvgTurtle(width, height)
    draw_func(t)
    t.save_as(filename)


write_file(draw_spiral, 'example2.svg', 500, 500)
print('Done.')



    
    

print("--- %s seconds ---" % (time.time() - start_time))
