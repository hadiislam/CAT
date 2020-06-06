# Set a CLI color
   # \033[32m = Green color
   # \033[31m = red color
   # \033[m = Reset color



class logo:
  @classmethod
  def tool_header(self):
    print('''

\033[m
      
  ____      _                ____      _   
 / ___|   _| |__   ___ _ __ / ___|__ _| |_ 
| |  | | | | '_ \ / _ \ '__| |   / _` | __|
| |__| |_| | |_) |  __/ |  | |__| (_| | |_ 
 \____\__, |_.__/ \___|_|   \____\__,_|\__|
      |___/                    \033[32mVersion \033[31m3.5           

\033[m============================================= \033[m ''')

  @classmethod
  def tool_footer(self):
    print('''
''')


  @classmethod
  def not_ins(self):
    self.tool_header()
    print ('''
\033[31m[ + ]  \033[m We can't install CyberCat. \033[m
\033[31m[ + ]  \033[m There are some error. \033[m
\033[31m[ + ]  \033[m Please try again after some time. \033[m ''')
\033[m[\033[32m0\033[m]  For Back.
    self.tool_footer()

  @classmethod
  def ins_tnc(self):
    self.tool_header()
    print ('''
\033[31m[ + ] \033[m Use It At Your Own Risk.
\033[31m[ + ] \033[m No Warranty.
\033[31m[ + ] \033[m Use it legal purpose only.
\033[31m[ + ] \033[m We are not responsible for your actions.
\033[31m[ + ] \033[m Do not do things that are forbidden.
\033[31m If you are installing this tool.
 That means you are agree with all terms.

\033[m[\033[32m0\033[m]  For Back.     ''')
    self.tool_footer()

  @classmethod
  def ins_sc(self):
    self.tool_header()
    print ('''
\033[31m[ + ] \033[m CyberCat installed successfully.
\033[31m[ + ] \033[m To run CyberCat.
\033[31m[ + ] \033[m Type CAT in your terminal.''')
    self.tool_footer()

  @classmethod
  def update(self):
    self.tool_header()
    print ('''
\033[m[\033[32m1\033[m]  Update your CyberCat.
\033[m[\033[32m0\033[m]  For Back.''')
    self.tool_footer()

  @classmethod
  def updated(self):
    self.tool_header()
    print ('''
\033[m[ + ] \033[32mCyberCat Updated Successfully.
\033[m[ + ] \033[32mPress Enter and Restart CyberCat
      to continue.\033[m''')
    self.tool_footer()

  @classmethod
  def nonet(self):
    self.tool_header()
    print ('''
\033[31m[ + ]  \033[mNo network connection?
\033[31m[ + ]  \033[mAre you offline?
\033[31m[ + ]  \033[mPlease try again after some time.
\033[m[\033[32m0\033[m]  For Back.   ''')
    self.tool_footer()

  @classmethod
  def update_error(self):
    self.tool_header()
    print ('''
\033[31m[ + ]  \033[mWe can't Update CyberCat.
\033[31m[ + ]  \033[mPlease try again after some time.
\033[m[\033[32m0\033[m]  For Back.    ''')
    self.tool_footer()


  @classmethod
  def about(self,total):
    self.tool_header()
    print (f'''
\033[32m[ + ] Tool Name :- \033[mCyberCat
\033[32m[ + ] Author :- \033[m Hadi
\033[32m[ + ] Tools :- \033[mtotal {total} tools.
\033[32m[ + ] \033[32mCyberCat is automatic tool installer.
\033[32m[ + ] \033[32mMade for termux and linux based system.
\033[32m[ + ] Note :- Use this tool at your own risk.

\033[m[\033[32m0\033[m]  For Back.''')
    self.tool_footer()


  @classmethod
  def install_tools(self):
    print ("""\033[m[\033[32m * \033[m]\033[32m Select Your Tool : \033[m """)

  @classmethod
  def already_installed(self,name):
    self.tool_header()
    print(f'''
\033[31m[ + ] \033[m Sorry ??
\033[31m[ + ] \033[32m'{name}' \033[mis already Installed !!
''')
    self.tool_footer()

  @classmethod
  def installed(self,name):
    self.tool_header()
    print(f'''
\033[32m[ + ] \033[mInstalled Successfully !!
\033[32m[ + ] \033[31m'{name}' \033[mis Installed Successfully !!
\033[m[\033[32m0\033[m]  For Back.     ''')
    self.tool_footer()

  @classmethod
  def not_installed(self,name):
    self.tool_header()
    print(f'''
\033[31m[ + ] \033[mSorry ??
\033[31m[ + ] '{name}'\033[m is not Installed !!
\033[m[\033[32m0\033[m]  For Back.''')
    self.tool_footer()

  @classmethod
  def back(self):
    print ("""\
[ 00 ] Back
 """)

  @classmethod
  def updating(self):
    print ("""\033[m \033[m[\033[32m*\033[m]\033[32m Updating CyberCat \033[m """)

  @classmethod
  def installing(self):
    print ("""\033[m[\033[32m*\033[m]\033[32m Installing.. \033[m """)

  @classmethod
  def menu(self,total):
    self.tool_header()
    print (f'''
\033[m[ \033[32m1 \033[m] Show all tools.
\033[m[ \033[32m2 \033[m] Tools Category.
\033[m[ \033[32m3 \033[m] Update CyberCat.
\033[m[ \033[32m4 \033[m] About Us.
\033[m[ \033[32mu \033[m] Uninstall.
\033[m[ \033[32mx \033[m] For Exit.''')
    self.tool_footer()

  @classmethod
  def exit(self):
    self.tool_header()
    print ('''
\033[32m[ + ] \033[mThanks for using CyberCat
\033[32m[ + ] \033[mGood By..... :)\033[m''')
    self.tool_footer()
