import tkinter as tk

running = False
hr, mins, sec = 0, 0, 0


def start():
    global running
    if not running:
        update()
        running = True


def pause():
    global running
    if running:
        stopwatch_label.after_cancel(update_time)
        running = False


def reset():
    global running
    if running:
        stopwatch_label.after_cancel(update_time)
        running = False
    global hr, mins, sec
    hr, mins, sec = 0, 0, 0
    stopwatch_label.config(text='00:00:00')


def update():
    global hr, mins, sec
    sec += 1
    if sec == 60:
        mins += 1
        sec = 0
    if mins == 60:
        hr += 1
        mins = 0

    hours_string = f'{hr}' if hr > 9 else f'0{hr}'
    minutes_string = f'{mins}' if mins > 9 else f'0{mins}'
    seconds_string = f'{sec}' if sec > 9 else f'0{sec}'

    stopwatch_label.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)

    global update_time
    update_time = stopwatch_label.after(1000, update)


root = tk.Tk()
root.geometry('485x220')
root.title('Stopwatch')


stopwatch_label = tk.Label(text='00:00:00', font=('Arial', 80))
stopwatch_label.pack()


start_button = tk.Button(text='start', height=5, width=7, font=('Arial', 20), command=start)
start_button.pack(side=tk.LEFT)
pause_button = tk.Button(text='pause', height=5, width=7, font=('Arial', 20), command=pause)
pause_button.pack(side=tk.LEFT)
reset_button = tk.Button(text='reset', height=5, width=7, font=('Arial', 20), command=reset)
reset_button.pack(side=tk.LEFT)
quit_button = tk.Button(text='quit', height=5, width=7, font=('Arial', 20), command=root.quit)
quit_button.pack(side=tk.LEFT)


root.mainloop()
