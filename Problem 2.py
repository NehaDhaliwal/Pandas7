# Count Salary Categories

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low_sal = len(accounts[accounts['income'] < 20000])
    avg_sal = len(accounts[(accounts['income'] >= 20000) & (accounts['income'] <= 50000)])
    high_sal = len(accounts[accounts['income'] > 50000])
    df = pd.DataFrame([['Low Salary', low_sal], ["Average Salary", avg_sal], ["High Salary", high_sal]])
    df = df.rename(columns = {0 : "category", 1 : "accounts_count"})
    print(df)
    return df

data = [[3, 108939], [2, 12747], [8, 87709], [6, 91796]]
accounts = pd.DataFrame(data, columns=['account_id', 'income']).astype({'account_id':'Int64', 'income':'Int64'})
count_salary_categories(accounts)