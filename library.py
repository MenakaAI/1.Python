class Multiplerequest():
    def EvenOdd():
        num=int(input("Enter the num:"))
        if((num%2)==1):
            print ("Odd number")
            Message ="Odd number"
        else:
            print ("Even number")
            Message="Even number"
            return Message
        
        
    def BMI():
        Weight =int(input("Enter your Weight in kg :"))
        Height=int(input("Enter your Height in cm :"))
        BMI=Weight/(Height/100)**2
        if(BMI<18.5):
            print ("Underweight")
            Mes="Underweight"
        elif(BMI<24.9):
            print ("Normal")
            Mes="Normal"
        elif(BMI <39.9):
            print ("Overweight")

            Mes="Overweight"
        else:
            print("Obese")
            Mes="Obese"
        return Mes
        
    def addition(num1,num2):
        addition=num1+num2
        print (addition)
        
    def Subfields():
        flds = ["MachineLearning","NeutralNetwork","Vision","Robotics","SpeechProcessing","NLP"]
        for num in flds:
            print(num)
        return num
    
    def MarriageEligibility():
        Gender=input("Enter your Gender:")
        Age=int(input("Enter you age:"))
        if(Age>20):
            print("Eligible for male")
            txt=("Eligible for male")    
        elif(Age>17):
            print("Eligible for FeMale")
            txt=("Eligible for FeMale")
        else:
            print("Not Eligible for marraige")
            txt=("Not Eligible for marraige")
            
    def Percentage(sub1,sub2,sub3,sub4,sub5):
        tol=sub1+sub2+sub3+sub4+sub5
        print("Total :", tol)
        per=tol/5
        print("Percentage :", per)
        return per
 
    def triangle():
        H=int(input("Enter height:"))
        B=int(input("Enter breadth:"))
        Formula=(H*B)/2
        print("Area of Triangle",Formula)
        H1=int(input("Enter height:"))
        H2=int(input("Enter height:"))
        B2=int(input("Enter breadth:"))
        F1=H1+H2+B2
        print("Permiter of Traingle",F1)
   
