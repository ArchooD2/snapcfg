from setuptools import setup, find_packages

setup(
    name='snapcfg',
    version='0.1.1',
    packages=find_packages(),
    description='Validate configs against a flexible app-defined schema.',
    author='PJ Hayes',
    author_email='archood2next@gmail.com',
    license='MPL-2.0',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)'
    ],
    python_requires='>=3.6',
    install_requires=[
        'pyyaml',
        'typer',
        'rich',
        'snaparg'
    ],
    entry_points={
    'console_scripts': [
        'snapcfg = snapcfg.__main__:main',
        ],
    },

)
