import turtle

print("--------Make Among us Character of your chioce--------")
c=input("Enter color for body:")
g=input("Enter color for glass:")
bg=input("Enter color for bagpack:")
d=input("Start drawing y/n:")

if d=='y':

    bodyc=c
    bodyshadow=''
    glassc = g
    glassshadow=''
    bag = bg
    t = turtle.Turtle()
    turtle.Screen().bgcolor("seagreen")
    def body():

        t.pensize(20)
        t.speed(8)
        t.fillcolor(bodyc)
        t.begin_fill()

            #rightside:
        t.right(90)
        t.forward(50)
        t.right(180)
        t.circle(40,-180)
        t.right(180)
        t.forward(200)

            #head curve:
        t.right(180)
        t.circle(100,-180)
                #left side:
        t.backward(20)
        t.left(15)
        t.circle(500,-20)
        t.backward(20)

            #t.backward(200)
        t.circle(40,-180)
        t.left(7)
        t.backward(50)

            #hip:
        t.up()
        t.left(90)
        t.forward(10)
        t.right(90)
        t.down()
        t.right(240)
        t.circle(50,-70)

        t.end_fill()

    def glass():
        t.up()
        t.right(230)
        t.forward(100)
        t.left(90)
        t.forward(20)
        t.right(90)
        t.down()
        t.fillcolor(glassc)
        t.begin_fill()
        t.right(150)
        t.circle(90,-55)
        t.right(180)
        t.forward(1)
        t.right(180)
        t.circle(10,-65)
        t.right(180)
        t.forward(110)
        t.right(180)
        t.circle(50,-190)
        t.right(170)
        t.forward(80)
        t.right(180)
        t.circle(45,-30)
        t.end_fill()

    def backpack():

        t.up()
        t.right(60)
        t.forward(100)
        t.right(90)
        t.forward(75)

        t.fillcolor(bag)
        t.begin_fill()
        t.down()
        t.forward(30)
        t.right(255)
        t.circle(300,-30)
        t.right(260)
        t.forward(30)
        t.end_fill()
        turtle.Screen().exitonclick()

    #draw()
    body()
    glass()
    backpack()
else:
    print("Have a nice day!")
  













