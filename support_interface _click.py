import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def btn_check_vuln():
    sys.stdout.flush()

def btn_help_click():
    sys.stdout.flush()

def btn_quit_click():
    sys.stdout.flush()

def btn_scan_click():
    sys.stdout.flush()

def btn_stop_click():
    sys.stdout.flush()

def select_all():
    sys.stdout.flush()

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import web_scan
    web_scan.vp_start_gui()

