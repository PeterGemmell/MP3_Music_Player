import pygame #used to create video games, music players etc
import tkinter as tkr # used to develop a GUI
from tkinter.filedialog import askdirectory #it permit to select dir
import os #it permits to interact with the operating system

music_player = tkr.Tk()
music_player.title("Life In Music")
music_player.geometry("450x350")

directory = askdirectory()
os.chdir(directory) # This permits to change the current directory
song_list = os.listdir() # This returns the list of files songs

# Here we create a variable which brings the interface to display items to the user.
# We then create a for loop in order to push the programme to select each item from the song list and
# insert them into the list box.
play_list = tkr.Listbox(music_player, font="Helvetica 12 bold",
bg="yellow", selectmode=tkr.SINGLE)

for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos += 1

# We use pygame for loading and playing sounds
pygame.init()
pygame.mixer.init()

# Here we will define functions to control the music player. We also use tkinter to create the buttons
# on the interface.

def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()


# Next we create the buttons for the interface of the music player

Button1 = tkr.Button(music_player, width=5, height=3,font="Helvetica 12 bold", text="PLAY", command=play, bg="blue",fg="white")
Button2 = tkr.Button(music_player, width=5, height=3, font=”Helvetica 12 bold”, text=”STOP”, command=stop, bg=”red”, fg=”white”)
Button3 = tkr.Button(music_player, width=5, height=3, font=”Helvetica 12 bold”, text=”PAUSE”, command=pause, bg=”purple”, fg=”white”)
Button4 = tkr.Button(music_player, width=5, height=3, font=”Helvetica 12 bold”, text=”UNPAUSE”, command=unpause, bg=”orange”, fg=”white”)
