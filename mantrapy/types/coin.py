from dataclasses import dataclass
from typing import List


@dataclass
class Coin:
    denom: str
    amount: str


class Coins(List[Coin]):

    def __init__(self, *args):
        super().__init__(*args)
