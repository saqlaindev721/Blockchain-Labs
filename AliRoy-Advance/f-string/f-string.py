letter = "hey my name is {1} and im form {0}"
country = "pakistan"
name = "ali"

print(letter.format(country, name))
print(f"Hey my name is {name} and I am from {country}")

txt = "for only {price: 2f} dollars!"
print(txt.format(price = 4004.44))