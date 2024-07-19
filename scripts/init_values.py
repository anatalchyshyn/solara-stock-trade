import dataclasses
from typing import Callable

@dataclasses.dataclass(frozen=False)
class RuleItem:
    indicator: str
    start: int
    finish: int
    value: int

init_rules_custom = [
    RuleItem("RSI_14", 0, 0, 0),
    RuleItem("ADX_14", 0, 0, 0),
    RuleItem("52_weeks", 0, 0, 0),
]

init_rules_default = [
    RuleItem("RSI_14", 0, 50, 1),
    RuleItem("RSI_14", 50, 60, 4),
    RuleItem("RSI_14", 60, 70, 5),
    RuleItem("RSI_14", 70, 80, 4),
    RuleItem("RSI_14", 80, 100, 3),
    
    RuleItem("ADX_14", 0, 20, 1),
    RuleItem("ADX_14", 20, 30, 2),
    RuleItem("ADX_14", 30, 40, 5),
    RuleItem("ADX_14", 40, 70, 4),
    
    RuleItem("52_weeks", 0, 30, 1),
    RuleItem("52_weeks", 30, 50, 3),
    RuleItem("52_weeks", 50, 80, 5),
    RuleItem("52_weeks", 80, 90, 4),
    RuleItem("52_weeks", 90, 101, 2),
]

init_weights_custom = {
    "RSI_14": 0,
    "ADX_14": 0,
    "52_weeks": 0,
}

init_weights_default = {
    "RSI_14": 6,
    "ADX_14": 5,
    "52_weeks": 1,
}