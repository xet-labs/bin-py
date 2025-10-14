import webbrowser
import pyautogui
import time
import random



def startup(url):
    #-startup_open
    time.sleep(5)
    webbrowser.open(url)
    print('--url opened--')
    
    #_refresh
    time.sleep(6)
    pyautogui.hotkey('ctrl','r')
    print('refreshed---1')
    time.sleep(10)
    pyautogui.hotkey('ctrl','r')
    print('refreshed---2')
    time.sleep(10)

        
    
    
def ig_h():
    url="https://www.instagram.com"

    #--DEFAULTs
    thres=20
    rep=3
    #thres=int(input("enter threshold:"))
    
    #_count_vars
    global c1
    srep=1
    c2=1
    r1=0
    r2=0
    
    id2='ig_h'
    #startup(url)

    #_driver_code->
    while True:
        pyautogui.scroll(-150)
        print(c1,id2,'(',srep,'/',rep,')-','(',c2,'/',thres,')','--''(r1-',+r1,' *r2-',+r2,')')
        c2+=1
        
        
        #_interval_btwn_scrolldowns--
        #time.sleep(0.1)

        #_double_tab
        if r1<=1:
            r2=random.randrange(80,120,30)
            print("if_r2",r2)#!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if r1==r2:
            pyautogui.click(button='left',clicks=2,interval=0.4)
            r1=0
            print("clicked--if_r1",r1)#!!!!!!!!!!!!!!!!!!!!!!!!!!!
            
        r1+=1
        
    
    
        #close tab
        print('----',c1,'(',srep,'/',rep,')-','(',c2,'/',thres,')')
           
        if c2==thres: 
            pyautogui.hotkey('ctrl','w')
            print('closed------')
            c1+=1
            c2=1
            
            srep+=1
            
            
        if srep==rep+1:
            srep=1
            print('**==BROKEN==**')
            ig_h()
            #break

        
        
        
        
        
    

def fb_w():
    url="https://www.facebook.com/watch"

    #--DEFAULTs
    thres=300
    rep=3
    #thres=int(input("enter threshold:"))
    
    #_count_vars
    global c1
    srep=1
    c2=0
    
    
    id1='fb_w'
    startup(url)

    #_driver_code->
    while True:
        pyautogui.scroll(-120)
        print(c1,id2,'--',c2,)
        c2+=1

        
        #_interval_btwn_scrolldowns
        time.sleep(0.6)

        #close tab
        if c2==thres:
            pyautogui.hotkey('ctrl','w')
            print('closed------')
            c1+=1
            c2=1
            srep+=1
            
            
        if srep==rep+1:
            srep=1
            break
        



def yt_r():
    url="https://www.youtube.com/shorts"
    #_count_vars
    global c1
    thres=1
    startup(url)
    while True:
        pyautogui.press('pagedown')
        thres+=1
        #_interval_btwn_scrolldowns
        time.sleep(0.8)

        #close tab
        if thres==150:
            pyautogui.hotkey('ctrl','w')
            print('closed------')
            c1+=1
            c2=1
            
            break
        
#ig_h()
#------------------------------------------------------------------

#-browser_selection--
browser = webbrowser.get('"C:Program Files\BraveSoftware\Brave-Browser\Application\Brave.exe" %s')



#-count_var's
c1=1 #global_reps
c2=1


#-program-execution
print('--> \'1\' for custom configs\n--> \'enter\' for defaults')
start_qs=''
start_qs=input('--> ')#!!comment for direct execution-->

if start_qs=='1':

    #-enable modules param
    print('\n--enable_modules--\n--> 1_ig\n--> 2_fb\n--> 3_yt')
    enable_mod=input('--> ')

    #-config params for 'ig'-->
    if '1' in enable_mod:
        print('\n--module \'ig_h\' enabled--')
        print('--> \'1\' for custom parameters\n--> \'enter\' for defaults')
        ig_param=input('--> ')
        if ig_param =='1':
            ig_rep=int(input('repetitions--> '))
            ig_thres=int(input('threshold--> '))
        elif ig_param=='':
            print('module \'ig_h\' DEFAULTS loaded')
        else:
            while ig_param!='1' and ig_param!='':
                print('\n--enter specific selection!!!--')
                print('--module \'ig_h\' enabled--')
                print('--> \'1\' for custom parameters\n--> \'enter\' for defaults')
                ig_param=input('--> ')
                if ig_param =='1':
                    ig_rep=int(input('repetitions--> '))
                    ig_thres=int(input('threshold--> '))
                    #continue
                elif ig_param=='':
                    print('module \'ig_h\' DEFAULTS loaded')
                    #continue
               

    #-config params for 'fb'-->
    if '2' in enable_mod:
        print('\n--module \'fb_w\' enabled--')
        print('--> \'1\' for custom parameters\n--> \'enter\' for defaults')
        fb_param=input('--> ')
        if fb_param =='1':
            fb_rep=int(input('repetitions--> '))
            fb_thres=int(input('threshold--> '))
        elif fb_param=='':
            print('module \'ig_h\' DEFAULTS loaded')
        else:
            print('\n--enter specific selection!!!--')
            while fb_param!='1' and fb_param!='':
                if fb_param =='1':
                    fb_rep=int(input('repetitions--> '))
                    fb_thres=int(input('threshold--> '))
                elif fb_param=='':
                    print('module \'ig_h\' DEFAULTS loaded')
                 
                
            


elif start_qs=='':
    print('\n--engaging_defaults--')

#wont continue if 'start_qs' value outside defined params..
else:
    while start_qs!='1' and start_qs!='':
        print('\n--enter specific selection!!!--')
        print('--> \'1\' for custom configs\n--> \'enter\' for defaults')
        start_qs=input('--> ')
        if start_qs=='1':
            print('\n--enable_modules--\n--> 1_ig\n--> 2_fb\n--> 3_yt')
            enable_mod=input('--> ')

        






              
    




    
