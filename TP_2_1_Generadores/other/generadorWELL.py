import numpy as np

class WellGenerator:
    def __init__(self, seed):
        self.index = 0
        self.state = [0]*624
        self.state[0] = seed & 0xFFFFFFFF
        for i in range(1, 624):
            self.state[i] = ((1812433253 * (self.state[i-1] ^ (self.state[i-1] >> 30)) + i) & 0xFFFFFFFF)
        
    def random(self):
        y = 0
        mag01 = [0, 0x9908B0DF]
        if self.index == 0:
            self.twist()
        y = self.state[self.index]
        self.index = (self.index + 1) % 624
        y ^= (y >> 11)
        y ^= ((y << 7) & 0x9D2C5680)
        y ^= ((y << 15) & 0xEFC60000)
        y ^= (y >> 18)
        return (float(y) / 0xFFFFFFFF)

    def twist(self):
        for i in range(624):
            tmp = ((self.state[i] & 0x80000000) + (self.state[(i+1)%624] & 0x7FFFFFFF))
            self.state[i] = (self.state[(i+397)%624] ^ (tmp >> 1))
            if (tmp % 2) != 0:
                self.state[i] ^= 0x9908B0DF
        self.index = 0
    

