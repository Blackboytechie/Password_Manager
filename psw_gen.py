import random


class PasswordGenerator:
    def __init__(self):
        self.d_chr = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                      "T","U", "V", "W", "X", "Y", "Z"]
        self.d_sys = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_"]
        self.d_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.d_list = []

    def generate(self):
        password = ""
        pass_list = []
        self.d_list = [pass_list.append(random.choice(self.d_chr)) for x in range(0, 4)]
        self.d_list = [pass_list.append(random.choice(self.d_sys)) for x in range(0, 4)]
        self.d_list = [pass_list.append(random.choice(self.d_num)) for x in range(0, 4)]
        random.shuffle(pass_list)
        # print(pass_list)
        for x in pass_list:
            password += x
        # print(f"the generated password is : {password}")
        return password

