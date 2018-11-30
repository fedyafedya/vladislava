from matplotlib import pyplot as plt
years = ['2011', '2012', '2013', '2014', '2015', '2016', '2017'] #годы
salary = [1800, 2000, 1950, 1700, 2000, 1500, 1700] #зарплата в долларах
xs = [i + 0.1 for i, _ in enumerate(years)]
plt.bar(xs, salary) #создать толбчатую диаграмму
plt.title("Software Engineer") #добавить название диаграммы
plt.ylabel("$") #добавить подпись к оси y
plt.xlabel("years") #добавить подпись к оси x
plt.xticks([i + 0.5 for i, _ in enumerate(years)], years) #добавить метки на оси х
plt.show() #показать диаграмму
