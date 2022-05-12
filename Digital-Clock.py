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

        #Creating Clock#

        #Adding Clock Components#

        time_label = Label(clock_tab, font = 'calibri 40 bold', Foreground= 'black')
        time_label.pack (anchor='center')
        date_label = Label(clock_tab, font = 'calibri 40 bold', forground = 'black')
        date_label.pack(andchor='s')

        #Clock Function#

        def clock():
                date_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S/%p")
                date,time1 = date_time.split(
                time2, time3 = time.split('/')
                hour, minutes, seconds = time2.split(':')

                if int(hour) > and init(hour) < 24:
                        time = str(int(hours) - 12) + ':' + minutes + ':' + seconds + ' ' + time3
                   else:
                           time = time2 + ' ' + time3
                        time_label.config(text=time)
                        date_label.config(text=date)        
                )

        # Creating Alarm#       

          get_alarm_time_entry = Entry(alarm_tab, font = 'calibri 15 bold')
          get_alarm_time_entry.pack(anchor='center')
          alarm_instructions_label = Label(alarm_tab, font = 'calibri 10 bold', text = "Enter Alarm Time. Eg -> 01:30 PM, 01 -> Hour, 30 -> Minutes")
          alarm_instructions_label.pack(anchor='s')
          set_alarm_button = Button(alarm_tab, text = "Set Alarm", command=alarm)
          set_alarm_button.pack(anchor='s')
          alarm_status_label = Label(alarm_tab, font = 'calibri 15 bold')
          alarm_status_label.pack(anchor='s') 

          # Alarm Function #