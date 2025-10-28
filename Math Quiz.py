from tkinter import *
from random import randint, choice

root = Tk()
root.title("Maths Quiz")
root.geometry("600x520") 
root.configure(bg="#f0f4f7")

question = StringVar()
answer = StringVar()
givenAnswer = StringVar()
score = IntVar()
questionNumber = IntVar()
timer = IntVar(value=10)

timer_id = None

def updateTimer():
    global timerLabel, timer_id
    if timer.get() > 0:
        timer.set(timer.get() - 1)
        timerLabel.config(text=f"Time left: {timer.get()} s")
        timer_id = root.after(1000, updateTimer)
    else:
        checkAnswer(timeout=True)

def generateQuestion():
    global questionLabel, timerLabel, timer_id
    questionNumber.set(questionNumber.get() + 1)
    number1 = randint(1, 10)
    number2 = randint(1, 10)
    operator = choice(['+', '-', '*', '/'])
    question.set(f'{number1}{operator}{number2}')
    answer.set(str(eval(question.get())))
    givenAnswer.set('')
    questionLabel.config(text=f"Question: {question.get()}")
    if timer_id:
        root.after_cancel(timer_id)
    timer.set(10)
    timerLabel.config(text=f"Time left: {timer.get()} s")
    updateTimer()

def checkAnswer(timeout=False):
    global scoreLabel, resultLabel, timer_id
    if timer_id:
        root.after_cancel(timer_id)
    if questionNumber.get() > 10:
        return
    resultLabel.config(text="")
    user_ans = givenAnswer.get() if not timeout else ""
    correct_ans = answer.get()
    if user_ans == correct_ans:
        score.set(score.get() + 1)
        resultLabel.config(text="Correct", fg="green")
    elif timeout:
        resultLabel.config(text="Time's up!", fg="orange")
    else:
        resultLabel.config(text="Incorrect", fg="red")
    scoreLabel.config(text=f"Score: {score.get()}")
    if questionNumber.get() == 10:
        scoreLabel.config(text=f"Final score: {score.get()}")
        resultLabel.config(text="Quiz Complete!", fg="blue")
    else:
        root.after(1000, generateQuestion)

def restart():
    global scoreLabel
    score.set(0)
    questionNumber.set(0)
    generateQuestion()
    scoreLabel.config(text=f"Score: {score.get()}")
    resultLabel.config(text="Result", fg="blue")


for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(10):
    root.grid_rowconfigure(i, pad=5)

headingLabel = Label(root, text="Math Quiz", font=('arial', 28, 'bold'), bg="#f0f4f7")
headingLabel.grid(row=0, column=0, columnspan=4, pady=(28, 10))

questionScale = Scale(root, from_=0, to=10, orient=HORIZONTAL, length=400, variable=questionNumber, state=DISABLED, bg="#f0f4f7", highlightthickness=0)
questionScale.grid(row=1, column=0, columnspan=3, padx=(80,10), sticky="ew")

completeQuestionLabel = Label(root, text="10th question", bg="#f0f4f7", font=('arial', 11))
completeQuestionLabel.grid(row=1, column=3, sticky="w")

questionLabel = Label(root, text="", font=('arial', 22), bg="#f0f4f7")
questionLabel.grid(row=2, column=0, columnspan=4, pady=(8, 18), sticky="ew")

# Centered answerEntry, submitButton to right
answerEntry = Entry(root, textvariable=givenAnswer, font=('arial', 20), width=20, justify='center')
answerEntry.grid(row=3, column=1, columnspan=2, sticky="ew")

submitButton = Button(root, text="Submit", font=('arial', 15), fg="white", bg="#3498db", command=lambda: checkAnswer(False), width=10, relief=GROOVE, cursor="hand2")
submitButton.grid(row=3, column=3, padx=(15, 35))

resultLabel = Label(root, text="Result", font=('arial', 20), fg="#34495e", bg="#f0f4f7")
resultLabel.grid(row=5, column=0, columnspan=4, pady=10, sticky="ew")

scoreLabel = Label(root, text=f"Score: {score.get()}", font=('arial', 20), fg="#2d3436", bg="#f0f4f7")
scoreLabel.grid(row=6, column=0, columnspan=4, pady=10, sticky="ew")

timerLabel = Label(root, text="Time left: 10 s", font=('arial', 18), fg="#8e44ad", bg="#f0f4f7")
timerLabel.grid(row=7, column=0, columnspan=4, pady=(0,15), sticky="ew")

restartButton = Button(root, text="Restart", font=('arial', 15), width=35, command=restart, fg="white", bg="#e17055", relief=GROOVE, cursor="hand2")
restartButton.grid(row=8, column=0, columnspan=4, pady=10)

generateQuestion()
root.mainloop()
