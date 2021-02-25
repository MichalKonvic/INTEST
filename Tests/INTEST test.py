import speedtest
import os
import config
from time import localtime, strftime
from time import sleep
from os import system, name 

# define my clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

#Importat variables for saving
config.globalDown = "0"
config.globalUp = "0"
config.globalPing = "0"



def tester():
    st = speedtest.Speedtest()
    tester.download =round(st.download()/1000000)
    tester.upload =round(st.upload()/1000000)
    #Ping part
    servernames =[]
    st.get_servers(servernames)
    tester.ping = round(st.results.ping)

#Screens 
def Main_Screen():
    clear()
    opt = int(input('''

        ██╗███╗   ██╗████████╗███████╗███████╗████████╗
        ██║████╗  ██║╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
        ██║██╔██╗ ██║   ██║   █████╗  ███████╗   ██║   
        ██║██║╚██╗██║   ██║   ██╔══╝  ╚════██║   ██║   
        ██║██║ ╚████║   ██║   ███████╗███████║   ██║   
        ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚══════╝   ╚═╝   
                    The Internet tester
                        By Mihal                          
                    
           [i] Select:
            1) Download Speed
            2) Upload Speed
            3) Ping


           [?] Choice: '''))
    if opt == 1:
        config.globalDown = 1
        print('           [i] Download: ',config.globalDown, 'Mbps')
        end_controler()
    elif opt == 2:
        config.globalUp = 1 
        print('           [i] Upload: ',config.globalUp, 'Mbps')
        end_controler()
    elif opt == 3:
        config.globalPing = 1
        print('           [i] Ping',config.globalPing,'ms')
        end_controler()
    else:
        print("\n           [!] Invalid choice!")
        print("           [i] Restarting...")
        sleep(1)
        clear()
        Main_Screen()

def end_controler():
    end_control_int = input("           [?] Do you want to test something else? [Y/N]: ")
    if(end_control_int == 'Y' or end_control_int == 'y'):
        Main_Screen()
    elif(end_control_int == 'N' or end_control_int == 'n'):
        SaveResults = input("           [?] Do you want to Save results? [Y/N]: ")
        if (SaveResults == 'Y' or SaveResults == 'y'):
            Save_screen()
        elif(SaveResults == 'N' or SaveResults == 'n'):
            End_Screen()
        else:
            Save_screen()
    else:
        Main_Screen()

def Save_screen():
    print("           [i] Saving Results...")
    config.FN = str(strftime("Results %Y-%m-%d_%H-%M.txt", localtime()))
    config.SF = open(config.FN, "w")
    config.SF.write("Results from ")
    config.SF.write(str(strftime("%Y-%m-%d %H:%M:%S", localtime())))
    config.SF.write('\n')
    if (config.globalDown != "0"):          #Download if
        config.SF.write("Download Speed: ")
        config.SF.write(str(config.globalDown))
        config.SF.write(" Mbps")
        config.SF.write('\n')
        config.globalDown_Saved = bool(True)
    else:
        config.globalDown_Saved = bool(True)
    if (config.globalUp != "0"):          #Upload if
        config.SF.write("Upload Speed: ")
        config.SF.write(str(config.globalUp))
        config.SF.write(" Mbps")
        config.SF.write('\n')
        config.globalUp_Saved = bool(True)
    else:
        config.globalUp_Saved = bool(True)
    if(config.globalPing != "0"):         #Ping if
        config.SF.write("Ping: ")
        config.SF.write(str(config.globalPing))
        config.SF.write(" ms")
        config.globalPing_Saved = bool(True)
    else:
        config.globalPing_Saved = bool(True)
    if(config.globalDown_Saved == True and config.globalUp_Saved == True and config.globalPing_Saved == True):
        config.SF.close()
    else:
        print("           [!] Saving Failed!")
        sleep(2)
        exit()
    clear()
    print("           [i] Saved to ",os.path.dirname(__file__),"\\",config.FN)
    print("           [i] Successfully Saved!")
    sleep(5)
    End_Screen()

def End_Screen():
    clear()
    print('Exiting.')
    sleep(1)
    clear()
    print('Exiting..')
    sleep(1)
    clear()
    print('Exiting...')
    clear()
    exit()


#Program start Here(After all variables and calls)
has_started = None
if(has_started == None):
    Main_Screen()
    has_started = True
else:
    pass