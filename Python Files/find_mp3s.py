#This program is folder specific!!!
# It searches through all the folders and files at the given location
# and creates a file, where all the song files are written to.

from os import listdir, walk
from os.path import isfile
import re

target = open("List of songs.txt", "w")

def get_songs_only():
    dirs = [x for x in walk("D:\Ivan\Multimedia\My music")]
    

    for element in dirs:

        target.write("\n" + element[0] + "\n\n\n")

        if len(element[2]) > 0:
            
            for song in element[2]:

                if song[-1] == "g":
                    continue

                if song[-2] == "p" or song[-2] == "a":

                    target.write(song + "\n")
        
        

    target.close()

    
get_songs_only()

