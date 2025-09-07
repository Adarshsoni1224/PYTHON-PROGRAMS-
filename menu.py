next_choice=True
billing_amount=0
while next_choice:
	choice=int(input("Enter1 for Samosa\nEnter 2 for Tea\nEnter 3 for Coffee\nEnter 4 for Jalebi\nEnter 5 for kachori\nEnter 6 for pohe\nEnter a vaild choice:"))
	if choice == 1:
		quantity=int(input("Enter No of Samosa:"))
		price=10
		amount=quantity*price
	elif  choice==2:
		quantity=int(input("Enter No of Tea :"))
		price=5
		amount=quantity*price
	elif choice==3:
		quantity=int(input("Enter No of Coffee:"))
		price=50
		amount=quantity*price
	elif choice==4:
		quantity=int(input("Enter No of Jalebi:"))
		price=10
		amount=quantity*price
	elif choice==5:
		quantity=int(input("Enter No of kachori:"))
		price=15
		amount=quantity*price
	elif choice==6:
		quantity=int(input("Enter No for pohe:"))
		price=20
		amount=quantity*price
	else:
		print("invaild")
	billing_amount=billing_amount+amount
	next_choice=input("Enter Y to add other item or any a key to stop")
	if next_choice=="Y"or next_choice=="Y":
		next_choice==True
	else:
		next_choice==False

print("Bills Details")
print("Your Bill is {} inr".format(billing_amount))