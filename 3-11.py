from mcpi.minecraft import Minecraft
we = Minecraft.create()
x,y,z = we.player.getPos()
number = 1

for i in range(8):
    for j in range(number):
        we.spawnEntity(x,y,z,60)
    number = number *2
    we.postToChat("這次生成了"+str(number)+"隻蠹蟲")