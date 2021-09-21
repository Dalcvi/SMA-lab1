import numpy as np
from plotter import Plotter
from variables import method, title, function, functionNumber

if(functionNumber == 1):
    n = 4
    plotter = Plotter(5)
elif(functionNumber == 2):
    n = 3
    plotter = Plotter(4)
elif(functionNumber == 3):
    n = 1
    plotter = Plotter(2)

def findInitialRootsIntervals(f, rootsAmount, start, end):
    stepsAmount = 150
    foundRoots = 0
    rootsIntervals = []
    stepSize = np.float16(end - start) / stepsAmount
    currentStep = 0
    while currentStep < stepsAmount and foundRoots != rootsAmount:
        currentIntervalStart = start + np.multiply(stepSize, currentStep)
        currentIntervalEnd = currentIntervalStart + stepSize

        currentIntervalStartValue = f(currentIntervalStart)
        currentIntervalEndValue = f(currentIntervalEnd)
        if np.sign(currentIntervalStartValue) != np.sign(currentIntervalEndValue):
            rootsIntervals.append([currentIntervalStart, currentIntervalEnd])

            foundRoots += 1
        currentStep += 1
    return rootsIntervals


def functionXYPoints(f, intervalStart, intervalEnd, pointsAmount):
    stepSize = np.float128((intervalEnd - intervalStart)) / pointsAmount
    xPoints = []
    yPoints = []
    for i in range(0, pointsAmount):
        x = intervalStart + stepSize * i
        y = f(x)
        xPoints.append(x)
        yPoints.append(y)
    return [xPoints, yPoints]

plotter.setTitle(title)
rootFinder = method(function, plotter)

if(functionNumber == 1):
    initialInterval = [-1, 23.67]
elif(functionNumber == 2):
    initialInterval = [-10, 10]
elif(functionNumber == 3):
    initialInterval = [0, 10]

initialRootsIntervals = findInitialRootsIntervals(
    function, n, initialInterval[0], initialInterval[1]
)
print(initialRootsIntervals)
roots = []
for bigInterval in initialRootsIntervals:
    roots.append(rootFinder.findRoot(bigInterval[0], bigInterval[1]))

if(functionNumber == 3):
    mainPolynomialFunctionXYPoints = functionXYPoints(
    function,
    0,
    10,
    100,
)
else:
    mainPolynomialFunctionXYPoints = functionXYPoints(
        function,
        initialRootsIntervals[0][0] - 0.25,
        initialRootsIntervals[n - 1][1] + 0.25,
        100,
    )
plotter.plotLine(
    0, mainPolynomialFunctionXYPoints[0], mainPolynomialFunctionXYPoints[1]
)
plotter.enableGrid(0)

subplot = 1

for interval in initialRootsIntervals:
    plotter.plotMarker(
        0, interval[0], function(interval[0]), "Red", "o", 8
    )
    plotter.plotMarker(
        0, interval[1], function(interval[1]), "Red", "o", 8
    )

for foundRoot in roots:
    rootFinder.plotTitle(subplot, foundRoot)
    rootFinder.plot(subplot, foundRoot, function, "Green", "o", 8)
    
    rootFinder.plot(0, foundRoot, function, "Green", "o", 8)
    interval = rootFinder.plotInterval(foundRoot)
    intervalXYPoints = functionXYPoints(
        function,
        interval[0],
        interval[1],
        100,
    )
    plotter.plotLine(
        subplot,
        intervalXYPoints[0],
        intervalXYPoints[1],
    )
    plotter.enableGrid(subplot)

    subplot += 1
if(functionNumber == 1):
    print(np.roots(function))

plotter.show()
