import pandas as pd
from datetime import datetime

def save_history(
    department,
    probability
):

    try:

        df = pd.read_csv(
            "history.csv"
        )

    except:

        df = pd.DataFrame()

    new_data = pd.DataFrame([{

        "Timestamp":
        datetime.now(),

        "Department":
        department,

        "Probability":
        round(probability*100,2)

    }])

    df = pd.concat(
        [df,new_data],
        ignore_index=True
    )

    df.to_csv(
        "history.csv",
        index=False
    )
