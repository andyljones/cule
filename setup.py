from setuptools import find_packages, setup, Extension
from pathlib import Path

setup(name='torchcule',
      version='0.1.0',
      description='A GPU RL environment package for PyTorch',
      url='https://github.com/andyljones/cule',
      author='Andy Jones',
      author_email='andyjones.ed@gmail.com',
      # Exclude the build files.
      packages=find_packages(exclude=['build', 'pkg']),
      package_data={'': list(Path('.').glob('*.so'))})

