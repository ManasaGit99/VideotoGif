# First need to import moviepy package using pip
# pip install moviepy
from moviepy.editor import VideoFileClip;

# download any mp4 video
# place it in the current working project folder

# give the file name in the function VideoFileClip
video = VideoFileClip("Shinchan.mp4.mp4")
video.write_gif("Shinchan.gif")

# Finally, the video clip is converted to gif using write_gif method
