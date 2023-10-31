import pandas as pd

def make_df(cols, ind):
    data = {c : [str(c) + str(i) for i in ind] for c in cols}
    return pd.DataFrame(data, ind)

def main():
    pass

if __name__ == "__main__":
    main()