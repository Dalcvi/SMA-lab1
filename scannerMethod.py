import numpy as np
from constants import precision


class ScannerMethod:
    def __init__(self, f, plotter):
        self.f = f
        self.plotter = plotter

    def findRoot(self, intervalStart, intervalEnd):
        stepSize = (intervalEnd - intervalStart) / 10
        print("Interval start: {0}; Interval End: {1}".format(intervalStart, intervalEnd))
        return self.scanRecursive(
            intervalStart,
            intervalStart + stepSize,
            1,
            intervalEnd,
            stepSize,
        )

    def scanRecursive(
        self,
        intervalStart,
        intervalEnd,
        step,
        parentIntervalEnd,
        stepSize,
    ):
        currentIntervalStartValue = self.f(intervalStart)
        currentIntervalEndValue = self.f(intervalEnd)

        doesChangeSign = np.sign(currentIntervalStartValue) != np.sign(
            currentIntervalEndValue
        )
        if doesChangeSign:
            currentPrecision = abs(currentIntervalEndValue - currentIntervalStartValue)
            print("step: {0}; x1: {1} x2: {2}; prec: {3}".format(step, intervalStart, intervalEnd, currentPrecision))
            if currentPrecision < precision:
                return [intervalStart, intervalEnd]

            innerIntervalStart = intervalStart
            innerStepSize = (intervalEnd - intervalStart) / 10
            innerIntervalEnd = innerIntervalStart + innerStepSize
            return self.scanRecursive(
                innerIntervalStart,
                innerIntervalEnd,
                step + 1,
                intervalEnd,
                innerStepSize,
            )

        if intervalEnd > parentIntervalEnd:
            return []

        return self.scanRecursive(
            intervalEnd,
            intervalEnd + stepSize,
            step,
            parentIntervalEnd,
            stepSize,
        )

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
