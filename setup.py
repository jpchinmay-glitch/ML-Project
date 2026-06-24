from setuptools import find_packages, setup

def get_requirements(path):
    with open(path) as f:
        requirements = f.readlines()
    requirements = [req.replace("\n", "") for req in requirements]
    if "-e ." in requirements:
        requirements.remove("-e .")
    return requirements

setup(
    name='MLproject',
    version='0.0.1',
    author='chinmay',
    author_email='jpchinmay@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)