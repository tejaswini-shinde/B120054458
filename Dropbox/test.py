#Group B: C4 
#!/usr/bin/python

import Tkinter
#import urllib
import os
import sys


def sap2():
        print("Deletting Dir")
        name = raw_input('Enter name of new Directory :')
        os.system("./dropbox_uploader.sh delete "+name+"")
        print("Operation Successfully Completed")

def sap3():
        print("Create Directory : ")
        name = raw_input('Enter name of new Directory :')
        os.system("./dropbox_uploader.sh mkdir "+name+"")
        print("Operation Successfully Completed")

def sap5():
        print("Directories are :  : ")
        
        os.system("./dropbox_uploader.sh list")
        print("Operation Successfully Completed")
        

def sap6():
        print("Directories are :  : ")
        
        os.system("./dropbox_uploader.sh upload /home/dbsl/a.txt /")
        print("Operation Successfully Completed")
        
        

def sap7():
        print("Directories are :  : ")
        
        os.system("./dropbox_uploader.sh download /a.txt /home/dbsl/4316")

        print("Operation Successfully Completed")
	os.system("cat /home/dbsl/4316/a.txt")        

        
def sap4():
        exit(0)

class simpleapp_tk(Tkinter.Tk):
      def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

      def initialize(self):
        self.grid()
       
        
        button = Tkinter.Button(self,text="Delete",command=sap2)
        button.grid(column=1,row=2)

        button = Tkinter.Button(self,text="Create Directory",command=sap3)
        button.grid(column=1,row=4)
        
        button = Tkinter.Button(self,text="List Directories",command=sap5)
        button.grid(column=1,row=6)
        
        button = Tkinter.Button(self,text="Exit",command=sap4)
        button.grid(column=1,row=8)

		button = Tkinter.Button(self,text="Upload",command=sap6)
        button.grid(column=1,row=10) 
        
        button = Tkinter.Button(self,text="view",command=sap7)
        button.grid(column=1,row=12) 
        
                  
if __name__ == "__main__":
   app = simpleapp_tk(None)
   app.title('CLOUD COMMANDS')
   app.mainloop()










