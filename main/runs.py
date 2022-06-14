import os

def main():
    for directory in ["other"]:
        for file in os.listdir("../data/" + directory + "/"):
            if file[-4:] == "json":
                os.system("./main " + directory + "/" + file)

if __name__ == "__main__":
    main()
