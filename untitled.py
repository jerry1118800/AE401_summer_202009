from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()

time.sleep(5)

X,Y,Z=mc.player.getTilePos()

mc.setBlocks(X+3,Y+4,Z+2,X-3,Y-4,Z-2,103)
