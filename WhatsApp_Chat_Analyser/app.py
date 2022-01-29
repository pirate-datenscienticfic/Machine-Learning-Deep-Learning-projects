import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt
import seaborn as sns



st.sidebar.title("Whatsapp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    
    
    df = preprocessor.preprocess(data)
    #st.dataframe(df)
    
    ### Fetch unique user
    user_list = df['user'].unique().tolist()
    user_list.remove("group_notification")
    user_list.sort()
    user_list.insert(0, "Overall")
    
    selected_user = st.sidebar.selectbox("Show Analysis wrt", user_list)
    
    if st.sidebar.button("Show Analysis"):
        ## Basic stats
        num_messages, words, no_media, link_share = helper.fetch_stats(selected_user, df)
        st.title("Top Statistics")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(words)
        with col3:
            st.header("Media Shared")
            st.title(no_media)
            
        with col4:
            st.header("Links shared")
            st.title(link_share)
        
        ## Monthly TimeLine
        st.title("Monthly TimeLine")
        timeline = helper.monthly_timeline(selected_user, df)
        fig, ax = plt.subplots()
        
        ax.plot(timeline["Time"], timeline["messages"], color="green")
        plt.xticks(rotation="vertical")
        st.pyplot(fig)
        
        ## Daily TimeLine
        st.title("Daily TimeLine")
        timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        
        ax.plot(timeline["Only_date"], timeline["messages"], color="green")
        plt.xticks(rotation="vertical")
        st.pyplot(fig)
        
        ## Activity Map
        st.title("Activity Map")
        col1, col2 = st.columns(2)
        
        with col1:
            st.header("Most busy day")
            busy_day = helper.week_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.barh(busy_day.index, busy_day.values)
            plt.xticks(rotation="vertical")
            st.pyplot(fig)
            
        with col2:
            st.header("Most busy Month")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color="orange")
            plt.xticks(rotation="vertical")
            st.pyplot(fig)
            
        user_heatmap = helper.activity_heatmap(selected_user, df)
        fig, ax = plt.subplots()
        ax = sns.heatmap(user_heatmap)
        st.pyplot(fig)
        

        ## Finding the busiest users in the group
        if selected_user == "Overall":
            st.title("Most Busy Users")
            x, new_df = helper.most_busy_users(df)
            fig, ax = plt.subplots()

            col1, col2 = st.columns(2)
            
            with col1:
                ax.bar(x.index, x.values, color="red")
                plt.xticks(rotation="vertical")
                st.pyplot(fig)
            
            with col2:
                st.dataframe(new_df)
                
        ## Wordcloud
        st.title("WordCloud")
        df_wc = helper.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)
        
        ## Most Common word
        most_common_word = helper.most_common_words(selected_user, df)
        
        fig, ax = plt.subplots()
        
        ax.barh(most_common_word[0], most_common_word[1])
        plt.xticks(rotation="vertical")
        
        st.title("Most Common word")        
        #st.dataframe(most_common_word)
        
        st.pyplot(fig)
        
        ## Emoji Analysis
        emoji_df = helper.emoji_helper(selected_user, df)
        emoji_df = emoji_df.head(10)
        st.title("Emoji Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.dataframe(emoji_df)
        with col2:
            fig, ax = plt.subplots()
            ax.pie(emoji_df[1], labels=emoji_df[0], autopct="%.2f")
            st.pyplot(fig)
            
        
### https://whatsup-chat-analysis.herokuapp.com/