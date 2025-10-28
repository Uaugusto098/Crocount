import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
import webview
from tkhtmlview import HTMLLabel
import threading
import multiprocessing
from time import strftime

#funções
count=0
def webb(): 
    url="https://www.youtube.com/"
    webview.create_window('Player Mor',url,on_top=True)
    webview.start()
    
def insta():
      url='https://www.instagram.com/'
      webview.create_window('Insta',url,on_top=True)
      webview.start()

def netflix():
      url='https://www.netflix.com/browse'
      webview.create_window('Netflix',url,on_top=True)
      webview.start()
    
def process():
       multiprocessing.Process(target=webb).start()

def processinsta():
      multiprocessing.Process(target=insta).start()

def processnetflix():
      multiprocessing.Process(target=netflix).start()




