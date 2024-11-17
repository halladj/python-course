import pandas as pd
df = pd.DataFrame({
    "name" : ["hamza","abdou","zaki"],
    "grade" : ["A+","A+","A+"],
})
#print(df)


df = pd.DataFrame([
    ["hamza","A+"],
    ["abdou","A+"],
    ["zaki","A+"],
], columns=["name","grade"])
#print(df)


df = pd.read_csv("students.csv")
#print(df)

df.head(3)
#print(df.head(3))

df.tail(2)
#print(df.tail(2))

#print(df.describe())

df[df.Age > 25]
#print(df[df.Age>25])
