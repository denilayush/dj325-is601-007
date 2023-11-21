class DictToObject:
    #dj325 19/11/23
    def __init__(self, dictionary):
        for key in dictionary:
            setattr(self, key, dictionary[key])