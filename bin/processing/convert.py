# check files for trucks
# check for optimiality

import os
import json
import shutil

dataSet = 'P'
path = '..\data\Vrp-Set-' + dataSet + '\\' + dataSet

def main():
    for i in os.listdir(path):

        # move the solution file over to the sets directory
        if i[-3:] == 'sol':
            shutil.move(path + '\\' + i, '..\data\\' + dataSet + '\\' + i)

        # else the file is a vrp file
        else:
            nFlag = False
            dFlag = False
            nodes = []
            demand = []
            best = None
            n = None
            capacity = None
            trucks = int(i[:-4].split('-')[-1][1:])

            # get the values
            with open(path + '\\' + i) as f:
                for line in f.readlines():
                    if line[0:3] == 'COM':
                        #best = float(line.split(' : ')[1])
                        best = float(line.split(' ')[-1][:-2])
                    elif line[0:3] == 'DIM':
                        n = int(line.split(' : ')[-1])
                    elif line[0:3] == 'CAP':
                        capacity = int(line.split(' : ')[1])
                    elif line[0:3] == 'NOD':
                        nFlag = True
                    elif line[0:3] == 'DEM':
                        dFlag = True
                        nFlag = False
                    elif line[0:3] == 'DEP':
                        break
                    elif nFlag == True:
                        x = float(line.split(" ")[1])
                        y = float(line.split(" ")[2])
                        nodes.append([x, y])
                    elif dFlag == True:
                        d = float(line.split(" ")[1])
                        demand.append(d)

            # make sure all the values are presented
            if n != None:
                if capacity != None:
                    if best != None:
                        if len(nodes) > 0:
                            if len(demand) > 0: pass
                            else: continue
                        else: continue
                    else: continue
                else: continue
            else: continue

            data = {"NODES":n, "ROUTES":trucks, "CAPACITY":capacity, "BEST":best, "OPTIMAL":0, "LOCATION":nodes, "DEMAND":demand}

            with open("..\data\\" + dataSet + "\\" + i[:-3] + "json", 'w') as f:
                json.dump(data, f, indent=4)

if __name__ == "__main__":
    main()
