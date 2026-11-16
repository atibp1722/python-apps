import webbrowser
from fpdf import FPDF
import os

# class for bill
class Bill:
    # bill properties
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

# class for each friend along with their share of final amount to pay
class Friend:
    # friend properties
    def __init__(self, name, days_stayed):
        self.name = name
        self.days_stayed = days_stayed
    # how much each friend has to pay based on days stayed
    def pay_bill(self, bill, friend2):
        total_days = self.days_stayed + friend2.days_stayed
        if total_days == 0:
            return 0.0
        # friend portion of total days stayed
        coef = self.days_stayed / total_days
        # share based on portion
        amount_to_pay = bill.amount * coef
        return (round(amount_to_pay, 2))

# class for pdf report
class Rent_Report:
    # file information
    def __init__(self, file_name):
        self.file_name = file_name
    # build pdf report and open in browser
    def generate_report(self, friend1, friend2, bill):
        os.makedirs(os.path.dirname(self.file_name), exist_ok=True)
        # initialie fpdf object
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        # add icon if it exists
        if os.path.exists('rent-calc/house.png'):
            pdf.image('rent-calc/house.png', w=50, h=50)
        # font to be used
        pdf.set_font(family='times', size=20)
        pdf.cell(w=0, h=50, text='RENT REPORT', border=0, align='C', ln=1)
        # stay period and bill labels
        pdf.cell(w=100, h=50, text='Stay Period:', border=0)
        pdf.cell(w=175, h=50, text=bill.period, border=0, ln=1)
        # friend1's name and share to pdf
        pdf.cell(w=100, h=50, text=friend1.name+"'s share", border=0)
        pdf.cell(w=175, h=50, text=str(friend1.pay_bill(bill, friend2)), border=0, ln=1)
        # friend2's name and share to pdf
        pdf.cell(w=100, h=50, text=friend2.name+"'s share", border=0)
        pdf.cell(w=175, h=50, text=str(friend2.pay_bill(bill,friend1)), border=0, ln=1)
        # save pdf file
        pdf.output(self.file_name)
        # open pdf in browser
        webbrowser.open('file://'+os.path.realpath(self.file_name))

# prompt user for amount and time
amount = float(input('Enter rent amount: '))
period = input('Enter time period: ')
# prompt for friend1's info
f1 = input('Enter friend name: ')
days_stayed_1 = int(input(f'Enter no. of days {f1} stayed: '))
# prompt for friend2's info
f2 = input('Enter friend name: ')
days_stayed_2 = int(input(f'Enter no. of days {f2} stayed: '))
# instantitate objects
test = Bill(amount=amount, period=period)
frnd1 = Friend(name=f1, days_stayed=days_stayed_1)
frnd2 = Friend(name=f2, days_stayed=days_stayed_2)
print()
# show results in console terminal
print("Total amount due:", test.amount)
print(f"{f1}'s share: ", frnd1.pay_bill(bill=test, friend2=frnd2))
print(f"{f2}'s share: ", frnd2.pay_bill(bill=test, friend2=frnd1))
# cleaned file name 
safe = period.replace(" ", "_").replace("/", "-")
pdf_rep = Rent_Report(file_name=f'rent-calc/{safe}.pdf')
pdf_rep.generate_report(friend1=frnd1, friend2=frnd2, bill=test)