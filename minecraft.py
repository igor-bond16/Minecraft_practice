from mcpi.minecraft import Minecraft
from mcpi.block import *
import time

time.sleep(3)


mc = Minecraft.create()
pos = mc.player.getTilePos()

block_type = mc.getBlock(pos.x,pos.y-1,pos.z)

while True:
    if block_type == 2:
        mc.setBlock(pos.x,pos.y,pos.z,38)
        