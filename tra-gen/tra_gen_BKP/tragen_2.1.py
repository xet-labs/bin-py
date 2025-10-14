import webbrowser
import pyautogui
import time
import random


#!--debugging
#>--'0' for disable | else '1' (!any int)--<
maintenance_id={

    
    'startup':1,
    'tab_opener':43




    }
print(maintenance_id)



#--browser_selection-->
browser_hub={



    'brave' : '"C:Program Files\BraveSoftware\Brave-Browser\Application\Brave.exe" %s',
    #'chrome' : '"C:\Program Files\Google\Chrome\Application\chrome.exe" %s',
    
    
    
   }

#--count_vars-->
c1=1 #global_reps




#-------------------DEFINED-FUNCTIONS------------------->



#browser=webbrowser.get('"C:\Program Files\Google\Chrome\Application\chrome.exe" %s')
#print(browser)
def tragen_defaults():
    while True:
        #--browser selection--
        global browser
        for name , browser in browser_hub.items() :
            print("browser:",name,"\npath:",browser)
        
            #browser=webbrowser.get(browser)
            print(browser)
            if c1!=1:
                tab_opener()
           
            
            #--enable|sequence for modules--
            print('\n\n')
            
            seq=2
            
            seq=str(seq)
            print('>>-- seq:',seq,'--')
            
            for seq2 in seq:
                seq2=int(seq2)
                print('seq2:',seq2)
                
                #if c1!=1:
                    #tab_opener()

                #----DEFAULT MODULES---->
                #--ig-->
                if seq2 ==1:
                    ig_h(thres=500,rep=1,time_intv=1,scroll=0)   
                    #ig_h()

                #--fb-->
                if seq2 ==2:
                    fb_w(thres=80,rep=1,time_intv=8,scroll=0)
                    #fb_w()
                
                #--yt-->
                if seq2 ==3:
                    yt_s(thres=250,rep=2,time_intv=2,scroll=0)
                    #yt_s()
                        
                


def startup(url):
   
    id1='startup'

    #--maintenance-->
    
    if id1 in maintenance_id.keys():
        if maintenance_id[id1]==0 or maintenance_id[id1]=='0': 
            print('\n!!!--','maintenance.'+id1,'--\n')
            return
        
    global browser    
    #browser=browser_path

    #--startup_open-->
    time.sleep(4)

    #browser_path=browser
    #webbrowser.get(browser).open_new_tab(url)
    webbrowser.open_new_tab(url)

    print('--url opened--','"',url,'"')
    
    #--refresh-->
    time.sleep(6)
    pyautogui.hotkey('ctrl','r')
    print('refreshed---1')
    time.sleep(10)
    pyautogui.hotkey('ctrl','r')
    print('refreshed---2')
    time.sleep(10)

        
    
def tab_opener():
    id1='tab_opener'

        #--maintenance-->
    if id1 in maintenance_id.keys():
        if maintenance_id[id1]==0 or maintenance_id[id1]=='0': 
            print('\n!!!--','maintenance.'+id1,'--\n')
            return
        
    #-----------------------
    #max_tabs/browser------!!
    #n=int(input('max tabs/browser:')or 20)
    n=20
    #-----------------------
    #breakout_at_max_of_-browserWindow
    #x=int(input('breakout at max of cycles:')or 0)
    x=2


    print("\n***RECAPTURE***")
    print("tabs/browser-",n)
    print("disengage deployment after cycles",x)

        

    browser = webbrowser.get('"C:Program Files\BraveSoftware\Brave-Browser\Application\Brave.exe" %s')
    url1="chrome://newtab"
    url2="instagram.com"
    #tab count
    t=1
    #browser_count
    b=0
    d=1



    while True:
        #time.sleep(.3)
        print("\n\n-->coordinating deployment batch","xv.",d,"...",end='')
        
        #time.sleep(3)#----------------------time_int between browser
        print("\n\ndeploying in T-minus--")
        time.sleep(0.3)
        print("..5")
        time.sleep(0.3)
        print("..4")
        time.sleep(0.2)
        print("..3")
        time.sleep(0.1)
        print("..2")
        time.sleep(0.02)
        print("..")
        time.sleep(0.01)
        print("..")
        #time.sleep()
        print("bo0OM")
        #time.sleep()

        
        #count
        c=0
        
        #open tabs o_0
        browser.open_new_tab(url1)
        
        time.sleep(3)#-----------------time_int after opening browser
        while True:
            time.sleep(.7) #--------------------time_int between tabs

            #keystroke
            pyautogui.keyDown("ctrl")
            pyautogui.press("t")
            pyautogui.keyUp("ctrl")
            print('total_tabs--',t)
            t+=1
            c+=1
            
            if c==n:
                print("closing tab")
                time.sleep(4) #-----------------time_int before closing tabs
                pyautogui.keyDown("alt")
                pyautogui.press("f4")
                pyautogui.keyUp("alt")
                
                #print('--tabs/b--',c)
                
                b+=1
                d+=1
                print("--cycles completed-->",b)
                break
        if x !=0:
            if b==x:
                print("donedanaaaaaaaaaaaaaaaaaaaaa....")
                break



def ig_h(thres=400,rep=4,time_intv=0.3,scroll=-220):

    url="https://www.instagram.com"
   
        
    id1='ig_h'
    print('--',id1,'--')
    



    
    #--count_vars-->
    global c1
    crep=1
    cthres=1
    r1=1
    r2=0
    



    #--startup_url-->
    startup(url)

    #--confirmation-->
    conf=('0_o\n'
          '--arming auto controll--')
    #pyautogui.confirm(conf)
    
    #--corsor_reposition-->
    print('corsor_reposition--1')
    pyautogui.moveTo(490,480)
    pyautogui.click()

    #--driver_code-->
    while True:
        #--dot_difference
        if cthres%2==0:
            dot='..'
        else:
            dot='...'
            
        print(c1,id1,'(',crep,'/',rep,')-(',cthres,'/',thres,')-(intv:',time_intv,'pagdown' if scroll==0 else scroll,')','(rint:',r1,'/',r2,')',dot)
        #print(f"{c1},{id1}({crep}/{rep}) - ({cthres}/{thres}) - (intv:{time_intv}{'pagdown' if scroll==0 else scroll}),(rint:{r1}/{r2}){dot}")
       

        #--scroll length-->
        if scroll==0:
            pyautogui.press('pagedown')
        else:
            pyautogui.scroll(scroll)        
        

        cthres+=1

        #--interval_btwn_scrolldowns-->
        time.sleep(time_intv)


        #--random_double_tap's-->
        if r1<=1:
            r2=random.randrange(80,120,30)
            print('**--to be 2s_tapped after',r2,'--**')
        if r1==r2+1:
            pyautogui.click(button='left',clicks=2,interval=0.4)
            print("**--2s_tapped",r1,'--**')
            r1=0
        r1+=1
        

        #--close tab-->
        if cthres==thres+1: 
            print('--closed--\n\n')
            #time.sleep(4)
            c1+=1
            cthres=1
            crep+=1
            
            #--corsor_reposition-->
            print('corsor_reposition--2')
            pyautogui.moveTo(490,480)
            pyautogui.click()

            if crep!=rep+1:
                #--close_opened_tab-->
                pyautogui.hotkey('ctrl','w')
                startup(url)

            

        #--close function-->   
        if crep==rep+1:
            print('**--EXIT--**\n\n')
            pyautogui.hotkey('ctrl','w')
            #time.sleep(4)
            break

        
        
        
        
    
def fb_w(thres=400,rep=6,time_intv=0.3,scroll=-220):

    #url="https://www.facebook.com/watch"
    url="https://www.facebook.com"


    id1='fb_w'
    print('--',id1,'--')
    
    

    #thres=int(input("enter threshold:"))
    
    #--count_vars-->
    global c1
    crep=1
    cthres=1
    r1=1
    r2=0
    



    #--startup_url-->
    startup(url)

    #--confirmation-->
    #pyautogui.confirm('--arming auto controll--')
    
    #--corsor_reposition-->
    print('corsor_reposition--1')
    pyautogui.moveTo(604,698)
    #pyautogui.click()
    pyautogui.moveTo(460,220)
    pyautogui.click()

    #--driver_code-->
    while True:
        #--dot_difference
        if cthres%2==0:
            dot='..'
        else:
            dot='...'
            
        print(c1,id1,'(',crep,'/',rep,')-(',cthres,'/',thres,')-(intv:',time_intv,'pagedown' if scroll==0 else scroll,')',dot)


        #--scroll length-->
        if scroll==0:
            pyautogui.press('pagedown')
        else:
            pyautogui.scroll(scroll)        
 
        cthres+=1

        #--interval_btwn_scrolldowns-->
        time.sleep(time_intv)

        '''
        #--random_double_tap's-->
        if r1<=1:
            r2=random.randrange(80,120,30)
            print('**--to be 2s_tapped after',r2,'--**')
        if r1==r2+1:
            pyautogui.click(button='left',clicks=2,interval=0.4)
            print("**--2s_tapped",r1,'--**')
            r1=0
        r1+=1
        '''        

        #--close tab-->
        if cthres==thres+1: 
            print('--closed--\n\n')
            #time.sleep(4)
            c1+=1
            cthres=1
            crep+=1
            
            #--corsor_reposition-->
            print('corsor_reposition--2')
            pyautogui.moveTo(604,698)
           # pyautogui.click()
            pyautogui.moveTo(460,220)
            pyautogui.click()

            
            if crep!=rep+1:
                #--close_opened_tab-->
                pyautogui.hotkey('ctrl','w')
                startup(url)

            

        #--close function-->   
        if crep==rep+1:
            print('**--EXIT--**\n\n')
            pyautogui.hotkey('ctrl','w')
            #time.sleep(4)
            break
 




def yt_s(thres=150,rep=4,time_intv=3,scroll=0):

    url="https://www.reddit.com/r/popular/"
    #thres=int(input("enter threshold:"))


    id1='yt_s'
    print('--',id1,'--')


    
    #--count_vars-->
    global c1
    crep=1
    cthres=1
    r1=1
    r2=0
    



    #--startup_url-->
    startup(url)

    #--confirmation-->
    #pyautogui.confirm('--arming auto controll--')
    
    #--corsor_reposition-->
    print('corsor_reposition--1')
    pyautogui.moveTo(490,480)
    #pyautogui.click()

    #--driver_code-->
    while True:
        #--dot_difference
        if cthres%2==0:
            dot='..'
        else:
            dot='...'
            
        print(c1,id1,'(',crep,'/',rep,')-(',cthres,'/',thres,')-(intv:',time_intv,'pagdown' if scroll==0 else scroll,')',dot)



        #--scroll length-->
        if scroll==0:
            pyautogui.press('pagedown')
        else:
            pyautogui.scroll(scroll)        
 
        cthres+=1

        #--interval_btwn_scrolldowns-->
        time.sleep(time_intv)

        '''
        #--random_double_tap's-->
        if r1<=1:
            r2=random.randrange(80,120,30)
            print('**--to be 2s_tapped after',r2,'--**')
        if r1==r2+1:
            pyautogui.click(button='left',clicks=2,interval=0.4)
            print("**--2s_tapped",r1,'--**')
            r1=0
        r1+=1
        '''        

        #--close tab-->
        if cthres==thres+1: 
            print('--closed--\n\n')
            #time.sleep(4)
            c1+=1
            cthres=1
            crep+=1
            
            #--corsor_reposition-->
            print('corsor_reposition--2')
            pyautogui.moveTo(490,480)
            #pyautogui.click()

            
            if crep!=rep+1:
                #--close_opened_tab-->
                pyautogui.hotkey('ctrl','w')
                startup(url)

            

        #--close function-->   
        if crep==rep+1:
            print('**--EXIT--**\n\n')
            pyautogui.hotkey('ctrl','w')
            #time.sleep(4)
            break
#------------------------------------------------------------------




        




def init_qs():
    #-count_var's
    c1=1 #global_reps
    c2=1

    #-program-execution
    print('--> \'1\' for custom configs\n--> \'enter\' for defaults')
    start_qs=''
    start_qs=input('--> ')#!!comment for direct execution-->
    #print('\nstart_qs',start_qs)##

    if start_qs=='1':

        def fenable_mod():
            #-enable modules param
            print('\n--enable_modules--\n--> 1_ig\n--> 2_fb\n--> 3_yt')
            enable_mod=input('--> ')

            #wont continue if 'enable_mod' value outside defined params..
            if enable_mod.isnumeric()==True:
                for i in enable_mod:
                    i=int(i)
                    if i>3 or i<1:
                        print('\n--enter defined value for \'enable_modules\'--')
                        fenable_mod()
                
                
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


            
            else:
                print('\n--unexpected character!!--\n--enter defined value--')
                fenable_mod()


            
        #-initiating modules function
        fenable_mod()                 
                    
                


    elif start_qs=='':
        print('\n--engaging_defaults--')
        tragen_defaults()

    #wont continue if 'start_qs' value outside defined params..
    else:
        while start_qs!='1' and start_qs!='':
            print('\n--enter specific selection !!!--')
            init_qs()

        
init_qs()
#ig_h()




              
    




    
