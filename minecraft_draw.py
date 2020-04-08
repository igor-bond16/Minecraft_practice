import math
from PIL import Image
from mcpi.minecraft import Minecraft
from mcpi.block import *


toRGB = {
    "WOOL_BLACK": (26,22,22),
    "WOOL_BLUE": (46,57,142),
    "WOOL_BROWN": (79,51,31),
    "WOOL_CYAN": (47,111,137),
    "WOOL_GRAY": (64,64,64),
    "WOOL_GREEN": (53,71,27),
    "WOOL_LIGHT_BLUE": (107,138,201),
    "WOOL_LIGHT_GRAY": (155,161,161),
    "WOOL_LIME": (66,174,57),
    "WOOL_MAGENTA": (180,81,189),
    "WOOL_ORANGE": (219,125,63),
    "WOOL_PINK": (208,132,153),
    "WOOL_PURPLE": (127,62,182),
    "WOOL_RED": (151,52,49),
    "WOOL_WHITE": (222,222,222),
    "WOOL_YELLOW": (177,166,39),
}

def getNearRgbBlockid(mr,mg,mb):
    distant_dict = {}
    for blockid in toRGB:
        r,g,b = toRGB[blockid]
        distance = math.sqrt((mr-r)*(mr-r)+(mg-g)*(mg-g)+(mb-b)*(mb-b))
        distant_dict[blockid] = distance
        
    srt_distance_dict = sorted(distant_dict.items(),key=lambda x:x[1])
    key,value = srt_distance_dict[0]
    
    return key

mc = Minecraft.create()
pos = mc.player.getTilePos()

img = Image.open("download.jpeg")
img = img.resize((100,100))

if img.mode != "RGB":
    img = img.convert("RGB")
    
width,height = img.size

for wx in range(width):
    for hy in range(height):
        r,g,b = img.getpixel((wx,hy))
        mc.setBlock(pos.x+wx,pos.y,pos.z+hy,getNearRgbBlockid(r,g,b))