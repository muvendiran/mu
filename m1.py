ma = input("Please Enter Your Own Character : ")

if((ma >= 'a' and ma <= 'z') or (ma >= 'A' and ma <= 'Z')): 
    print("The Given Character ", ma, "is an Alphabet") 
elif(ch >= '0' and ch <= '9'):
    print("The Given Character ", ma, "is a Digit")
else:
    print("The Given Character ", ma, "is Not an Alphabet or a Digit")
