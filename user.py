class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self

    def enroll(self):
        if self.is_rewards_member == True:
            print('Already a member')
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        if (self.gold_card_points - amount) > 0:
            self.gold_card_points -= amount
        else: 
            print('Not enough points')
        return self


user_john = User('John', 'Bosco', 'jbosco@gmail.com', 54)
user_john.display_info().enroll().spend_points(50).display_info().enroll()

user_emma = User('Emma', 'Woods', 'ewoods@yahoo.com', 38)
user_ephraim = User('Ephraim', 'Silver', 'esilver@aol.com', 43)

user_emma.enroll().spend_points(80).display_info()
user_ephraim.display_info().spend_points(40)