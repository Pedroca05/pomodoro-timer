import time

def pomodoro(focus_time, counter):
    
    if focus_time == None:
        focus_time = 0.2 * 60

    while focus_time >= 0:

        print('\033c', end="")
        f_time = time.gmtime(focus_time)

        minutes = focus_time // 60
        seconds = focus_time % 60
        
        print (f"{minutes:02}:{seconds:02}")

        time.sleep(1)

        focus_time -= 1
    
    Shortrest(counter)

def Shortrest(counter):
    if focus_time == None:
        focus_time = 25 * 60 # this is the base of pomodoro, but you can change for your own needs

    while focus_time >= 0:

        print('\033c', end="")
        f_time = time.gmtime(focus_time)

        minutes = focus_time // 60
        seconds = focus_time % 60
        
        print (f"{minutes:02}:{seconds:02}")

        time.sleep(1)

        focus_time -= 1

    counter += 1
    
    if counter <= 3: 
        Longrest()
    else:
        pomodoro(focus_time,counter) 

def Longrest():

    if focus_time == None:
        focus_time = 2 * 60

    while focus_time >= 0:

        print('\033c', end="")
        f_time = time.gmtime(focus_time)

        minutes = focus_time // 60
        seconds = focus_time % 60
        
        print (f"{minutes:02}:{seconds:02}")

        time.sleep(1)

        focus_time -= 1
    
    print('\033c', end="")
    print("Finish")