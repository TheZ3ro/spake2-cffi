# SPAKE2 for Python
Python3 FFI wrapper for [spake2-c](https://github.com/MuntashirAkon/spake2-c) by @[MuntashirAkon](https://github.com/MuntashirAkon)

<!-- begin-short -->

[SPAKE2](https://www.ietf.org/id/draft-irtf-cfrg-spake2-26.html) is a a Password Authenticated Key Exchange (PAKE) protocol run between two parties for deriving a strong shared key with no risk of disclosing the password.
*spake2-cffi* is the simplest way to use it in Python and PyPy:

> **Note**
> Currently the spake2-c package support only `SPAKE2-edwards25519-SHA512-HKDF-HMA` / spake25519 as implemented by Google's boringssl library.


```pycon
>>> from spake2 import Spake2
>>> alice = Spake2_Alice(b'alice name', b'bob name')
>>> message = alice.generate_message(b'password')
... # exchange messages with bob
>>> shared_key = alice.process_msg(bob_message)
>>> print(shared_key)
b'5c12af40e2bf2e30ac637652cdfc4f6367ed82542ec7640906532a1cd3e71e6bd74f76432d9ce3eb8d50c8c016fa88b3434fe84b878d1f67c01fa9f9d01db63c'
```
<!-- end-short -->

## Project Information

- [**PyPI**](https://pypi.org/project/spake2-cffi/)
- [**Source Code**](https://github.com/TheZ3ro/spake2-cffi)

### Credits

*spake2-cffi* is maintained by [TheZero](https://thezero.org/).
