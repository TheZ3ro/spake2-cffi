import os
import sys

from setuptools import setup

base_dir = os.path.dirname(__file__)
src_dir = os.path.join(base_dir, "src")

# When executing the setup.py, we need to be able to import ourselves, this
# means that we need to add the src/ directory to the sys.path.
sys.path.insert(0, src_dir)

setup(name="spake2-cffi",
      py_modules=["spake2-c"],
      cffi_modules=["src/spake2/build_spake2.py:ffibuilder"],
      setup_requires=["cffi>=1.0.0"],
      install_requires=["cffi>=1.0.0"],
      )
