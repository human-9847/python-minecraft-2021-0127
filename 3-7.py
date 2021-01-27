def plantTree(x,y,z):
    we.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,18)
    we.setBlocks(x,y,z,x,y+4,z,17)
from mcpi.minecraft import Minecraft
we = Minecraft.create()
x,y,z = we.player.getTilePos()
for i in range(0,50,5):
    plantTree(x+i,y,z)
