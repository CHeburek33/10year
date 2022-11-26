import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('StudentsPerformance .csv')

df.info()

#df['math score'].plot(kind = 'pie')

#plt.show()

#Гипотеза 1: Результат экзамена выше если у сдающего оба родителя не имеют высшего образования

masters_degree = df[df['parental level of education']=="master's degree"]['math score'].max()
associates_egree = df[df['parental level of education']=="associate's degree "]['math score'].max()
bachelors_degree = df[df['parental level of education']=="bachelor's degree"]['math score'].max()
some_college = df[df['parental level of education']=="some college"]['math score'].max()
high_school = df[df['parental level of education']=="high school"]['math score'].max()
some_high_school = df[df['parental level of education']=="some high school"]['math score'].max()

print("Результат экзамена выше если у сдающего оба родителя не имеют высшего образования")

print("Уровни образования родителей")
print("\n1 - master's degree",masters_degree)
print("2 - associate's degree",associates_egree)
print("3 - bachelor's degree",bachelors_degree)
print("4 - some college",some_college)
print("5 - high school",high_school) 
print("6 - some high school",some_high_school)

print('\nГипотеза подтверждена')

s = pd.Series(data = [masters_degree,associates_egree,bachelors_degree,some_college,high_school,some_high_school],
index = ['Высшее образование','Степень младшего специалиста','Степень бакалавра','Колледж','Старшая школа',"До старшая школа"])

s.plot(kind = 'barh')
#set_title('Результаты тестов')
plt.show()