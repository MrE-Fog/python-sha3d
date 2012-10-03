import _sha3
import copy

class _SHA3Base(object):
    """Base class for SHA-3 implementations with different digest sizes.
    """

    def __init__(self, s=None):
        self._s = _sha3.sha3()
        self._s.init(self.digest_size * 8)
        if s is not None:
            self._s.update(s)

    def copy(self):
        """Return a copy of the hash object."""
        c = copy.copy(self)
        c._s = self._s.copy()
        return c

    def update(self, s):
        """Update this hash object's state with the provided string."""
        return self._s.update(s)

    def digest(self):
        """Return the digest value as a string of binary data."""
        return self._s.digest()

    def hexdigest(self):
        """Return the digest value as a string of hexadecimal digits."""
        return self.digest().encode('hex')

    @property
    def digestsize(self):
        return self.digest_size

    @property
    def block_size(self):
        raise NotImplementedError('block size not exposed')


class SHA3224(_SHA3Base):
    digest_size = 28
    name = 'sha3-224'


class SHA3256(_SHA3Base):
    digest_size = 32
    name = 'sha3-256'


class SHA3384(_SHA3Base):
    digest_size = 48
    name = 'sha3-384'


class SHA3512(_SHA3Base):
    digest_size = 64
    name = 'sha3-512'
