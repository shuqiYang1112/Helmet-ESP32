import os
import subprocess

class avitomp4:

    def avi_to_web_mp4(self, input_file_path):
        output_file_path = input_file_path[:-9] + 'static/video/video.mp4'
        cmd = 'ffmpeg -y -i {} -vcodec h264 {}'.format(input_file_path, output_file_path)
        subprocess.call(cmd, shell=True)
        return output_file_path
