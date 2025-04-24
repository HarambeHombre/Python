import time
import tkinter as tk

# Open file and assign content
file = open('test_content.txt')
content = file.read()
content = content.splitlines()

# Turn content into a list
temp_list = []
for word in content:
    for i in range(len(word)):
        temp_list.append(word[i])

# Create a list that holds count of missed letters
missed = []

# Timer starts when program starts
start_time = time.time()

# Create a list for correct letters typed
correct_letters = []

max_time = 60

# Function that reads users typed letters one by one and checks them against the temp_list, if letter is correct background turns green, if wrong background turns red,
# it also displays the letters you type under the entry field to show your progress. Once all letters typed in the program ends, it displays a
# completed_message showing how many characters you typed from program start to end of content list. progress, and entry are removed from program, and displays only
# the completed message and initial content list.
def key_pressed(e):
    i = 0
    global letters
    letters = ''
    entered_text = e
    for char in temp_list[i]:
        if entered_text.char == char:
            temp_list.remove(char)
            correct_letters.append(entered_text.char)
            typing_area.configure(background="green")
            i += 1
        else:
            missed.append(entered_text.char)
            typing_area.configure(background="red")
        for letter in correct_letters:
            letters += letter
            progress.config(text=f'{letters}')
        if not temp_list:
            # completed_message.config(text=f'Congrats you typed: {len(letters)} characters, in {time.time() - start_time} seconds, and only had {len(missed)} mistakes')
            completed_message.config(text=f'Your Words Per Minute are: {len(letters) / 5}, you made {len(missed)} mistakes.')
            typing_area.config(state='disabled')
            typing_area.destroy()
            progress.destroy()
            timer_label.destroy()

# Create a timer that stops the program after 60 seconds
def timer():
    global max_time
    max_time -= 1
    timer_label.configure(text=f'Time left: {max_time} seconds')
    if max_time > 0:
        # schedule next update 1 second later
        window.after(1000, timer)
    else:
        completed_message.config(text=f'Your Words Per Minute are: {len(letters) / 5}, you made {len(missed)} mistakes.')
        typing_area.config(state='disabled')
        typing_area.destroy()
        progress.destroy()
        timer_label.destroy()

# Create window
window = tk.Tk()
window.title('Key typing speed test')
window.geometry('600x200')

# Label that holds content
content_label = tk.Label(text=f'Words to type:\n{content}', wraplength=550, justify="left")
content_label.pack(pady=20)

# Entry that holds user input
text_variable = tk.StringVar()
typing_area = tk.Entry(window, name='typing_area', textvariable=text_variable, width=100)
typing_area.pack(padx=20)

# Will display typed words while they are being typed here
progress = tk.Label()
progress.pack()

timer_label = tk.Label(window, text=f'Time left: {max_time} seconds')
timer_label.pack(pady=10)

# Display a message at end of test to show results
completed_message = tk.Label(wraplength=550, justify="left")
completed_message.pack(padx=10)

window.after(1000, timer) # start the update 1 second later

typing_area.bind('<KeyPress>', key_pressed)

window.mainloop()