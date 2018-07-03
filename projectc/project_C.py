from packageb.package_B import PackageB


class ProjectC(PackageB):
    def __init__(self):
        pass

    def print_version(self):
        super().print_version()
        print('=== Project C ===')
