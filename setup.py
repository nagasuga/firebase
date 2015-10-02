from distutils.core import setup
setup(
    name='firebase',
    version='0.1.0',
    packages=['firebase'],
    install_requires=[
        'requests',
        'firebase-token-generator',
    ],
    dependency_links=[],
    description='Python library to use Firebase',
    author='Jeff Nagasuga',
    url='https://github.com/nagasuga/firebase.git',
    keywords=[],
    classifiers=[],
)
