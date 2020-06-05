# Tool Name :- Tool-X
# Author :- Rajkumar dusad
# Date :- 1/11/2017

import os
import sys
from time import sleep
from modules.logo import *
from modules.system import *

# Set a CLI color
    GR = "\033[32m" # green color
    RD = "\033[31m" # red color
    RS = "\033[m" # Reset color
    
class tool:
  @classmethod
  def install(self):
    while True:
      system=sys()
      os.system("clear")
      logo.ins_tnc()
      inp=input("GR Do you want to install CyberCat [Y/n]> RS")
      if inp=="y" or inp=="Y":
        os.system("clear")
        logo.installing()
        if system.sudo is not None:
          
          #require root permission
          if os.path.exists(system.conf_dir+"/CAT"):
            pass
          else:
            os.system(system.sudo+" mkdir "+system.conf_dir+"/CAT")
          os.system(system.sudo+" cp -r modules core CAT.py "+system.conf_dir+"/CAT")
          os.system(system.sudo+" cp -r core/CAT "+system.bin)
          
          os.system(system.sudo+" chmod +x "+system.bin+"/CAT")
          
          os.system("cd .. && "+system.sudo+" rm -rf CAT")
          if os.path.exists(system.bin+"/CAT") and os.path.exists(system.conf_dir+"/CAT"):
            os.system("clear")
            logo.ins_sc()
            tmp=input("RS[GR*RS]GR Choose :RS ")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input("")
            break
        else:
          if os.path.exists(system.conf_dir+"/CAT"):
            pass
          else:
            os.system("mkdir "+system.conf_dir+"/CAT")
          os.system("cp -r modules core CAT.py "+system.conf_dir+"/CAT")
          os.system("cp -r core/CAT "+system.bin)
          os.system("cp -r core/CAT "+system.bin)
          os.system("chmod +x "+system.bin+"/CAT")
          os.system("cd .. && rm -rf CAT")
          if os.path.exists(system.bin+"/CAT") and os.path.exists(system.conf_dir+"/CAT"):
            os.system("clear")
            logo.ins_sc()
            tmp=input("RS[GR*RS]GR Choose :RS")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input("RS[GR*RS]GR Choose :RS")
            break
      else:
        break

if __name__=="__main__":
  try:
    tool.install()
  except KeyboardInterrupt:
    os.system("clear")
    logo.exit()
