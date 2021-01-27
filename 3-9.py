from mcpi.minecraft import Minecraft
we = Minecraft.create()
x,y,z = we.player.getTilePos()
base = 18
height = (base//2)+1
for i in range(height):
    x1 = x + i
    y1 = y + i
    z1 = z + i
    
    x2 = x + base - i
    z2 = z + base - i
    we.setBlocks(x1,y1,z1,x2,y1,z2,46)