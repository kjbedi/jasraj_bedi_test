class Version:
    """
    The Vehicle object contains lots of vehicles.
    """
    def __init__(self, ver_num):
        """
        This is the constructor of the Line class.
        :param ver_num: The ver_num contains the version number.
        :type ver_num: str
        """
        self.ver_num = ver_num


class VersionUtil:
    @staticmethod
    def compare(v1, v2):
        """
        Checks which version string is greater.

        :param v1: Version object 1
        :param v2: Version object 2
        :returns: Returns 1 if version string in v1 is greater than the version string in v2;
        returns -1 if version string of v2 is greater than the version string of v1. Returns 0 if the version
        string of both v1 and v2 are equal.
        """
        ver1 = v1.ver_num.split(".")
        ver2 = v2.ver_num.split(".")
        counter = 0
        while counter < len(ver1):
            if int(ver1[counter]) > int(ver2[counter]):
                return 1
            if int(ver2[counter]) > int(ver1[counter]):
                return -1
            counter += 1
        return 0


def main():
    """
    This is the first function called by the main program
    """
    version1 = Version("1.0.5")
    version2 = Version("1.0.4")
    print(VersionUtil.compare(version1, version2))


if __name__ == "__main__":
    main()




