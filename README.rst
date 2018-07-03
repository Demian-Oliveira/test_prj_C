===================
Header 1
===================

**Header 2**

- create a virtual environment
    python3 -m venv ~/PycharmProjects/envs/ProjectC
    source activate ProjectC

- install the chosen tag version (thru the PyCharm Terminal)
    pip install -e git://github.com/dmyanster/test_pkg_A.git@v0.0.4#egg=PackageA.egg-info

- test
    cd bin
    ./set-PackageA-version 0.0.4
    ./set-PackageB-version 0.0.1
    ./run
