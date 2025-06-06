class Solution:
    def __init__(self):
        self._list = []
        self._dict = {}

    def insert(self, val: int) -> bool:
        if val in self._dict:
            return False

        self._list.append(val)
        self._dict[val] = len(self._list) - 1

        return True

    def remove(self, val: int) -> bool:
        if not val in self._dict:
            return False

        pos = self._dict[val]
        val_last = self._list[-1]

        self._list[pos] = val_last
        self._dict[val_last] = pos

        self._list.pop()
        del self._dict[val]

        return True

    def get_random(self) -> int:
        return random.choice(self._list)
