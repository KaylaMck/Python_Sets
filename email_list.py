subscribers = set()
unsubscribers = set()

def add_email(email, set_name):
    if set_name == "subscribers":
        subscribers.add(email)
    elif set_name == "unsubscribers":
        unsubscribers.add(email)

    print(f"Email '{email}' added to {'subscribers' if set_name == subscribers else 'unsubscribers'}.")


def remove_email(email, set_name):
    if set_name == "subscribers":
        if email in subscribers:
            subscribers.remove(email)
            print(f"{email} removed from {set_name}")
        else:
            print(f"{email} not found in {set_name}")

    elif set_name == "unsubscribers":
        if email in unsubscribers:
            unsubscribers.remove(email)
            print(f"{email} removed from {set_name}")
        else:
            print(f"{email} not found in {set_name}")

def display_emails(set_name):
    if set_name == "subscribers":
        for subscriber in subscribers:
            print(subscriber)
    
    elif set_name == "unsubscribers":
        for unsubscriber in unsubscribers:
            print(unsubscriber)


def find_active_subscribers():
    return subscribers.difference(unsubscribers)


add_email("user1@example.com", "subscribers")
add_email("user3@example.com", "subscribers")
add_email("user4@example.com", "subscribers")
add_email("user11@example.com", "subscribers")
add_email("user5@example.com", "subscribers")
add_email("user6@example.com", "subscribers")
add_email("user2@example.com", "subscribers")
add_email("user5@example.com", "subscribers")
add_email("user2@example.com", "subscribers")
add_email("user7@example.com", "subscribers")
add_email("user8@example.com", "subscribers")
add_email("user9@example.com", "subscribers")
add_email("user2@example.com", "subscribers")
add_email("user11@example.com", "subscribers")
add_email("user7@example.com", "subscribers")
add_email("user10@example.com", "subscribers")
add_email("user12@example.com", "subscribers")
add_email("user6@example.com", "unsubscribers")
add_email("user8@example.com", "unsubscribers")
add_email("user1@example.com", "unsubscribers")
add_email("user10@example.com", "unsubscribers")

print("All Subscribers:")
display_emails("subscribers")

print("All Unsubscribers:")
display_emails("unsubscribers")

print("Active Subscribers")
print(find_active_subscribers())