# libraries
from turtle import *
from random import randint
import turtle


#line 
ending = 150
#turtle color
character = Turtle()
character.color("White")
#screen color
display = Screen()
display.bgcolor("Black")
#function turtlemove
def turtlemove(turtles, x, y):
  turtles.penup()
  turtles.goto(x,y)
  turtles.pendown()
#where it will move
turtlemove(character,-200, 200)
#speed
character.speed(0)
character.setheading(270)

# for loop to  make a range for where it should move
for i in range(0, 500, 20):
  turtlemove(character, -200 + i , 200)
  character.write(int(1 + i/20), align = "center")
  turtlemove(character, -200 + i , 180)
  character.forward(400)
#our turtle contestants
redT = Turtle()
redT.shape("turtle")
redT.color("#ff0000")
orangeT = Turtle()
orangeT.shape("turtle")
orangeT.color("#FFA533")
yellowT = Turtle()
yellowT.shape("turtle")
yellowT.color("#FFF933")
greenT = Turtle()
greenT.shape("turtle")
greenT.color("#08FF00")
blueT = Turtle()
blueT.shape("turtle")
blueT.color("#00B6FF")
purpleT = Turtle()
purpleT.shape("turtle")
purpleT.color("#9B00FF")
#some type of list for all the turtles so they can have the controls made in the  function
turtleplayer = [redT, orangeT, yellowT,greenT, blueT, purpleT]
y = 160
#a for loop to seperate turtles and make them move
for turtlecharacter in turtleplayer:
  turtlemove(turtlecharacter, -200 , y)
  y -= 70
#if turtle hasnt crosed line
def checkIfWon(turtl):
  if(turtl.xcor() >= ending):
    return Turtle
  else:
    return False

winner = "nobody"
turtleplayer = [redT, orangeT, yellowT,greenT, blueT, purpleT]
redT.name = "red"
orangeT.name = "orange"
yellowT.name = "yellow"
greenT.name = "green"
blueT.name = "blue"
purpleT.name = "purple"

#if a turtle crossed the line
while winner == "nobody" :
  for i in turtleplayer :
    i.forward(randint(0,10))
    if checkIfWon(i):
      
      winner = i.name

turtle.color('deep pink')
style = ('Courier', 15, 'bold')
turtle.write("Nice! Our winner today is " +  winner, font=style, align='center')
turtle.hideturtle()



def something():

  response = input()
  response.capitalize()
  if response == "I like Turtles":

   print( """ 
  Sea Turtle
                _,.---.---.---.--.._ 
            _.-' `--.`---.`---'-. _,`--.._
           /`--._ .'.     `.     `,`-.`-._\
          ||   \  `.`---.__`__..-`. ,'`-._/
     _  ,`\ `-._\   \    `.    `_.-`-._,``-.
  ,`   `-_ \/ `-.`--.\    _\_.-'\__.-`-.`-._`.
 (_.o> ,--. `._/'--.-`,--`  \_.-'       \`-._ \
  `---'    `._ `---._/__,----`           `-. `-\
            /_, ,  _..-'                    `-._\
            \_, \/ ._(
             \_, \/ ._\
              `._,\/ ._\
                `._// ./`-._
         LGB      `-._-_-_.-'
""" )

  if response == "Turtles are bad":

    print( """    
https://www.youtube.com/watch?v=oHg5SJYRHA0
""" )
something()