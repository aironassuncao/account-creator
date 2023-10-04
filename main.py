import PySimpleGUI as sg
import random


class ScreenDisplay:
    sg.theme('DarkBlue4')

    def __init__(self):
        layout = [
            [sg.Text('Name', size=(10, 0)), sg.Input(size=(37, 0), key='name')],
            [sg.Text('Age', size=(10, 0)), sg.Input(size=(37, 0), key='age')],
            [sg.Text('Gender', size=(10, 0)), sg.Checkbox('Male', key='male'), sg.Checkbox('Female', key='female'),
             sg.Checkbox('Non-Binary', key='nonbinary')],
            [sg.Text('Job', size=(10, 0)), sg.Input(size=(37, 0), key='job')],
            [sg.Text('Monthly Income', size=(10, 0)), sg.Input(size=(37, 0), key='income')],
            [sg.Text('Email', size=(10, 0)), sg.Input(size=(37, 0), key='email')],
            [sg.Button('Send')],
            [sg.Output(size=(57, 20))]

        ]

        self.window = sg.Window('Data Collect').layout(layout)

    def main(self):
        while True:
            with open('Data_Generated.txt', 'a') as outputfile:

                self.button, self.values = self.window.Read()
                name = self.values['name']
                age = self.values['age']
                male = self.values['male']
                female = self.values['female']
                job = self.values['job']
                income = self.values['income']
                email = self.values['email']
                nonbinary = self.values['nonbinary']

                print(f'Name: {name}', file=outputfile)
                print(f'Age: {age}', file=outputfile)

                if male is True:
                    print('Gender: Male', file=outputfile)

                if female is True:
                    print('Gender: Female', file=outputfile)

                if nonbinary is True:
                    print('Gender: Non-Binary', file=outputfile)

                print(f'Job: {job}', file=outputfile)
                print(f'Income: {income}', file=outputfile)
                print(f'Email: {email}', file=outputfile)
                print(' --------------------------------------')
                print(f'User account for {name} created.')
                print(" ")
                print(f'ID Number : {random.randrange(10000, 99999)}-{random.randint(1, 99)}', file=outputfile)
                print(f'Password: {random.randint(0000, 9999)} ', file=outputfile)
                print(" ", file=outputfile)

            print(f'Name: {name}')
            print(f'Age: {age}')

            if male is True:
                print('Gender: Male')

            if female is True:
                print('Gender: Female')

            if nonbinary is True:
                print('Gender: Non-Binary')

            print(f'Job: {job}')
            print(f'Income: {income}')
            print(f'Email: {email}')
            print(' --------------------------------------')
            print(" ")


tela = ScreenDisplay()
tela.main()

if __name__ == '__main__':
    tela = ScreenDisplay()
    tela.main()
