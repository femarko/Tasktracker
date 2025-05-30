from typing import Any, Protocol, TypeVar, Unpack


T = TypeVar("T")


class RepoProto(Protocol[T]):
    """
    This class defines interface of a repository.

    Concrete implementations of this class are supposed to encapsulate
    operations with database or other data storage.
    """
    async def add(self, instance: T) -> None: ...
    async def get(self, instance_id: int) -> T | None: ...


