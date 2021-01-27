from mcpi.minecraft import Minecraft
we = Minecraft.create()
while True:
     hits = we.events.pollBlockHits()
     if len(hits)>0:
         a = hits[0]
         x,y,z = a.pos.x,a.pos.y,a.pos.z
         block = we.getBlock(x,y,z)
         we.postToChat("你打到了"+str(block))