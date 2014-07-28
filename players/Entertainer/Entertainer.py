from sys import argv
print("PSSBSPPBSB"[len(argv)<2 or (len(argv[1])+argv[1].count("B"))%10])