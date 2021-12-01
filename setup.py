from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="phylab-jmd",
    version="0.1.0",
    license='MIT',
    author="Joseph Diza",
    author_email="josephm.diza@gmail.com",
    description="Python library and executable for conducting lab reports",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jmdaemon/phylab",
    project_urls={ "Bug Tracker": "https://github.com/jmdaemon/phylab/issues", },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires=">=3.6",
    py_modules=['phylab.util', 'phylab.calc', 'phylab.lab'],
    install_requires=['argparse',],
    entry_points={
        'console_scripts': [
            'phylab = phylab.phylab_cmd:main',
        ],
    },
    test_suite='tests',
)
