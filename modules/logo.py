# Set a CLI color
    GR = "\033[32m" # green color
    RD = "\033[31m" # red color
    RS = "\033[m" # Reset color



class logo:
  @classmethod
  def tool_header(self):
    print('''

RS
         _____           _    __  __
        |_   _|__   ___ | |   \ \/ /
          | |/ _ \ / _ \| |____\  /
          | | (_) | (_) | |____/  \    
          |_|\___/ \___/|_|   /_/\_\ RDv2.1


RS ============================================= RS ''')

  @classmethod
  def tool_footer(self):
    print(''' GR
=============================================== RS ''')


  @classmethod
  def not_ins(self):
    self.tool_header()
    print ('''
RD  [ + ]  RS We can't install CyberCat. RS
RD  [ + ]  RS There are some error. RS
RD  [ + ]  RS Please try again after some time. RS ''')
    self.tool_footer()

  @classmethod
  def ins_tnc(self):
    self.tool_header()
    print ('''
RD  [ + ] RS Use It At Your Own Risk.
RD  [ + ] RS No Warranty.
RD  [ + ] RS Use it legal purpose only.
RD  [ + ] RS We are not responsible for your actions.
RD  [ + ] RS Do not do things that are forbidden.

RD If you are installing this tool.
 that means you are agree with all terms.''')
    self.tool_footer()

  @classmethod
  def ins_sc(self):
    self.tool_header()
    print ('''
RD    [ + ] RS Tool-X installed successfully.
RD    [ + ] RS To run Tool-X.
RD    [ + ] RS Type Tool-X in your terminal.''')
    self.tool_footer()

  @classmethod
  def update(self):
    self.tool_header()
    print ('''
RS    [GR1RS]  Update your Tool-X.
RS    [GR0RS]  For Back.''')
    self.tool_footer()

  @classmethod
  def updated(self):
    self.tool_header()
    print ('''
RS      [ + ] GRTool-X Updated Successfully.
RS      [ + ] GRPress Enter to continue.RS''')
    self.tool_footer()

  @classmethod
  def nonet(self):
    self.tool_header()
    print ('''
RD  [ + ]  RSNo network connection?
RD  [ + ]  RSAre you offline?
RD  [ + ]  RSPlease try again after some time.''')
    self.tool_footer()

  @classmethod
  def update_error(self):
    self.tool_header()
    print ('''
RD  [ + ]  RSWe can't Update CyberCat.
RD  [ + ]  RSPlease try again after some time.''')
    self.tool_footer()


  @classmethod
  def about(self,total):
    self.tool_header()
    print (f'''
GR       [+] Tool Name :- RSTool-X
GR       [+] Author :- RS Hadi
GR       [+] Tools :- RStotal {total} tools.
GR       [+] RSCyberCat is automatic tool installer.
GR       [+] RSMade for termux and linux based system.
GR       [+] Note :- Use this tool at your own risk.''')
    self.tool_footer()


  @classmethod
  def install_tools(self):
    print (""" RS[GR*RS]GR Select Your Tool : RS """)

  @classmethod
  def already_installed(self,name):
    self.tool_header()
    print(f'''
RD  [ + ] RS Sorry ??
RD  [ + ] GR'{name}' RSis already Installed !!
''')
    self.tool_footer()

  @classmethod
  def installed(self,name):
    self.tool_header()
    print(f'''
GR  [ + ] RSInstalled Successfully !!
GR  [ + ] RD'{name}' RSis Installed Successfully !!
''')
    self.tool_footer()

  @classmethod
  def not_installed(self,name):
    self.tool_header()
    print(f'''
RD  [ + ] RSSorry ??
RD  [ + ] '{name}'RS is not Installed !!
''')
    self.tool_footer()

  @classmethod
  def back(self):
    print ("""RS =============================================
GR  [00] Back                                   |
 RS=============================================""")

  @classmethod
  def updating(self):
    print ("""RS RS[GR*RS]GR Updating CyberCat RS """)

  @classmethod
  def installing(self):
    print ("""RS[GR*RS]GR Installing.. RS """)

  @classmethod
  def menu(self,total):
    self.tool_header()
    print (f'''
RS  [ GR1 RS] Show all tools.
RS  [ GR2 RS] Tools Category.
RS  [ GR3 RS] Update Tool-X.
RS  [ GR4 RS] About Us.
RS  [ GRU RS] Uninstall.
RS  [ GRx RS] For Exit.''')
    self.tool_footer()

  @classmethod
  def exit(self):
    self.tool_header()
    print ('''
GR         [ + ] RSThanks for using Tool-X
GR         [ + ] RSGood By..... :)RS''')
    self.tool_footer()
