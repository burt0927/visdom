import os
from setuptools import setup
from pkg_resources import get_distribution, DistributionNotFound


def get_dist(pkgname):
    try:
        return get_distribution(pkgname)
    except DistributionNotFound:
        return None


here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'py/visdom/VERSION')) as version_file:
    version = version_file.read().strip()

readme = open('README.md').read()

requirements = [
    'numpy>=1.8',
    'scipy',
    'requests',
    'tornado',
    'pyzmq',
    'six',
    'torchfile',
    'websocket-client',
]
pillow_req = 'pillow-simd' if get_dist('pillow-simd') is not None else 'pillow'
requirements.append(pillow_req)

setup(
    # Metadata
    name='visdom',
    version=version,
    author='Allan Jabri, Jack Urbanek, Laurens van der Maaten',
    author_email='jju@fb.com',
    url='https://github.com/facebookresearch/visdom',
    description='A tool for visualizing live, rich data for Torch and Numpy',
    long_description=readme,
    license='CC-BY-NC-4.0',

    # Package info
    packages=['visdom'],
    package_dir={'': 'py'},
    package_data={'visdom': ['static/*.*', 'static/**/*']},
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
)
