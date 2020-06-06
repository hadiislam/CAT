

import os
import sys
from time import sleep
from modules.logo import *
from modules.system import *

    
class tool:
  @classmethod
  def install(self):
    while True:
      system=sys()
      os.system("clear")
      logo.ins_tnc()
      inp=input("\033[32m Do you want to install CyberCat [Y/n]> \033[m")
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
            tmp=input("\033[m[\033[32m*\033[m]\033[32m Choose :\033[m ")
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
            tmp=input("\033[m[\033[32m*\033[m]\033[32m Choose :\033[m")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input("\033[m[\033[32m*\033[m]\033[32m Choose :\033[m")
            break
      else:
        break

if __name__=="__main__":
  try:
    tool.install()
  except KeyboardInterrupt:
    os.system("clear")
    logo.exit()
