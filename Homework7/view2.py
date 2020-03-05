import sys
import os
import tkinter as tk
import tkinter.simpledialog


def view(fileName, view_size=25):
    #check to see if the file is empty
    if os.path.getsize(fileName) < 1:
        print("Error: specified file is empty")
        return

    with open(fileName, 'r') as f:
        #save positions into a list
        offsets = [0]
        currentPos = 0

        #get the offsets
        i = 0
        while f.readline():
            i += 1
            if i % view_size == 0:
                f.seek(f.tell())
                offsets.append(f.tell())
        f.seek(0,2)
        fileEnd = f.tell()

        #update the text in the window to be the current page
        def updateText(tkText, window):
            result = []
            #move to the current position
            nonlocal offsets
            nonlocal currentPos
            f.seek(offsets[currentPos])
            
            nextPos = currentPos + 1
            if nextPos == len(offsets):
                nextPos = 0

            #add lines into a list 
            while f.tell() != offsets[nextPos] and f.tell() != fileEnd:
                result.append(f.readline())

            #if the list of lines is too short, lengthen it
            while len(result) < view_size:
                result.append('\n')

            #update the tkinter textbox
            text.config(state=tk.NORMAL)
            tkText.delete('1.0', tk.END)
            tkText.insert('1.0', ''.join(result))
            text.config(state=tk.DISABLED)
            
            #update window title
            window.title(f.name + ' - Page ' + str(currentPos+1))

        #change the page number to be the given page
        def changePageNumber(num, tkText, window):
            nonlocal currentPos
            currentPos = num
            if currentPos < 0:
                currentPos = len(offsets) - 1
            elif currentPos >= len(offsets):
                currentPos = 0
            updateText(tkText, window)

        #change the page number to one given by the user
        def getPageNumber(tkText, window):
            changePageNumber(tk.simpledialog.askinteger('Page Number', 'Enter page number')-1, tkText, window)
        
        #create the window
        mainWindow = tk.Tk()
        scrollbar = tk.Scrollbar(orient=tk.HORIZONTAL)
        scrollbar.pack(side=tk.BOTTOM, fill='x')

        text = tk.Text(height=view_size, width=50, wrap=tk.NONE, xscrollcommand=scrollbar.set)
        text.pack()
        updateText(text, mainWindow)

        scrollbar.config(command=text.xview)

        buttonFrame=tk.Frame(mainWindow)
        buttonFrame.pack(side=tk.BOTTOM)

        bWidth = 8
        pad=2
        top = tk.Button(buttonFrame, command=lambda : changePageNumber(0, text, mainWindow), text='TOP', width=bWidth)
        top.grid(column=0, row=1, padx=pad)
        up = tk.Button(buttonFrame, command=lambda : changePageNumber(currentPos-1, text, mainWindow), text='UP', width=bWidth)
        up.grid(column=1, row=1, padx=pad)
        down = tk.Button(buttonFrame, command=lambda : changePageNumber(currentPos+1, text, mainWindow), text='DOWN', width=bWidth)
        down.grid(column=2, row=1, padx=pad)
        bottom = tk.Button(buttonFrame, command=lambda : changePageNumber(len(offsets)-1, text, mainWindow), text='BOTTOM', width=bWidth)
        bottom.grid(column=3, row=1, padx=pad)
        page = tk.Button(buttonFrame, command=lambda : getPageNumber(text, mainWindow), text='PAGE', width=bWidth)
        page.grid(column=4, row=1, padx=pad)
        quitButton = tk.Button(buttonFrame, command=lambda : sys.exit(), text='QUIT', width=bWidth)
        quitButton.grid(column=5, row=1, padx=pad)
        mainWindow.mainloop()
            
def main():
    if len(sys.argv) > 2:
        view(sys.argv[1], sys.argv[2])
    else:
        view(sys.argv[1])
    
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('Error: No file specified')
    else:
        main()