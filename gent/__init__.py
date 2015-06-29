__all__ = []

def export(defn):
    # Use this decorator to tag exported functions
    globals()[defn.__name__] = defn
    __all__.append(defn.__name__)
    return defn

from . import slow_chain
from . import fast_chain
