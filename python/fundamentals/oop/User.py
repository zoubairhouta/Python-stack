class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Email:", self.email)
        print("Age:", self.age)
        print("Rewards Member:", self.is_rewards_member)
        print("Gold Card Points:", self.gold_card_points)

    def enroll(self):
        if self.is_rewards_member:
            print(f"{self.first_name} is already a rewards member.")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200

    def spend_points(self, points):
        if self.is_rewards_member:
            if points <= self.gold_card_points:
                self.gold_card_points -= points
                print(f"{points} points spent.")
            else:
                print(" Unable to spend.")
        else:
            print("User is not a rewards member. Unable to spend points.")


samir = User("Samir", "Kahla", "samir@example.com", 59)
samir.enroll()
samir.display_info()

mounira = User("Mounira", "Jben", "mounira@example.com", 25)
mounira.enroll()
mounira.spend_points(80)
mounira.display_info()

latifa = User("Latifa", "Hargma", "latifa@example.com", 76)
latifa.display_info()