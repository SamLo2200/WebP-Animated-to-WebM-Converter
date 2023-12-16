import subprocess

# Remember to change the following path variables in order for this script to work

# file
# pathToWebpmux (located in grep_file_info function)
# extractedPath (located in extract_animated_webp function)
# source (The folder path should be same as the extractedPath variable, located in the render function)
# endOutput (located in the render function) 
# pathToFFMPEG (located in the render function)



#### Reminder for people who are not familiar with python 

# In python, for any path, you need to use \\ to represent a layer of folder

# For example if the file path is: "C:\Users\sam\Downloads\WebP_Animated_Extractor" 
# Please change it to "C:\\Users\\sam\\Downloads\\WebP_Animated_Extractor" 



##Dependencies download url
# 1: https://developers.google.com/speed/webp/download 
# 2: https://www.gyan.dev/ffmpeg/builds/ (Recommended to install the full version, because I haven't test whether the essential ffmpeg will work)

while True: 
    fileNameUser = input("name of the file: ") #The file name of the corresponding webp file name, e.g. animated1.webp, please enter animated1
    file = f'C:\\Users\\sam\\Downloads\\WebP_Animated_Extractor\\WebP_source\\{fileNameUser}.webp'

    class converter:

        def grep_file_info(file):
            global pathToWebpmux
            pathToWebpmux = "C:\\Users\\sam\\Downloads\\WebP_Animated_Extractor\\Dependencies\\libwebp\\bin\\webpmux.exe" #webpmux.exe location
        

            ##Get the total Frames of a webp animated file---------------------------

            getFileFrameNo1 = subprocess.run([pathToWebpmux, '-info', file], capture_output=True, text=True)
            getFileFrameNo2 = subprocess.run(['findstr', '/C' ':' "Number of frames:"], capture_output=True, text=True, input=getFileFrameNo1.stdout) #A follow up process to get total of frames in the webp file
    
            #print(getFileFrameNo2.stdout)

            global processedInfo

            processedInfo = getFileFrameNo2.stdout.split(' ', 3).pop()
            #print(processedInfo)
        

            converter.extract_animated_webp(int(processedInfo))
    

            #-----------------------------------------------------------------------

        def extract_animated_webp(totalFrame):
            frame = 1 
            while frame < totalFrame + 1:
            
                print("[python]" + str(frame))

                if frame < 10:
                    outFileName = str(fileNameUser + "_") + str("0") + str(frame)
                else: 
                    outFileName = str(fileNameUser + "_") + str(frame)

                extractedPath = f"C:\\Users\\sam\\Downloads\\WebP_Animated_Extractor\\extraction_temp\\{outFileName}.webp" #Where you want to store the extracted images, requires manual cleanup later 

                #EXtract------------------
            
                Extration = subprocess.run([pathToWebpmux, '-get', 'frame', str(frame), file, '-o', str(extractedPath)], capture_output=True, text=True) #break animated webp into individual webp file
                print(Extration)


                if frame == totalFrame:
                    converter.render(totalFrame)

                #------------------------
                frame = frame + 1

        def render(totalFrame): 

            source = "C:\\Users\\sam\\Downloads\\WebP_Animated_Extractor\\extraction_temp\\" + fileNameUser + "_%02d.webp" ##The folder path should be same as the extractedPath variable
            endOutput = "C:\\Users\\sam\\Downloads\\WebP_Animated_Extractor\\output\\" + fileNameUser + ".webm" #Where you want to store the output webm file  

            pathToFFMPEG = "C:\\Users\\sam\\Downloads\\WebP_Animated_Extractor\\Dependencies\\ffmpeg\\bin\\ffmpeg.exe" #FFmpeg.exe location 

            #print(source)

            #no compression
            #Render = subprocess.run(['C:\\Users\\sam\\Downloads\\ffmpeg-2023-09-04-git-f8503b4c33-full_build\\bin\\ffmpeg.exe', '-framerate', str(totalFrame), '-i',str(source), '-c:v', 'libvpx-vp9', '-pix_fmt', 'yuva420p', endOutput],capture_output=True, text=True)
            
            #With Compression
            Render = subprocess.run([pathToFFMPEG, '-y', '-framerate', str(totalFrame), '-i',str(source), '-crf', '0', '-b:v', '1.7M', endOutput],capture_output=True, text=True) #
            print(Render)


    converter.grep_file_info(file)
