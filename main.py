

try:
    age = 10
    if age<18:
        raise ValueError("Not eligible for VOTE")
    else:
        print("Eligible for Vote")
        
except ZeroDivisionError as e:
    print("Exception Occured = > "+ str(e))

except ValueError as e:
    print("Exception occured")

except:
    print("Exception occured")

else:
    print("Program excecuted succesfully....")


finally:
    print("Harman Ltd")