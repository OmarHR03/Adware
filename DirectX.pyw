import webbrowser
from threading import Timer
import time


def openTabs():
    new = 1
    url="https://www.facebook.com/"
    webbrowser.open(url, new=new)
    webbrowser.open_new("http://www.prada.com/en.html?cc=CA")
    webbrowser.open_new("http://web2.vegasworld.com/fx/?utm_campaign=google_slots&utm_medium=cpc&utm_source=google")
    webbrowser.open_new("https://www.miniclip.com/games/en/")
    webbrowser.open_new("https://www.youtube.com/watch?v=48rz8udZBmQ")
        

    


starttime = time.time()
while True:
    t = Timer(300.0,openTabs)
    t.start()
    time.sleep(15.0 - (time.time() % 15.0))
