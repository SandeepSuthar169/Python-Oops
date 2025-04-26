class Chartbook:
    __user_id = 1

    def __init__(self):
        self.id = Chartbook.__user_id
        Chartbook.__user_id += 1
        self.__name = " defualt user"
        self.username = " "
        self.pssword = " "
        self.loggedin = False
        # self.menu()

    @staticmethod
    def get_id():
        return Chartbook.__user_id

    @staticmethod 
    def set_id(val):
        Chartbook.__user_id = val       



    def get_name(self):
        return self.__name
    

    def set_name(self, values):
        self.__name = values
       



    def menu(self):
        user_input = input('''Wlecode to my chartbook
                        1. Press 1 to signup 
                        2. Press 2 to signin
                        3. Press 3 to write a post
                        4. Press 4 to message a friend
                        5. Press any other kwy to exit''')   
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.send_msg()
        else:
            exit()

    def signup(self):
        email = input("Enter your email here :->>") 
        pwd = input("setup your passwored here :->>") 
        self.username = email
        self.password = pwd
        print("You have siged up successfully !")
        print("\n")
        self.menu()
    
    def signin(self):
        if self.username == "" and self.password == "":
            print("Plase signup first by pressing 1 in hte main menu")
        else:
            uname = input("Enter your email/username here :->>") 
            pwd = input("Enter your password here :->>") 
            if self.username == uname and self.password == pwd:
                print("you have signed in successfully okk") 
                self.loggedin = True
            else:
                print("plase input correct credentials...")
        print("\n")
        self.menu()    


    def my_post(self):
        if self.loggedin == True:
            txt = input("Enter your masseage here:->>") 
            print(f"Following content has been posted :->> {txt}")

        else:
            print("you need to signin forst to post sometging.....") 
        print("\n")
        self.menu()   

    

    def send_msg(self):
        if self.loggedin ==True:
            txt = input("enter your masage here ::->>") 
            friend = input("whon ot send the msg :->>")
            print(f"your massage has been send to {friend}") 
        else:
            print(print('you need to sigin first to post something..........'))
        print("\n") 
        self.menu()                                      


# obj = Chartbook()            