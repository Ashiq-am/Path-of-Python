def validateRatio(self, rect):
    (x, y), (width, height), rect_angle = rect

    if (width > height):
        angle = -rect_angle

    else:
        angle = 90 + rect_angle

    if angle > 15:
        return False

    if (height == 0 or width == 0):
        return False

    area = width * height

    if not self.preRatioCheck(area, width, height):
        return False

    else:
        return True


def preRatioCheck(self, area, width, height):
    min = self.min_area
    max = self.max_area

    ratioMin = 2.5
    ratioMax = 7

    ratio = float(width) / float(height)

    if ratio < 1:
        ratio = 1 / ratio

    if (area < min or area > max) or (ratio < ratioMin or ratio > ratioMax):
        return False

    return True
