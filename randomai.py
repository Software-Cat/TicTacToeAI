import aibase
import random


class AI(aibase.AIBase):
    def __init__(self) -> None:
        super().__init__()
        return None

    def __turn__(self):
        super().__init__()
        return (random.randint(0, 2), random.randint(0, 2))
