from mcpi.minecraft import Minecraft
we = Minecraft.create()
import random,time

while True:
    x,y,z, = we.player.getPos()
    a = random.uniform(-20,20)
    b = random.uniform(-20,20)
    y = y+30
    we.spawnEntity(x+a,y,z+b,93)
    time.sleep(0.1)