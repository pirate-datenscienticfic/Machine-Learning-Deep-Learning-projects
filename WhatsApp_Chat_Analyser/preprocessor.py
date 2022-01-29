### Function to convert text data to csv format and preprocessing it
import re
import pandas as pd


def preprocess(data):
    ## AM/PM format
    pattern = "\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s\wm\s-\s"

    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    df = pd.DataFrame({'User_message': messages, 'Message_dates': dates})

    ## Convert message_date&Time
    df["Message_dates"] = pd.to_datetime(df["Message_dates"], format='%d/%m/%y, %I:%M %p - ')
    df.rename(columns={"Message_dates": "Date"}, inplace=True)

    ## Separate users and messages
    users = []
    messages = []

    for msg in df["User_message"]:
        entry = re.split("([\w\W]+?):\s", msg)
        if entry[1:]: #User Name
            users.append(entry[1])
            messages.append(entry[2][:-1])
        else:
            users.append("group_notification")
            messages.append(entry[0])
            

    df["user"] = users
    df["messages"] = messages
    df.drop(columns=["User_message"], inplace=True)
    
    df["Year"] = df["Date"].dt.year
    df["Months"] = df["Date"].dt.month_name()
    df["Month"] = df["Date"].dt.month
    df["Day"] = df["Date"].dt.day
    df["Day_name"] = df["Date"].dt.day_name()

    df["Hour"] = df["Date"].dt.hour
    df["Minute"] = df["Date"].dt.minute
    
    
    period = []

    for hour in df[["Day_name", "Hour"]]["Hour"]:
        if hour == 23:
            period.append(str(hour) + "-" + str("00"))
        elif hour == 0:
            period.append(str("00") + "-" + str(hour+1))
        else:
            period.append(str(hour) + "-" + str(hour+1))
    
    df["period"] = period
    
    
    return df
