from pre_processing import result
import  pandas as pd
from PIL import Image

import streamlit as st


def parse(s):
    if(s=='Yes'):
        return 1
    return 0

def gender(g):
    if(g=='Male'):
        return 1
    return 0

l = ['no_of_trainings', 'previous_year_rating', 'length_of_service', 'KPIs_met >80%', 'awards_won?',
                'avg_training_score', 'Region', 'department', 'education', 'gender', 'recruitment_channel', 'age']



#st.title("HR Anlyser\n")
def main():
    html_temp = """
    <div style="background-color:Skyblue;padding:1.5px">
    <h1 style="color:white;text-align:center;">HR Anlyser</h1>
    </div><br>"""
    st.markdown(html_temp, unsafe_allow_html=True)
    st.title('Plese enter details : ')
    st.markdown('<style>h3{color: red;}</style>', unsafe_allow_html=True)

    form = st.form(key='my-form')
    base = "dark"
    primaryColor = "purple"

    no_train = form.number_input(l[0], min_value=0, step=1)
    pyr = form.slider(label=l[1], min_value=1, max_value=5)
    ls = form.number_input(l[2], min_value=0, step=1)
    kpi = form.selectbox(l[3], ['Yes', 'No'])
    awards = form.selectbox(l[4], ['Yes', 'No'])
    avg_train_score = form.number_input(l[5], min_value=0, step=1)
    region = form.number_input(l[6], min_value=1, step=1)
    dept = form.selectbox(l[7], ['Analytics', 'Finance', 'HR', 'Legal', 'Operations', 'Procurement', 'R&D',
                                 'Sales & Marketing', 'Technology'])
    edu = form.selectbox(l[8], ["Master's & above", "Bachelor's", 'Below Secondary'])
    g = form.selectbox(l[9], ['Male', 'Female'])
    r_ch = form.selectbox(l[10], ['referred', 'sourcing', 'other'])
    age = form.number_input(l[11], min_value=20, step=1)
    submit = form.form_submit_button('Submit')

    # st.write('Press submit')

    if submit:
        # st.write({e_id,no_train,pyr,ls,kpi,awards,avg_train_score,dept,region,edu,g,r_ch,age})
        ans = [no_train, pyr, ls, kpi, awards, avg_train_score, region, dept, edu, g, r_ch, age]
        # st.write(ans)
        ans[3] = parse(kpi)
        ans[4] = parse(awards)
        ans[9] = gender(g)
        # st.write(ans,type(ans))

        y = result(ans)
        # print("list : ", y)
        y = pd.DataFrame(y, columns=['is_promoted'])
        # print("final result : \n", y)
        # print(ans)
        if (y.values == 1):
            st.success(f' # Wow!!! You are promoted :) ')
            im = Image.open("success.jpg")
            st.image(im, width=700, caption="Success")
        else:
            st.warning(f'# You need to work on your skills,All the Best:) ')
            im = Image.open("try.jpg")
            st.image(im, width=700, caption="Focus")



if __name__ == '__main__':
    main()
