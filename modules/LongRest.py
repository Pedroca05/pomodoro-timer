import time

def Longrest(focus_time,):

    if focus_time == None or focus_time == 0:
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