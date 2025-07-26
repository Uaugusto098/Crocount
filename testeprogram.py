from tkhtmlview import HTMLLabel
import tkinter as tk
import webview


url = "https://www.youtube.com/watch?v=JsZMlGCcjug"
webview.create_window("YouTube Player", url)
webview.start()
root = tk.Tk()
html = """
<iframe width="560" height="315" src="https://www.youtube.com/watch?v=JsZMlGCcjug"
frameborder="0" allowfullscreen></iframe>
"""
label = HTMLLabel(root, html=html)
label.pack(fill="both", expand=True)
root.mainloop()
