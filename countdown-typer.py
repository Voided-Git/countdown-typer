# keyboard module
from keyboard import write, wait, press_and_release
from os import system
from time import sleep


# set the window title
system("title CountdownTyper")


# check if an input is integer
def is_int(args: str):
    try:
        int(args)
        return True
    except ValueError:
        return False


# time inputting
def time_input(prompt: str):
    time = "NONE"
    while not is_int(time) and not is_int(time[:-1]) and not is_int(time[:-2]) and not time.upper() == "INF":
        time = input(prompt)

    return time


# convert time
def raw_time(time: str):
    _1end = time[len(time) - 1].upper()
    _2end = time[len(time) - 2].upper()
    if is_int(time[:-1]):
        _1rawtime = int(time[:-1])
    if is_int(time[:-2]):
        _2rawtime = int(time[:-2])

    if is_int(time) or _1end == "S":
        return _1rawtime

    elif _1end == "M":
        return _1rawtime * 60

    elif _1end == "H":
        return _1rawtime * 3600

    elif _1end == "D":
        return _1rawtime * 86400

    elif _1end == "W":
        return _1rawtime * 604800

    elif _2end == "MO":
        return _2rawtime * 2592000

    elif _1end == "Y":
        return _1rawtime * 31536000

    elif _2end == "DE":
        return _2rawtime * 315360000

    elif _1end == "C":
        return _1rawtime * 3153600000

    elif _2end == "MI":
        return _2rawtime * 31536000000

    elif time.upper() == "INF":
        return "INFINITY"

    return False


# infinite sender
def infinity_sender():
    i = 0
    write("∞")
    press_and_release("return")
    sleep(1)

    while True:
        i += 1
        write(f"∞ - {i}")
        press_and_release("return")
        sleep(1)


# main loop
while True:
    # asking for the time sent
    time = time_input("Enter the time sent: ")
    time = raw_time(time)

    # logical processing
    if time:
        # waiting for 't' and removing the 't' once pressed
        print("Press 't' to start counting down.")
        wait("t")
        press_and_release("backspace")

        if time == "INFINITY":
            # sending from infinity
            infinity_sender()

        else:
            # sending the message x number of times subtracting 1 each time
            for i in range(0, time + 1):
                write(str(time - i))
                press_and_release("return")
                sleep(1)

    # when finished
    input("All done! (press enter to continue)")
    # cleanup
    system("cls")
