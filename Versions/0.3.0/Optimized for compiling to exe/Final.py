#!/usr/bin/python
import speedtest
import os
import config
import platform
import sys
from colored import fg, bg, attr
from time import localtime, strftime
from time import sleep
from os import system, name



#Important variables for saving
config.Has_Tested = bool(False)
config.Results_Saved = bool(False)
config.globalDown = "0"
config.globalUp = "0"
config.globalPing = "0"

# clear function 
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    else:               # for mac and linux(here, os.name is 'posix') 
        _ = system('clear')

#Platform to system
platsystem = platform.system()

#colors
reset = attr('reset')
red = fg(9)
yellow = fg(222)
purple = fg(92)
blue = fg(26)
white = fg(7)
cyan = fg(117)
orange = fg(208)
green = fg(84)

#clears terminal
clear()

if platsystem.startswith("Windows"):
    class Titles:
        def waiting(self):
            system("title "+"INTEST I Status: Waiting")
        def testing(self, what):
            system("title "+"INTEST I Status: Testing "+what)
        def loading(self):
            system("title "+"INTEST I Status: Loading")
        def saving(self):
            system("title "+"INTEST I Status: Saving")
        def exiting(self):
            system("title "+"INTEST I Status: Exiting")
        def in_menu(self):
            system("title "+"                                                            INTEST              ")
        def errors(self):
            system("title "+"INTEST I Status: Error")
    Titles().in_menu()
    print('You are using ',platsystem)
    per = input('do you want to use colors [Y/N]: ')
    if per == "Y" or per == "y":
        pass
    else:
        reset = ""
        red = ""
        yellow = ""
        purple = ""
        blue = ""
        white = ""
        cyan = ""
        orange = ""
        green = ""
else:
    class Titles:
        def waiting(self):
            pass
        def testing(self, what):
            pass
        def loading(self):
            pass
        def saving(self):
            pass
        def exiting(self):
            pass
        def in_menu(self):
            pass
        def errors(self):
            pass

class tester:
    config.st = speedtest.Speedtest()

    def Download(self):
        config.Has_Tested = bool(True)
        download =round(config.st.download()/1000000)
        config.globalDown = download
        

    def Upload(self):
        config.Has_Tested = bool(True)
        upload =round(config.st.upload()/1000000)
        config.globalUp = upload
        

    def Ping(self):
        config.Has_Tested = bool(True)
        servernames = []
        config.st.get_servers(servernames)
        sleep(1)
        ping = round(config.st.results.ping)
        config.globalPing = ping

class INTESTER:
    def Menu_Download(self):
        if (config.globalDown != "0"):
            config.menDown = white+": "+reset+cyan+str(config.globalDown)+green+" Mbps"+reset
        else:
            config.menDown = ""

    def Menu_Upload(self):
        if (config.globalUp != "0"):
            config.menUp = white+": "+reset+cyan+str(config.globalUp)+green+" Mbps"+reset
        else:
            config.menUp = ""

    def Menu_Ping(self):
        if (config.globalPing != "0"):
            config.menPing = white+": "+reset+cyan+str(config.globalPing)+green+" ms"+reset
        else:
            config.menPing = ""

    def Exiting(self):
        print(cyan+"           [i] "+white+"Exiting..."+reset)
        sleep(1)
        clear()
        sys.exit()
    def Print_Screen(self):
        self.Menu_Download()
        self.Menu_Upload()
        self.Menu_Ping()
        clear()
        Titles().in_menu()
        print(purple+'''

                  ___           ___           ___           ___           ___     
      ___        /\\__\\         /\\  \\         /\\  \\         /\\  \\         /\\  \\    
     /\\  \\      /::|  |        \\:\\  \\       /::\\  \\       /::\\  \\        \\:\\  \\   
     \\:\\  \\    /:|:|  |         \\:\\  \\     /:/\\:\\  \\     /:/\\ \\  \\        \\:\\  \\  
     /::\\__\\  /:/|:|  |__       /::\\  \\   /::\\~\\:\\  \\   _\\:\\~\\ \\  \\       /::\\  \\
  __/:/\\/__/ /:/ |:| /\\__\\     /:/\\:\\__\\ /:/\\:\\ \\:\\__\\ /\\ \\:\\ \\ \\__\\     /:/\\:\\__\\
 /\\/:/  /    \\/__|:|/:/  /    /:/  \\/__/ \\:\\~\\:\\ \\/__/ \\:\\ \\:\\ \\/__/    /:/  \\/__/
 \\::/__/         |:/:/  /    /:/  /       \\:\\ \\:\\__\\    \\:\\ \\:\\__\\     /:/  /     
  \\:\\__\\         |::/  /     \\/__/         \\:\\ \\/__/     \\:\\/:/  /     \\/__/      
   \\/__/         /:/  /                     \\:\\__\\        \\::/  /                 
                 \\/__/                       \\/__/         \\/__/                  
                                                                                                                                              

'''+reset
+'''
                                The Internet tester
                                    By '''+red+'''Mihal                          
''')
        print(yellow+'''            1)'''+white+''' Download Speed'''+config.menDown)
        print(yellow+'''            2)'''+white+''' Upload Speed'''+config.menUp)
        print(yellow+'''            3)'''+white+''' Ping'''+config.menPing)
        print(yellow+'''            4)'''+white+''' Auto Mode''')
        print(yellow+'''            5)'''+white+''' Save Results''')
        print(yellow+'''            6)'''+white+''' Exit'''+reset)
        self.Selector()

    def Selector(self):
        try:
            opt = int(input(orange+'''

           [?]'''+white+''' Choice: '''+reset))
        except:
            print(red+"           [!]"+white+" Invalid Choice"+reset)
            sleep(1)
            self.Print_Screen()
        else:
            if opt == 1:
                Titles().testing(what="Download speed")
                print(cyan+"           [i] "+white+"Testing")
                tester().Download()
                self.Print_Screen()
            if opt == 2:
                Titles().testing(what="Upload Speed")
                print(cyan+"           [i] "+white+"Testing")
                tester().Upload()
                self.Print_Screen()
            if opt == 3:
                Titles().testing(what="Ping")
                print(cyan+"           [i]"+white+" Testing")
                tester().Ping()
                self.Print_Screen()
            if opt == 4:
                Titles().testing(what="Download speed")
                print(cyan+"           [i] "+white+"Testing")
                tester().Download()
                Titles().testing(what="Upload Speed")
                tester().Upload()
                Titles().testing(what="Ping")
                tester().Ping()
                self.Print_Screen()
            if opt == 5:
                if (config.globalDown == "0" and config.globalUp == "0" and config.globalPing == "0"):
                    Titles().errors()
                    print(red+"           [!]"+white+" No results to save"+reset)
                    sleep(3)
                    self.Print_Screen()
                else:
                    self.Save_Results()
            if opt == 6:
                Titles().exiting()
                if(config.Has_Tested == True):
                    if (config.Results_Saved == True):
                        self.Exiting()
                    else:
                        print(red+"           [!]"+white+" Unsaved content detected")
                        ext = input(orange+"           [?]"+white+" Save results [Y/N]: ")
                    if (ext == "Y" or ext == "y"):
                        self.Save_Results()
                    elif(ext == "N" or ext == "n"):
                        self.Exiting()
                    else:
                        self.Print_Screen()
                else:
                    self.Exiting()
            else:
                print(red+"           [!]"+white+" Invalid Choice"+reset)
                sleep(1)
                self.Print_Screen()

    def Save_Results(self):
        print(cyan+"           [i]"+white+" Don't use following characters in File Name : "+red+""" \\ / : * ? " < > |"""+reset)
        try:
            FName = input(orange+"           [?]"+white+" File name: "+reset)
            if(FName == "-TIME"):
                config.FN = str(strftime("Results %Y-%m-%d-%H-%M-%S.txt", localtime()))
                config.SF = open(config.FN, "w")
            else:
                config.FN = str(FName+".txt")
                config.SF = open(config.FN, "w")
        except:
            Titles().errors()
            print(red+"           [!]"+white+" Invalid File name")
            print(red+"           [!]"+white+" Don't use following characters in File Name : "+red+""" \\ / : * ? " < > |"""+reset)
            sleep(2)
            print(red+"           [!]"+white+" Saving Failed"+reset)
            sleep(2)
            self.Print_Screen()
        else:
            Titles().saving()
            print(cyan+"           [i]"+white+" Saving Results"+reset) 
            config.SF.write("Results from ")
            config.SF.write(str(strftime("%Y-%m-%d %H:%M:%S", localtime())))
            config.SF.write('\n\n')
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
                config.Results_Saved = bool(True)
                config.SF.close()
                print(cyan+"           [i]"+white+" Saved to "+blue+config.FN+reset)
                print(cyan+"           [i]"+white+" Successfully Saved!"+reset)
                sleep(4)
            else:
                Titles().errors()
                print(red+"           [!]"+white+" Saving Failed"+reset)
                sleep(2)
                self.Print_Screen()
            self.Print_Screen()
if __name__ == '__main__':
    clear()
    print("Loading")
    INTESTER().Menu_Download()
    INTESTER().Menu_Upload()
    INTESTER().Menu_Ping()
    INTESTER().Print_Screen()