

class Object(dict):

    def __getattr__(self, name):
        return self.get(name)


    