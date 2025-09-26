import pandas as pd

# читаем Excel с данными компаний
df = pd.read_excel(r"C:\Users\Пользователь\Desktop\Аналитик данных 1\[SW.BAND] 2 МОДУЛЬ PYTHON\[SW.BAND] Доп задания\4_inn.xls")

# читаем список ИНН из текстового файла
necessary_inn = pd.read_csv(r"C:\Users\Пользователь\Desktop\Аналитик данных 1\[SW.BAND] 2 МОДУЛЬ PYTHON\[SW.BAND] Доп задания\4_necessary_inn.txt", header=None)[0].tolist()

# фильтруем по нужным ИНН
filtered_df = df[df["head_inn"].isin(necessary_inn)]

# сохраняем результат
filtered_df.to_csv("selected_inn.csv", index=False)

# считаем сумму по колонке income.RUB
income_sum = filtered_df["income,RUB"].sum()

print("Сумма колонки income,RUB в отобранных данных:", income_sum)
