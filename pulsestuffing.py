# written by Dustin Frandle 2/22/2021
def calculateStuffTDM(smallestInBits, largestInBits, sizeOfTimeSlotInBitsPerSecond, additionalBits, numOfInputs):
    inputDataRateInBitsPerSecond = stuffedBits(smallestInBits, largestInBits)
    totalData = numOfInputs * inputDataRateInBitsPerSecond
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

def stuffedBits(smallestInBits, largestInBits):
    stuffing = largestInBits - smallestInBits
    print("the " + str(smallestInBits) + " bit/s ch(s). were stuffed with " + str(stuffing) + " bits")
    return largestInBits

def findNumberOfInputs(dataRate, totalData):
    return totalData / dataRate