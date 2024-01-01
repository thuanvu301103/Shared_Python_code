from moviepy.editor import *
import random


'''
    Create short clip randomly from long video
'''
def create_rnd_clip (video_lnk, length, clip_lnk):

    # video_lnk: path of the origin video file
    # length: length of new clip (seconds) 
    # clip_lnk: path of the created clip
    try:
        video = VideoFileClip(video_lnk)
        video_length = video.duration
        start = random.randint(0, int(video_length - length))
        clip = video.subclip(start, start + length)
        clip.write_videofile(clip_lnk ,codec='libx264')
        return True
    except:
        return False


