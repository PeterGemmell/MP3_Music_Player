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
