num_list=[]
user_name=input("Enter your name:")
print()
for i in range(1,4):
    num=int(input(f"Enter your {i} favorite number:"))
    num_list.append(num)

print(f"\nHello,{user_name}!let's explore your favorite number:")
for num in num_list:
    if num % 2 == 0:
        print(f"The number {num} is even.")
    else:
        print(f"The number {num} is odd.")
print()
for num in num_list:
    print(f"The number {num} and its square:({num},{num ** 2})")
sum_numbers=sum(num_list)
print(f"\nAmazing! The sum of your favorite numbers is: {sum_numbers}")
if sum_numbers == 0 or sum_numbers == 1:
    print(num, "is not a prime number")
elif sum_numbers > 1:
    for i in range(2, sum_numbers):
        if (num % i) == 0:
            prime = True
    if prime:=True:
        print(f"Alas! {sum_numbers}, is not a prime number")
    else:
        print(f"Wow! {sum_numbers}, is a prime number")