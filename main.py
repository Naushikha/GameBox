import tkinter as tk

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        pad=3
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.escape_now)            
    def escape_now(self,event):
        exit()

root=tk.Tk()
root.wm_attributes('-type', 'splash')
app=FullScreenApp(root)
root.after(1, lambda: root.focus_force()) # Force focus onto window

root.mainloop()