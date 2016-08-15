

class Kifu:
    
    def __init__(self):
        self.kifu = []
    
    def add(self, from_x, from_y, to_x, to_y, promote, koma):
        self.kifu.append((from_x, from_y, to_x, to_y, promote, koma))

    def pop(self):
        return self.kifu.pop()

