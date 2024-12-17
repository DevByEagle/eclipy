class Collection:
    def __init__(self, *args):
        self.data = list(args)

    def __repr__(self):
        return f"Collection({', '.join(map(str, self.data))})"

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __delitem__(self, index):
        del self.data[index]

    def insert(self, index, value):
        self.data.insert(index, value)

    def get(self):
        return self.data.pop()

    def sort(self):
        self.data.sort()
