import pandas as pd
from datetime import datetime

def save_history(department, probability):

    try:
        df = pd.read_csv("history.csv")

    except:
        df = pd.DataFrame()

    new_row = pd.DataFrame([{
        "Timestamp": datetime.now(),
        "Department": department,
        "Probability": probability
    }])

    df = pd.concat(
        [df, new_row],
        ignore_index=True
    )

    df.to_csv(
        "history.csv",
        index=False
    )
