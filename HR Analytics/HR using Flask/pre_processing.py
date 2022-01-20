from methods import *
import pickle


def result(l):
    user_col = ['no_of_trainings', 'previous_year_rating', 'length_of_service', 'KPIs_met >80%', 'awards_won?',
                'avg_training_score', 'Region', 'department', 'education', 'gender', 'recruitment_channel', 'age']
    input_data = list(l)
    '''
    print(csv_col,len (csv_col))
    print(csv_data,len(csv_data),"\n")
    '''
    #print(user_col, len(user_col))
    #print(input_data, len(input_data))

    # change age to age_bins
    input_data = age_to_age_bins(input_data)
    #print(user_col, len(user_col))
    #print(input_data, len(input_data))

    model_input = ['no_of_trainings', 'previous_year_rating', 'length_of_service',
                   'KPIs_met >80%', 'awards_won?', 'avg_training_score', 'Region',
                   'department_Finance', 'department_HR', 'department_Legal',
                   'department_Operations', 'department_Procurement', 'department_R&D',
                   'department_Sales & Marketing', 'department_Technology',
                   'education_Below Secondary', "education_Master's & above", 'gender_m',
                   'recruitment_channel_referred', 'recruitment_channel_sourcing',
                   'age_30', 'age_40']

    # time for Encoding
    col = user_col[:7]
    model_input_encode = input_data[:7]  # (0 to 6 copy)
    '''
    print(model_input)
    print(col)
    print(model_input_encode, len(model_input_encode))
    '''

    # call functions
    # Department
    dept = one_hot_dept(input_data[7])
    #print("\nDEP - ", dept)
    model_input_encode = model_append(dept, model_input_encode)
    #print(model_input_encode, len(model_input_encode))

    # Education
    edu = one_hot_edu(input_data[8])
    #print("\nEDU - ", edu)
    model_input_encode = model_append(edu, model_input_encode)
    #print(model_input_encode, len(model_input_encode))

    # Gender
    g = (input_data[9])
    model_input_encode.append(g)
    print(model_input_encode, len(model_input_encode))

    # RC
    rc = one_hot_rc(input_data[10])
    #print("\nRC - ", rc)
    model_input_encode = model_append(rc, model_input_encode)
    #print(model_input_encode, len(model_input_encode))

    # Age bin
    age = one_hot_age(input_data[11])
    #print("AGE - ", age)
    model_input_encode = model_append(age, model_input_encode)
   # print(model_input_encode, len(model_input_encode))

    # Encoding done
    # change list to frame

    data_encode = pd.DataFrame(np.array(model_input_encode).reshape(-1, len(model_input_encode)))
    #print("\n\n", data_encode, len(data_encode))

    # Predict Results

    model = pickle.load(open('Decision_Tree_Model.pickle', 'rb'))
    print(model)
    y = model.predict(data_encode)
    # y = model.predict(data_scale)
    print("OUTPUT : ", y, "\n\n")

    return y