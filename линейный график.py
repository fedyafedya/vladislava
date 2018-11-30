from matplotlib import pyplot as plt
years = [2011, 2012, 2013, 2014, 2015, 2016, 2017] #годы
salary = [1800, 2000, 1950, 1700, 2000, 1500, 1700] #зарплата в долларах
plt.plot(years, salary, color='green', marker='0', linestyle='solid') #создать линейную диаграмму
plt.title("Software Engineer - Python") #добавить название диаграммы
plt.ylabel("$") #добавить подпись к оси y
plt.xlabel("years") #добавить подпись к оси x
plt.show() #показать диаграмму
