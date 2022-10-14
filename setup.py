from distutils.core import setup, Extension
from setuptools import find_packages

setup(
    name="pyfirelib",
    version="0.1",
    author="Helge Krueger",
    author_email="helge.krueger@gmail.com",
    description="Wrapper around firelib",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/helge.krueger/firelib",
    ext_modules=[
        Extension(
            "firelib",
            ["src/fireLib.i", "src/fireLib.c"],
            include_dirs=["src"],
            swig_opts=["-modern", "-I../include"],
        ),
    ],
    packages=find_packages('src'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
