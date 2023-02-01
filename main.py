class Array:
    def __init__(self, capacity):
        self.arr = []
        self.len = 0

        if capacity < 0:
            raise "Enta khawal"
        self.capacity = capacity
        
