'''Create a Python program that simulates a library system with these features:
Store details of 3 books — each with:
title (string)
author (string)
price (float)
copies_available (int)
Print all book details in a neat format (like a catalog).
Simulate a borrow action:
Reduce the number of copies of one book by 1.
Print the updated catalog.
Simulate a return action:
Increase the number of copies of another book by 1.
Print the updated catalog again.
Finally, calculate the total value of all books in stock (price × copies for each book, then sum).'''

title_1=input("Enter the title of book:")
author_1=input("Enter the author name:")
price_1=float(input("Enter the price of book:"))
copies_available_1=int(input("Enter the copies available:"))

title_2=input("Enter the title of book:")
author_2=input("Enter the author name:")
price_2=float(input("Enter the price of book:"))
copies_available_2=int(input("Enter the copies available:"))

title_3=input("Enter the title of book:")
author_3=input("Enter the author name:")
price_3=float(input("Enter the price of book:"))
copies_available_3=int(input("Enter the copies available:"))

print(f"Title: {title_1}, Author name:{author_1}, Price: {price_1}, Copies available: {copies_available_1}")
print(f"Title: {title_2}, Author name:{author_2}, Price: {price_2}, Copies available: {copies_available_2}")
print(f"Title: {title_3}, Author name:{author_3}, Price: {price_3}, Copies available: {copies_available_3}")

copies_available_1=copies_available_1-1
copies_available_3=copies_available_3+1
print(f"Title: {title_1}, Author name:{author_1}, Price: {price_1}, Copies available: {copies_available_1}")
print(f"Title: {title_2}, Author name:{author_2}, Price: {price_2}, Copies available: {copies_available_2}")
print(f"Title: {title_3}, Author name:{author_3}, Price: {price_3}, Copies available: {copies_available_3}") 

stock_1=price_1*copies_available_1
stock_2=price_2*copies_available_2
stock_3=price_3*copies_available_3
Total_stock=stock_1+stock_2+stock_3
print(f"Total stocks of books are: {Total_stock}")





