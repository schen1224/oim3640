# name = input("Please enter your name:")
# print("hello,", name)

lyrics = "banana\n" * 10  # \n提行
print(lyrics)


actor = "sabrina"
year = "2022"
print(f"{actor} lives in {year}!")


pi = 3.1415926
print(f"pi equals to {pi:.5f}.")  # 5f means 5 decimals
print(
    f"pi equals to {pi:8.5f}."
)  # 8 means 8 places for the entire numer, so 3 places before the dot. it is used for having a better formatting
print(f"pi equals to {pi:8.2f}.")  # so 5 places before dot


a = 2021
# binary
print(f"{a:b}")
# hexadecimal
print(f"{a:x}")
# octal
print(f"{a:o}")
# scientific
print(f"{a:e}")

#> alligen to the right
#< alligen to the left
#^ middle
