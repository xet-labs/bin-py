import webbrowser
import pyautogui
import time



c1=1
c2=1
c3=1
ain=1
aif=0
browser = webbrowser.get('"C:Program Files\BraveSoftware\Brave-Browser\Application\Brave.exe" %s')


#browser.open_new_tab(url)
while True:
    if ain==0:
        url="https://www.instagram.com/"
        ain=1
        a='ig','1'
    elif ain==1:
        if aif==0:
            url="https://www.facebook.com/watch/"
            ain=0
            aif=1
            
            a='fb_W','3'
        else:
            url="https://www.facebook.com/"
            ain=0
            aif=0
            a='fb_H','2'
        




    webbrowser.open(url)#---driver
    #browser.open_new_tab(url)
    print(a,'--url opened--')

    time.sleep(6)
    pyautogui.hotkey('ctrl','r')
    print('refreshed---1')
    time.sleep(10)
    pyautogui.hotkey('ctrl','r')
    print('refreshed---2')
    time.sleep(10)
    
    while True:
        pyautogui.press('pagedown')
        print(c1,'-',a,'---',c2)
        
        time.sleep(0.8)
        print("time.sleep--0.6")
        c2+=1

        
        if c2==150:
            pyautogui.hotkey('ctrl','w')#close tab
            print('closed------')
            c1+=1
            c2=1
            time.sleep(5)
            
            break

