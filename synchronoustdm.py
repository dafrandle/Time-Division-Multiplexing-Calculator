# written by Dustin Frandle 2/22/2021
import math
def calculateSyncTDM(smallestInBits, largestInBits, sizeOfTimeSlotInBitsPerSecond, additionalBits, *args):
    inputDataRateInBitsPerSecond = findInputRate(smallestInBits, largestInBits)
    totalData = 0
    for val in args:
        totalData = val + totalData
    numberOfInputs = findNumberOfInputs(inputDataRateInBitsPerSecond, totalData)
    outputFrameSizeInBits = numberOfInputs * sizeOfTimeSlotInBitsPerSecond + additionalBits
    outputFrameRateInFramesPerSeconds = inputDataRateInBitsPerSecond / sizeOfTimeSlotInBitsPerSecond
    inputDurationInSeconds = 1 / inputDataRateInBitsPerSecond
    outputDurationInSeconds = inputDurationInSeconds * (1 / numberOfInputs)
    timeSlotDurationInSeconds = sizeOfTimeSlotInBitsPerSecond / numberOfInputs
    outputDataRateInBitsPerSecond = outputFrameSizeInBits * outputFrameRateInFramesPerSeconds
    outputFrameDurationInSeconds = 1 / outputFrameRateInFramesPerSeconds
    efficiency = (outputFrameSizeInBits - additionalBits) / outputFrameSizeInBits
    print("Input Data Rate: " + str(inputDataRateInBitsPerSecond) + " Bits/s")
    print("Number of Inputs: " + str(numberOfInputs))
    print("Output frame size: " + str(outputFrameSizeInBits) + " Bits")
    print("Output frame rate: " + str(outputFrameRateInFramesPerSeconds) + " Frames a second")
    print("Input duration: " + str(inputDurationInSeconds * 1000) + " Milliseconds")
    print("Output duration: " + str(outputDurationInSeconds * 1000) + " Milliseconds")
    print("Time slot duration: " + str(timeSlotDurationInSeconds) + " Milliseconds")
    print("Output data rate: " + str(outputDataRateInBitsPerSecond) + " Bits/s")
    print("Output frame duration: " + str(outputFrameDurationInSeconds * 1000) + " Milliseconds")
    print("Efficiency: " + str(efficiency))


def findInputRate(smallestInBits, largestInBits):
    result = 0
    if largestInBits % smallestInBits == 0:
        result = largestInBits
    else:
        result = math.gcd(largestInBits, smallestInBits)
    return result


def findNumberOfInputs(dataRate, totalData):
    return totalData / dataRate