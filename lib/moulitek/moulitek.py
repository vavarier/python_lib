from mt_exec import *
from mt_print import *
from mt_trace import *

test = Category("Salut", "Test qui dit bonjour")
seq = test.add_sequence("SLP^DLQSF", "éslp^ldsfsd")
seq.add_test("oskfoskf", "slqlwlsp")
seq.add_test("sfsd545sdfs", "sd3fsd432")
seq.set_status("sfsd545sdfs", True)
seq.test_exist()
seq.set_status("oskfoskf", False, reason=SEGFAULT, expected="Oui", got="Non")

gen_trace()
