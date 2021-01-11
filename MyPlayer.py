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
