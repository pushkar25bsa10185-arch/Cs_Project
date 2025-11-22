# Simple Insurance Policy CRUD Manager with hardcoded dataset

policies = [
    {
        "policy_number": "P1001",
        "holder_name": "Alice Johnson",
        "policy_type": "Health",
        "premium_amount": "5000"
    },
    {
        "policy_number": "P1002",
        "holder_name": "Bob Smith",
        "policy_type": "Life",
        "premium_amount": "7000"
    },
    {
        "policy_number": "P1003",
        "holder_name": "Carlos Davis",
        "policy_type": "Vehicle",
        "premium_amount": "3000"
    }
]

def add_policy():
    policy_number = input("Enter Policy Number: ")
    holder_name = input("Enter Policy Holder Name: ")
    policy_type = input("Enter Policy Type (Health/Life/Vehicle etc.): ")
    premium_amount = input("Enter Premium Amount: ")
    policy = {
        "policy_number": policy_number,
        "holder_name": holder_name,
        "policy_type": policy_type,
        "premium_amount": premium_amount
    }
    policies.append(policy)
    print("Policy added successfully.\n")

def view_policies():
    if not policies:
        print("No policies available.\n")
        return
    print("List of Insurance Policies:")
    for i, policy in enumerate(policies, 1):
        print(f"{i}. Policy Number: {policy['policy_number']}, Holder: {policy['holder_name']}, Type: {policy['policy_type']}, Premium: {policy['premium_amount']}")
    print()

def update_policy():
    policy_num = input("Enter the Policy Number to update: ")
    for policy in policies:
        if policy['policy_number'] == policy_num:
            print("Enter new details (leave blank to keep current value):")
            new_holder = input(f"Current Holder Name ({policy['holder_name']}): ")
            new_type = input(f"Current Policy Type ({policy['policy_type']}): ")
            new_premium = input(f"Current Premium Amount ({policy['premium_amount']}): ")
            
            if new_holder:
                policy['holder_name'] = new_holder
            if new_type:
                policy['policy_type'] = new_type
            if new_premium:
                policy['premium_amount'] = new_premium
            print("Policy updated successfully.\n")
            return
    print("Policy not found.\n")

def delete_policy():
    policy_num = input("Enter the Policy Number to delete: ")
    for i, policy in enumerate(policies):
        if policy['policy_number'] == policy_num:
            policies.pop(i)
            print("Policy deleted successfully.\n")
            return
    print("Policy not found.\n")

def main_menu():
    while True:
        print("Insurance Policy CRUD Manager")
        print("1. Add Policy")
        print("2. View Policies")
        print("3. Update Policy")
        print("4. Delete Policy")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_policy()
        elif choice == '2':
            view_policies()
        elif choice == '3':
            update_policy()
        elif choice == '4':
            delete_policy()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main_menu()
