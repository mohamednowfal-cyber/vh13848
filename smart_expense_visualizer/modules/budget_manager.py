# Budget setting and alerting

def check_budget(df, limit):
    total = df['Amount'].sum()
    return total > limit
