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
    def sub(self, num1, num2):
        if num1 == 'ans' or num2 == 'ans':
            self.sub(self.ans,num2) if num1 =="ans" and num2 != "ans" else self.sub(num1,self.ans)
        else:
            num1 = self._check_number(num1)
            num2 = self._check_number(num2)
            self.ans = num1 - num2
        return(self.ans)
    def div(self, num1, num2):
        if num1 == 'ans' or num2 == 'ans':
            self.div(self.ans,num2) if num1 =="ans" and num2 != "ans" else self.div(num1,self.ans)
        else:
            num1 = self._check_number(num1)
            num2 = self._check_number(num2)
            self.ans = num1 / num2
        return(self.ans)
    def mul(self, num1, num2):
        if num1 == 'ans' or num2 == 'ans':
            self.mul(self.ans,num2) if num1 =="ans" and num2 != "ans" else self.mul(num1,self.ans)
        else:
            num1 = self._check_number(num1)
            num2 = self._check_number(num2)
            self.ans = num1 * num2
        return(self.ans)
if __name__ == "__main__":
    Cal = Mycalc()
    STR = ""
    while STR != "quit":
        STR = input("Enter you calculation :\n")
        if "+" in STR:
            nums = STR.split("+")
            r = Cal.add(nums[0].strip(),nums[1].strip())
            print(r)
        elif "-" in STR:
            nums = STR.split("-")
            r = Cal.sub(nums[0].strip(),nums[1].strip())
            print(r)
        elif "/" in STR:
            nums = STR.split("/")
            r = Cal.div(nums[0].strip(),nums[1].strip())
            print(r)
        elif "*" in STR:
            nums = STR.split("*")
            r = Cal.mul(nums[0].strip(),nums[1].strip())
            print(r)
    print("HAVE A NICE DAY!!")
    
Cal = Mycalc()
@pytest.mark.parametrize("num1,num2,z",[("ans",2,2),(10,"ans",12),(10,-5,5)])
def test_method(num1,num2,z):
    assert z == Cal.add(num1,num2)