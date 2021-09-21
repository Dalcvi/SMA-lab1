import numpy as np
from constants import precision

class ChordMethod:
    def __init__(self, f, plotter):
        self.f = f
        self.plotter = plotter

    def findRoot(self, intervalStart, intervalEnd):
        currentPrecision = intervalEnd - intervalStart
        xLeftPoint = intervalStart
        xRightPoint = intervalEnd
        print("Interval start: {0}; Interval End: {1}".format(xLeftPoint, xRightPoint))
        step = 1
        while precision < currentPrecision:
            yLeftPoint = self.f(xLeftPoint)
            yRightPoint = self.f(xRightPoint)
            if(yLeftPoint == 0):
                print("step: {0}; xLeft: {1}; xRight: {2}; prec: {3}".format(step, xLeftPoint - np.power(10, np.float128(-15)), xLeftPoint + np.power(10, np.float128(-15)), np.power(10, np.float128(-15))*2))
                return [xLeftPoint - np.power(10, np.float128(-15)), xLeftPoint + np.power(10, np.float128(-15))]
            if(yRightPoint == 0):
                print("step: {0}; xLeft: {1}; xRight: {2}; prec: {3}".format(step, xRightPoint - np.power(10, np.float128(-15)), xRightPoint + np.power(10, np.float128(-15)), np.power(10, np.float128(-15))*2))
                return [xRightPoint - np.power(10, np.float128(-15)), xRightPoint + np.power(10, np.float128(-15))]
            yList = [yLeftPoint, yRightPoint]
            k = abs(np.float128(yList[0]) / np.float128(yList[1]))
            newInterval = self.calculateNewInterval([xLeftPoint, xRightPoint], k)

            xRightPoint = newInterval[1]
            xLeftPoint = newInterval[0]
            currentPrecision = xRightPoint - xLeftPoint
            print("step: {0}; xLeft: {1}; xRight: {2}; prec: {3}".format(step, xLeftPoint, xRightPoint, currentPrecision))
            step += 1
        return [xLeftPoint, xRightPoint]
    
    def calculateNewInterval(self, interval, k):
        xLeftPoint = interval[0]
        xRightPoint = interval[1]
        xMiddlePoint = np.float128((xLeftPoint + (k * xRightPoint))) / np.float128((1 + k))
        if np.sign(self.f(xLeftPoint)) != np.sign(self.f(xMiddlePoint)):
            xRightPoint = xMiddlePoint
        else:
            xLeftPoint = xMiddlePoint
        return [xLeftPoint, xRightPoint]
    
    def plot(self, subplot, interval, f, color, marker, markerSize):
        self.plotter.plotMarker(
            subplot, interval[0], f(interval[0]), color, marker, markerSize
        )
        self.plotter.plotMarker(
            subplot, interval[1], f(interval[1]), color, marker, markerSize
        )

    def plotInterval(self, interval):
        intervalDiff = interval[1] - interval[0]
        return [interval[0] - intervalDiff, interval[1] + intervalDiff]
    
    def plotTitle(self, subplot, interval):
        self.plotter.setSubplotTitle(subplot, ("[{start}] - [{end}]".format(start=interval[0], end=interval[1])))
