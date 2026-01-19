import math

class ConstantForcing:
    def __init__(self, c):
        self.c = c

    def __call__(self, t):
        return self.c
    

class SinForcing:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, t):
        return self.a * math.sin(self.b * t)
    

class CosForcing:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, t):
        return self.a * math.cos(self.b * t)
    

class ConstantHeavySideForcing:
    def __init__(self, c, z):
        self.c = c
        self.z = z

    def __call__(self, t):
        if t >= self.z:
            return self.c
        return 0
    

class SinHeavySideForcing:
    def __init__(self, a, b, z):
        self.a = a
        self.b = b
        self.z = z

    def __call__(self, t):
        if t >= self.z:
            return self.a * math.sin(self.b * t)
        return 0


class CosHeavySideForcing:
    def __init__(self, a, b, z):
        self.a = a
        self.b = b
        self.z = z

    def __call__(self, t):
        if t >= self.z:
            return self.a * math.cos(self.b * t)
        return 0