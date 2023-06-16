#from ..TP_2_2_GeneradorDistribuido.Metodo_Transformada import ExponencialT as Exponential
from matplotlib import pyplot as plt
from numpy import random


class MM1:
    def __init__(self, lambda1: float, lambda2: float, max_q: int) -> None:
        """lambda1: Parameter for exponential dist of arrival times
        lambda2: Parameter for exponential dist of service times"""
        self.qlim = max_q
        # self.arrivalTimes = Exponential(random.random(10000), lambda1)
        # self.serveTimes = Exponential(random.random(10000), lambda2)
        self.arrivalTimes = list(random.exponential(lambda1, 10000))
        self.serveTimes = list(random.exponential(lambda2, 10000))
        self.events = []
        self.eventTimes = []
        self.time = 0
        self.inQueue = 0
        self.served = 0
        self.rejected = 0
        self.inQat = []
        self.serverIsFree = True

    def Simulate(self, maxTime: int):
        # First arrival
        self.time = self.arrivalTimes.pop(0)
        self.events.append("arrival")
        self.eventTimes.append(self.time)
        self.serverIsFree = False  # direct to server
        # self.inQueue += 1 #given user went direct to server, queue didnt increase
        self.inQat.append((self.inQueue, self.time))

        while(self.time < maxTime and len(self.arrivalTimes) > 0 and len(self.serveTimes) > 0):
            if(self.serveTimes[0] < self.arrivalTimes[0] and not self.serverIsFree):
                self.arrivalTimes[0] -= self.serveTimes[0]
                self.time += self.serveTimes.pop(0)
                self.eventTimes.append(self.time)
                self.events.append("departure")
                self.serverIsFree = True  # user exits server
                self.served += 1
                if self.inQueue > 0:  # at least one user in queue
                    self.inQueue -= 1  # user get server
                    self.serverIsFree = False
            else:
                self.serveTimes[0] -= self.arrivalTimes[0]
                self.time += self.arrivalTimes.pop(0)
                self.eventTimes.append(self.time)
                if(self.inQueue == self.qlim):
                    self.events.append("reject")
                    self.rejected += 1
                    continue
                else:
                    self.events.append("arrival")
                    if self.inQueue > 0:  # at least one user in queue
                        self.inQueue += 1  # new user gets into queue
                    else:  # no users in queue
                        self.serverIsFree = False  # new user gets direct to server
            self.inQat.append((self.inQueue, self.time))


m = MM1(5, 6, 5)
m.Simulate(200)
print(m.events)
print(m.inQat)
print(f"{m.rejected=}, {m.served=}")
