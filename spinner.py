# AAACoder Art-271
from turtle import *
import colorsys

bgcolor('black')
tracer(300)
h = 0.7
goto( -110, 100)

for i in range(300):
	c = colorsys.hsv_to_rgb(h ,1 , 1)
	color(c)
	begin_fill( )
	circle( -70+ ( i*0.1) ,240)
	forward(300-i)
	left(29)
	backward(700-i)
	end_fill( )
	h += 0.005
	
done( )
