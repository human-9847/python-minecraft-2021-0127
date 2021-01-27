from mcpi.minecraft import Minecraft
we = Minecraft.create()
x,y,z = we.player.getTilePos()
for i in range(0,20):
    we.setBlock(x+i+1,y-1,z+i,46)
    we.setBlock(x+i+2,y-1,z+i,46)
    we.setBlock(x+i+3,y-1,z+i,46)