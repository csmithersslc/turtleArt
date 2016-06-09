#This program draws shapes to show how classes work

#We first import the turtle library
import turtle
window = turtle.Screen()
window.bgcolor("purple")

def draw_square():

	#To show the art, we need to have a window screen so we can see what is happening
	#I chose to make a dark background
	

	#Make the turtle object then an instance of that class/object
	#In other words now that we make on object from the template
	# I named the tutle in this instance Charles with a turtle shape, white color and a custom speed
	charles = turtle.Turtle()
	charles.shape("turtle")
	charles.color("white")
	charles.speed(20)

	move = 50
	#since we are doing this step a few times, a loop is adviasable.  Using a for loop since he's doing this FOR a certain number of times
	for move in range (0, 100):
		#we then call the forward function in the library to tell the turtle to move an x distance
		charles.right(5)
		charles.forward(100)
		#now the turtle has to stop and turn to the right 90 degrees
		charles.right(90)
		#let's make more intricate shapes
		#more_moves = 8
		#for more_moves in range (0, 100):
				#doing a loop within the loop to make a cool mandala type of shape
		#	charles.right(80)
		#	charles.forward(100)
			
			
	
#another turtle and another shape
def draw_triangle():
	robert = turtle.Turtle()
	robert.color("black")
	robert.shape("circle")
	robert.speed(1)

#same rules with the loop.  since he is making a triangle, he is only making 3 moves
	move = 3
	for move in range(0, 3):
		robert.right(120)
		robert.forward(120)
	
	


def draw_circle():
	#let's make another turtle with a new shape, color, and speed
	darwin = turtle.Turtle()
	darwin.shape("classic")
	darwin.color("yellow")
	darwin.speed(5)

	#We'll make Darwin do a different shape, a circle with a radius of 100
	darwin.circle(-100)

draw_square()
draw_triangle()
draw_circle()
window.exitonclick()
#can you tell I read my biology well?  Charles Robert Darwin was an interesting fellow