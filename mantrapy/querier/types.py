from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


@dataclass
class QueryResponse(Generic[T]):
    """
    Generic response wrapper with error handling
    """

    data: Optional[T] = None
    error: Optional[str] = None
    status_code: Optional[int] = None

    def is_success(self) -> bool:
        return self.error is None and self.status_code in {200, 201, 202}
