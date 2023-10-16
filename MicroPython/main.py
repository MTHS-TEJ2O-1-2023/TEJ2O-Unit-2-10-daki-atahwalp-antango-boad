"""
Created by: Daki A.B
Created on: Oct 2023
This module turns on certain RGB LEDs based on the light level
"""

from microbit import *


# screen clean up
display.clear()
amount_of_light = input.lightlevel()
neopixelstrip = neopixel.NeoPixel(pin0, 4)
neopixelstrip[0] = (0, 0, 0)
neopixelstrip[1] = (0, 0, 0)
neopixelstrip[2] = (0, 0, 0)
neopixelstrip[3] = (0, 0, 0)
neopixelstrip.show()
display.show(Image.HAPPY)

while True:
    # if button A is pressed, run the program
    if button_a.is_pressed():
        display.show(Image.HAPPY)
        neopixelstrip[0]

        if amount_of_light <= 51:
            neopixelstrip[0] = (0, 0, 0)
            neopixelstrip[1] = (0, 0, 0)
            neopixelstrip[2] = (0, 0, 0)
            neopixelstrip[3] = (0, 0, 0)
            neopixelstrip.show()
            display.scroll("0")

        # if light level is equal or greater than 52 one all neopixels on
        if amount_of_light >= 52:
            neopixelstrip[0] = (255, 0, 255)
            neopixelstrip.show()
            display.scroll("1")

        # if light level is equal or greater than 208 turn two neopixels on
        if amount_of_light >= 104:
            neopixelstrip[0] = (255, 0, 255)
            neopixelstrip[1] = (255, 0, 255)
            neopixelstrip.show()
            display.scroll("2")

        # if light level is equal or greater than 156 turn three neopixels on
        if amount_of_light >= 156:
            neopixelstrip[0] = (255, 0, 255)
            neopixelstrip[1] = (255, 0, 255)
            neopixelstrip[2] = (255, 0, 255)
            neopixelstrip.show()
            display.scroll("3")

        # if light level is equal or greater than 208 turn all neopixels on
        if amount_of_light >= 208:
            neopixelstrip[0] = (255, 0, 255)
            neopixelstrip[1] = (255, 0, 255)
            neopixelstrip[2] = (255, 0, 255)
            neopixelstrip[3] = (255, 0, 255)
            neopixelstrip.show()
            display.scroll("4")

    # when button B is pressed turn neopixel lights off
    if button_b.is_pressed():
        display.clear()
        neopixelstrip[0] = (0, 0, 0)
        neopixelstrip[1] = (0, 0, 0)
        neopixelstrip[2] = (0, 0, 0)
        neopixelstrip[3] = (0, 0, 0)
        neopixelstrip.show()
        display.show(Image.HAPPY)
