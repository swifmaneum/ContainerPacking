from DataModels.Part import Part


class JutCalculator(object):
    @staticmethod
    def jut(module, part):
        return part.width * part.length - JutCalculator.max_intersect(module, part)

    @staticmethod
    def max_intersect(a, b):
        intersect_no_rotation = JutCalculator.intersect_area(a, b)
        intersect_rotation = JutCalculator.intersect_area(a, Part(b.width, b.length, 1))
        return max(intersect_no_rotation, intersect_rotation)

    @staticmethod
    def intersect_area(a, b):
        # https://stackoverflow.com/a/27162334/5730444
        dx = min(a.length, b.length)
        dy = min(a.width, b.width)
        if (dx >= 0) and (dy >= 0):
            return dx * dy
        else:
            return 0
