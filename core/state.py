
class State(object):

    data: dict
    _observers: []

    def __init__(self,data):
        self.data = data
        self._observers = []

    def __getattr__(self, name):
        return self.data.get(name)

    def __set_self__(self, value):
        self.data = value
        for callback in self._observers:
            callback()
    
    def __get_self__(self):
        return self.data

    def set_state(self, value):
        if type(value) != dict:
            raise TypeError(f'Expected dict got {type(value)}')
        if self.data != value:
            self.data = {**self.data, **value}    
            for callback in self._observers:
                callback()
        
    def bind_to(self, callback):
        if callback:
            self._observers.append(callback)
    
    def __str__(self):
        return f'={self.data}'
