# coding=utf8
#launch from cmd: python setup.py build
     
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["torch", "scipy.optimize", "scipy.integrate","os","numpy", "cv2", "tensorflow", "matplotlib","imageio"]}

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
    options={"build_exe": build_exe_options},
    executables=[target]
    )