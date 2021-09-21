from secantMethod import SecantMethod
from chordMethod import ChordMethod
from scannerMethod import ScannerMethod
import numpy as np

polynomialFunction = np.poly1d([-0.79, 6.17, -16.66, 17.91, -6.19])

def transcendentalFunction(x):
    return 2 * x * np.cos(x) - np.power((x/2+0.5), 3)

def secondFunction(m):
    if(m == 0):
        return -np.Infinity
    return 100*np.power(np.e, np.float128(-(0.05*3)/m)) + ((m*9.8)/0.05) * (np.power(np.e, np.float128(-(0.05*3)/m))-1)-49

# CHANGE THESE
functionNumber = 3
rootFinder = 3
# -------------
methods = {
    1: ScannerMethod,
    2: ChordMethod,
    3: SecantMethod
    }
titles = {
    1: 'Scanner',
    2: 'Chord',
    3: 'Secant'
}
functions = {
    1: polynomialFunction,
    2: transcendentalFunction,
    3: secondFunction
}
# -------------

method = methods.get(rootFinder)
title = titles.get(rootFinder)
function = functions.get(functionNumber)