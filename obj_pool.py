from typing import Any, Generic, Type, TypeVar
from weakref import WeakValueDictionary

_T = TypeVar('_T')


class ObjPool(Generic[_T]):
    def __init__(self, kls: Type[_T]):
        self.kls = kls
        self.pool: WeakValueDictionary[str, _T] = WeakValueDictionary()

    def __call__(self, key, *args: Any, **kwds: Any) -> _T:
        ret = self.pool.get(key)
        if ret is None:
            ret = self.kls(key, *args, **kwds)  # type: ignore
            self.pool[key] = ret
        return ret
