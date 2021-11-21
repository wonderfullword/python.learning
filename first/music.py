# violator
#
# 1.Выведите общее время звучания всех песен.
# 2.Создайте список песен, время звучаниях которых больше 5 минут
# 3.Создайте новый словарь тех песен, в название которых состоит из одного слова

songsdict = {
'World in My Eyes': 4.76,
'Sweetest Perfection': 5.43,
'Personal Jesus': 4.56,
'Halo': 4.30,
'Waiting for the Night': 6.07,
'Enjoy the Silence': 4.6,
'Policy of Truth': 4.88,
'Blue Dress': 4.18,
'Clean': 5.68,
}
d=[]
song=[]
for key, values in songsdict.items():
    print(key, values)
    d.append(values)
    print(sum(d))
