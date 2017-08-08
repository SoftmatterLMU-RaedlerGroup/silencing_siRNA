#! /usr/bin/env python3

def getTimeStamp():
    """Returns a human-readable string representation of the current time"""
    import time
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d–%H%M%S")

def getOutpath():
    """Returns (and creates, if necessary) the path to a directory called “out” inside the current directory."""
    import os
    outpath = os.path.join(os.getcwd(), 'out')
    if not os.path.isdir(outpath) and not os.path.lexists(outpath):
        os.mkdir(outpath)
    return outpath

