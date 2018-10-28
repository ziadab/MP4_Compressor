import os

print("Welcome to MP4 compresser\n\n")
path = str(input("Put the path of the mp4 file : "))

if os.path.exists(path):
    if ".mp4" in path:
        new_path = str(input("\n Put the new mp4 path : "))
        os.system("ffmpeg -i "+ path + " -vcodec h264 -acodec mp2" + new_path)
        print("Done.")
    else:
        print('\nSorry but the file should be an mp4')
else:
    print("\nSorry :( But the file not found")
