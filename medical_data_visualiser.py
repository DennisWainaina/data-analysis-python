import pandas as pd
df = pd.read_csv('medical_examination.csv')
height = df['height']
print(height)
print('The average height is', height.mean())

# Q1 : Creating an overweight column such that 1 is overweight and 0 is not overweight


def overweighted():
    height_in_metres = df['height']/100
    print(height_in_metres)
    df['BMI'] = df['weight'] / height_in_metres**2
    print(df['BMI'])
    print(df)
    bmi = df['BMI']
    print(bmi)
    list1 = []
    for i in bmi:
        if i > 25:
            overweight = 1
            list1.append(overweight)
        else:
            not_overweight = 0
            list1.append(not_overweight)

    df['overweight'] = list1

    print(df)


overweighted()

# Q2: Normalise the data If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1,
# make value 1


def normalise():
    cholestrol = df['cholesterol']
    list2 = []

    for t in cholestrol:
        if t > 1:
            t = 1
            list2.append(t)
        else:
            t = 0
            list2.append(t)

    df['cholesterol'] = list2
    print(df['cholesterol'])
    print(df)
    # This is to check if the code actually worked

    glucose = df['gluc']
    list3 = []
    for g in glucose:
        if g > 1:
            g = 1
            list3.append(g)
        else:
            g = 0
            list3.append(g)

    df['gluc'] = list3
    print(df['gluc'])
    print(df)
    # We do the same for the gluc column


normalise()

# Cleaning the data


def cleaning():
    # The first step is to filter out the data in ap_lo which is greater than the ap_hi column
    corrected_values = df['ap_lo'][df['ap_lo'] <= df['ap_hi']]
    print(corrected_values)
    corrected_values = df['ap_lo']
    print(df['ap_lo'])
    print(df)

    # The next step is to filter out data according to a certain percentile
    correct_height = df['height'][((df['height']) >= (df['height'].quantile(0.025))) &
                                  ((df['height']) < (df['height'].quantile(0.975)))]
    print(correct_height)
    df['height'] = correct_height
    correct_height1 = df['height'][(df['height']) < (df['height'].quantile(0.975))]
    print(correct_height1)

    correct_weight = df['weight'][((df['weight']) < (df['weight'].quantile(0.975))) &
                                  ((df['weight']) > (df['weight'].quantile(0.025)))]
    print(correct_weight)
    df['weight'] = correct_weight
    correct_weight1 = df['weight'][(df['weight']) > (df['weight'].quantile(0.025))]
    print(correct_weight1)

    print(df)

    
print('This is the final piece of code')

df.to_excel('medical_data.xlsx')

cleaning()
