import pandas as pd

def get_3cycle(pce_type, buffer, p1, p2):
    df = pd.read_csv(f"algs/{pce_type}{buffer}.csv")
    return df[p1][df.columns.get_loc(p2)]

if __name__ == "__main__":
    df = pd.read_csv("algs/UFRc.csv")
    print(df.head(5))
    print()
    p1, p2 = input().split()
    comm = df[p2][df.columns.get_loc(p1)]
    print(comm)