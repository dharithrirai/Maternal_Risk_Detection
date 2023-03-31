import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('Backend/ML/Maternal Health Risk Data Set.csv')

#Exploratory Data Analysis
upperlimit=df["Age"].mean()+1.5*df["Age"].std()
lowerlimit=18
print("upper limit",upperlimit)
print("lower limit", lowerlimit)


#Remove the age based data beyond the limit
error=df.loc[(df['Age']>=upperlimit)|(df['Age']<=lowerlimit)]

# remove outliers
new_df=df.loc[(df['Age']<upperlimit)&(df['Age']>=lowerlimit)]
print("Before",len(df))
print("After",len(new_df))
print("Outliers",len(df)-len(new_df))


new_df['RiskLevel'].replace({"high risk":"1","mid risk":"0","low risk":"0"}, inplace=True)
new_df['RiskLevel'] = new_df['RiskLevel'].astype(float)
print(new_df)

new_df.to_csv('Backend/ML/New_Maternal.csv', index=False)


#Train the data
train , test = train_test_split(new_df,test_size=0.15,random_state=35)
print(f"No. of training examples:{train.shape[0]}")
print(f"No. of testing examples:{test.shape[0]}")