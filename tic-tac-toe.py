from tkinter import *

#Add win condition
def Endcondition(winner) :
      msgwindow = Tk()
      msg = Message(msgwindow, text= winner + "is win!!!")
      msg.grid(row=0, column=0)
      for b in list:
            b["command"] = ""
			
def checked(i) :
      global player
      button = list[i]
  
      if button["text"] != "     " :
      if (button["text"] != "     "):
              return
      button["text"] = player 
      button["text"] = " "+player+" " 
      button["bg"] = "yellow"
  
      if player == "X" :
            player = "O"
            button["bg"] = "yellow"
      r = i//3
      c = i%3
      
      if (list[r*3]["text"] == list[r*3 + 1]["text"] == list[r*3 + 2]["text"]) or ( list[c]["text"] == list[c + 3]["text"] == list[c + 6]["text"] ) or ( list[0]["text"] == list[4]["text"] == list[8]["text"] != "     ") or (list[2]["text"] == list[4]["text"] == list[6]["text"] != "     ") :
            Endcondition(player)
      else :
            player = "X"
            button["bg"] = "lightgreen"

            if player == "X" :
                  player = "O"
                  button["bg"] = "yellow"
            else :
                  player = "X"
                  button["bg"] = "lightgreen"
      
window = Tk()
player = "X"
list= []

for i in range(9) :
      b = Button(window, text="     ", command=lambda k=i: checked(k))
      b.grid(row=i//3, column=i%3)
      list.append(b)

window.mainloop()
