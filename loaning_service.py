from datetime import datetime
from datetime import timedelta

class lender:   
    def __init__ (self,name=0,int_per_annum=0):
        #adding lender details
        self.name=name
        self.int_per_annum=int_per_annum

    def set_data(self,name,int_per_annum):
        #setting details
        self.name=name
        self.int_per_annum=int_per_annum
    
    def details(self):
        #printing details
        print("Name of Lender is {}".format(self.name));
        print("Interest is {}%  per annum ".format(self.int_per_annum));
    
class borrower(lender):
    def __init__(self,name=0,principal_amt=0,date_of_loan=0,duration_of_loan=0):
        #adding lender details
        self.name=name
        self.principal_amt=principal_amt
        self.date_of_loan=date_of_loan
        self.duration_of_loan=duration_of_loan    
    def set_data(self,name,principal_amt,begin_date_of_loan,duration_of_loan):
        #setting details
        self.name=name
        self.principal_amt=principal_amt
        self.begin_date_of_loan=begin_date_of_loan
        self.duration_of_loan=duration_of_loan
        
    def details(self):
        #print details
        print("Name of Borrower is {}".format(self.name));
        print("Principal Amount is {}".format(self.principal_amt));
        print("begin_date_of_loan is {}".format(self.begin_date_of_loan));
        print("duration_of_loan is {} days".format(self.duration_of_loan));
      
i=1
nl=1
nb=1
while(i==1):
    #making object of the classes
    x="X"+str(nl)
    y="Y"+str(nb)
    
    locals()[x]=lender()
    locals()[y]=borrower()

    #taking input from user
    l_a=input("Enter lender name: ")
    inter=int(input("Enter int_per_annum: "))
    locals()[x].set_data(l_a,inter)

    b_n=input("Enter borrower name: ")
    p_a=int(input("Enter principal_amt: "))
    begindate=input("Enter date of loan:(in YYYY-MM-DD) ")
    print("Enter duration_of_loan: ")
    Y=int(input("Total Number of years: "))
    M=int(input("Total Number of months: "))
    D=int(input("Total Number of days: "))
    Begindate = datetime.strptime(begindate, "%Y-%m-%d")
    D=D+M*30+Y*365
    locals()[y].set_data(b_n,p_a,begindate,D)

    #date of repayment calculation
    Enddate = Begindate + timedelta(days=D)

    #amount to repay calculation
    dur_in_yrs=D/365
    Amt_to_pay=p_a*(pow((1+inter/100),dur_in_yrs))

    k=int(input("\n\nTo get details of loan press 1 else 0"))
    
    #printing details of the loan
    if(k==1):
        print("\n\n\n\n   Details for the transaction\n\n")
        print("Serial number of lender is ",x)
        
        locals()[x].details()
        print("Serial number of borrower is ",y)
        locals()[y].details()
        print("The last date for loan repayment is :", Enddate)
        print("The amount to repay to lender is ",Amt_to_pay)
        

    i=int(input("\n\n\n\nfor new entry press 1 else 0"))

        

    
    



