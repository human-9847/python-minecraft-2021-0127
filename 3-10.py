from mcpi.minecraft import Minecraft
we = Minecraft.create()
x,y,z = we.player.getTilePos()
line1 = []
line2 = []
line3 = []
 
for i in range(1,4):
    line1.append(1*i)
    line2.append(2*i)
    line3.append(3*i)
we.setSign(x,y,z,63,0,str(line1),str(line2),str(line3))