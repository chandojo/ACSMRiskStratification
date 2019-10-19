from setuptools import setup, find_packages

setup(
    name='ACSMRiskStratification',
    version='0.1',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    python_requires='>=3.7, <4',
    url='',
    license='MIT License',
    author='chandojo',
    author_email='',
    description='Stratifies risk of cardiovascular disease based on American College of Sports Medicine',
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
