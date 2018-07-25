import random
import hashlib
from contextlib import contextmanager

def _set_seed(string):
    '''
    Set random seed based on MD5 hash of the string.

    On its own, this is destructive - use the context manager instead.
    '''
    digest = hashlib.sha256(string.encode('utf-8')).hexdigest()
    random.seed( int(digest,16) )

@contextmanager
def from_string(string):
    '''
    Generate consistent random numbers across multiple Python versions.

    Importantly, the original RNG state is restored afterward.

    >>> with seed.from_string('foo'):
    ...     print random.random()
    ...
    0.17073279722327472
    '''
    original_state = random.getstate()
    try:
        yield _set_seed(string)
    finally:
        random.setstate(original_state)
