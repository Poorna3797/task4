###### Assessment

###### I am going to provide two .csv files , you are supposed to work on them and have to provide solutions to the following problems

###### import necessary libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

###### merge those two csv files (after getting as dataframes, get them as a single dataframe)

from google.colab import drive
drive.mount("/content/gdrive")
import pandas as pd
data1 = pd.read_csv('/content/gdrive/My Drive/Colab Notebooks/college_1.csv')
data2 = pd.read_csv('/content/gdrive/My Drive/Colab Notebooks/college_2.csv')
data = pd.concat([data1, data2])

###### Take each csv file , split that csv file into multiple categories (example csv files are added in the repo) 


###### consider if the codekata score exceeds 15000 points(present week) then make a csv on those observations as Exceeded expectations.csv


###### if  10000<codekata score<15000   (Reached_expectations.csv)



###### if  7000<codekata score<10000   (Needs_Improvement.csv)


###### if  codekate score < 7000        (Unsatisfactory.csv)

Exceeded = data[(data['CodeKata Score'] > 15000)]
Exceeded.to_csv("Reached_expectations.csv")

data.columns

reached = data[(data['CodeKata Score'] > 10000) & (data['CodeKata Score'] < 15000)]

reached.to_csv("Reached_expectations.csv")

Needs = data[(data['CodeKata Score'] < 7000) & (data['CodeKata Score'] < 10000)]
Needs.to_csv("Needs_Improvement.csv")

Unsatisfactory = data[(data['CodeKata Score']< 7000)]
Unsatisfactory.to_csv("Unsatisfactory.csv")

Unsatisfactory

###### Average of previous week geekions vs this week geekions (i.e Previous Geekions vs CodeKata Score)

Avg = np.mean(data[["Previous Geekions", "CodeKata Score"]])
Avg

###### No of students participated 

No_students = (data["Name"]).count
No_students

###### #Average completion of python course or my_sql or python english or computational thinking

A_completion = np.mean(data[["python", "mysql", "python_en", "computational_thinking"]])
A_completion

###### rising star of the week (top 3 candidate who performed well in that particular week)

R_Stars = data.sort_values(by="Rising", ascending=False)
R_Stars.head(3)

###### Shining stars of the week (top 3 candidates who has highest geekions)

S_Stars = data.sort_values(by="Previous Geekions", ascending=False)
S_Stars.head(3)

###### Department wise codekata performence (pie chart)

value = data.groupby(['Department'], as_index=False)['CodeKata Score'].sum()
value
x = np.array(value['CodeKata Score'])
y = list(value['Department'])
plt.pie(x, labels = y)
plt.show()

###### Department wise toppers (horizantal bar graph or any visual representations of your choice)

Bar = data.groupby(['Department'], as_index=False)['CodeKata Score'].max()
Bar
x1 = np.array(Bar['CodeKata Score'])
y1 = np.array(Bar['Department'])
plt.bar(y1, x1)
plt.show()
Bar





