import pkg_resources
from packageb.package_B import PackageB


class ProjectC(PackageB):
    def __init__(self):
        pass

    def print_version(self):
        super().print_version()
        version = pkg_resources.require("projectc")[0].version
        print('Project_C: {}'.format(version))
