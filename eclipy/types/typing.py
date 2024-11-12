class Collection:
    def __init__(self):
        self._items = []
        self._is_sorted = False

    def __len__(self):
        return len(self._items)

    def __iter__(self): 
        return iter(self._items)

    def __repr__(self):
        return f"Collection({self._items})"

    def __getitem__(self, index):
        return self._items[index]

    def append(self, item = ..., /):
        self._items.append(item)

    def clear(self):
        self._items.clear()
        self._is_sorted = True
    
    def sort(self, reverse=False):
        self._items.sort(reverse=reverse)
        self._is_sorted = True

    @property
    def sorted(self):
        return self._is_sorted
