department_heads = ['Admin', 'Marketing', 'Accounting', 'Human Resources', 'Legal']

for department_head in department_heads:
    if department_head == 'Admin':
        print("Hello Systems Administrator, would you like to see the Status Report since your previous Login?")
    else:
        print(f"Welcome! {department_head} Department Lead, Let's have a Great day!")