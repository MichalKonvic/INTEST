    if (config.globalDown != "0"):          #Download if
        SF.write("Download Speed: ")
        SF.write(str(config.globalDown))
        SF.write(" Mbps")
        SF.write('\n')
        if (config.globalUp != "0"):          #Upload if
            SF.write("Upload Speed: ")
            SF.write(str(config.globalUp))
            SF.write(" Mbps")
            SF.write('\n')    
    elif (config.globalUp != "0"):          #Upload if
        SF.write("Upload Speed: ")
        SF.write(str(config.globalUp))
        SF.write(" Mbps")
        SF.write('\n')
    elif(config.globalPing != "0"):         #Ping if
        SF.write("Ping: ")
        SF.write(str(config.globalPing))
        SF.write(" ms")