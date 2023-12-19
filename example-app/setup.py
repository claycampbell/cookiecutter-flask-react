import versioneer
from setuptools import setup, find_packages

setup(
    name='example-app',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Example App is a Flask+React web app',
    author='',
    packages=find_packages(),
    include_package_data=True,
    license='MIT'
)
