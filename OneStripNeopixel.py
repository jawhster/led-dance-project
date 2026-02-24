#include all neccessary packages to get LEDs to work with Raspberry Pi
import time
import board
import neopixel

def constantColor(pixels, pixelStart, pixelEnd, rgb):
    pixels[pixelStart:pixelEnd] = [rgb[0], rgb[1], rgb[2]] * abs(pixelEnd - pixelStart)
    
def buildUp(pixels, pixelStart, pixelEnd, rgbStart, rgbEnd, brightStart, brightEnd, duration, steps, reverse = False):
    timePassed = 0
    timeIncrement = duration / steps # make function for all of these getIncrement
    redIncrement = (rgbEnd[0] - rgbStart[0]) / steps
    greenIncrement = (rgbEnd[1] - rgbStart[1]) / steps
    blueIncrement = (rgbEnd[2] - rgbStart[2]) / steps
    pixelIncrement = (pixelEnd - pixelStart) / steps
    brightIncrement = (brightEnd - brightStart) / steps
    pixelBuild = pixelStart
    red = rgbStart[0]
    green = rgbStart[1]
    blue = rgbStart[2]
    print(pixelStart, pixelEnd, pixelIncrement)
    
    while timePassed < duration:
        if reverse:
            timePassed += timeIncrement
            print(timePassed)
            pixelBuild += int(pixelIncrement)
            red += int(redIncrement)
            green += int(greenIncrement)
            blue += int(blueIncrement)
            print(red, green, blue)
            print(pixelBuild)
            pixels[pixelBuild:pixelStart] = [[red, green, blue]] * (pixelStart-pixelBuild)
            print(pixels[pixelBuild:pixelStart])
        else:
            timePassed += timeIncrement
            print(timePassed)
            pixelBuild += int(pixelIncrement)
            red += int(redIncrement)
            green += int(greenIncrement)
            blue += int(blueIncrement)
            print(red, green, blue)
            print(pixelBuild)
            pixels[pixelStart:pixelBuild] = [[red, green, blue]] * (pixelBuild-pixelStart)
            print(pixels[pixelStart:pixelBuild])
        time.sleep(timeIncrement)
    #pixelBuild += int(pixelIncrement)
    #print(pixelBuild)
    #pixels[pixelStart:pixelBuild] = [[red, green, blue]] * (pixelBuild-pixelStart)
    #print(pixels[pixelStart:pixelBuild])
    #time.sleep(timeIncrement)

#Initialise a strips variable, provide the GPIO Data Pin
#utilised and the amount of LED Nodes on strip and brightness (0 to 1 value)
pixels1 = neopixel.NeoPixel(board.D18, 60, brightness=0.01)

#Also create an arbitary count variable
x=0

#Focusing on a particular strip, use the command Fill to make it all a single colour
#based on decimal code R, G, B. Number can be anything from 255 - 0. Use a RGB Colour
#Code Chart Website to quickly identify a desired fill colour.
pixels1.fill((0, 220, 102))
print(type(pixels1))
print(type(pixels1[1:8]))
print(pixels1[8])

#Below demonstrates how to individual address a colour to a LED Node, in this case
#LED Node 10 and colour Blue was selected
pixels1[10] = (200, 0, 200)

#Sleep for three seconds, You should now have all LEDs showing light with the first node
#Showing a different colour
time.sleep(3)

#Little Light slider script, it will produce a nice loading bar effect all the way up
#and then all the way back
#This was created using a While Loop taking advantage of that arbitary variable to determine
#which LED Node we will taget/index with a different colour

buildUp(pixels1, 1, 41, (255, 0, 0), (0, 255, 0), 0.1, 0.1, 8, 8)
constantColor(pixels1, 1, 41, (0, 0, 255))

buildUp(pixels1, 41, 1, (255, 0, 0), (0, 255, 0), 0.1, 0.1, 8, 8, True)
constantColor(pixels1, 41, 1, (0, 0, 255))

buildUp(pixels1, 1, 41, (255, 0, 0), (0, 255, 0), 0.1, 0.1, 16, 8)
constantColor(pixels1, 1, 41, (0, 0, 255))

buildUp(pixels1, 41, 1, (255, 0, 0), (0, 255, 0), 0.1, 0.1, 16, 8, True)
constantColor(pixels1, 41, 1, (0, 0, 255))

#Below will loop until variabe x has value 35
while x<49:
    
    pixels1[x] = (255, 0, 0)
    pixels1[x-5] = (0, 255, 0)
    pixels1[x-10] = (0, 0, 255)
    #Add 1 to the counter
    x=x+1
    #Add a small time pause which will translate to 'smoothly' changing colour
    time.sleep(0.25)

#below section is the same process as above loop just in reverse
while x>-15:
    pixels1[x] = (255, 0, 0)
    pixels1[x+5] = (255, 0, 100)
    pixels1[x+10] = (0, 255, 0)
    x=x-1
    time.sleep(0.05)

#Add a brief time delay to appreciate what has happened    
time.sleep(4)



#Complete the script by returning all the LED to off
pixels1.fill((0, 0, 0))

