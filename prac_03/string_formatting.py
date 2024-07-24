year = 1922
brand = "Gibson"
model = "L-5"
price = 16036

output = f"{year} {brand.lower()} {model.replace('-', '_')} for about ${price:,}!"
print(output)



# Using a for loop to print the powers of 2
for i in range(11):
    power_of_two = 2 ** i
    print(f"2^{i:2} is {power_of_two:5}")

