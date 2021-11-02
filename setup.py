from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pylab-jmd",
    version="0.1.0",
    author="Joseph Diza",
    author_email="josephm.diza@gmail.com",
    description="Python library and executable for conducting lab reports",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jmdaemon/pylab",
    project_urls={
        "Bug Tracker": "https://github.com/jmdaemon/sap/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
    py_modules=['util', 'calc'],
    install_requires=[
        'argparse',
    ],
    entry_points={
        'console_scripts': [
            'pylab = pylab_cmd:main',
        ],
    },
    # setup_requires=['pytest-runner'],
    # tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
