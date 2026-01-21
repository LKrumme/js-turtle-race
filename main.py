# Turtle race 
import turtle
import random 
import math

win_length = 400 
win_heigth = 400

turtles = 4

screen = turtle.Screen()

win_readable = {'blue': 'Blau', 'red': 'Rot', 'green':'Grün', 'yellow': 'Gelb'}


turtle.screensize(win_length, win_heigth)
screen.setup(1920, 1080)


class racer(object): 
    def __init__(self, color, pos):
        self.pos = pos 
        self.color = color 
        self.turt = turtle.Turtle()
        self.turt.shape('turtle')
        self.turt.color(color)
        self.turt.penup()
        self.turt.setpos(pos)
        self.turt.setheading(0)
        self.turt.pensize(5)

    def move(self): 
        r = random.randrange(1,20)
        self.pos = (self.pos[0]+r, self.pos[1])
        self.turt.pendown()
        self.turt.forward(r)

      
    
    def reset(self):
        self.turt.penup()
        self.turt.home()

tList = []
winners = []
run = False

def game_loop():
    global run

    if not run:
        return

    for t in tList:
        t.move()

    for t in tList:
        if t.pos[0] > 750 and t not in winners:
            winners.append(t)

    if winners:
        show_winner()
        run = False
        return

    screen.ontimer(game_loop, 50)  # 20 FPS

def startGame():
    global tList, winners, run

    screen.clear()

    screen.onkey(startGame, "r")
    screen.listen()

    screen.bgpic('hintergrund1080p.png')
    turtle.hideturtle()

    tList = []
    winners = []
    run = True

    colors = ["red", "green", "blue", "yellow"]
    start = -(win_heigth / 2) + 20

    for i in range(turtles):
        newPosY = start + i * win_heigth // turtles
        tList.append(racer(colors[i], (-750, newPosY)))
        tList[i].turt.showturtle()

    game_loop()


def show_winner():
    winner = turtle.Turtle()
    winner.penup()
    winner.hideturtle()

    if len(winners) >= 2:
        for i, w in enumerate(winners[:2]):
            winner.color(w.color)
            winner.setpos(250 + i*300, 350)
            winner.write(
                f'Gewinner: {win_readable[w.color]}',
                align='center',
                font=('Times New Roman', 32, 'bold')
            )
    else:
        w = winners[0]
        winner.color(w.color)
        winner.setpos(450, 350)
        winner.write(
            f'Gewinner: {win_readable[w.color]}',
            align='center',
            font=('Times New Roman', 32, 'bold')
        )


screen.onkey(startGame, "r")
screen.listen()
screen.mainloop()