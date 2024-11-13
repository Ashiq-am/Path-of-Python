from concurrent.futures import ThreadPoolExecutor

def GFG(start, end):

    print(f"Processing range ({start}, {end})")

def Geek():

    start = 0
    end = 5
    with ThreadPoolExecutor(max_workers=4) as executor:

        for i in range(start, end):
            executor.submit(GFG, i, i+1)

if __name__ == "__main__":
    Geek()
