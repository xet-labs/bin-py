import pyautogui
import time

#------------------------------------------------------------
#--ig_config-->
ig_scrool_int=0.5

ig_scrool=-200



#--fb_config-->
fb_scrool_int=0.5

fb_scrool=0



#--yt_config-->
yt_scrool_int=

yt_scrool=






#------------------------------------------------------------
def scrool(scrool_t):
    if scrool_t=='0':
        pyautogui.press('pagedown')
    else:
        pyautogui.scroll(scrool_t)        
        
def ig_scrool(scrool,time):
    id1='ig'
    dot_c=1
    dot="..."
    while True:
        #-->module<_scrolldowns-->
        scrool(scrool)
        
        #-->module<_interval_btwn_scrolldowns-->
        time.sleep(time)
        
        if dot=='...':
            dot='..'
            
        elif dot=='..':
            dot='...'
       
        print(id1,'time:',time_t,'  scrool:','page_down' if scrool_t=='0' else scrool_t,dot)
        
           


def fbw_scrool():
    dot_c=1
    dot="..."
    while True:
        #--scroll length-->
        scrool_t=200


        #--interval_btwn_scrolldowns-->
        time_t=0.5
        


        #-->module<_scrolldowns-->
        scrool(scrool_t)
        
        #-->module<_interval_btwn_scrolldowns-->
        time.sleep(time_t)
        
        if dot=='...':
            dot='..'
            
        elif dot=='..':
            dot='...'
       
        print('time:',time_t,'  scrool:','page_down' if scrool_t=='0' else scrool_t,dot)
        
       


def yt_scrool():
    dot_c=1
    dot="..."
    while True:
        #--scroll length-->
        scrool_t=200


        #--interval_btwn_scrolldowns-->
        time_t=0.5
        


        #-->module<_scrolldowns-->
        scrool(scrool_t)
        
        #-->module<_interval_btwn_scrolldowns-->
        time.sleep(time_t)
        
        if dot=='...':
            dot='..'
            
        elif dot=='..':
            dot='...'
       
        print('time:',time_t,'  scrool:','page_down' if scrool_t=='0' else scrool_t,dot)
        
       
while True:
    ig_scrool(ig_scrool,ig_time)
    #fbw_scrool()
    #yt_scrool()

    
