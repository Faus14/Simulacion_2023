import numpy as np

class glc:
    
    def __init__(self, a, c, m, seed):
        self.a = a
        self.c = c
        self.m = m
        self.seed = seed
    
    def random(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed / self.m
    


