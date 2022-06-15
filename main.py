from pytube import YouTube


file1 = open('myfile.txt', 'r')
Lines = file1.readlines()
  
# Strips the newline character
for line in Lines:
    yt = YouTube(line)
    stream = yt.streams.get_audio_only()
    stream.download()
    print("Done")