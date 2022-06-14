#crossover, mutation, two opt, selection
import os

programs = ["main_v0000", "main_v0001", "main_v0010", "main_v0011", "main_v0100", "main_v0101", "main_v0110", "main_v0111", "main_v1000", "main_v1001", "main_v1010", "main_v1011", "main_v1100", "main_v1101", "main_v1110", "main_v1111"]
#problems = ["X-n101-k25", "X-n110-k13", "X-n120-k6", "X-n148-k46", "X-n176-k26", "X-n200-k36", "X-n228-k23", "X-n251-k28", "X-n275-k28", "X-n303-k21"]
problems = ["P-n16-k8"]
selection_rates = ["0.0", "0.05", "0.1"]
RUNS = 1#5

def comp():
    for prog in programs:
        os.system("g++ " + prog + ".cpp -o " + prog + " -lpthread")
        os.system("cp " + prog + " ../" + prog )
        print(prog + " compiled successfully!")

def main():
    os.chdir("../")
    count = 0
    for prob in problems:
        for prog in programs:
            if prog[-1] == "1":
                for rate in selection_rates:
                    for run in range(1, 1 + RUNS):
                        cmd = "./{} P/{}.json {} {}".format(prog, prob, run, rate)
                        #os.system(cmd)
                        #os.system('dir')
                        count +=1
                        #print("\n---", count, cmd, "---\n")
                        
            else:
                for run in range(1, 1 + RUNS):
                    cmd = "./{} P/{}.json {} None".format(prog, prob, run)
                    #os.system(cmd)
                    #os.system("pwd")
                    count +=1
                    #print("\n---",count,  cmd, "---\n")
    print(count)

if __name__ == "__main__":
    comp()
    main()
