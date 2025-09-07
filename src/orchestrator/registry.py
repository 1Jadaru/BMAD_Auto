from collections import OrderedDict
from typing import Callable, Iterable, Tuple


class StepRegistry:
    """Registry for mapping step names to callables."""

    def __init__(self) -> None:
        self._steps: "OrderedDict[str, Callable[[], None]]" = OrderedDict()

    def register(self, name: str, func: Callable[[], None]) -> None:
        """Register a new step."""
        self._steps[name] = func

    def get(self, name: str) -> Callable[[], None]:
        return self._steps[name]

    def steps(self) -> Iterable[Tuple[str, Callable[[], None]]]:
        """Return an iterable of registered steps in order."""
        return self._steps.items()
