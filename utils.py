from tabulate import tabulate

def display_df(df):
    return tabulate(df, headers="keys", tablefmt="psql", showindex=False)