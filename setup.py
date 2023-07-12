from setuptools import setup

setup(name="spake2-cffi",
      version="1.0",
      description="spake2-c python bindings",
      author="Davide TheZero",
      py_modules=["spake2-c"],
      setup_requires=["cffi"],
      cffi_modules=["src/build_spake2.py:ffibuilder"],
      install_requires=["cffi"],
      )
