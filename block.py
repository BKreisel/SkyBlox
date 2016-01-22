class block:
    def __init__(self, shape = [], orientation = 0):
        print("New Block Created")
        self.shape = shape
        self.orientation = orientation

    def rotate(self, dir):
        self.orientation = (self.orientation + dir) % len(self.shape)

    def get_pic(self):
        return self.shape[self.orientation]
