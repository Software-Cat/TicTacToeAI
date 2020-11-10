import abc
from typing import List, Tuple, Optional
import main


class AIBase(abc.ABC):
    @abc.abstractmethod
    def __init__(self) -> None:
        self.matrix: List[List[main.Game.State]]

    @abc.abstractmethod
    def __turn__(self) -> Optional[Tuple[int, int]]:
        pass
