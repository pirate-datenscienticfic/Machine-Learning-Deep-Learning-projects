from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji


extract = URLExtract()

def fetch_stats(selected_user ,df):
    
    if selected_user != "Overall":
        df = df[df["user"] == selected_user]
        
    # 1. fetch number of messages
    num_messages = df.shape[0]
    
    # 2. Number of words
    words = []
    for msg in df["messages"]:
        words.extend(msg.split())
    
    # 3. Fetch the number of media messages
    num_media_msg = df[df["messages"] == "<Media omitted>"].shape[0]
        
    # 4. Fetch number of links shared
    links = []
    for msg in df["messages"]:
        links.extend(extract.find_urls(msg))
    
        
    return num_messages, len(words), num_media_msg, len(links)
   
   
def most_busy_users(df):
    x = df["user"].value_counts().head()
    new_df = round((df["user"].value_counts()/df.shape[0])*100, 2).reset_index().rename(columns={"index": "Name", "user":"%_Active"})
    return x, new_df


def create_wordcloud(selected_user, df):

    f = open("stop_hinglish.txt", "r")
    stop_words = f.read()
    
    if selected_user != "Overall":
        df = df[df["user"] == selected_user]
        
    temp = df[df["user"] != "group_notification"]
    temp = temp[temp["messages"] != "<Media omitted>"]
    
    def remove_stop_words(msg):
        y = []
        for word in msg.lower().split():
            if word not in stop_words:
                y.append(word)
        return " ".join(y)    
    
    wc = WordCloud(width=500, height=500, min_font_size=10, background_color="white")
    temp["messages"] = temp["messages"].apply(remove_stop_words)
    df_wc = wc.generate(temp["messages"].str.cat(sep=" "))
    return df_wc


def most_common_words(selected_user, df):
    
    f = open("stop_hinglish.txt", "r")
    stop_words = f.read()
    
    if selected_user != "Overall":
        df = df[df["user"] == selected_user]
        
    temp = df[df["user"] != "group_notification"]
    temp = temp[temp["messages"] != "<Media omitted>"]
    
    words = []
    
    for msg in temp["messages"]:
        for word in msg.lower().split():
            if word not in stop_words:
                words.append(word)
                
    most_common_df = pd.DataFrame(Counter(words).most_common(25))
    return most_common_df



def emoji_helper(selected_user, df):
    
    if selected_user != "Overall":
        df = df[df["user"] == selected_user]
        
    emojis = []
    for msg in df["messages"]:
        emojis.extend([c for c in msg if c in emoji.UNICODE_EMOJI["en"]])
        
    emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))
    
    return emoji_df


def monthly_timeline(selected_user, df):
    
    if selected_user != "Overall":
        df = df[df["user"] == selected_user]
    
    timeline = df.groupby(["Year", "Month", "Months"]).count()["messages"].reset_index()
    
    times = []

    for i in range(timeline.shape[0]):
        times.append(timeline["Months"][i] + "-" + str(timeline["Year"][i]))

    timeline["Time"] = times
        
    return timeline


def daily_timeline(selected_user, df):
    
    if selected_user != "Overall":
        df = df[df["user"] == selected_user]
        
    df["Only_date"] = df["Date"].dt.date
    daily_timeline = df.groupby("Only_date").count()["messages"].reset_index()
    
    return daily_timeline



def week_activity_map(selected_user, df):
    
    if selected_user != "Overall":
        df = df[df["user"] == selected_user]
        
    return df["Day_name"].value_counts()


def month_activity_map(selected_user, df):
    
    if selected_user != "Overall":
        df = df[df["user"] == selected_user]
        
    return df["Months"].value_counts()


def activity_heatmap(selected_user, df):

    if selected_user != "Overall":
        df = df[df["user"] == selected_user]
        
    act_heatmap = df.pivot_table(index="Day_name", columns="period", values="messages", aggfunc="count").fillna(0)
    
    return act_heatmap


