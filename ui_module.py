from tkinter import *
import tkinter .font
import tkinter as tk
import webbrowser
import random
import urllib.request # import for the HTTP GET responses
import json # import json handling
import urllib.parse
import re
import api_module
import bank_module


#start root

##Creates the window from the imported Tkinter module
root = tk.Tk()

##Creates the size of the Window (root) set to touchscreen size
root.geometry("800x480")

##Creates the title of the Window (root)
root.title("Fortune Teller")

#Creates background color for Window (root)
root.configure(background='#7f0e9e')

#end root

#Creating the root frame labels
welcome = Label(root, text = "WELCOME TO OUR FORTUNE TELLER! \n\n\nPLEASE INSERT:", background = '#7f0e9e', foreground = '#000000', font = ("Helvetica", 21))
welcome.pack()

dollarSign = Label(root, text = "$", background = '#7f0e9e', foreground = '#000000', font = ("Helvetica", 21))
dollarSign.place(x = 357, y = 210)

#varaibles that connect to representive labels that display amount and strings
coinTotal = DoubleVar()
coinTotal.set(0.0)
zeroCoins = DoubleVar()
zeroCoins.set(0.0)
listDime = [" "]
listDime = StringVar()
listDime.set(" ")
listPenney = StringVar()
listPenney.set(" ")
listNickel = StringVar()
listNickel.set(" ")
listQuater = StringVar()
listQuater.set(" ")
negativeCoins = DoubleVar()
negativeCoins.set(0.0)
aries = StringVar()
aries.set(" ")

#functions to make the gui work pretty self explanatory here
def penney():
    global coinTotal
    coinTotal.set(round(coinTotal.get() + 0.01, 2))
    
def nickel():
    global coinTotal
    coinTotal.set(round(coinTotal.get() + 0.05, 2))

def dime():
    global coinTotal
    coinTotal.set(round(coinTotal.get() + 0.10, 2))  

def quater():
    global coinTotal
    coinTotal.set(round(coinTotal.get() + 0.25, 2))

def sendYesNo():
    global listPenney
    listPenney.set("")
    global coinTotal
    global zeroCoins
    global negativeCoins
    negativeCoins.set(0.01)
    if(coinTotal.get() <= zeroCoins.get()):
        listPenney.set("Low balance insert coins.")
    elif(coinTotal.get() - negativeCoins.get() < zeroCoins.get()):
        listPenney.set("Low balance insert coins.")
    else:    
        coinTotal.set(round(coinTotal.get() - 0.01, 2))
        listPenney
        listYesNo = ["Yes", "No"]
        ranListYesNo = random.choice(listYesNo)
        listPenney.set(listPenney.get() + ranListYesNo + "\n")


def factWebsite():
    global listNickel
    global coinTotal
    global zeroCoins
    global negativeCoins
    negativeCoins.set(0.05)
    if(coinTotal.get() <= zeroCoins.get()):
        listNickel.set("Low balance insert coins.")
    elif(coinTotal.get() - negativeCoins.get() < zeroCoins.get()):
        listNickel.set("Low balance insert coins.")
    else:
        coinTotal.set(round(coinTotal.get() - 0.05, 2))
        webbrowser.open('https://www.beagreatteacher.com/daily-fun-fact/') 

def sendAdvice():
    global listDime
    listDime.set("")
    global coinTotal
    global zeroCoins
    global negativeCoins
    negativeCoins.set(0.10)
    if(coinTotal.get() <= zeroCoins.get()):
        listDime.set("Low balance insert coins.")
    elif(coinTotal.get() - negativeCoins.get() < zeroCoins.get()):
        listDime.set("Low balance insert coins.")
    else:
        coinTotal.set(round(coinTotal.get() - 0.10, 2))
        listDime
        listAdvice = ["Drop out of college", "Cheat on your signficant other", "Theres always alcohol", "Coin Readers Suck",
                      "Only your mom Loves you", "Tinder never let you down"]
        ranListAdvice = random.choice(listAdvice)
        listDime.set(listDime.get() + ranListAdvice + "\n")
         
def capricorn():
    global listQuater
    global coinTotal
    global zeroCoins
    global negativeCoins
    negativeCoins.set(0.25)
    if(coinTotal.get() <= zeroCoins.get()):
        listQuater.set("Low balance insert coins.")
    elif(coinTotal.get() - negativeCoins.get() < zeroCoins.get()):
        listQuater.set("Low balance insert coins.")
    else:
        coinTotal.set(round(coinTotal.get() - 0.25, 2))
        webbrowser.open('https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=10')
    
def aquarius():
    global listQuater
    global coinTotal
    global zeroCoins
    global negativeCoins
    negativeCoins.set(0.25)
    if(coinTotal.get() <= zeroCoins.get()):
        listQuater.set("Low balance insert coins.")
    elif(coinTotal.get() - negativeCoins.get() < zeroCoins.get()):
        listQuater.set("Low balance insert coins.")
    else:
        coinTotal.set(round(coinTotal.get() - 0.25, 2))
        webbrowser.open('https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=11')
    
def pisces():
    global listQuater
    global coinTotal
    global zeroCoins
    global negativeCoins
    negativeCoins.set(0.25)
    if(coinTotal.get() <= zeroCoins.get()):
        listQuater.set("Low balance insert coins.")
    elif(coinTotal.get() - negativeCoins.get() < zeroCoins.get()):
        listQuater.set("Low balance insert coins.")
    else:
        coinTotal.set(round(coinTotal.get() - 0.25, 2))
        webbrowser.open('https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=12')
    
def aries():
    global aries
    global listHoroscope
    global readAries
    global listQuater
    global coinTotal
    global zeroCoins
    global negativeCoins
    negativeCoins.set(0.25)
    if(coinTotal.get() <= zeroCoins.get()):
        listQuater.set("Low balance insert coins.")
    elif(coinTotal.get() - negativeCoins.get() < zeroCoins.get()):
        listQuater.set("Low balance insert coins.")
    else:
        coinTotal.set(round(coinTotal.get() - 0.25, 2))
#creating and writing html of the webiste to the file
        urllib.request.urlretrieve("https://www.astrology.com/horoscope/daily/aries.html", "HTML.txt")
        html = open("HTML.txt")
        deleteLines = open("deleteLines.txt", "w")
#opening the test file and writing to a new file with the removed html tags
        lines = html.readlines()
        deleteLines.writelines(lines[374:-368])

        html.close()
        deleteLines.close()

        deleteLines = open("deleteLines.txt")
        noHTML = open("noHTML.txt", "w")

        for line in deleteLines:
            noHTML.write(re.sub(r'<[^>]+>'," ", line))

        deleteLines.close()
        noHTML.close()

        
        
        
        #noHTML = open("noHTML.txt")
        #aries=str(noHTML.read())
       
        
       
        #T=Text(horoscopeChoices, height =2, width=30)
        #T.pack()
        #T.insert(tk.END, aries)
        
        
        #print(aries)
       
def taurus():
    global listQuater
    global coinTotal
    global zeroCoins
    global negativeCoins
    negativeCoins.set(0.25)
    if(coinTotal.get() <= zeroCoins.get()):
        listQuater.set("Low balance insert coins.")
    else:
        coinTotal.set(round(coinTotal.get() - 0.25, 2))
        webbrowser.open('https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=2')
    
def gemini():
    global listQuater
    global coinTotal
    global zeroCoins
    global negativeCoins
    negativeCoins.set(0.25)
    if(coinTotal.get() <= zeroCoins.get()):
        listQuater.set("Low balance insert coins.")
    elif(coinTotal.get() - negativeCoins.get() < zeroCoins.get()):
        listQuater.set("Low balance insert coins.")
    else:
        coinTotal.set(round(coinTotal.get() - 0.25, 2))
        webbrowser.open('https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=3')
    
def cancer():
    global listQuater
    global coinTotal
    global zeroCoins
    global negativeCoins
    negativeCoins.set(0.25)
    if(coinTotal.get() <= zeroCoins.get()):
        listQuater.set("Low balance insert coins.")
    elif(coinTotal.get() - negativeCoins.get() < zeroCoins.get()):
        listQuater.set("Low balance insert coins.")
    else:
        coinTotal.set(round(coinTotal.get() - 0.25, 2))
        webbrowser.open('https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=4')
    
def leo():
    global listQuater
    global coinTotal
    global zeroCoins
    global negativeCoins
    negativeCoins.set(0.25)
    if(coinTotal.get() <= zeroCoins.get()):
        listQuater.set("Low balance insert coins.")
    elif(coinTotal.get() - negativeCoins.get() < zeroCoins.get()):
        listQuater.set("Low balance insert coins.")
    else:
        coinTotal.set(round(coinTotal.get() - 0.25, 2))
        webbrowser.open('https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=5')
    
def virgo():
    global listQuater
    global coinTotal
    global zeroCoins
    global negativeCoins
    negativeCoins.set(0.25)
    if(coinTotal.get() <= zeroCoins.get()):
        listQuater.set("Low balance insert coins.")
    elif(coinTotal.get() - negativeCoins.get() < zeroCoins.get()):
        listQuater.set("Low balance insert coins.")
    else:
        coinTotal.set(round(coinTotal.get() - 0.25, 2))
        webbrowser.open('https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=6')
    
def libra():
    global listQuater
    global coinTotal
    global zeroCoins
    global negativeCoins
    negativeCoins.set(0.25)
    if(coinTotal.get() <= zeroCoins.get()):
        listQuater.set("Low balance insert coins.")
    elif(coinTotal.get() - negativeCoins.get() < zeroCoins.get()):
        listQuater.set("Low balance insert coins.")
    else:
        coinTotal.set(round(coinTotal.get() - 0.25, 2))
        webbrowser.open('https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=7')
    
def scorpio():
    global listQuater
    global coinTotal
    global zeroCoins
    global negativeCoins
    negativeCoins.set(0.25)
    if(coinTotal.get() <= zeroCoins.get()):
        listQuater.set("Low balance insert coins.")
    elif(coinTotal.get() - negativeCoins.get() < zeroCoins.get()):
        listQuater.set("Low balance insert coins.")
    else:
        coinTotal.set(round(coinTotal.get() - 0.25, 2))
        webbrowser.open('https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=8')
    
def sagittarius():
    global listQuater
    global coinTotal
    global zeroCoins
    global negativeCoins
    negativeCoins.set(0.25)
    if(coinTotal.get() <= zeroCoins.get()):
        listQuater.set("Low balance insert coins.")
    elif(coinTotal.get() - negativeCoins.get() < zeroCoins.get()):
        listQuater.set("Low balance insert coins.")
    else:
        coinTotal.set(round(coinTotal.get() - 0.25, 2))
        webbrowser.open('https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=9')
#end functions

#label to display the total amount left root
totalDisplay = Label(root, textvariable = coinTotal, background = '#7f0e9e', foreground = '#000000', font = ("Helvetica", 21))
totalDisplay.place(x = 375, y = 210)

#Creating a function that will create the second frame which is the select menu
def opition():
#Designing the frame
    opition = Toplevel(root)
    opition.geometry("800x480")
    opition.configure(background='#7f0e9e')
#Adding labels to the frame
    labelSelect = Label(opition, text = "PLEASE SELECT AN OPITION BELOW!", background = '#7f0e9e', foreground = '#000000', font = ("Helvetica", 21))
    labelSelect.pack()
    labelMenu = Label(opition, text = "YES or NO - $0.01 \nRANDOM FACT - $0.05 \nADVICE - $0.10 \nHOROSCOPE - $0.25",
                      background = '#7f0e9e', foreground = '#000000', font = ("Helvetica", 21))
    labelMenu.pack()
    
    dollarSign = Label(opition, text = "$", background = '#7f0e9e', foreground = '#000000', font = ("Helvetica", 21))
    dollarSign.place(x = 355, y = 200)
    totalDisplay = Label(opition, textvariable = coinTotal, background = '#7f0e9e', foreground = '#000000', font = ("Helvetica", 21))
    totalDisplay.place(x = 375, y = 200)
    
#Creating the buttons to select an opition
    yesOrNoMenu = Button(opition, text = "YES OR NO", height = 3, width = 12, command = yn, background = '#7f0e9e', foreground = '#000000')
    yesOrNoMenu.place(x = 213, y = 260)

    randomFactMenu = Button(opition, text = "RANDOM FACT", height = 3, width = 12, command = fact, background = '#7f0e9e', foreground = '#000000')
    randomFactMenu.place(x = 307, y = 260)

    adviceMenu = Button(opition, text = "ADVICE", height = 3, width = 12, command = advice, background = '#7f0e9e', foreground = '#000000')
    adviceMenu.place(x = 401, y = 260)

    horoscopeMenu = Button(opition, text = "HOROSCOPE", height = 3, width = 12, command = horoscopeChoices, background = '#7f0e9e', foreground = '#000000')
    horoscopeMenu.place(x = 494, y = 260)

    opition.mainloop()

def yn():
#designing frame yn
    yn = Toplevel(root)
    yn.geometry("800x480")
    yn.configure(background='#7f0e9e')
#Adding labels to the frame
    labelYesNo = Label(yn, text = "YES OR NO", background = '#7f0e9e', foreground = '#000000', font = ("Helvetica", 21))
    labelYesNo.pack()
    dollarSign = Label(yn, text = "$", background = '#7f0e9e', foreground = '#000000', font = ("Helvetica", 21))
    dollarSign.place(x = 354, y = 100)
    totalDisplay = Label(yn, textvariable = coinTotal, background = '#7f0e9e', foreground = '#000000', font = ("Helvetica", 21))
    totalDisplay.place(x = 374, y = 100)
#Adding the Yes or No Button
    yesNoButton = Button(yn, text = "CLICK FOR YES OR NO", height = 6, width = 19, command = sendYesNo, background = '#7f0e9e', foreground = '#000000')
    yesNoButton.place(x = 330, y = 310)
    listYesNo = Label(yn, textvariable = listPenney, background = '#7f0e9e', foreground = '#000000', font = ("Helvetica", 21))
    listYesNo.place(x = 246, y = 210)

    yn.mainloop()

def fact():
#desiging fact frame
    fact = Toplevel(root)
    fact.geometry("800x480")
    fact.configure(background='#7f0e9e')
#Adding labels to the frame
    labelFact = Label(fact, text = "FACT\n\n\n", background = '#7f0e9e', foreground = '#000000', font = ("Helvetica", 21))
    labelFact.pack()
    dollarSign = Label(fact, text = "$", background = '#7f0e9e', foreground = '#000000', font = ("Helvetica", 21))
    dollarSign.place(x = 354, y = 100)
    totalDisplay = Label(fact, textvariable = coinTotal, background = '#7f0e9e', foreground = '#000000', font = ("Helvetica", 21))
    totalDisplay.place(x = 374, y = 100)
    factButton = Button(fact, text = "CLICK FOR FACT WEBSITE", height = 6, width = 19, command = factWebsite, background = '#7f0e9e', foreground = '#000000')
    factButton.place(x = 330, y = 310)
    listFact = Label(fact, textvariable = listNickel, background = '#7f0e9e', foreground = '#000000', font = ("Helvetica", 21))
    listFact.place(x = 240, y = 240)

    fact.mainloop()

def advice():
#designing advice frame
    advice = Toplevel(root)
    advice.geometry("800x480")
    advice.configure(background='#7f0e9e')
#Adding labels to the frame
    labelAdvice = Label(advice, text = "HERE IS YOUR ADVICE", background = '#7f0e9e', foreground = '#000000', font = ("Helvetica", 21))
    labelAdvice.pack()
    dollarSign = Label(advice, text = "$", background = '#7f0e9e', foreground = '#000000', font = ("Helvetica", 21))
    dollarSign.place(x = 354, y = 100)
    totalDisplay = Label(advice, textvariable = coinTotal, background = '#7f0e9e', foreground = '#000000', font = ("Helvetica", 21))
    totalDisplay.place(x = 374, y = 100)
    adviceButton = Button(advice, text = "CLICK FOR ADVICE", height = 6, width = 19, command = sendAdvice, background = '#7f0e9e', foreground = '#000000')
    adviceButton.place(x = 330, y = 310)
    listAdvice = Label(advice, textvariable = listDime, background = '#7f0e9e', foreground = '#000000', font = ("Helvetica", 21))
    listAdvice.place(x = 250, y = 240)

#closing the advice frame loop
    advice.mainloop()

def horoscopeChoices():
#desiging the horscope frame
    horoscopeChoices = Toplevel(root)
    horoscopeChoices.geometry("800x480")
    horoscopeChoices.configure(background='#7f0e9e')
#Adding labels to the horscope frame
    labelHoroscope = Label(horoscopeChoices, text = "HOROSCOPE", background = '#7f0e9e', foreground = '#000000', font = ("Helvetica", 21))
    labelHoroscope.pack()
    dollarSign = Label(horoscopeChoices, text = "$", background = '#7f0e9e', foreground = '#000000', font = ("Helvetica", 21))
    dollarSign.place(x = 354, y = 100)
    totalDisplay = Label(horoscopeChoices, textvariable = coinTotal, background = '#7f0e9e', foreground = '#000000', font = ("Helvetica", 21))
    totalDisplay.place(x = 374, y = 100)
    #T=tk.=Text(horoscopeChoices, height =2, width=30)
    #T.pack()
    #T.insert(tk.END, aries)

    textAries=Text(horoscopeChoices, height=7,width=100)
    textAries.pack()
    with open("noHTML.txt", "r") as aries:
            textAries.insert(INSERT, aries.read())
        
    
#buttons for the horscope choices to be selected    
    capricornButton = Button(horoscopeChoices, text = "CLICK FOR\n CAPRICORN", height = 6, width = 15, command = capricorn, background = '#7f0e9e', foreground = '#000000')
    capricornButton.place(x = 59, y = 240)
   
    aquariusButton = Button(horoscopeChoices, text = "CLICK FOR\n AQUARIUS", height = 6, width = 15, command = aquarius, background = '#7f0e9e', foreground = '#000000')
    aquariusButton.place(x = 173, y = 240)
    
    piscesButton = Button(horoscopeChoices, text = "CLICK FOR\n PISCES", height = 6, width = 15, command = pisces, background = '#7f0e9e', foreground = '#000000')
    piscesButton.place(x = 287, y = 240)
    
    ariesButton = Button(horoscopeChoices, text = "CLICK FOR\n ARIES", height = 6, width = 15, command = aries, background = '#7f0e9e', foreground = '#000000')
    ariesButton.place(x = 401, y = 240)
    
    taurusButton = Button(horoscopeChoices, text = "CLICK FOR\n TAURUS", height = 6, width = 15, command = taurus, background = '#7f0e9e', foreground = '#000000')
    taurusButton.place(x = 515, y = 240)
    
    geminiButton = Button(horoscopeChoices, text = "CLICK FOR\n GEMINI", height = 6, width = 15, command = gemini, background = '#7f0e9e', foreground = '#000000')
    geminiButton.place(x = 629, y = 240)
    
    cancerButton = Button(horoscopeChoices, text = "CLICK FOR\n CANCER", height = 6, width = 15, command = cancer, background = '#7f0e9e', foreground = '#000000')
    cancerButton.place(x = 59, y = 340)
    
    leoButton = Button(horoscopeChoices, text = "CLICK FOR\n LEO", height = 6, width = 15, command = leo, background = '#7f0e9e', foreground = '#000000')
    leoButton.place(x = 173, y = 340)
    
    virgoButton = Button(horoscopeChoices, text = "CLICK FOR\n VIRGO", height = 6, width = 15, command = virgo, background = '#7f0e9e', foreground = '#000000')
    virgoButton.place(x = 287, y = 340)
    
    libraButton = Button(horoscopeChoices, text = "CLICK FOR\n LIBRA", height = 6, width = 15, command = libra, background = '#7f0e9e', foreground = '#000000')
    libraButton.place(x = 401, y = 340)
    
    scorpioButton = Button(horoscopeChoices, text = "CLICK FOR\n SCORPIO", height = 6, width = 15, command = scorpio, background = '#7f0e9e', foreground = '#000000')
    scorpioButton.place(x = 515, y = 340)
    
    sagittariusButton = Button(horoscopeChoices, text = "CLICK FOR\n SAGITTARIUS", height = 6, width = 15, command = sagittarius, background = '#7f0e9e', foreground = '#000000')
    sagittariusButton.place(x = 629, y = 340)
#end buttons for horoscope

    listHoroscope = Label(horoscopeChoices, textvariable = listQuater, background = '#7f0e9e', foreground = '#000000', font = ("Helvetica", 21))
    listHoroscope.place(x = 250, y = 170)

    horoscopeChoices.mainloop()
    
#These are the button for the first frame
penney = Button(root, text = "PENNEY", height = 3, width = 12, command = penney, background = '#7f0e9e', foreground = '#000000')
penney.place(x = 213, y = 280)

nickel = Button(root, text = "NICKEL", height = 3, width = 12, command = nickel, background = '#7f0e9e', foreground = '#000000')
nickel.place(x = 307, y = 280)

dime = Button(root, text = "DIME", height = 3, width = 12, command = dime, background = '#7f0e9e', foreground = '#000000')
dime.place(x = 401, y = 280)

quater = Button(root, text = "QUATER", height = 3, width = 12, command = quater, background = '#7f0e9e', foreground = '#000000')
quater.place(x = 495, y = 280)

opition = Button(root, text = "DONE INSERTING", height = 3, width = 12, command = opition, background = '#7f0e9e', foreground = '#000000')
opition.place(x = 357, y = 360)

#closes the root loop
root.mainloop()
#closes the python code  
main()