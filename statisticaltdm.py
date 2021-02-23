# written by Dustin Frandle 2/22/2021
import math
def calculateStatTDM(numberOfSlotsPerFrame, characterSizeInBits, charactersPerSecond, sizeOfTimeSlotInBitsPerSecond, numberOfSources):
    slotAddressSizeInBits = math.ceil(math.log2(numberOfSources))
    outputFrameSizeInBits = numberOfSlotsPerFrame * (characterSizeInBits + slotAddressSizeInBits)
    outputFrameRateInFramesPerSeconds = charactersPerSecond / sizeOfTimeSlotInBitsPerSecond
    inputDurationInSeconds = 1 / charactersPerSecond
    outputDurationInSeconds = inputDurationInSeconds * (1 / numberOfSlotsPerFrame)
    timeSlotDurationInSeconds = sizeOfTimeSlotInBitsPerSecond / numberOfSlotsPerFrame
    outputDataRateInBitsPerSecond = outputFrameSizeInBits * outputFrameRateInFramesPerSeconds
    outputFrameDurationInSeconds = 1 / outputFrameRateInFramesPerSeconds
    print("Address size: " + str(slotAddressSizeInBits) + " Bits")
    print("Output frame size: " + str(outputFrameSizeInBits) + " Bits")
    print("Output frame rate: " + str(outputFrameRateInFramesPerSeconds) + " Frames/s")
    print("Input duration: " + str(inputDurationInSeconds*1000) + " Milliseconds")
    print("Output duration: " + str(outputDurationInSeconds*1000) + " Milliseconds")
    print("Time slot duration: " + str(timeSlotDurationInSeconds) + " Milliseconds")
    print("Output data rate: " + str(outputDataRateInBitsPerSecond) + " Bits/s")
    print("Output frame duration: " + str(outputFrameDurationInSeconds*1000) + " Milliseconds")