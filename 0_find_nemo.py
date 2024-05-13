from typing import List

nemo = ["Emily","Stich"]

def find_nemo(col:List[str]):
    for text in col:
        if text=="Nemo":
            print("Here is our Nemo")
            return
    print("Nemo is not there ((")

find_nemo([1,2,3])