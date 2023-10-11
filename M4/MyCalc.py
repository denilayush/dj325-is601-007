# dj325 10/10/23
import pytest

class Mycalc:
    ans = 0
    def _check_float(self,num):
        try:
            num = float(num)
            return True
        except:
            return False
        
    def _check_int(self,num):
        try:
            num = int(num)
            return True
        except:
            return False
    
    def _check_number(self,num):
        if self._check_int(num):
            return int(num)
        elif self._check_float(num):
            return float(num)
        else:
            raise Exception("Not a number")
    def add(self, num1, num2):
        if num1 == 'ans' or num2 == 'ans':
            self.add(self.ans,num2) if num1 =="ans" and num2 != "ans" else self.add(num1,self.ans)
        else:
            num1 = self._check_number(num1)
            num2 = self._check_number(num2)
            self.ans = num1 + num2
        return self.ans
    """
    dj325 10/11/23
    add() function performs addition of two numbers. 
    If either num1 or num2 is 'ans,' it uses the stored answer. 
    It also updates the stored answer with the result of the addition and returns it. 
    If 'ans' is not a valid number, it raises an exception.
    """

    def sub(self, num1, num2):
        if num1 == 'ans' or num2 == 'ans':
            self.sub(self.ans,num2) if num1 =="ans" and num2 != "ans" else self.sub(num1,self.ans)
        else:
            num1 = self._check_number(num1)
            num2 = self._check_number(num2)
            self.ans = num1 - num2
        return(self.ans)
    """
    dj325 10/11/23
    sub() function subtracts two numbers, with the option to use the stored answer ('ans') for calculations.
    It updates 'ans' with the result and returns it. If 'ans' is not a valid number, it raises an exception.
    """

    def div(self, num1, num2):
        if num1 == 'ans' or num2 == 'ans':
            self.div(self.ans,num2) if num1 =="ans" and num2 != "ans" else self.div(num1,self.ans)
        else:
            num1 = self._check_number(num1)
            num2 = self._check_number(num2)
            if num2 == 0:
                print("Number cannot be divided by zero")
                return "Will be Using previous ans value which is " + str(self.ans)
            else:
                self.ans = num1 / num2
        return(self.ans)
    """
    dj325 10/11/23
    If either num1 or num2 is 'ans', it checks which one is 'ans and uses the stored answer accordingly for the division. 
    It also checks for division by zero.
    If neither num1 nor num2 is 'ans,' 
    it checks whether both num1 and num2 are valid numbers (integers or floats) using the _check_number() method.
    If both num1 and num2 are valid numbers, it calculates their division, stores the result in the 'ans' attribute, 
    and returns the result. If num2 is zero, it prints a message and uses the previous 'ans' value.
    """

    def mul(self, num1, num2):
        if num1 == 'ans' or num2 == 'ans':
            self.mul(self.ans,num2) if num1 =="ans" and num2 != "ans" else self.mul(num1,self.ans)
        else:
            num1 = self._check_number(num1)
            num2 = self._check_number(num2)
            self.ans = num1 * num2
        return(self.ans)
    """
    dj325 10/11/23
    If either num1 or num2 is 'ans', it checks which one is 'ans and uses the stored answer accordingly for the multiplication.
    If neither num1 nor num2 is 'ans,' it checks whether both num1 and num2 are valid numbers (integers or floats)
    using the _check_number() method.
    If both num1 and num2 are valid numbers, it calculates their multiplication, stores the result in the 'ans' attribute, 
    and returns the result.
    """
if __name__ == "__main__":
    Cal = Mycalc()
    STR = ""
    while STR != "quit":
        STR = input("Enter you calculation :\n")
        if "+" in STR:
            nums = STR.split("+")
            r = Cal.add(nums[0].strip(),nums[1].strip())
            print("Result : ",r)
        elif "-" in STR:
            nums = STR.split("-")
            r = Cal.sub(nums[0].strip(),nums[1].strip())
            print("Result : ",r)
        elif "/" in STR:
            nums = STR.split("/")
            r = Cal.div(nums[0].strip(),nums[1].strip())
            print("Result : ",r)
        elif "*" in STR:
            nums = STR.split("*")
            r = Cal.mul(nums[0].strip(),nums[1].strip())
            print("Result : ",r)
    print("HAVE A NICE DAY!!")
    
Cal = Mycalc()
"""
dj325 10/11/23
test_method function is designed to test an add method of a class or module called Cal. Each test case is defined as a tuple with num1 and num2 as input arguments and z as the expected output. The @pytest.mark.parametrize decorator generates multiple test cases based on the provided parameters."""
@pytest.mark.parametrize("num1,num2,z",[(2,2,4),(1000,1,1001),(100,-5,95),(1003,-1003,0)])
def test_method(num1,num2,z):
    assert z == Cal.add(num1,num2)


"""
dj325 10/11/23
this test includes ans + num test cases, and z is variable to check it with the functions output to original expected output
"""
@pytest.mark.parametrize("num1,num2,z",[("ans",2,2),("ans",10002,10004),("ans",-4,10000),("ans",-10000,0)])
def test_method2(num1,num2,z):
    assert z == Cal.add(num1,num2)

"""
dj325 10/11/23
this test includes num subtact num test cases, and z is variable to check it with the functions output to original expected output
"""
@pytest.mark.parametrize("num1,num2,z",[(2,2,0),(100,50,50),(-50,4,-54),(100100,100,100000)])
def test_method3(num1,num2,z):
    assert z == Cal.sub(num1,num2)

"""
dj325 10/11/23
this test includes ans subtact num test cases, and z is variable to check it with the functions output to original expected output
it will use ans of previous function test which is 100000
"""
@pytest.mark.parametrize("num1,num2,z",[("ans",100002,-2),("ans",50,-52),("ans",-104,52),("ans",20,32)])
def test_method4(num1,num2,z):
    assert z == Cal.sub(num1,num2)

"""
dj325 10/11/23
this test includes number-mult-number test cases, and z is variable to check it with the functions output to original expected output
it will use ans check all the parameters for the mul function
"""
@pytest.mark.parametrize("num1,num2,z",[(1,1,1),(2,2,4),(98,98,9604),(9604,-65,-624260)])
def test_method5(num1,num2,z):
    assert z == Cal.mul(num1,num2)

"""
dj325 10/11/23
this test includes number-mult-number test cases, and z is variable to check it with the functions output to original expected output
it will use ans of previous function's output which is -624260
"""
@pytest.mark.parametrize("num1,num2,z",[("ans",-1,624260),("ans",2,1248520),("ans",5,6242600),("ans",5,31213000)])
def test_method6(num1,num2,z):
    assert z == Cal.mul(num1,num2)

"""
dj325 10/11/23
this test includes number-div-number test cases, and z is variable to check it with the functions output to original expected output
"""
@pytest.mark.parametrize("num1,num2,z",[(1,1,1),(22,11,2),(98000,98,1000),(-600,-2,300)])
def test_method7(num1,num2,z):
    assert z == Cal.div(num1,num2)

"""
dj325 10/11/23
this test includes number-div-number test cases, and z is variable to check it with the functions output to original expected output
It will use last task's ans which is 300
"""
@pytest.mark.parametrize("num1,num2,z",[("ans",2,150),("ans",1,150),("ans",-2,-75),("ans",-75,1)])
def test_method8(num1,num2,z):
    assert z == Cal.div(num1,num2)