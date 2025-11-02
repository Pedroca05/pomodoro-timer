import time
import modules.Pomodoro as pm

def Mainpage():
    # this section is just for open a .txt file who is the menu page
    # I'd make half of this part on python but I was very lazy at te moment I made this :P
 
    with open("modules/mainpage.txt", '+a') as menu:
        
        menu.seek(0)
        print(menu.read())

    choice = input("      Chosen your option\n")

    focus_time = None
    counter = 0

    if int(choice) == 1: 
        print("\033c",end="")
        pm.pomodoro(focus_time, counter) 


    elif int(choice) == 2 or str(choice) == 'exit':
        print('\033c', end='')
        print("bye bye")
    
    else:
        print('\033c',end='')
        
        print("try again")
        print('\033c',end='')
        

        waiting_time = 30
        
        while waiting_time > 0:

            f_wt = time.gmtime(waiting_time)
            seconds_wt = waiting_time % 60

            time.sleep(1)
            
            print("wait for 30 seconds for the system restart:")
            print(f"{seconds_wt:02}s")
            print('\033c',end='')
            waiting_time -= 1

        print('\033c',end='')
        Mainpage()

Mainpage()