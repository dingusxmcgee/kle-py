import copy
import json
from decimal import Decimal
from typing import (
    Union,
    List,
    Dict,
)


class Key:
    """A KLE Key"""

    def __init__(
        self,
        color: str = "#cccccc",
        labels: List[Union[str]] = None,
        text_color: List[Union[str, None]] = None,
        text_size: List[Union[int, float, None]] = None,
        default_text_color: str = "#000000",
        default_text_size: Union[int, float] = 3,
        x: Decimal = Decimal(0.0),
        y: Decimal = Decimal(0.0),
        width: Decimal = Decimal(1.0),
        height: Decimal = Decimal(1.0),
        x2: Decimal = Decimal(0.0),
        y2: Decimal = Decimal(0.0),
        width2: Decimal = Decimal(1.0),
        height2: Decimal = Decimal(1.0),
        rotation_x: Decimal = Decimal(0.0),
        rotation_y: Decimal = Decimal(0.0),
        rotation_angle: Decimal = Decimal(0.0),
        decal: bool = False,
        ghost: bool = False,
        stepped: bool = False,
        nub: bool = False,
        profile: str = "",
        sm: str = "",
        sb: str = "",
        st: str = ""
    ):
        self.color = color
        self.labels = ["" for i in range(12)]
        if labels is not None:
            self.labels = labels
        self.default_text_color = default_text_color
        self.text_color = ["" for i in range(12)]
        if text_color is not None:
            self.text_color = text_color
        self.default_text_size = default_text_size
        self.text_size = [None for i in range(12)]
        if text_size is not None:
            self.text_size = text_size
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x2 = x2
        self.y2 = y2
        self.width2 = width2
        self.height2 = height2
        self.rotation_x = rotation_x
        self.rotation_y = rotation_y
        self.rotation_angle = rotation_angle
        self.decal = decal
        self.ghost = ghost
        self.stepped = stepped
        self.nub = nub
        self.profile = profile
        self.sm = sm
        self.sb = sb
        self.st = st

    def __deepcopy__(self, memo: dict = None) -> "Key":
        """Creates a deep copy of the key.

        :return: A duplicate of the key.
        :rtype: Key
        """
        new_key = type(self)()
        memo[id(self)] = new_key
        new_key.__dict__.update(self.__dict__)
        new_key.labels = copy.deepcopy(self.labels, memo)
        new_key.text_color = copy.deepcopy(self.text_color, memo)
        new_key.text_size = copy.deepcopy(self.text_size, memo)
        return new_key

    def __str__(self) -> str:
        d = dict()
        d["x"] = float(self.x)
        d["y"] = float(self.y)
        d["x2"] = float(self.x2)
        d["y2"] = float(self.y2)
        d["width"] = float(self.width)
        d["height"] = float(self.height)
        d["width2"] = float(self.width2)
        d["height2"] = float(self.height2)
        d["rotation_angle"] = float(self.rotation_angle)
        d["rotation_x"] = float(self.rotation_x)
        d["rotation_y"] = float(self.rotation_y)
        d["labels"] = self.labels
        d["text_color"] = self.text_color
        d["text_size"] = self.text_size
        d["color"] = self.color
        d["profile"] = self.profile
        d["nub"] = self.nub
        d["ghost"] = self.ghost
        d["stepped"] = self.stepped
        d["decal"] = self.decal
        d["sm"] = self.sm
        d["sb"] = self.sb
        d["st"] = self.st
        return json.dumps(d, indent=4)
