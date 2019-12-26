import sqlite3


class SignInAuthenticator:
    def __init__(self):
        self.db = sqlite3.connect('data.db')
        self.cur = self.db.cursor()

    def main(self):
        self.choice('Do you want to sign up(Y/N): ')
        self.login()

    def choice(self, prompt):
        ans = input(prompt)
        if ans.lower() == 'n':
            pass
        elif ans.lower() == 'y':
            self.signup()

        else:
            self.choice(prompt)

    def signup(self):
        print('Sign Up')
        email = input('email: ')
        password = input('password: ')

        self.cur.execute(f"INSERT INTO users(email,password)  VALUES('{email}', '{password}') ")
        self.db.commit()
        print('now u can login')
        self.login()

    def login(self):
        limit = 0
        while limit < 5:
            limit += 1
            print('Write ur email and password')
            email = input('email: ')
            password = input('pass: ')
            self.cur.execute(f"SELECT * FROM users WHERE email='{email}' AND password='{password}'")
            if self.cur.fetchone() is not None:
                print(f'WELCOME ur now logged in!')
                exit()
            else:
                print('Invalid username or password')


SignInAuthenticator().main()
