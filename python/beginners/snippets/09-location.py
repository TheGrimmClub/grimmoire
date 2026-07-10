def location(self):
    return "im Verlies" if self._in_dungeon else "vor dem Verlies"


def __str__(self):
    return f"🧍 {self._name} wartet {self.location()}."
