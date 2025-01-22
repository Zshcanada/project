class User:
    def _init_(self, username, password):
        self.username = username
        self.password = password
        self.logged_in = False

    def login(self, entered_password):
        if entered_password == self.password:
            self.logged_in = True
            print(f"Welcome, {self.username}!")
        else:
            print("Incorrect password. Please try again.")

    def logout(self):
        self.logged_in = False
        print(f"Goodbye, {self.username}!")

# Example usage:
user1 = User("example_user", "password123")
user1.login("password123")
user1.logout()
