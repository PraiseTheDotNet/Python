import datetime

import pandas as pd


if __name__ == '__main__':
    df_build = pd.read_csv("files/moscow-buildings.csv", index_col=7)
    print('До удаления:')
    print(df_build.info())
    df_build = df_build[df_build["house_year"] != 'н.д.']
    print('После удаления:')
    print(df_build.info())
    year_data = [int(i) for i in df_build["house_year"]]
    df_build["house_year"] = year_data
    print('После замены формата:')
    print(df_build.info())

    min_year = min(year_data)
    max_year = max(year_data)
    print('Минимальный год:', min_year)
    print('Максимальный год:', max_year)
    before = len(df_build.index)
    print('До удаления:', before)
    current_date = datetime.datetime.now()
    df_build = df_build[(df_build["house_year"] >= 1760) & (df_build["house_year"] <= current_date.year)]
    after = len(df_build.index)
    print('После удаления:', after)
    print('Удалено:', before - after)

    print('Басманный:')
    basm_data = df_build[(df_build["area_id"] == 2281050) | (df_build["area_name"] == 'муниципальный округ Басманный')]
    print(basm_data.head())

    print('Количество домов по району')
    print(df_build[["area_name", "area_id"]].groupby("area_name").agg('count')
          .rename(columns={'area_name': 'Район', 'area_id': 'Количество'}))

    print('Вычисляем возраст дома')
    df_build['house_age'] = current_date.year - df_build["house_year"]
    print(df_build.head(10))
    print('Средний возраст дома по району')
    print(df_build[['area_name', 'house_age']].groupby('area_name').agg('mean')
          .rename(columns={'area_name': 'Район', 'house_age': 'Средний возраст'}))

    print('Самый старый дом:')
    data = df_build.loc[df_build['house_age'].idxmax()]
    print('Адрес:', data['full_address'])
    print('Год постройки:', data['house_year'])
    print('Возраст:', data['house_age'])

