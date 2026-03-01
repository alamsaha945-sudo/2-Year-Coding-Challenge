# tip calculator
custmer=int(input("khota taka hoyeche bill?:  "))
tip=int(input("khoto taka tips dite chau:   "))
bill_peyment=int(input("khoto jon mile bill ta deben?:  "))
total_bill=custmer+tip
print(f"total bill hobe {total_bill}")
print(f"ekjon mile bill debe {total_bill}\{bill_peyment} hobe{total_bill/bill_peyment:.2f}")