from mcpi.minecraft import Minecraft
we = Minecraft.create()

while True:
    hits = we.events.pollProjectileHits()
    if len(hits) >0:
        a = hits[0]
        x,y,z = a.pos.x,a.pos.y,a.pos.z
        we.createExplosion(x,y,z,power=100)
        