from abc import ABC, abstractmethod
from pathlib import Path

LOCAL_STORAGE_BACKEND = "local"

class StorageBackend(ABC):
    
    @abstractmethod
    async def save(self, file_path: str, content: bytes) -> str: ...

    @abstractmethod
    async def get(self, file_path: str) -> bytes: ...

    @abstractmethod
    async def delete(self, file_path: str) -> None: ...


class LocalStorage(StorageBackend):
    def __init__(self, base_dir: Path):
        self.base_dir = base_dir

    async def save(self, file_path: str, content: bytes) -> str:
        full_path = self.base_dir / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        full_path.write_bytes(content)
        return str(full_path)
    
    async def get(self, file_path) -> bytes:
        full_path = self.base_dir / file_path
        return full_path.read_bytes()
    
    async def delete(self, file_path: str) -> None:
        full_path = self.base_dir / file_path
        full_path.unlink(missing_ok=True)



def get_storage(storage_backend: str, base_dir: Path) -> StorageBackend:
    if storage_backend == LOCAL_STORAGE_BACKEND:
        return LocalStorage(base_dir=base_dir)
    raise ValueError("Storage system not supported yet")