import os
import pandas as pd
import matplotlib.pyplot as plt

base_path = r"C:\Users\Пользователь\Desktop\4_data\data"

# список для всех DataFrame
all_data = []

# проходим по всем датам
for date_folder in os.listdir(base_path):
    date_path = os.path.join(base_path, date_folder)
    if not os.path.isdir(date_path):
        continue

    # проходим по пользователям внутри даты
    for user_folder in os.listdir(date_path):
        user_path = os.path.join(date_path, user_folder)
        data_file = os.path.join(user_path, "data.csv")

        if os.path.exists(data_file):
            # читаем csv
            df = pd.read_csv(data_file)

            # добавляем столбцы name и date
            df["name"] = user_folder
            df["date"] = date_folder

            all_data.append(df)

# объединяем всё в один датафрейм
final_df = pd.concat(all_data, ignore_index=True)

print(final_df.head())

# группируем по пользователю и суммируем количество товаров
user_totals = final_df.groupby("name")["quantity"].sum()

# находим максимум
max_qty = user_totals.max()

# выбираем всех юзеров с таким значением
top_users = user_totals[user_totals == max_qty].index

# сортируем
top_users_sorted = sorted(top_users)

# строка с именами через запятую
result = ', '.join(top_users_sorted)

print("Пользователь(и), купившие больше всего товаров:", result)
print("Количество товаров:", max_qty)

product_totals = final_df.groupby('product_id')['quantity'].sum().sort_values(ascending=False)

top10 = product_totals.head(10)

# строим барплот
plt.figure(figsize=(10, 6))
top10.plot(kind="bar")
plt.title("Топ-10 товаров по числу проданных единиц")
plt.xlabel("product_id")
plt.ylabel("Общее количество")
plt.xticks(rotation=45)
plt.show()

product_56 = product_totals.get(56, 0)
print("Всего продано товара с product_id==56:", product_56)

# убедимся, что колонка date в формате даты
final_df["date"] = pd.to_datetime(final_df["date"])

daily_sales = final_df.groupby('date')['quantity'].sum()

# строим график
plt.figure(figsize=(10, 6))
daily_sales.plot(kind="bar")
plt.title("Продажи по дням")
plt.xlabel("Дата")
plt.ylabel("Количество проданных товаров")
plt.xticks(rotation=45)
plt.show()

# группируем по пользователю и товару
user_product_dates = final_df.groupby(['name', 'product_id'])['date'].nunique()

# находим пары (user, product), где товар покупался более чем в 1 день
repeated_purchases = user_product_dates[user_product_dates > 1]

# получаем список уникальных пользователей
users_with_repeats = repeated_purchases.index.get_level_values("name").unique()

# итог: количество пользователей
num_users_with_repeats = len(users_with_repeats)

print("Количество пользователей, которые покупали одни и те же товары в разные дни:", num_users_with_repeats)
print("Список пользователей:", list(users_with_repeats))




























