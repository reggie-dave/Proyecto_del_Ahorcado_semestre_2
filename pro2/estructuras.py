class Pila:
    def __init__(self):
        self.items = []
    def apilar(self, item):
        self.items.append(item)
    def desapilar(self):
        return self.items.pop() if not self.esta_vacia() else None
    def esta_vacia(self):
        return len(self.items) == 0

class Cola:
    def __init__(self):
        self.items = []
    def encolar(self, item):
        self.items.append(item)
    def desencolar(self):
        return self.items.pop(0) if not self.esta_vacia() else None
    def esta_vacia(self):
        return len(self.items) == 0
