import pgzrun
TITLE="Quizmaster"
HEIGHT=650
WIDTH=870
marquee_box=Rect(0,0,870,80)
questionbox=Rect(0,0,650,150)
timerbox=Rect(0,0,150,150)
optionbox1=Rect(0,0,300,150)
optionbox2=Rect(0,0,300,150)
optionbox3=Rect(0,0,300,150)
optionbox4=Rect(0,0,300,150)
skipbox=Rect(0,0,150,330)
optionboxes=[optionbox1,optionbox2,optionbox3,optionbox4]
marquee_box.move_ip(0,0)
questionbox.move_ip(20,100)
timerbox.move_ip(700,100)
skipbox.move_ip(700,270)
optionbox1.move_ip(20,270)
optionbox2.move_ip(370,270)
optionbox3.move_ip(20,450)
optionbox4.move_ip(370,450)
marqueemsg=""
def draw():
    screen.fill("black")
    screen.draw.filled_rect(marquee_box,"pink")
    screen.draw.filled_rect(questionbox,"#b47ef2")
    screen.draw.filled_rect(timerbox,"#8de0af")
    screen.draw.filled_rect(skipbox,"pink")
    for optionbox in optionboxes:
        screen.draw.filled_rect(optionbox,"lightblue")
    marqueemsg="Welcome to Quiz Master!"
    screen.draw.textbox(marqueemsg,marquee_box,color="white",shadow=(0.5,0.5),scolor="#7b7d79")
def movemarquee():
    marquee_box.x-=2
    if marquee_box.right<0:
        marquee_box.left=WIDTH
def update():
    movemarquee()

pgzrun.go()

