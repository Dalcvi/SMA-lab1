import numpy as np
from constants import precision


class SecantMethod:
    def __init__(self, f, plotter):
        self.f = f
        self.plotter = plotter

    def findRoot(self, intervalStart, intervalEnd):
        firstPoint = intervalEnd
        secondPoint = np.float16(intervalEnd - ((intervalEnd - intervalStart) / 20))
        print("First point: {0}; Second point: {1}".format(firstPoint, secondPoint))
        points = [firstPoint, secondPoint]
        currentPrecision = intervalEnd - intervalStart
        currentPoint = 1
        while precision < currentPrecision:
            nextPoint = points[currentPoint] - (
                (
                    (points[currentPoint] - points[currentPoint - 1])
                    / (
                        np.float128(self.f(points[currentPoint]))
                        - np.float128(self.f(points[currentPoint - 1]))
                    )
                )
            ) * self.f(points[currentPoint])
            points.append(nextPoint)
            currentPrecision = abs(nextPoint - points[currentPoint])
            print("step: {0}; next point: {1}; prec: {2}".format(currentPoint, nextPoint, currentPrecision))
            currentPoint += 1

        return points[currentPoint]
    
    def plot(self, subplot, root, f, color, marker, markerSize):
        self.plotter.plotMarker(
            subplot, root, f(root), color, marker, markerSize
        )

    def plotInterval(self, root):
        intervalHalfSize = np.power(10, np.float16(-10))
        return [root - intervalHalfSize, root + intervalHalfSize]
    
    def plotTitle(self, subplot, root):
        self.plotter.setSubplotTitle(subplot, ("{root}".format(root=root)))
