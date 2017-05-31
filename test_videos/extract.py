import os
from moviepy.editor import *

def extract_frames(movie, times, imgdir):
    clip = VideoFileClip(movie)
    for t in times:
        imgpath = os.path.join(imgdir, '{}.jpg'.format(t))
        clip.save_frame(imgpath, t)

movie = 'solidWhiteRight.mp4'
imgdir = 'frames'
times = 0.1, 0.63, 0.947, 1.2, 3.8, 6.7

extract_frames(movie, times, imgdir)
