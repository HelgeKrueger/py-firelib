from setuptools import Extension, find_packages, setup
from setuptools.command.build_py import build_py


class BuildPy(build_py):
    def run(self):
        self.run_command("build_ext")
        super(build_py, self).run()


setup(
    name="pyfirelib",
    version="0.1",
    author="Helge Krueger",
    author_email="helge.krueger@gmail.com",
    description="Wrapper around firelib",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/helge.krueger/firelib",
    cmdclass={
        "build_py": BuildPy,
    },
    packages=find_packages("src"),
    package_dir={"": "src"},
    package_data={"": ["*.pyd"]},
    ext_modules=[
        Extension(
            "_firelib",
            ["src/fireLib.i", "src/fireLib.c"],
            include_dirs=["src"],
            swig_opts=["-I src"],
        ),
        Extension(
            name="firelib",
            sources=["src/fireLib.i", "src/fireLib.c"],
        ),
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
