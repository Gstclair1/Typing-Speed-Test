from tkinter import *
import time

test_text ="A data entry clerk is a member of staff employed to enter or update data into a computer system. \n" \
           "Data is often entered into a computer from paper documents using a keyboard. The keyboards used can \n" \
           "often have special keys and multiple colors to help in the task and speed up the work. Proper \n" \
           "ergonomics at the workstation is a common topic considered. The Data Entry Clerk may also use a \n" \
           "mouse, and a manually-fed scanner may be involved. Speed and accuracy, not necessarily in that \n" \
           "order, are the key measures of the job; it is possible to do this job from home. Proofreader \n" \
           "applicants are tested primarily on their spelling, speed, and skill in finding errors in the \n" \
           "sample text. Toward that end, they may be given a list of ten or twenty classically difficult \n" \
           "words and a proofreading test, both tightly timed. The proofreading test will often have a maximum \n" \
           "number of errors per quantity of text and a minimum amount of time to find them. The goal of this \n" \
           "approach is to identify those with the best skill set."


double_check_text = "A data entry clerk is a member of staff employed to enter or update data into a computer system. Data is often entered into a computer from paper documents using a keyboard. The keyboards used can often have special keys and multiple colors to help in the task and speed up the work. Proper ergonomics at the workstation is a common topic considered. The Data Entry Clerk may also use a mouse, and a manually-fed scanner may be involved. Speed and accuracy, not necessarily in that order, are the key measures of the job; it is possible to do this job from home. Proofreader applicants are tested primarily on their spelling, speed, and skill in finding errors in the sample text. Toward that end, they may be given a list of ten or twenty classically difficult words and a proofreading test, both tightly timed. The proofreading test will often have a maximum number of errors per quantity of text and a minimum amount of time to find them. The goal of this approach is to identify those with the best skill set."

window = Tk()
window.title("Typing Speed Test")
window.config(height=600, width=1200)


def start():
    global entry, go
    text = Label(text=test_text, font=("arial", 12))
    text.grid(row=1, column=0, columnspan=3, pady=20)
    entry = Text(width=60, height=10)
    entry.grid(row=3, column=0, columnspan=3, pady=20)
    start_btn.config(text="Restart Typing Test")
    go = Label(text="Go!")
    go.grid(row=2, column=1, pady=20)
    window.after(60000, calculate)


def restart():
    global entry, go
    done_lbl.destroy()
    user_result.destroy()
    text = Label(text=test_text, font=("arial", 12))
    text.grid(row=1, column=0, columnspan=3, pady=20)
    entry = Text(width=60, height=10)
    entry.grid(row=3, column=0, columnspan=3, pady=20)
    go = Label(text="Go!")
    go.grid(row=2, column=1, pady=20)
    window.after(60000, calculate)


def calculate():
    global done_lbl, user_result
    result = entry.get("1.0", "end")
    go.destroy()
    entry.destroy()
    start_btn.destroy()
    restart_btn = Button(window, text="Restart Typing Test", command=restart)
    restart_btn.grid(row=4, column=1, padx=200, pady=100)
    score = 0
    missed = 0
    characters_per_word = 5
    for word in range(0, len(result)):
        if result[word] == double_check_text[word]:
            score += 1
        else:
            missed += 1
    done_lbl = Label(text=f"Times Up!\nScore: {score/characters_per_word}\nWords Missed: {missed/characters_per_word}\nTyping Speed: {(score-missed)/characters_per_word} WPM")
    done_lbl.grid(row=2, column=1, pady=20)
    user_result = Message(text=result, font=("arial", 12), width=600)
    user_result.grid(row=3, column=0, columnspan=3, pady=20)

main_lbl = Label(text="Welcome to the Typing Speed Test!\nGood Luck!")
main_lbl.grid(row=0, column=0, columnspan=3, padx=200, pady=50)
start_btn = Button(window, text="Start Typing Test", command=start)
start_btn.grid(row=4, column=1, padx=200, pady=100)

window.mainloop()
