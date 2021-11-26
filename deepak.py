class decoration:

    def __init__(self,rt='',s=0,p=0,r=0,t=0,a=1800,name='',address='',cindate='',coutdate='',):

        print ("\n\n*****WELCOME TO DEEPAK TENT*****\n")

        self.rt=rt

        self.r=r

        self.t=t

        self.p=p

        self.s=s
        self.a=a
        self.name=name
        self.address=address
        self.cindate=cindate
        self.coutdate=coutdate

    def inputdata(self):
        self.name=input("\nEnter your name:")
        self.address=input("\nEnter your address:")
        self.cindate=input("\nEnter your Function  date:")
        self.coutdate=input("\nEnter your Function end date")
        
        
    def stagerent(self):

        print ("We have the following stages price for you:-")

        print ("1.  Stage with Orignal flowers---->rs 6000 PD\-")

        print ("2.  Stage with duplicate Flower---->rs 5000 PD\-")

        print ("3.  medium Decoration---->rs 4000 PD\-")

        print ("4.  low class decoration---->rs 3000 PD\-")

        x=int(input("Enter Your Choice Please->"))

        d=int(input("For How Many Days Did You :"))

        if(x==1):

            print ("you have Stage with Orignal flowers")

            self.s=6000*d

        elif (x==2):

            print ("you have Stage with Orignal flowers")

            self.s=5000*d

        elif (x==3):

            print ("you have Medium decoration")

            self.s=4000*d

        elif (x==4):
            print ("you have low decoration")

            self.s=3000*d

        else:

            print ("please choose a decoration type")

        print ("your stage decoration rent is =",self.s,"\n")

    def otherthingbill(self):

        print("*****What you have*****")

        print("1.buffet table-->Rs20","2.chair-->Rs10","3.sofas-->Rs90","4.stachu-->Rs110","5.multicolour light-->Rs150","6.Exit")


        while (1):

            c=int(input("Enter your choice:"))


            if (c==1):
                d=int(input("Enter the quantity:"))
                self.r=self.r+20*d

            elif (c==2):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+10*d

            elif (c==3):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+90*d

            elif (c==4):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+110*d

            elif (c==5):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+150*d

            elif (c==6):
                break;
            else:
                print("Invalid option")

        print ("Total food Cost=Rs",self.r,"\n")

    def	utensilsbill(self):
        print ("******utensils list*******")

        print ("1.steelbowl-->Rs3","2.big vessal-->Rs400","3.medium vessal-->Rs300","4.small vessal-->Rs200","5.kadhai->Rs500","6.Exit")

        while (1):
            #brought to you by code-projects.org

            e=int(input("Enter your choice:"))

            if (e==1):
                f=int(input("Enter the quantity:"))
                self.t=self.t+3*f

            elif (e==2):
                f=int(input("Enter the quantity:"))
                self.t=self.t+400*f

            elif (e==3):
                f=int(input("Enter the quantity:"))
                self.t=self.t+300*f

            elif (e==4):
                f=int(input("Enter the quantity:"))
                self.t=self.t+200*f

            elif (e==5):
                f=int(input("Enter the quantity:"))
                self.t=self.t+500*f
            elif (e==6):
                break;
            else:

                print ("Invalid option")


        print ("Total utensils bill=Rs",self.t,"\n")

    

    def display(self):
        print ("******Decoration BILL******")
        print ("Customer details:")
        print ("Customer name:",self.name)
        print ("Customer address:",self.address)
        print ("Check in date:",self.cindate)
        print ("Check out date",self.coutdate)
        print ("Your stage rent is:",self.s)
        print ("Your Other things bill is:",self.r)
        print ("Your utensils bill is:",self.t)

        self.rt=self.s+self.t+self.p+self.r

        print ("Your sub total bill is:",self.rt)
        print ("Additional Service Charges is",self.a)
        print ("Your grandtotal bill is:",self.rt+self.a,"\n")
        

            

        

        

def main():

    a=decoration()
    

    while (1):
        print("1.Enter Customer Data")
        
        print("2.Calculate stagerent")

        print("3.Calculate otherthing bill")

        print("4.Calculate utensils bill")

        print("5.Show total cost")

        print("6.EXIT")

        b=int(input("\nEnter your choice:"))
        if (b==1):
            a.inputdata()

        if (b==2):

            a.stagerent()

        if (b==3):

            a.otherthingbill()

        if (b==4):

            a.utensilsbill()


        if (b==5):

            a.display()

        if (b==6):

            quit()



main()

