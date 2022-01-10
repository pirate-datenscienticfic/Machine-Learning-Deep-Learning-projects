import pandas as pd
import numpy as np

def age_bin(age):
    age = int(age)
    if(age<30):
        age = 20
    elif(age>=30 & age <40):
        age = 30
    else:
        age = 40
    return age

#chnage age to age_bins
def age_to_age_bins (input_user):
    # do encosing for categorical data
    age = int(input_user[-1])
    input_user.remove(age)
    #print(age,type(age))
    age = age_bin(age)
    input_user.append(age)
    #print(input_user)
    return input_user

def model_append(d,l):
    for i in d:
        l.append(d[i])
    return l

#Encode categorical columns

#encode gender
'''
def gender(g):
    if(g==1):
        return 1
    return 0
'''

# create eye matrix for encoding
def one_hot_encode(x,n_classes):
    return tuple(np.eye(n_classes,dtype=int)[x])

#-----------------------------------------------------
# 1 encode department
# Analytics is all zero
def one_hot_dept(x_in):
    org_dept = ['Finance', 'HR', 'Legal', 'Operations',
                    'Procurement','R&D', 'Sales & Marketing','Technology']

    dept = ['department_Finance', 'department_HR', 'department_Legal', 'department_Operations',
            'department_Procurement',
            'department_R&D', 'department_Sales & Marketing','department_Technology']
    n_classes = len(dept)
    z = [0] * n_classes
    data = [i for i in range(n_classes)]
    ans = one_hot_encode(data,n_classes)
    d = dict(zip(dept, z))
    for i in range(n_classes):
        if (x_in == org_dept[i]):
            d = dict(zip(dept, ans[i]))
            #print(d)
            break
    #print("\nDEP - ",d)
    return d
#-------------------------------------------------
# 2 encode education
def one_hot_edu(x_in):
    # Bachelor's , left all zero for it
    org_edu = ["Below Secondary","Master's & above"]
    edu = ["education_Below Secondary", "education_Master's & above"]
    n_classes = len(edu)
    z = [0] * n_classes
    data = [i for i in range(n_classes)]
    ans = one_hot_encode(data,n_classes)
    d = dict(zip(edu, z))
    for i in range(n_classes):
        if (x_in == org_edu[i]):
            d = dict(zip(edu, ans[i]))
            #print(d)
            break
    #print("\nEDU - ",d)
    return  d
#-----------------------------------------
# 3 encode recruitment_channel
def one_hot_rc(x_in):
    #  other, left all zero for it
    # rc - > recruitment_channel
    org_rc = ['referred', 'sourcing']

    rc = ['recruitment_channel_referred', 'recruitment_channel_sourcing']
    n_classes = len(rc)
    z = [0] * n_classes
    data = [i for i in range(n_classes)]
    ans = one_hot_encode(data,n_classes)
    d = dict(zip(rc, z))
    for i in range(n_classes):
        if (x_in == org_rc[i]):
            d = dict(zip(rc, ans[i]))
            #print(d)
            break
    #print("\nRC - ",d)
    return d
#-----------------------------------------
# 4 encode age_bins
def one_hot_age(x_in):
    #  20, left all zero for it
    # rc - > recruitment_channel
    x_in = int(x_in)
    org_age = [30,40]
    age = ['age_bins_30', 'age_bins_40']
    n_classes = len(age)
    z = [0] * n_classes
    data = [i for i in range(n_classes)]
    ans = one_hot_encode(data,n_classes)
    d = dict(zip(age, z))
    for i in range(n_classes):
        if (x_in == org_age[i]):
            d = dict(zip(age, ans[i]))
            #print(d)
            break
    #print("\nAGE - ",d)
    return d
