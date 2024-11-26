import pgzrun
TITLE="Quizmaster"
HEIGHT=650
WIDTH=870
timeleft=10
questions=[]
questioncount=0
questionindex=0
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
questionsfile="questions.txt"
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
    screen.draw.textbox(question[0],questionbox,color="white",shadow=(0,0.5),scolor="#7b7d79")
    index=1
    for optionbox in optionboxes:
        screen.draw.textbox(question[index],optionbox,color="white",shadow=(0,0.5),scolor="#7b7d79")
        index+=1
    screen.draw.textbox("Skip",skipbox,color="white",shadow=(0,0.5),scolor="#7b7d79",angle=90)
    screen.draw.textbox(str(timeleft),timerbox,color="white",shadow=(0,0.5),scolor="#7b7d79")
def movemarquee():
    marquee_box.x-=2
    if marquee_box.right<0:
        marquee_box.left=WIDTH
def update():
    movemarquee()
def readquestionfile():
    global questioncount,questions,questionsfile
    q=open(questionsfile,"r")
    for i in q:
        questions.append(i)
        questioncount+=1 
    q.close()

def readnextquestion():
    global questionindex
    questionindex+=1
    return questions.pop(0).split(",")

readquestionfile()
question=readnextquestion()  
pgzrun.go()

