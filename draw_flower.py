#This program draws shapes to show how classes work

#We first import the turtle library
import turtle
window = turtle.Screen()
window.bgcolor("green")

def draw_square():

	#To show the art, we need to have a window screen so we can see what is happening
	#I chose to make a dark background
	

	#Make the turtle object then an instance of that class/object
	#In other words now that we make on object from the template
	# I named the tutle in this instance Charles with a turtle shape, white color and a custom speed
	daisy = turtle.Turtle()
	daisy.shape("turtle")
	daisy.color("white")
	daisy.speed(20)

	move = 50
	#since we are doing this step a few times, a loop is adviasable.  Using a for loop since he's doing this FOR a certain number of times
	for move in range (0, 43):
		#we then call the forward function in the library to tell the turtle to move an x distance
		daisy.right(5)
		daisy.forward(100)
		#now the turtle has to stop and turn to the right 90 degrees
		daisy.right(90)
		#let's make more intricate shapes
	daisy.forward(200)
		
			

draw_square()

window.exitonclick()
#can you tell I read my biology well?  Charles Robert Darwin was an interesting fellow