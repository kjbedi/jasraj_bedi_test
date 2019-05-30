class Line:
    """
    The Line object contains two points
    """
    def __init__(self, p1, p2):
        """
        This is the constructor of the Line class
        :param p1: p1 is the starting point of the line on the x axis.
        :param p2: p2 is the ending point of the line on the x axis.
        :type p1: int
        :type p2: int
        """
        self.p1 = p1
        self.p2 = p2


class LineUtil:
    """
    This is the LineUtil class. It contains static methods relating to the Line object.
    """
    @staticmethod
    def is_overlap(line1, line2):
        """
        This is a boolean method tells whether line1 and line2 intersect or not.
        :param line1: The first line object.
        :param line2: The second line object.
        :type line1: Line
        :type line2: Line
        """
        if line1.p1 < line2.p1 and line1.p2 <= line2.p1:
            return False
        elif line1.p1 < line2.p1 <= line1.p2:
            return True
        elif line2.p1 <= line1.p1 and line2.p2 <= line1.p1:
            return False
        elif line2.p1 <= line1.p1 <= line2.p2:
            return True


def main():
    """
    This is the first function called by the main program
    """
    line1 = Line(1, 5)
    line2 = Line(5, 8)
    print(LineUtil.is_overlap(line1, line2))


if __name__ == "__main__":
    main()

