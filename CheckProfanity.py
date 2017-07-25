import urllib

def read_text():
    #change file path to the document that needs to be checked
    text = open("C:\Users\Admin\Documents\profanity_check.txt")
    content = text.read()
    return(content)
    text.close()

def check_profanity(text):
    textCheck = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
    result = textCheck.read()
    textCheck.close()
    if "true" in result:
        print("!!! Please revise document, profanity detected.")
    elif "false" in result:
        print("Document safe, no profanity detected.")
    else:
        print("Error: document not scanned properly.")
    
check_profanity(read_text())
