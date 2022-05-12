from tkinter import *  # importing modules#
from tkinter.ttk import *
import datetime
import platform
try:
        import winsound #windows
except:
        import os #other

        # Making Tinker Window#
        window = Tk()
        window.title("Clock")
        window.geometry('500x250')

           #Adding  tkinker tab control#
        tabs_control = Notebook(window)
        clock_tab = Frame(tabs_control)
        alarm_tab = Frame(tabs_control)
        stopwatch_tab = Frame(tabs_control)
        timer_tab = Frame(tabs_control)
        tabs_control.add(clock_tab, text="Clock")
        tabs_control.add(alarm_tab, text="Alarm")
        tabs_control.add(stopwatch_tab, text="Stopwatch")
        tabs_control.add(timer_tab, text="Timer")
        tabs_control.pack(expand = 1, fill ="both")