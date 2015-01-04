from string import Template

def get_user_info():
        name = input('Name: ')
        age = input('Age: ')
        username = input('Reddit username: ')
        template = Template('your name is ${n}, you are ${a} years old, '
                'and your username is ${u}')
        output = template.substitute(n=name, a=age, u=username)
        print(output)

if __name__ == "__main__":
        get_user_info()
