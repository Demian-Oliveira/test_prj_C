from setuptools import setup

setup(
    # Needed to silence warnings
    name='ProjectC',
    url='https://github.com/dmyanster/test_prj_C',
    author='Dmyan',
    author_email='dmyan@qwerty.com',
    # Needed to actually package something
    packages=['projectc'],

    # # Needed for dependencies
    install_requires=['packageb'],

    # *strongly* suggested for sharing
    version='0.0.2',

    license='private test code',
    description='any description',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.rst').read(),
    # # if there are any scripts
    # scripts=['scripts/hello.py'],
)