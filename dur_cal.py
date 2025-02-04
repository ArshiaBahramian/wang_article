class DurCal:
    def __init__(self, wd, h, i):
        self.i = i
        self.wd = wd
        self.h = h

    def computee(self):
        v = {
            1: 1.9,
            2: 10.0,
            3: 2.3,
            4: 3.0,
            5: 7.5,
            6: 2.7,
            7: 12.6,
            8: 3.2,
            9: 5.6,
            10: 12.4,
            11: 11.1,
            12: 2.8,
            13: 5.1,
            14: 11.0,
            15: 11.2,
            16: 2.2,
            17: 4.5,
            18: 10.0,
            19: 6.4,
            20: 3.6
        }
        PP = (
        (5, 8, 1), (5, 9, 0.9), (5, 10, 0.85), (5, 11, 0.65), (5, 12, 0.6), (6, 8, 0.9), (6, 9, 0.85), (6, 10, 0.8),
        (6, 11, 0.65), (6, 12, 0.6), (7, 8, 0.75), (7, 9, 0.7), (7, 10, 0.65), (7, 11, 0.6), (7, 12, 0.55))
        for tup in PP:
            if tup[0] == self.wd and tup[1] == self.h:
             E = tup[2]
        if not E:
            raise ValueError("مقدار مورد نظر برای E پیدا نشد.")

        D = v[self.i+1]/((self.h/8)*E)
        return D , E

# NB = DurCal(5,9,2)
# ZX = print(NB.computee())