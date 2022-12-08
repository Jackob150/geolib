from setuptools import setup, find_packages

setup(
    name='geolib',
    version='0.0.1',
    description='Analytical geometry library',
    author='Jackob150',
    author_email='jackob150@gmail.com',
    packages=find_packages(include=['src', 'src.*', 'utils', 'utils.*', 'examples', 'examples.*']),
    entry_points={
        'console_scripts': ['geolib_example=examples.perp_tangent:run_example']
    },
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)