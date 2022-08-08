from PIL import Image
import cv2
from math import sqrt

videoName = "arbys" #no file ending, has to be .mp4
outputPath = "C:\\Users\\User\\Desktop\\unwichtiger shit\\rob a fucking bank kid\\hm\\workspace\\output\\"
imageWidth = 70 #// 70, wouldnt change since thats the default width of the console
imageHeight = 34 #//34 for short, less for longer e.g. 32 if you use more than 34 + a newline it gets cut off at the top

emojis = [['😃', (255, 204, 77)], ['😡', (218, 47, 71)], ['🙊', (191, 105, 82)], ['✅', (119, 178, 85)], ['❤', (187, 26, 52)], ['💙', (93, 173, 236)], ['💚', (120, 177, 89)], ['💛', (253, 203, 88)], ['💜', (170, 142, 214)], ['⚫', (0, 0, 0)], ['🌕', (204, 214, 221)], ['🐷', (244, 171, 186)], ['📀', (255, 217, 131)], ['🍊', (244, 144, 12)], ['🍪', (217, 158, 130)], ['🍑', (255, 136, 108)], ['🍐', (166, 211, 136)], ['🐙', (146, 102, 204)], ['👕', (59, 136, 195)], ['👛', (234, 89, 110)], ['💭', (189, 221, 244)], ['🍓', (204, 62, 83)], ['💰', (253, 216, 136)], ['🌳', (92, 145, 59)], ['🎀', (221, 46, 68)], ['🐘', (153, 170, 181)], ['💼', (154, 78, 28)], ['🌚', (102, 117, 127)], ['⚪', (255, 255, 255)]]

def closest_color(rgb): #// gets the most fitting emoji to use for the pixel to represent
    r, g, b = rgb
    color_diffs = []
    for z in emojis:
        color = z[1]
        cr, cg, cb = color
        color_diff = sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2)
        color_diffs.append((color_diff, z[0]))
    return min(color_diffs)[1]

def turnascii(image_path): #// takes an image path as input and returns the emojified version of that image with the square size of <imageWidth>
   img = Image.open(image_path)
   newWidth = imageWidth
   newHeight = imageWidth / 2
   
   img = img.convert("RGB")
   pixels = img.getdata()
   newPixels = [closest_color(pixel) for pixel in pixels]

   newPixels = ''.join(newPixels)

   newPixels_count = len(newPixels)
   #print(newPixels_count)
   asciiImage = [newPixels[index:index + newWidth] for index in range(0, newPixels_count, newWidth)]
   asciiImage = "".join(asciiImage)
   return asciiImage + "N"
           
vidCap = cv2.VideoCapture(videoName+".mp4")
length = int(vidCap.get(cv2.CAP_PROP_FRAME_COUNT))
count = 1
totalMessage = ""
while True:
    success,image = vidCap.read()
    if success:
        resized = cv2.resize(image,(imageWidth,imageHeight))
        cv2.imwrite(f"./frames/frame{count}.jpg", resized)  
        totalMessage += turnascii(f"./frames/frame{count}.jpg")
        print(f"Rendered frame: {count}/{length}")
        count += 1
    else:
        print(f"Done. Rendered all {count-1} frames")
        break
 
with open(f"{outputPath}{videoName}.txt", "w+", encoding="utf-8") as fle:
    fle.write(totalMessage)
