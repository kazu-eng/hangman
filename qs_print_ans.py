ans = input("Where do you want to trip in the world?:")
with open("fav_country.txt", "w", encoding="utf-8") as f:
    f.write(ans.upper())

