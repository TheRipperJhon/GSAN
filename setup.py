import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='gsan',
    version='3.0.3',
    author='Franccesco Orozco',
    author_email='franccesco@codingdose.info',
    description='Extract subdomains from HTTPS sites',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://franccesco.github.io/getaltname/',
    packages=setuptools.find_packages(),
    install_requires=[
        'colorama',
        'pyperclip',
        'termcolor',
        'tldextract',
        'tqdm',
        'pyopenssl',
        'pyasn1',
        'ndg-httpsclient',
    ],
    entry_points={
        'console_scripts': [
            'gsan = gsan.__main__:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
        ],
    )
