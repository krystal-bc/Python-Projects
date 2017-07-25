import time
import webbrowser
import ctypes

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxA(0, text, title, style)


numBreaks = 0

print("Timer started "+ time.ctime()+ ". Press Ctrl+C in Shell to terminate.")
while (numBreaks < 3):
    time.sleep(2*60*60)
    #print("Time to take break #"+str(numBreaks+1))
    Mbox('Hi busy bee', 'Time to take break #'+str(numBreaks+1), 1)
    #webbrowser.open("https://www.youtube.com/watch?v=0CSKB7CzrZU")
    print("Break message "+str(numBreaks+1)+" sent "+ time.ctime())
    numBreaks = numBreaks + 1

print("Program terminated "+ time.ctime())
