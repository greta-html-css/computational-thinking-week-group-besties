# Station 2 Dates and Days of the Week (in Japanese Kanji)

# Observations
# 09:40:20, 2023-09-25, "月曜日 (Monday)", 2024-06-20
# 09:42:17, 2023-06-10, "土曜E (Saturday)", 2024-04-21
# 09:42:21, 2023-02-09, "木曜日 (Thursday)", 2024-11-03
# 09:42:41, 2023-01-25, "水曜日 (Wednesday)", 2024-05-10
# 09:42:59, 2023-02-16, "木曜日 (Thursday)", 2024-04-07
# 09:43:01, 2023-09-10, "日曜日 (Sunday)", 2024-07-16
# 09:43.14, 2023-03-12, "日曜日 (Sunday)", 2024-09-26
# 09:43:21, 2023-10-11, "水曜日 (Wednesday)", 2024-08-11
# 09:43:32, 2023-11-07, "火曜日 (Tuesday)", 2024-06-09
# 09:43:44, 2023-07-24,"月曜日 (Monday)", 2024-06-25



def solution_station_2(d):
    # Using Zeller’s Congruence to figure out the day of the week
    q, m, y = map(int, d.split('-'))  # day, month, year

    if m < 3:   
        m += 12
        y -= 1

    k = y % 100  # yearpart
    j = y // 100 # century

    h = (q + (13 * (m + 1)) // 5 + k + k // 4 + j // 4 + 5 * j) % 7  
    wd = ['土曜E (Saturday)', '日曜日 (Sunday)', '月曜日 (Monday)', '火曜日 (Tuesday)', '水曜日 (Wednesday)', '木曜日 (Thursday)', '金曜且 (Friday)']

    return(wd[h])

# Station 5 - Simultanious Observstions
# 10:23:00, "Yang Yang", 4, "Madeleine"
# 10:23:10, "Twan", 1, "Sara"
# 10:23:20, "Sem", 3, "Wenhao"
# 10:23:30, "Amir", 3, "Ivar"
