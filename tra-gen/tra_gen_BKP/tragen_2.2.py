import webbrowser
import pyautogui
import time
import random

'''
#!--debugging
#>>- '0' for disable else empty -<<
class debug:
    debugall='0'
    startup=0

'''


#--browser_selection-->
        #"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe" --profile-directory="Profile 1"
#def_browser=str('C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe" --profile-directory="Profile 1') 
#browser = webbrowser.get('def_browser%s')
browser = webbrowser.get('"C:Program Files\BraveSoftware\Brave-Browser\Application\Brave.exe" %s')




#--count_vars-->
c1=1 #global_reps







#-------------------DEFINED-FUNCTIONS------------------->


def startup(url):
    pass
    id1='startup'
    '''    
    #--maintenance-->
    id1=id1.debug()
    if id1.startup=='0' or id1.debugall=='0':
        pass
    '''

    #--startup_open-->
    time.sleep(4)
    webbrowser.open_new(url)
    print('--url opened--','"',url,'"')
    
    #--refresh-->
    time.sleep(6)
    pyautogui.hotkey('ctrl','r')
    print('refreshed---1')
    time.sleep(10)
    pyautogui.hotkey('ctrl','r')
    print('refreshed---2')
    time.sleep(10)

        
def scrool_page(scrool):
    if scroll=='0':
        pyautogui.press('pagedown')
    else:
        pyautogui.scroll(scroll)        
        
    
def ig_h(thres=200,rep=8,scroll_len=0.5,):
    
    url="https://www.instagram.com"

    #thres=int(input("enter threshold:"))
    
    #--count_vars-->
    global c1
    crep=1
    cthres=1
    r1=0
    r2=0
    
    id1='ig_h'

    #--startup_url-->
    startup(url)

    #--confirmation-->
    #pyautogui.confirm('--arming auto controll--')
    
    #--corsor_reposition-->
    print('corsor_reposition--1')
    pyautogui.moveTo(490,480)
    pyautogui.click()

    #--driver_code-->
    while True:

        print(c1,id1,'(',crep,'/',rep,')-','(',cthres,'/',thres,')--','(rint_count_',r1,'-',r2,'_rint_target'')')


        #--scroll length-->
        if scroll_len=='0':
            pyautogui.press('pagedown')
        else:
            pyautogui.scroll(scroll_len) 



        cthres+=1

        #--interval_btwn_scrolldowns-->
        time.sleep(0.3)


        #--random_double_tap's-->
        if r1<=1:
            r2=random.randrange(80,120,30)
            print('**--to be 2s_tapped after',r2,'--**')
        if r1==r2:
            pyautogui.click(button='left',clicks=2,interval=0.4)
            print("**--2s_tapped",r1,'--**')
            r1=0
        r1+=1
        

        #--close tab-->
        if cthres==thres: 
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

        
        
        
        
        
    

def fb_w(thres=200,rep=6):
    url="https://www.facebook.com/watch"
    
    #thres=int(input("enter threshold:"))
    
    #--count_vars-->
    global c1
    crep=1
    cthres=1
    r1=0
    r2=0
    
    id1='fbw'

    #--startup_url-->
    startup(url)

    #--confirmation-->
    #pyautogui.confirm('--arming auto controll--')
    
    #--corsor_reposition-->
    print('corsor_reposition--1')
    pyautogui.moveTo(490,480)
    pyautogui.click()

    #--driver_code-->
    while True:

        print(c1,id1,'(',crep,'/',rep,')-','(',cthres,'/',thres,')--')


        #--scroll length-->
        pyautogui.scroll(-200)

        cthres+=1

        #--interval_btwn_scrolldowns-->
        time.sleep(0.5)

        '''
        #--random_double_tap's-->
        if r1<=1:
            r2=random.randrange(80,120,30)
            print('**--to be 2s_tapped after',r2,'--**')
        if r1==r2:
            pyautogui.click(button='left',clicks=2,interval=0.4)
            print("**--2s_tapped",r1,'--**')
            r1=0
        r1+=1
        '''        

        #--close tab-->
        if cthres==thres: 
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
 




def yt_s(thres=150,rep=4,):
    url="https://www.youtube.com/shorts"
#thres=int(input("enter threshold:"))
    
    #--count_vars-->
    global c1
    crep=1
    cthres=1
    r1=0
    r2=0
    
    id1='yt_s'

    #--startup_url-->
    startup(url)

    #--confirmation-->
    #pyautogui.confirm('--arming auto controll--')
    
    #--corsor_reposition-->
    print('corsor_reposition--1')
    pyautogui.moveTo(490,480)
    pyautogui.click()

    #--driver_code-->
    while True:

        print(c1,id1,'(',crep,'/',rep,')-','(',cthres,'/',thres,')--')


        #--scroll length-->
        #pyautogui.scroll(-200)
        pyautogui.press('pagedown')

        cthres+=1

        #--interval_btwn_scrolldowns-->
        time.sleep(3)

        '''
        #--random_double_tap's-->
        if r1<=1:
            r2=random.randrange(80,120,30)
            print('**--to be 2s_tapped after',r2,'--**')
        if r1==r2:
            pyautogui.click(button='left',clicks=2,interval=0.4)
            print("**--2s_tapped",r1,'--**')
            r1=0
        r1+=1
        '''        

        #--close tab-->
        if cthres==thres: 
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
#------------------------------------------------------------------





def tragen_defaults():
    dig_h=
    while True:
        #if c1!=1:
            #print('\n\n\n')
        print('yt_s')
        yt_s()

        
        print('fb_w')
        fb_w()

            
        print('ig_h')
        ig_h()

        




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




              
    




    
