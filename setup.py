# coding=utf8
#launch from cmd: python setup.py build
     
from cx_Freeze import setup, Executable

target = Executable(
    script="removebg.py",
    base="Win32GUI",
    icon="logo.ico"
    )

setup(
    name="RemoveBG",
    version="0.1",
    description="RemoveBG - Remove image background software",
    author="Xosé Brais Noya García",
    executables=[target]
    )