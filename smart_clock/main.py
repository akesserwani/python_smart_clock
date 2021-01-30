from Tkinter import *
import time
import datetime
from PIL import ImageTk, Image
import os
import random
import pygame
import re


global main_root
#Enter path to your folder here
main_root = '#'


root = Tk()
root.geometry("800x480")
root.resizable(width=False, height=False)
root.config(cursor="none")
root.overrideredirect(True) 
canvas = Canvas(root, height = 680, width = 1200, highlightthickness = 0)
canvas.pack()
pygame.init()


#data
global data
global alarms
data = {1: "t", 2: "brightness", 3: "nightmode", 4: "wallpaper"}
alarms = {1:["06:00:00", False], 2:["06:00:00", False],  3:["06:00:00", False], 4:["06:00:00", False]}

#window Speed
global window_speed
window_speed = -180

#main background image and time
background_image = ['images/fjord.gif']
image = Image.open(main_root + background_image[0])
image = image.resize((900, 480), Image.ANTIALIAS) 
image = ImageTk.PhotoImage(image)
background = canvas.create_image(0, 0, image=image, anchor=NW)

label = canvas.create_text(370,200, fill="white",font="Helvetica 72 bold")

#palette colors
global background_color
global icon_color
global dark_icon_color
global night_shade
global light_night_shade

background_color = "#AAABB8"
icon_color = "#2E9CCA"
dark_icon_color = "#29648A"
night_shade = "#25274D"
light_night_shade = "#464866"


#load icons here
exit_icon = Image.open(main_root + 'icons/exit_icon.gif')
exit_icon = exit_icon.resize((50, 50), Image.ANTIALIAS) 
exit_icon = ImageTk.PhotoImage(exit_icon)

settings_icon = Image.open(main_root + 'icons/settings_icon.gif')
settings_icon = settings_icon.resize((80, 80), Image.ANTIALIAS) 
settings_icon = ImageTk.PhotoImage(settings_icon)

music_icon = Image.open(main_root + 'icons/music_icon.gif')
music_icon = music_icon.resize((100, 100), Image.ANTIALIAS) 
music_icon = ImageTk.PhotoImage(music_icon)

alarm_icon = Image.open(main_root + 'icons/alarm_icon.gif')
alarm_icon = alarm_icon.resize((100, 100), Image.ANTIALIAS) 
alarm_icon = ImageTk.PhotoImage(alarm_icon)

alarm_add_icon = Image.open(main_root + 'icons/alarm_add_icon.gif')
alarm_add_icon = alarm_add_icon.resize((80, 80), Image.ANTIALIAS) 
alarm_add_icon = ImageTk.PhotoImage(alarm_add_icon)

alarm_on_icon = Image.open(main_root + 'icons/alarm_on_icon.gif')
alarm_on_icon = alarm_on_icon.resize((50, 50), Image.ANTIALIAS) 
alarm_on_icon = ImageTk.PhotoImage(alarm_on_icon)

alarm_off_icon = Image.open(main_root + 'icons/alarm_off_icon.gif')
alarm_off_icon = alarm_off_icon.resize((50, 50), Image.ANTIALIAS) 
alarm_off_icon = ImageTk.PhotoImage(alarm_off_icon)

play_icon = Image.open(main_root + 'icons/play_icon.gif')
play_icon = play_icon.resize((300, 300), Image.ANTIALIAS) 
play_icon = ImageTk.PhotoImage(play_icon)

pause_icon = Image.open(main_root + 'icons/pause_icon.gif')
pause_icon = pause_icon.resize((300, 300), Image.ANTIALIAS) 
pause_icon = ImageTk.PhotoImage(pause_icon)

bamboo_icon = Image.open(main_root + 'icons/bamboo_icon.gif')
bamboo_icon = bamboo_icon.resize((150, 150), Image.ANTIALIAS) 
bamboo_icon = ImageTk.PhotoImage(bamboo_icon)

drop_icon = Image.open(main_root + 'icons/drop_icon.gif')
drop_icon = drop_icon.resize((120, 150), Image.ANTIALIAS) 
drop_icon = ImageTk.PhotoImage(drop_icon)

noise_icon = Image.open(main_root + 'icons/noise_icon.gif')
noise_icon = noise_icon.resize((150, 150), Image.ANTIALIAS) 
noise_icon = ImageTk.PhotoImage(noise_icon)

wave_icon = Image.open(main_root + 'icons/wave_icon.gif')
wave_icon = wave_icon.resize((150, 150), Image.ANTIALIAS) 
wave_icon = ImageTk.PhotoImage(wave_icon)


#toggle buttons
global toggled_one
global toggled_two
global toggled_three
global toggled_four
toggled_one = [True]
toggled_two = [True]
toggled_three = [True]
toggled_four = [True]


#alarm ringer sounds
global alarm_sound
alarm_sound = [main_root + "alarm_sounds/alarm_classic.mp3"]


def digitalclock():
   text_input = time.strftime("%I:%M %p")
   canvas.itemconfig(label, text=text_input)
   canvas.after(200, digitalclock)


class Menu():

    @staticmethod
    def menu():
        global up
        global menu_bar
        global btn_one
        global btn_two
        global btn_three
        global btn_four
        global alarm_icon_draw
        global music_icon_draw
        global settings_icon_draw

        up = False
        menu_bar = canvas.create_rectangle(500,400, 0, 0, fill = background_color, outline = background_color)
        canvas.move(menu_bar, 130, 500)

        circle_size = 120
        btn_one = canvas.create_oval(circle_size,circle_size, 0, 0, fill = icon_color, outline = icon_color)
        canvas.move(btn_one, 180, 430)
        alarm_icon_draw = canvas.create_image(190, 440, image=alarm_icon, anchor=NW)

        btn_two = canvas.create_oval(circle_size,circle_size, 0, 0, fill = icon_color, outline = icon_color)
        canvas.move(btn_two, 320, 430)
        music_icon_draw = canvas.create_image(330, 440, image=music_icon, anchor=NW)

        btn_three = canvas.create_oval(circle_size,circle_size, 0, 0, fill = icon_color, outline = icon_color)
        canvas.move(btn_three, 470, 430)
        settings_icon_draw = canvas.create_image(490, 450, image=settings_icon, anchor=NW)



        canvas.tag_bind(background, "<Button-1>", Menu.menu_up)
        canvas.tag_bind(btn_one, "<Button-1>", Alarm.alarm)
        canvas.tag_bind(btn_two, "<Button-1>", Music.music)
        canvas.tag_bind(btn_three, "<Button-1>", Settings.settings)
        canvas.tag_bind(alarm_icon_draw, "<Button-1>", Alarm.alarm)
        canvas.tag_bind(music_icon_draw, "<Button-1>", Music.music)
        canvas.tag_bind(settings_icon_draw, "<Button-1>", Settings.settings)


    @staticmethod
    def menu_up(event):
        global up
        if up == False:
            while True:
                canvas.after(1, canvas.move(menu_bar, 0, -50))
                canvas.after(1, canvas.move(btn_one, 0, -50))
                canvas.after(1, canvas.move(btn_two, 0, -50))
                canvas.after(1, canvas.move(btn_three, 0, -50))
                canvas.after(1, canvas.move(alarm_icon_draw, 0, -50))
                canvas.after(1, canvas.move(music_icon_draw, 0, -50))
                canvas.after(1, canvas.move(settings_icon_draw, 0, -50))

                root.update()
                if canvas.coords(menu_bar)[1] == 400.0 or canvas.coords(btn_one)[1] == 300.0 or canvas.coords(btn_two)[1] == 300.0 or canvas.coords(btn_three)[1] == 300.0 or canvas.coords(alarm_icon_draw)[1] == 300.0 or canvas.coords(music_icon_draw)[1] == 300.0 or canvas.coords(settings_icon_draw)[1] == 300.0:
                    break
            up = True
        elif up == True:
            while True:
                canvas.after(1, canvas.move(menu_bar, 0, 50))
                canvas.after(1, canvas.move(btn_one, 0, 50))
                canvas.after(1, canvas.move(btn_two, 0, 50))
                canvas.after(1, canvas.move(btn_three, 0, 50))
                canvas.after(1, canvas.move(alarm_icon_draw, 0, 50))
                canvas.after(1, canvas.move(music_icon_draw, 0, 50))
                canvas.after(1, canvas.move(settings_icon_draw, 0, 50))

                root.update()

                if canvas.coords(menu_bar)[1] == 600.0 or canvas.coords(btn_one)[1] == 600.0 or canvas.coords(btn_two)[1] == 600.0 or canvas.coords(btn_three)[1] == 600.0 or canvas.coords(alarm_icon_draw)[1] == 600.0 or canvas.coords(music_icon_draw)[1] == 600.0 or canvas.coords(settings_icon_draw)[1] == 600.0:
                    break   
            up = False
        
    @staticmethod
    def menu_down():
        global up

        if up == True:
            while True:
                canvas.after(1, canvas.move(menu_bar, 0, 50))
                canvas.after(1, canvas.move(btn_one, 0, 50))
                canvas.after(1, canvas.move(btn_two, 0, 50))
                canvas.after(1, canvas.move(btn_three, 0, 50))
                canvas.after(1, canvas.move(alarm_icon_draw, 0, 50))
                canvas.after(1, canvas.move(music_icon_draw, 0, 50))
                canvas.after(1, canvas.move(settings_icon_draw, 0, 50))

                root.update()
                if canvas.coords(menu_bar)[1] == 600.0 or canvas.coords(btn_one)[1] == 600.0 or canvas.coords(btn_two)[1] == 600.0 or canvas.coords(btn_three)[1] == 600.0 or canvas.coords(alarm_icon_draw)[1] == 600.0 or canvas.coords(music_icon_draw)[1] == 600.0 or canvas.coords(settings_icon_draw)[1] == 600.0:
                    break   
            up = False



class Alarm:
    @staticmethod
    def alarm(event):
        global alarm_background
        global alarm_exit_btn
        global clock_box_one
        global clock_box_two
        global clock_box_three
        global clock_box_four
        global time_text_one
        global time_text_two
        global time_text_three
        global time_text_four
        global toggle_one
        global toggle_two
        global toggle_three
        global toggle_four
        global toggle_button_one
        global toggle_button_two
        global toggle_button_three
        global toggle_button_four
        global accent_one
        global accent_two
        global accent_three
        global accent_four

        alarm_background = canvas.create_rectangle(800,480, 0, 0, fill = background_color)
        canvas.move(alarm_background, 900, 0)

        alarm_exit_btn = canvas.create_image(20, 20, image=exit_icon, anchor=NW)
        canvas.move(alarm_exit_btn, 920, 20)
        canvas.tag_bind(alarm_exit_btn, "<Button-1>", Exit.alarm_exit)
    
        clock_box_one = canvas.create_rectangle(300, 100, 0, 0, fill=background_color, tag = "clock_box_one", outline = background_color)
        canvas.move(clock_box_one, 1050, 50)

        clock_box_two = canvas.create_rectangle(300, 100, 0, 0, fill=background_color, tag = "clock_box_two", outline = background_color)
        canvas.move(clock_box_two, 1050, 150)

        clock_box_three = canvas.create_rectangle(300, 100, 0, 0, fill=background_color, tag = "clock_box_three", outline = background_color)
        canvas.move(clock_box_three, 1050, 250)

        clock_box_four = canvas.create_rectangle(300, 100, 0, 0, fill=background_color, tag = "clock_box_four", outline = background_color)
        canvas.move(clock_box_four, 1050, 350)


        time_text_one = canvas.create_text(0,0, fill="white",font="Helvetica 50 bold", text = alarms[1][0], tag = "clock_box_one")
        canvas.move(time_text_one, 1150, 100)

        time_text_two = canvas.create_text(0,0, fill="white",font="Helvetica 50 bold", text = alarms[2][0], tag = "clock_box_two")
        canvas.move(time_text_two, 1150, 200)

        time_text_three = canvas.create_text(0,0, fill="white",font="Helvetica 50 bold", text = alarms[3][0], tag = "clock_box_three")
        canvas.move(time_text_three, 1150, 300)

        time_text_four = canvas.create_text(0,0, fill="white",font="Helvetica 50 bold", text = alarms[4][0], tag = "clock_box_four")
        canvas.move(time_text_four, 1150, 400)

        toggle_size = 60

        if toggled_one[0] == False:
            toggle_button_one = canvas.create_oval(toggle_size, toggle_size, 0, 0, fill=icon_color, tag = "toggle_one", outline = icon_color)
            canvas.move(toggle_button_one, 1450, 68)
            toggle_one = canvas.create_image(20, 20, image=alarm_on_icon, anchor=NW, tag = "toggle_one")
            canvas.move(toggle_one, 1435, 55)
        elif toggled_one[0] == True:
            toggle_button_one = canvas.create_oval(toggle_size, toggle_size, 0, 0, fill="gray", tag = "toggle_one", outline = "gray")
            canvas.move(toggle_button_one, 1450, 68)
            toggle_one = canvas.create_image(20, 20, image=alarm_off_icon, anchor=NW, tag = "toggle_one")
            canvas.move(toggle_one, 1435, 55)

        if toggled_two[0] == False:
            toggle_button_two = canvas.create_oval(toggle_size, toggle_size, 0, 0, fill=icon_color, tag = "toggle_two", outline = icon_color)
            canvas.move(toggle_button_two, 1450, 168)
            toggle_two = canvas.create_image(20, 20, image=alarm_on_icon, anchor=NW, tag = "toggle_two")
            canvas.move(toggle_two, 1435, 155)
        elif toggled_two[0] == True:
            toggle_button_two = canvas.create_oval(toggle_size, toggle_size, 0, 0, fill= "gray", tag = "toggle_two", outline = "gray")
            canvas.move(toggle_button_two, 1450, 168)
            toggle_two = canvas.create_image(20, 20, image=alarm_off_icon, anchor=NW, tag = "toggle_two")
            canvas.move(toggle_two, 1435, 155)

        if toggled_three[0] == False:
            toggle_button_three = canvas.create_oval(toggle_size, toggle_size, 0, 0, fill=icon_color, tag = "toggle_three", outline = icon_color)
            canvas.move(toggle_button_three, 1450, 268)
            toggle_three = canvas.create_image(20, 20, image=alarm_on_icon, anchor=NW, tag = "toggle_three")
            canvas.move(toggle_three, 1435, 255)
        elif toggled_three[0] == True:
            toggle_button_three = canvas.create_oval(toggle_size, toggle_size, 0, 0, fill= "gray", tag = "toggle_three", outline = "gray")
            canvas.move(toggle_button_three, 1450, 268)
            toggle_three = canvas.create_image(20, 20, image=alarm_off_icon, anchor=NW, tag = "toggle_three")
            canvas.move(toggle_three, 1435, 255)

        if toggled_four[0] == False:
            toggle_button_four = canvas.create_oval(toggle_size, toggle_size, 0, 0, fill=icon_color, tag = "toggle_four", outline = icon_color)
            canvas.move(toggle_button_four, 1450, 368)
            toggle_four = canvas.create_image(20, 20, image=alarm_on_icon, anchor=NW, tag = "toggle_four")
            canvas.move(toggle_four, 1435, 355)
        elif toggled_four[0] == True:
            toggle_button_four = canvas.create_oval(toggle_size, toggle_size, 0, 0, fill= "gray", tag = "toggle_four", outline = "gray")
            canvas.move(toggle_button_four, 1450, 368)
            toggle_four = canvas.create_image(20, 20, image=alarm_off_icon, anchor=NW, tag = "toggle_four")
            canvas.move(toggle_four, 1435, 355)



        canvas.tag_bind(clock_box_one, "<Button-1>", Alarm.create_alarm)
        canvas.tag_bind(clock_box_two, "<Button-1>", Alarm.create_alarm)
        canvas.tag_bind(clock_box_three, "<Button-1>", Alarm.create_alarm)
        canvas.tag_bind(clock_box_four, "<Button-1>", Alarm.create_alarm)
        canvas.tag_bind(time_text_one, "<Button-1>", Alarm.create_alarm)
        canvas.tag_bind(time_text_two, "<Button-1>", Alarm.create_alarm)
        canvas.tag_bind(time_text_three, "<Button-1>", Alarm.create_alarm)
        canvas.tag_bind(time_text_four, "<Button-1>", Alarm.create_alarm)

        canvas.tag_bind(toggle_one, "<Button-1>", Alarm.toggle_button)
        canvas.tag_bind(toggle_button_one, "<Button-1>", Alarm.toggle_button)
        canvas.tag_bind(toggle_two, "<Button-1>", Alarm.toggle_button)
        canvas.tag_bind(toggle_button_two, "<Button-1>", Alarm.toggle_button)
        canvas.tag_bind(toggle_three, "<Button-1>", Alarm.toggle_button)
        canvas.tag_bind(toggle_button_three, "<Button-1>", Alarm.toggle_button)
        canvas.tag_bind(toggle_four, "<Button-1>", Alarm.toggle_button)
        canvas.tag_bind(toggle_button_four, "<Button-1>", Alarm.toggle_button)

        accent_one = canvas.create_rectangle(300, 5, 0, 0, fill=icon_color,  outline = icon_color)
        canvas.move(accent_one, 1080, 140)
        accent_two = canvas.create_rectangle(300, 5, 0, 0, fill=icon_color,  outline = icon_color)
        canvas.move(accent_two, 1080, 240)
        accent_three = canvas.create_rectangle(300, 5, 0, 0, fill=icon_color,  outline = icon_color)
        canvas.move(accent_three, 1080, 340)
        accent_four = canvas.create_rectangle(300, 5, 0, 0, fill=icon_color,  outline = icon_color)
        canvas.move(accent_four, 1080, 440)

        Menu.menu_down()
        while True:
            canvas.after(1, canvas.move(alarm_background, window_speed, 0))
            canvas.after(1, canvas.move(alarm_exit_btn, window_speed, 0))
            canvas.after(1, canvas.move(clock_box_one, window_speed, 0))
            canvas.after(1, canvas.move(clock_box_two, window_speed, 0))
            canvas.after(1, canvas.move(clock_box_three, window_speed, 0))
            canvas.after(1, canvas.move(clock_box_four, window_speed, 0))
            canvas.after(1, canvas.move(time_text_one, window_speed, 0))
            canvas.after(1, canvas.move(time_text_two, window_speed, 0))
            canvas.after(1, canvas.move(time_text_three, window_speed, 0))
            canvas.after(1, canvas.move(time_text_four, window_speed, 0))
            canvas.after(1, canvas.move(toggle_one, window_speed, 0))
            canvas.after(1, canvas.move(toggle_two, window_speed, 0))
            canvas.after(1, canvas.move(toggle_three, window_speed, 0))
            canvas.after(1, canvas.move(toggle_four, window_speed, 0))
            canvas.after(1, canvas.move(toggle_button_one, window_speed, 0))
            canvas.after(1, canvas.move(toggle_button_two, window_speed, 0))
            canvas.after(1, canvas.move(toggle_button_three, window_speed, 0))
            canvas.after(1, canvas.move(toggle_button_four, window_speed, 0))
            canvas.after(1, canvas.move(accent_one, window_speed, 0))
            canvas.after(1, canvas.move(accent_two, window_speed, 0))
            canvas.after(1, canvas.move(accent_three, window_speed, 0))
            canvas.after(1, canvas.move(accent_four, window_speed, 0))


            root.update()

            if canvas.coords(alarm_background)[0] == 0.0 or canvas.coords(alarm_exit_btn)[0] == 100.0 or canvas.coords(clock_box_one)[0] == 100.0 or canvas.coords(clock_box_two)[0] == 200.0 or canvas.coords(clock_box_three)[0] == 100.0 or canvas.coords(clock_box_four)[0] == 200.0 or canvas.coords(time_text_one)[0] == 100.0 or canvas.coords(time_text_two)[0] == 100.0 or canvas.coords(time_text_three)[0] == 100.0 or canvas.coords(time_text_four)[0] == 100.0:
                break

    @staticmethod
    def create_alarm(event):
        global ca_background
        global ca_exit_button
        global alarm_text
        global hour_down_btn
        global hour_up_btn
        global label_one
        global minute_down_btn
        global minute_up_btn
        global label_two
        global submit_rect
        global alarms
        global number
        global numberTwo
        global add_alarm
        

        clock_tag = event.widget.gettags("current")[0]

        ca_background = canvas.create_rectangle(800,480, 0, 0, fill = background_color)
        canvas.move(ca_background, 900, 0)
        ca_exit_button = canvas.create_image(20, 20, image=exit_icon, anchor=NW)
        canvas.move(ca_exit_button, 920, 20)
        canvas.tag_bind(ca_exit_button, "<Button-1>", Exit.create_alarm_exit)

        alarm_text = canvas.create_text(1000,200, fill="white",font="Helvetica 30 bold", text = "")

        hour_down_btn = canvas.create_rectangle(0, 0, 200, 100, fill= icon_color, outline = icon_color)
        hour_up_btn = canvas.create_rectangle(0, 0, 200, 100, fill=icon_color, outline = icon_color) 
        canvas.move(hour_down_btn, 1050, 300)
        canvas.move(hour_up_btn, 1050, 50)

        number = 6
        label_one = canvas.create_text(0,0, fill="white",font="Helvetica 100 italic bold", text = str(number))
        canvas.move(label_one, 1150, 220)

        minute_down_btn = canvas.create_rectangle(0, 0, 200, 100, fill=icon_color, outline = icon_color)
        minute_up_btn = canvas.create_rectangle(0, 0, 200, 100, fill=icon_color, outline = icon_color) 
        canvas.move(minute_down_btn, 1350, 300)
        canvas.move(minute_up_btn, 1350, 50)

        numberTwo = 30
        label_two = canvas.create_text(0,0, fill="white",font="Helvetica 100 italic bold", text = str(numberTwo))
        canvas.move(label_two, 1450, 220)


        submit_rect = canvas.create_oval(0, 0, 100, 100, fill=icon_color, outline = icon_color) 
        canvas.move(submit_rect, 1590, 370)

        add_alarm = canvas.create_image(1600, 380, image=alarm_add_icon, anchor=NW)


        while True:
            canvas.after(1, canvas.move(ca_background, window_speed, 0))
            canvas.after(1, canvas.move(ca_exit_button, window_speed, 0))
            canvas.after(1, canvas.move(alarm_text, window_speed, 0))
            canvas.after(1, canvas.move(hour_down_btn, window_speed, 0))
            canvas.after(1, canvas.move(hour_up_btn, window_speed, 0))
            canvas.after(1, canvas.move(label_one, window_speed, 0))
            canvas.after(1, canvas.move(minute_down_btn, window_speed, 0))
            canvas.after(1, canvas.move(minute_up_btn, window_speed, 0))
            canvas.after(1, canvas.move(label_two, window_speed, 0))
            canvas.after(1, canvas.move(submit_rect, window_speed, 0))
            canvas.after(1, canvas.move(add_alarm, window_speed, 0))

            root.update()

            if canvas.coords(ca_background)[0] == 0.0 or canvas.coords(ca_exit_button)[0] == 100.0 or canvas.coords(alarm_text)[0] == 150.0 or canvas.coords(hour_down_btn)[0] == 100.0 or canvas.coords(hour_up_btn)[0] == 100.0 or canvas.coords(label_one)[0] == 100.0 or canvas.coords(minute_down_btn)[0] == 200.0 or canvas.coords(minute_up_btn)[0] == 200.0 or canvas.coords(label_two)[0] == 200.0 or canvas.coords(submit_rect)[0] == 500.0:
                break

        
        canvas.tag_bind(minute_up_btn, "<Button-1>", Alarm.minute_up)
        canvas.tag_bind(minute_down_btn, "<Button-1>", Alarm.minute_down)
        canvas.tag_bind(hour_up_btn, "<Button-1>", Alarm.hour_up)
        canvas.tag_bind(hour_down_btn, "<Button-1>", Alarm.hour_down)
        canvas.tag_bind(submit_rect, "<Button-1>",lambda event, clock_event = clock_tag: Alarm.submit(event, clock_event))
        canvas.tag_bind(add_alarm, "<Button-1>",lambda event, clock_event = clock_tag: Alarm.submit(event, clock_event))


    @staticmethod
    def hour_up(event):
        global number

        if number in range(1, 24):
            number += 1
            canvas.itemconfig(label_one, text=str(number))

        if number == 24:
            canvas.itemconfig(hour_up_btn, fill = dark_icon_color, outline = "")
        elif number in range(1,23):
            canvas.itemconfig(hour_up_btn, fill = icon_color, outline = "")

        if number in range(1,24):
            canvas.itemconfig(hour_down_btn, fill = icon_color, outline = "")

    
    @staticmethod
    def hour_down(event):
        global number

        if number in range(2, 25):
            number -= 1
            canvas.itemconfig(label_one, text=str(number))

        if number == 1:
            canvas.itemconfig(hour_down_btn, fill = dark_icon_color, outline = "")
        elif number in range(2,24):
            canvas.itemconfig(hour_down_btn, fill = icon_color, outline = "")

        if number in range(1,24):
            canvas.itemconfig(hour_up_btn, fill = icon_color, outline = "")

    @staticmethod
    def minute_up(event):
        global numberTwo

        if numberTwo in range(0, 60):
            numberTwo += 5
            canvas.itemconfig(label_two, text=str(numberTwo))

            if numberTwo == 60:
                canvas.itemconfig(label_two, text= "00")
            elif numberTwo == 5:
                canvas.itemconfig(label_two, text= "05")
        
        if numberTwo == 60:
            canvas.itemconfig(minute_up_btn, fill = dark_icon_color, outline = "")
        elif numberTwo in range(0,59):
            canvas.itemconfig(minute_up_btn, fill = icon_color, outline = "")
        
        if numberTwo in range(0, 60):
            canvas.itemconfig(minute_down_btn, fill = icon_color, outline = "")


    @staticmethod
    def minute_down(event):
        global numberTwo
        
        if numberTwo in range(1, 61):
            numberTwo -= 5
            canvas.itemconfig(label_two, text=str(numberTwo))

        if numberTwo == 0:
            canvas.itemconfig(minute_down_btn, fill = dark_icon_color, outline = "")
        elif numberTwo in range(1, 60):
            canvas.itemconfig(minute_down_btn, fill = icon_color, outline = "")

        if numberTwo in range(0, 60):
            canvas.itemconfig(minute_up_btn, fill = icon_color, outline = "")

        if numberTwo == 0:
            canvas.itemconfig(label_two, text= "00")
        elif numberTwo == 5:
            canvas.itemconfig(label_two, text= "05")

    @staticmethod
    def submit(event,clock_event):
        global alarms
        global time_text_list
        global clock_event_value

        clock_event_value = clock_event


        if number < 10 and numberTwo >= 10:
            if numberTwo == 60:
                time_string = "0" + str(number) + ":" + "00:00"
            else:
                time_string = "0" + str(number) + ":" + str(numberTwo) + ":00"

        elif number < 10 and numberTwo < 10:
            if numberTwo == 60:
                time_string = str(number) + ":" + "00:00"
            else:
                time_string = "0" + str(number) + ":" + "0" + str(numberTwo) + ":00"

        elif numberTwo < 10:
            time_string = str(number) + ":" + "0" + str(numberTwo) + ":00"
        else:
            time_string = str(number) + ":" + str(numberTwo) + ":00"

        if clock_event_value == "clock_box_one":
            canvas.itemconfig(time_text_one, text = time_string)
            alarms[1][0] = time_string
            alarms[1][1] = True
        elif clock_event_value == "clock_box_two":
            canvas.itemconfig(time_text_two, text = time_string)
            alarms[2][0] = time_string
            alarms[2][1] = True
        elif clock_event_value == "clock_box_three":
            canvas.itemconfig(time_text_three, text = time_string)
            alarms[3][0] = time_string
            alarms[3][1] = True
        elif clock_event_value == "clock_box_four":
            canvas.itemconfig(time_text_four, text = time_string)
            alarms[4][0] = time_string
            alarms[4][1] = True

        #start alarm clock when submit clicked
        #close set alarm page
        Exit.create_alarm_exit_nonevent()
        canvas.after(200, Alarm.alarmFunc)
        

    #code for active alarm clock
    global cancel_alarm
    cancel_alarm = None

    @staticmethod
    def alarmFunc():
        global number
        global numberTwo
        
        alarm = clock_event_value


        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")


        if alarm == "clock_box_one":
            alarm_clock_var = alarms[1][0]
            alarm_bool = alarms[1][1]
        elif alarm == "clock_box_two":
            alarm_clock_var = alarms[2][0]
            alarm_bool = alarms[2][1]
        elif alarm == "clock_box_three":
            alarm_clock_var = alarms[3][0]
            alarm_bool = alarms[3][1]
        elif alarm == "clock_box_four":
            alarm_clock_var = alarms[4][0]
            alarm_bool = alarms[4][1]


        if now == alarm_clock_var and alarm_bool == True:
            #alarm window
            cancel_alarm = canvas.after_cancel(Alarm.alarm_window())

        canvas.after(200, Alarm.alarmFunc)


    @staticmethod
    def toggle_button(event):
        global toggled
        
        if event.widget.gettags("current")[0] == "toggle_one":
            if toggled_one[0] == False:
                canvas.itemconfig(toggle_one, image = alarm_off_icon)
                canvas.itemconfig(toggle_button_one, fill = "gray", outline = "gray")
                alarms[1][1] = False
                toggled_one[0] = True
            elif toggled_one[0] == True:
                canvas.itemconfig(toggle_one, image = alarm_on_icon)
                canvas.itemconfig(toggle_button_one, fill = icon_color, outline = icon_color)
                alarms[1][1] = True
                toggled_one[0] = False
        elif event.widget.gettags("current")[0] == "toggle_two":
            if toggled_two[0] == False:
                canvas.itemconfig(toggle_two, image = alarm_off_icon)
                canvas.itemconfig(toggle_button_two, fill = "gray", outline = "gray")
                alarms[2][1] = False
                toggled_two[0] = True
            elif toggled_two[0] == True:
                canvas.itemconfig(toggle_two, image = alarm_on_icon)
                canvas.itemconfig(toggle_button_two, fill = icon_color, outline = icon_color)
                alarms[2][1] = True
                toggled_two[0] = False
        elif event.widget.gettags("current")[0] == "toggle_three":
            if toggled_three[0] == False:
                canvas.itemconfig(toggle_three, image = alarm_off_icon)
                canvas.itemconfig(toggle_button_three, fill = "gray", outline = "gray")
                alarms[3][1] = False               
                toggled_three[0] = True
            elif toggled_three[0] == True:
                canvas.itemconfig(toggle_three, image = alarm_on_icon)
                canvas.itemconfig(toggle_button_three, fill = icon_color, outline = icon_color)
                alarms[3][1] = True               
                toggled_three[0] = False
        elif event.widget.gettags("current")[0] == "toggle_four":
            if toggled_four[0] == False:
                canvas.itemconfig(toggle_four, image = alarm_off_icon)
                canvas.itemconfig(toggle_button_four, fill = "gray", outline = "gray")
                alarms[4][1] = False               
                toggled_four[0] = True
            elif toggled_four[0] == True:
                canvas.itemconfig(toggle_four, image = alarm_on_icon)
                canvas.itemconfig(toggle_button_four, fill = icon_color, outline = icon_color)
                alarms[4][1] = True               
                toggled_four[0] = False


    @staticmethod
    def alarm_window():
        global alarm_window_background
        global alarm_window_clear
        global snooze_button
        global snooze_label
        global time_label


        pygame.mixer.music.load(main_root + alarm_sound[0]) 
        pygame.mixer.music.play(loops = -1) 

        alarm_window_background = canvas.create_rectangle(800,480, 0, 0, fill = background_color, outline = background_color)
        canvas.move(alarm_window_background, 900, 0)
        #canvas.tag_bind(alarm_window_clear, "<Button-1>", pass)

        snooze_button = canvas.create_rectangle(300, 100, 0, 0, fill = icon_color, outline = icon_color)
        canvas.move(snooze_button, 1150, 200)
        
        snooze_label = canvas.create_text(1300,250, fill="white",font="Helvetica 50 bold", text = "Snooze")


        time_label = canvas.create_text(1300,100, fill="white",font="Helvetica 72 bold")
        def digitalclock_two():
            text_input = time.strftime("%I:%M %p")
            canvas.itemconfig(time_label, text=text_input)
            canvas.after(200, digitalclock_two)

        digitalclock_two()
        canvas.tag_bind(snooze_button, "<Button-1>", Exit.alarm_window_exit)
        canvas.tag_bind(snooze_label, "<Button-1>", Exit.alarm_window_exit)

        Menu.menu_down()

        while True:
            canvas.after(1, canvas.move(alarm_window_background, window_speed, 0))
            canvas.after(1, canvas.move(snooze_button, window_speed, 0))
            canvas.after(1, canvas.move(time_label, window_speed, 0))
            canvas.after(1, canvas.move(snooze_label, window_speed, 0))

            root.update()

            if canvas.coords(alarm_window_background)[0] == 0.0 or canvas.coords(snooze_button)[0] == 200.0 or canvas.coords(time_label)[0] == 200.0:
                break
            

class Music():
    @staticmethod
    def music(event):
        global music_clear
        global music_background
        global music_catalog_rect_one
        global music_catalog_rect_two
        global music_catalog_rect_three
        global music_catalog_rect_four
        global drop_icon_button
        global wave_icon_button
        global noise_icon_button
        global bamboo_icon_button


        music_background = canvas.create_rectangle(800,480, 0, 0, fill = background_color, outline = background_color)
        canvas.move(music_background, 900, 0)
        music_clear = canvas.create_image(20, 20, image=exit_icon, anchor=NW)
        canvas.move(music_clear, 920, 20)
        canvas.tag_bind(music_clear, "<Button-1>", Exit.music_exit)

        music_catalog_rect_one = canvas.create_rectangle((0, 0, 200, 200), fill=icon_color, outline = icon_color, tag = "1")
        canvas.move(music_catalog_rect_one, 1050, 20)
        music_catalog_rect_two = canvas.create_rectangle((0, 0, 200, 200), fill=icon_color, outline = icon_color, tag = "2")
        canvas.move(music_catalog_rect_two, 1320, 20)
        music_catalog_rect_three = canvas.create_rectangle((0, 0, 200, 200), fill=icon_color, outline = icon_color, tag = "3")
        canvas.move(music_catalog_rect_three, 1050, 270)
        music_catalog_rect_four = canvas.create_rectangle((0, 0, 200, 200), fill=icon_color, outline = icon_color, tag = "4")
        canvas.move(music_catalog_rect_four, 1320, 270)

        drop_icon_button = canvas.create_image(1085, 50, image=drop_icon, anchor=NW, tag = "1")
        wave_icon_button = canvas.create_image(1350, 50, image=wave_icon, anchor=NW, tag = "2")
        noise_icon_button = canvas.create_image(1075, 300, image=noise_icon, anchor=NW, tag = "3")
        bamboo_icon_button = canvas.create_image(1350, 300, image=bamboo_icon, anchor=NW, tag = "4")



        canvas.tag_bind(music_catalog_rect_one, "<Button-1>", Music.music_player)
        canvas.tag_bind(music_catalog_rect_two, "<Button-1>", Music.music_player)
        canvas.tag_bind(music_catalog_rect_three, "<Button-1>", Music.music_player)
        canvas.tag_bind(music_catalog_rect_four, "<Button-1>", Music.music_player)
        canvas.tag_bind(drop_icon_button, "<Button-1>", Music.music_player)
        canvas.tag_bind(wave_icon_button, "<Button-1>", Music.music_player)
        canvas.tag_bind(noise_icon_button, "<Button-1>", Music.music_player)
        canvas.tag_bind(bamboo_icon_button, "<Button-1>", Music.music_player)

        Menu.menu_down()

        while True:
            canvas.after(1, canvas.move(music_background, window_speed, 0))
            canvas.after(1, canvas.move(music_clear, window_speed, 0))
            canvas.after(1, canvas.move(music_catalog_rect_one, window_speed, 0))
            canvas.after(1, canvas.move(music_catalog_rect_two, window_speed, 0))
            canvas.after(1, canvas.move(music_catalog_rect_three, window_speed, 0))
            canvas.after(1, canvas.move(music_catalog_rect_four, window_speed, 0))
            canvas.after(1, canvas.move(drop_icon_button, window_speed, 0))
            canvas.after(1, canvas.move(wave_icon_button, window_speed, 0))
            canvas.after(1, canvas.move(noise_icon_button, window_speed, 0))
            canvas.after(1, canvas.move(bamboo_icon_button, window_speed, 0))

            root.update()

            if canvas.coords(music_background)[0] == 0.0 or canvas.coords(music_clear)[0] == 100.0:
                break
            
    @staticmethod
    def music_player(event):
        global main_root
        global mp_exit_button
        global mp_background
        global play_button
        global playing
        global play_icon_button

        songs = {}
        direc = main_root + "music"
        path = os.listdir(direc)


        if ".DS_Store" in path:
            path.remove(".DS_Store")

        for items in path:
            songs.update({path.index(items) + 1: [items, main_root+ "music/" + items]})

        def play(event):
            global playing
            if playing == False:
                pygame.mixer.music.pause() 
                canvas.itemconfig(play_button, fill = dark_icon_color, outline = dark_icon_color)
                canvas.itemconfig(play_icon_button, image = pause_icon)
                playing = True
            elif playing == True:
                pygame.mixer.music.unpause() 
                canvas.itemconfig(play_button, fill = icon_color, outline = icon_color)
                canvas.itemconfig(play_icon_button, image = play_icon)
                playing = False

        #loops through list to identiy song to play
        song_name = event.widget.gettags("current")[0]
        for key in songs:
            if song_name == str(key):
                song_id = songs[int(song_name)][0]
                pygame.mixer.music.load(songs[int(song_name)][1]) 
                pygame.mixer.music.play(loops = -1) 

        #draw music player interface
        mp_background = canvas.create_rectangle(800,480, 0, 0, fill = background_color, outline = background_color)
        canvas.move(mp_background, 900, 0)
        mp_exit_button = canvas.create_image(20, 20, image=exit_icon, anchor=NW)
        canvas.move(mp_exit_button, 920, 20)

        playing = False
        play_button = canvas.create_oval(300,300, 0, 0, fill = icon_color, outline = icon_color)
        canvas.move(play_button, 1150, 100)
        play_icon_button = canvas.create_image(1150, 100, image=play_icon, anchor=NW)

        canvas.tag_bind(play_button, "<Button-1>", play)
        canvas.tag_bind(play_icon_button, "<Button-1>", play)

        canvas.tag_bind(mp_exit_button, "<Button-1>", Exit.music_player_exit)

        #animate out
        while True:
            canvas.after(1, canvas.move(mp_background, -100, 0))
            canvas.after(1, canvas.move(mp_exit_button, -100, 0))
            canvas.after(1, canvas.move(play_button, -100, 0))
            canvas.after(1, canvas.move(play_icon_button, -100, 0))

            root.update()

            if canvas.coords(mp_background)[0] == 0.0 or canvas.coords(mp_exit_button)[0] == 100.0 or canvas.coords(play_button)[0] == 200:
                break




class Settings():
    @staticmethod
    def settings(event):
        global buttonFour
        global rectFour
        global power_text
        global alarm_sound_text
        global version_info_text
        global credit_info_text
        global power_button
        global alarm_sound_button

        global alarm_sound_index

        alarm_sound_index = [1]

        rectFour = canvas.create_rectangle(400,480, 0, 0, fill = background_color, outline = background_color)
        canvas.move(rectFour, 900, 0)
        buttonFour = canvas.create_image(20, 20, image=exit_icon, anchor=NW)
        canvas.move(buttonFour, 920, 20)
        canvas.tag_bind(buttonFour, "<Button-1>", Exit.settings_exit)

        power_button = canvas.create_rectangle(150,60, 0, 0, fill = icon_color, outline = icon_color)
        canvas.move(power_button, 975, 150)
        alarm_sound_button = canvas.create_rectangle(150,60, 0, 0, fill = icon_color, outline = icon_color)
        canvas.move(alarm_sound_button, 975, 250)

        power_text = canvas.create_text(1045,180, fill="white",font="Helvetica 15 bold", text = "Power")
        alarm_sound_text = canvas.create_text(1050,280, fill="white",font="Helvetica 15 bold", text = "Classic Alarm")
        version_info_text = canvas.create_text(1050,420, fill="white",font="Helvetica 15 bold", text = "SuperNova 1.0")
        credit_info_text = canvas.create_text(1050,440, fill="white",font="Helvetica 15 bold", text = "Developed By Ali Kesserwani")

        canvas.tag_bind(power_button, "<Button-1>", Settings.power)
        canvas.tag_bind(alarm_sound_button, "<Button-1>", Settings.alarm_sound)
        canvas.tag_bind(power_text, "<Button-1>", Settings.power)
        canvas.tag_bind(alarm_sound_text, "<Button-1>", Settings.alarm_sound)


        Menu.menu_down()
        while True:
            canvas.after(1, canvas.move(rectFour, -100, 0))
            canvas.after(1, canvas.move(buttonFour, -100, 0))
            canvas.after(1, canvas.move(power_text, -100, 0))
            canvas.after(1, canvas.move(alarm_sound_text, -100, 0))
            canvas.after(1, canvas.move(version_info_text, -100, 0))
            canvas.after(1, canvas.move(power_button, -100, 0))
            canvas.after(1, canvas.move(alarm_sound_button, -100, 0))
            canvas.after(1, canvas.move(credit_info_text, -100, 0))

            root.update()

            if canvas.coords(rectFour)[0] == 500.0 or canvas.coords(buttonFour)[0] == 550.0:
                break

    @staticmethod
    def power(event):
        global black_out
        black_out = canvas.create_rectangle(800,480, 0, 0, fill = "black", outline = "black")
        canvas.tag_bind(black_out, "<Button-1>", Settings.power_on)
    
    @staticmethod
    def power_on(event):
        canvas.delete(black_out)
        Exit.settings_exit_nonevent()

    @staticmethod
    def alarm_sound(event):
        if alarm_sound_index[0] == 1:
            canvas.itemconfig(alarm_sound_text, text = "Fresh Morning")
            canvas.itemconfig(alarm_sound_button, fill = night_shade, outline = night_shade)
            alarm_sound_index[0] = 2
            alarm_sound[0] = main_root + "alarm_sounds/fresh_morning.mp3"

            pygame.mixer.music.load(alarm_sound[0]) 
            pygame.mixer.music.play() 

        elif alarm_sound_index[0] == 2:
            canvas.itemconfig(alarm_sound_text, text = "Classical Alarm")
            canvas.itemconfig(alarm_sound_button, fill = icon_color, outline = icon_color)
            alarm_sound_index[0] = 1
            alarm_sound[0] = main_root + "alarm_sounds/alarm_classic.mp3"

            pygame.mixer.music.load(alarm_sound[0]) 
            pygame.mixer.music.play()


global window_speed_reverse
window_speed_reverse = 180

class Exit():
    @staticmethod
    def alarm_exit(event):
        Menu.menu_down()
        while True:
            canvas.after(1, canvas.move(alarm_background, window_speed_reverse, 0))
            canvas.after(1, canvas.move(alarm_exit_btn, window_speed_reverse, 0))
            canvas.after(1, canvas.move(clock_box_one, window_speed_reverse, 0))
            canvas.after(1, canvas.move(clock_box_two, window_speed_reverse, 0))
            canvas.after(1, canvas.move(clock_box_three, window_speed_reverse, 0))
            canvas.after(1, canvas.move(clock_box_four, window_speed_reverse, 0))
            canvas.after(1, canvas.move(time_text_one, window_speed_reverse, 0))
            canvas.after(1, canvas.move(time_text_two, window_speed_reverse, 0))
            canvas.after(1, canvas.move(time_text_three, window_speed_reverse, 0))
            canvas.after(1, canvas.move(time_text_four, window_speed_reverse, 0))
            canvas.after(1, canvas.move(toggle_one, window_speed_reverse, 0))
            canvas.after(1, canvas.move(toggle_two, window_speed_reverse, 0))
            canvas.after(1, canvas.move(toggle_three, window_speed_reverse, 0))
            canvas.after(1, canvas.move(toggle_four, window_speed_reverse, 0))
            canvas.after(1, canvas.move(toggle_button_one, window_speed_reverse, 0))
            canvas.after(1, canvas.move(toggle_button_two, window_speed_reverse, 0))
            canvas.after(1, canvas.move(toggle_button_three, window_speed_reverse, 0))
            canvas.after(1, canvas.move(toggle_button_four, window_speed_reverse, 0))
            canvas.after(1, canvas.move(accent_one, window_speed_reverse, 0))
            canvas.after(1, canvas.move(accent_two, window_speed_reverse, 0))
            canvas.after(1, canvas.move(accent_three, window_speed_reverse, 0))
            canvas.after(1, canvas.move(accent_four, window_speed_reverse, 0))

            root.update()

            if canvas.coords(alarm_background)[0] == 900.0 or canvas.coords(alarm_exit_btn)[0] == 1000.0 or canvas.coords(clock_box_one)[0] == 1000.0 or canvas.coords(clock_box_two)[0] == 1100.0 or canvas.coords(clock_box_three)[0] == 1000.0 or canvas.coords(clock_box_four)[0] == 1100.0 or canvas.coords(time_text_one)[0] == 1000.0 or canvas.coords(time_text_two)[0] == 1100.0 or canvas.coords(time_text_three)[0] == 1000.0 or canvas.coords(time_text_four)[0] == 1100.0:
                break





    @staticmethod
    def create_alarm_exit(event):
        Menu.menu_down()
        while True:
            canvas.after(1, canvas.move(ca_background, window_speed_reverse, 0))
            canvas.after(1, canvas.move(ca_exit_button, window_speed_reverse, 0))
            canvas.after(1, canvas.move(alarm_text, window_speed_reverse, 0))
            canvas.after(1, canvas.move(hour_down_btn, window_speed_reverse, 0))
            canvas.after(1, canvas.move(hour_up_btn, window_speed_reverse, 0))
            canvas.after(1, canvas.move(label_one, window_speed_reverse, 0))
            canvas.after(1, canvas.move(minute_down_btn, window_speed_reverse, 0))
            canvas.after(1, canvas.move(minute_up_btn, window_speed_reverse, 0))
            canvas.after(1, canvas.move(label_two, window_speed_reverse, 0))
            canvas.after(1, canvas.move(submit_rect, window_speed_reverse, 0))
            canvas.after(1, canvas.move(add_alarm, window_speed_reverse, 0))

            root.update()

            if canvas.coords(ca_background)[0] == 900.0 or canvas.coords(ca_exit_button)[0] == 1000.0 or canvas.coords(alarm_text)[0] == 1050.0 or canvas.coords(hour_down_btn)[0] == 900.0 or canvas.coords(hour_up_btn)[0] == 1000.0 or canvas.coords(label_one)[0] == 1000.0 or canvas.coords(minute_down_btn)[0] == 1100.0 or canvas.coords(minute_up_btn)[0] == 1100.0 or canvas.coords(label_two)[0] == 1100.0 or canvas.coords(submit_rect)[0] == 1400.0:
                break

    @staticmethod
    def create_alarm_exit_nonevent():
        Menu.menu_down()
        while True:
            canvas.after(1, canvas.move(ca_background, window_speed_reverse, 0))
            canvas.after(1, canvas.move(ca_exit_button, window_speed_reverse, 0))
            canvas.after(1, canvas.move(alarm_text, window_speed_reverse, 0))
            canvas.after(1, canvas.move(hour_down_btn, window_speed_reverse, 0))
            canvas.after(1, canvas.move(hour_up_btn, window_speed_reverse, 0))
            canvas.after(1, canvas.move(label_one, window_speed_reverse, 0))
            canvas.after(1, canvas.move(minute_down_btn, window_speed_reverse, 0))
            canvas.after(1, canvas.move(minute_up_btn, window_speed_reverse, 0))
            canvas.after(1, canvas.move(label_two, window_speed_reverse, 0))
            canvas.after(1, canvas.move(submit_rect, window_speed_reverse, 0))
            canvas.after(1, canvas.move(add_alarm, window_speed_reverse, 0))

            root.update()

            if canvas.coords(ca_background)[0] == 900.0 or canvas.coords(ca_exit_button)[0] == 1000.0 or canvas.coords(alarm_text)[0] == 1050.0 or canvas.coords(hour_down_btn)[0] == 900.0 or canvas.coords(hour_up_btn)[0] == 1000.0 or canvas.coords(label_one)[0] == 1000.0 or canvas.coords(minute_down_btn)[0] == 1100.0 or canvas.coords(minute_up_btn)[0] == 1100.0 or canvas.coords(label_two)[0] == 1100.0 or canvas.coords(submit_rect)[0] == 1400.0:
                break


    @staticmethod
    def music_exit(event):
        Menu.menu_down()
        while True:
            canvas.after(1, canvas.move(music_background, window_speed_reverse, 0))
            canvas.after(1, canvas.move(music_clear, window_speed_reverse, 0))
            canvas.after(1, canvas.move(music_catalog_rect_one, window_speed_reverse, 0))
            canvas.after(1, canvas.move(music_catalog_rect_two, window_speed_reverse, 0))
            canvas.after(1, canvas.move(music_catalog_rect_three, window_speed_reverse, 0))
            canvas.after(1, canvas.move(music_catalog_rect_four, window_speed_reverse, 0))
            canvas.after(1, canvas.move(drop_icon_button, window_speed_reverse, 0))
            canvas.after(1, canvas.move(wave_icon_button, window_speed_reverse, 0))
            canvas.after(1, canvas.move(noise_icon_button, window_speed_reverse, 0))
            canvas.after(1, canvas.move(bamboo_icon_button, window_speed_reverse, 0))

            root.update()

            if canvas.coords(music_background)[0] == 900.0 or canvas.coords(music_clear)[0] == 1000.0:
                break

    @staticmethod
    def settings_exit(event):
        pygame.mixer.music.stop()

        Menu.menu_down()
        while True:
            canvas.after(1, canvas.move(rectFour, window_speed_reverse, 0))
            canvas.after(1, canvas.move(buttonFour, window_speed_reverse, 0))
            canvas.after(1, canvas.move(power_text, window_speed_reverse, 0))
            canvas.after(1, canvas.move(alarm_sound_text, window_speed_reverse, 0))
            canvas.after(1, canvas.move(version_info_text, window_speed_reverse, 0))
            canvas.after(1, canvas.move(power_button, window_speed_reverse, 0))
            canvas.after(1, canvas.move(alarm_sound_button, window_speed_reverse, 0))
            canvas.after(1, canvas.move(credit_info_text, window_speed_reverse, 0))

            root.update()

            #crash error so update code
            if canvas.coords(rectFour)[0] == 500.0 or canvas.coords(buttonFour)[0] == 500.0:
                break
    
    @staticmethod
    def settings_exit_nonevent():
        pygame.mixer.music.stop()

        Menu.menu_down()
        while True:
            canvas.after(1, canvas.move(rectFour, window_speed_reverse, 0))
            canvas.after(1, canvas.move(buttonFour, window_speed_reverse, 0))
            canvas.after(1, canvas.move(power_text, window_speed_reverse, 0))
            canvas.after(1, canvas.move(alarm_sound_text, window_speed_reverse, 0))
            canvas.after(1, canvas.move(version_info_text, window_speed_reverse, 0))
            canvas.after(1, canvas.move(power_button, window_speed_reverse, 0))
            canvas.after(1, canvas.move(alarm_sound_button, window_speed_reverse, 0))
            canvas.after(1, canvas.move(credit_info_text, window_speed_reverse, 0))

            root.update()

            #crash error so update code
            if canvas.coords(rectFour)[0] == 500.0 or canvas.coords(buttonFour)[0] == 500.0:
                break


    @staticmethod
    def music_player_exit(event):
        Menu.menu_down()
        while True:
            canvas.after(1, canvas.move(mp_background, window_speed_reverse, 0))
            canvas.after(1, canvas.move(mp_exit_button, window_speed_reverse, 0))
            canvas.after(1, canvas.move(play_button, window_speed_reverse, 0))
            canvas.after(1, canvas.move(play_icon_button, window_speed_reverse, 0))

            root.update()

            if canvas.coords(mp_background)[0] == 900.0 or canvas.coords(mp_exit_button)[0] == 1000.0 or canvas.coords(play_button)[0] == 1100:
                break

    @staticmethod
    def alarm_window_exit(event):
        Menu.menu_down()

        #stop alarm
        pygame.mixer.music.stop()

        while True:
            canvas.after(1, canvas.move(alarm_window_background, window_speed_reverse, 0))
            canvas.after(1, canvas.move(snooze_button, window_speed_reverse, 0))
            canvas.after(1, canvas.move(time_label, window_speed_reverse, 0))
            canvas.after(1, canvas.move(snooze_label, window_speed_reverse, 0))

            root.update()

            if canvas.coords(alarm_window_background)[0] == 900.0 or canvas.coords(snooze_button)[0] == 1100.0 or canvas.coords(time_label)[0] == 1100.0:
                break





#start functions
digitalclock()
Menu.menu()

root.mainloop()
