# written by Dustin Frandle 2/22/2021
# designed to be used on a NumWorks Calculator
import statisticaltdm
import synchronoustdm
import pulsestuffing

print("Select TDM")
print("1. Synchronous/Multilevel/Multiple-slot")
print("2. Statistical")
print("3. Pulse-Stuffing")
entry = input("")
if entry == "1":
    a = input("smallest input channel in bits/s: ")
    b = input("largest input channel in bits/s: ")
    c = input("the size of the time slot: ")
    d = input("additional bits: ")
    e = input("sum of the data rate of each channel: ")
    print("---------------------------------------")
    synchronoustdm.calculateSyncTDM(float(a), float(b), float(c), float(d), float(e))
elif entry == "2":
    a = input("number of slots: ")
    b = input("the size in bits of a character: ")
    c = input("the data rate of incoming character per second: ")
    d = input("the size of the time slot: ")
    e = input("number of sources: ")
    print("---------------------------------------")
    statisticaltdm.calculateStatTDM(float(a), float(b), float(c), float(d), float(e))
elif entry == "3":
    a = input("smallest input channel in bits/s: ")
    b = input("largest input channel in bits/s: ")
    c = input("the size of the time slot: ")
    d = input("additional bits: ")
    e = input("number of input channels: ")
    print("---------------------------------------")
    pulsestuffing.calculateStuffTDM(float(a), float(b), float(c), float(d), float(e))
