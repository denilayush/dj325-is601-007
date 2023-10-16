import pytest
# make sure there's an __init__.py in this test folder and that
# the test folder is in the same folder as the mini project content
from PumpkinMachine import PumpkinMachine
from PumpkinMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, OutOfStockException,InvalidPaymentException

@pytest.fixture
def machine():
    pm = PumpkinMachine()
    return pm


#10/15/23
#dj325
# Test 1 - pumpkin must be the first selection (can't add face stencils or extrass without a pumpkin choice)
def test_InvalideStageException(machine):
    # with pytest.raises(Exception):
    #     machine.handle_face_stencil_choice("Happy Face")
    with pytest.raises(InvalidStageException):
        machine.pick_face_stencil("Happy Face")

#10/15/23
#dj325
# Test 2 - can only add face stencils if they're in stock
def test_face_stencils_are_added_when_in_stock(machine):
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.face_stencils[0].quantity = 0
    with pytest.raises(OutOfStockException):
        machine.pick_face_stencil("Happy Face")


# Test 3 - can only add extras if they're in stock
#10/15/23
#dj325
def test_extras_are_added_when_in_stock(machine):
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("next")
    machine.extras[1].quantity = 0
    with pytest.raises(OutOfStockException):
        machine.pick_extras("LED Candle")

#10/15/23
#dj325
# Test 4 - Can add up to 3 face stencils of any combination
def test_add_upto_3_face_stencils(machine):
    machine.handle_pumpkin_choice("large pumpkin")
    machine.handle_face_stencil_choice("Toothy Face")
    machine.handle_face_stencil_choice("spooky face")
    machine.handle_face_stencil_choice("Scream Face")
    with pytest.raises(ExceededRemainingChoicesException):
        machine.handle_face_stencil_choice("Scream Face")

#10/15/23
#dj325
# Test 5 - Can add up to 3 extras of any combination
def test_add_upto_3_face_extras(machine):
    machine.handle_pumpkin_choice("large pumpkin")
    machine.handle_face_stencil_choice("Toothy Face")
    machine.handle_face_stencil_choice("spooky face")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("Paint Kit")
    machine.handle_extra_choice("Googly Eyes")
    machine.handle_extra_choice("Dry Ice")
    with pytest.raises(ExceededRemainingChoicesException):
        machine.handle_extra_choice("Sticker Pack")

#10/15/23
#dj325
# Test 6 - cost must be calculated properly based on the choices (check for currency format as part of this) (test case should have a few permutations of at least 3 valid pumpkins [hint parameterized tests])
@pytest.mark.parametrize("pumpkin,face,extras,cost,wrong_total,total",[("large pumpkin","Toothy Face", "Paint Kit", "7.00","6.00","7.00" ),
                                                    ("Medium Pumpkin","Spooky Face", "Glitter", "3.75", "3.25" , "3.75" ),
                                                    ("small pumpkin","Toothy Face", "Dry Ice", "3.25", "3.50", "3.25" ),
                                                    ("large pumpkin","Toothy Face", "Paint Kit", "7.00", "7.25", "7.00" )])
def test_cost_calculation(machine,pumpkin,face,extras,cost,wrong_total,total):
    machine.handle_pumpkin_choice(pumpkin)
    machine.handle_face_stencil_choice(face)
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice(extras)
    machine.handle_extra_choice("done")
    with pytest.raises(InvalidPaymentException):
        machine.handle_pay(cost,wrong_total)
    try:
        machine.handle_pay(cost,total)
    except InvalidPaymentException:
        pytest.fail("InvalidPaymentException should not have been raised.")


#10/15/23
#dj325
#Test 7 - Total Sales (sum of costs) must be calculated properly (test case should have a few permutations of at least 3 valid pumpkins [hint parameterized tests])
pumpkin_machine = PumpkinMachine()

@pytest.mark.parametrize("pumpkin,face,extras,cost,total, total_sales",[("large pumpkin","Toothy Face", "Paint Kit", "7.00","7.00",7 ),
                                                    ("Medium Pumpkin","Spooky Face", "Glitter", "3.75", "3.75", 10.75 ),
                                                    ("small pumpkin","Toothy Face", "Dry Ice", "3.25",  "3.25", 14 ),
                                                    ("large pumpkin","Toothy Face", "Paint Kit", "7.00",  "7.00", 21 )])
def test_total_sales(pumpkin,face,extras,cost,total,total_sales):
    pumpkin_machine.handle_pumpkin_choice(pumpkin)
    pumpkin_machine.handle_face_stencil_choice(face)
    pumpkin_machine.handle_face_stencil_choice("next")
    pumpkin_machine.handle_extra_choice(extras)
    pumpkin_machine.handle_extra_choice("done")
    pumpkin_machine.handle_pay(cost,total)
    assert total_sales == pumpkin_machine.total_sales

#10/15/23
#dj325
#Test 8 - Total products variable should properly increment for each purchase
pumpkin_machine_new = PumpkinMachine()

@pytest.mark.parametrize("pumpkin,face,extras,cost,total,face_stencil_remaining,extras_remaining",[
                                                    ("Mini Pumpkin","Scream Face", "Small Candle", "2.25","2.25",7,9),
                                                    ("Mini Pumpkin","Scream Face", "Small Candle", "2.25","2.25",5,8),
                                                    ("Mini Pumpkin","Scream Face", "Small Candle", "2.25","2.25",3,7)])
def test_variable_should_increment(pumpkin,face,extras,cost,total,face_stencil_remaining,extras_remaining):
    pumpkin_machine_new.handle_pumpkin_choice(pumpkin)
    pumpkin_machine_new.handle_face_stencil_choice(face)
    pumpkin_machine_new.handle_face_stencil_choice(face)
    pumpkin_machine_new.handle_face_stencil_choice("next")
    pumpkin_machine_new.handle_extra_choice(extras)
    pumpkin_machine_new.handle_extra_choice("done")
    pumpkin_machine_new.handle_pay(cost,total)
    assert face_stencil_remaining  == pumpkin_machine_new.face_stencils[1].quantity
    assert extras_remaining  == pumpkin_machine_new.extras[0].quantity