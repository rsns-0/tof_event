from setuptools import setup, find_packages

setup(
    name='tof_event',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'pathlib',
        'pyautogui',
        'retry',
    ],
)