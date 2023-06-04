import moviepy.editor as mp
my_clip = mp.VideoFileClip(r"How To Flirt Using Your Eyes.mp4")
my_clip
my_clip.audio.write_audiofile(r"Audio File of Video 2.mp3")
