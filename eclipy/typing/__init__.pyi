from typing import Any

class Collection:
    def __init__(self, *args: Any) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self, index: int) -> Any: ...
    def __setitem__(self, index: int, value: Any) -> None: ...
    def __delitem__(self, index: int) -> None: ...
    
    def insert(self, value: Any) -> None: ...
    def remove(self, value: Any) -> None: ...
    def get(self) -> Any: ...
    def sort(self) -> None: ...
