class Collide():
    def __init__ (self):
        self.offset_x = 0
        self.offset_y = 0
    
    def collide(self,obj1,obj2):
        self.offset_x = obj2.x - obj1.x
        self.offset_y = obj2.y - obj1.y
        return obj1.mask.overlap(obj2.mask, (self.offset_x, self.offset_y)) != None
        
        
        