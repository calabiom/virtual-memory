## main.py
## Mark Calabio 12488362

## SIMPLE VERSION of Project 2

from collections import defaultdict
## Part 1: INITIALIZATION

## We initialize PM from an input file consisting of 2 lines
##  - Line 1 contains triples of integers, which define the contents of the ST
##  - Line 2 contains triples of integers, which define the contents of the PTs

## s, z, f means: PT of segment s resides in frame f; length of segment s is z
## We initialize: PM[2*s] = z, and PM[2*s + 1] = f
##   A segment s occupies the entries 2s and 2s+1.

PM = [0] * 524288

def setup_segment_table(s,z,f):
    if (2*s) > len(PM):
        return -1
    
    PM[2*s] = z
    PM[2*s + 1] = f

    #print("PM[2*s] = z = ", PM[2*s]) 
    #print("PM[2*s + 1] = f = ", PM[2*s + 1])
    return "Page table of Segment {} resides in Frame {}; length of Segment {} is {}".format(s,f,s,z)

def setup_page_table(s, p, f):
    idx = (PM[2*s + 1] * 512) + p
    #print(idx)

    if idx > len(PM):
        return -1
    
    PM[idx] = f

    #print("PM[PM[2*s + 1] * 512) + p] = f = ", PM[idx])
    return "Page {} of Segment {} resides in Frame {}".format(p,s,f)


def initialize():
    f = open("input.txt", "r")  # init-no-dp.txt

    line_count = 0
    for line in f:

        line_count += 1

        bag = []
        for element in line.split():
            bag.append(int(element))
            if len(bag) == 3:
                if line_count == 1:
                    result = setup_segment_table(bag[0], bag[1], bag[2])
                    #print(result)
                else:
                    result = setup_page_table(bag[0], bag[1], bag[2])
                    #print(result)
                del bag[:]
            


## Part 2: TRANSLATION
                
# 1. Break VA into s, p, w, pw
# 2. If pw ≥ PM[2s], then report error; VA is outside of the segment boundary
# 3. Else PA = PM[PM[2s + 1]*512 + p]*512 + w

def convert_to_physical_address():
    f = open("input2.txt", "r")     #  input-no-dp.txt
    output = open("output-no-dp.txt", "w+")

    for line in f:

        for element in line.split():
            result = None
            
            va = int(element)

            ## Find the values of the following by bitwise manipulation
            s = None
            w = None
            p = None
            pw = None
            
            print(va)
            
            # binary_va_str = '{:032b}'.format(int(va))
            
            s = va >> 18
            w = va & 511        # 111111111
            p1 = va >> 9
            p2 = p1 & 511       # 111111111
            pw = va & 262143    # 111111111 111111111

            #print(s, p2, w, pw)

            if pw >= PM[2*s]:
                result = -1
            else:
                r1 = PM[2*s + 1] * 512
                r2 = PM[r1 + p2] * 512
                result = r2 + w

            print("Physical address is: ", result)
            
            output.write(str(result))
            output.write(" ")


            




initialize()
convert_to_physical_address()


            

