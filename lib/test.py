from pickle import FALSE
from moulitek.moulitek import *
init_moulitek()
cat1 = Category("Basic tests", "Simple tests to begin")
seq = cat1.add_sequence("Loop on basic files")
seq.add_test("First test")
seq.add_test("Second test")
seq.add_test("Third test")
seq.add_test("Last test")
seq.set_status("First test", True)
seq.set_status("Second test", False, SEGFAULT, expected="0", got="139")
seq.set_status("Third test", False, BADOUTPUT, expected="OK", got="KO")
seq.set_status("Last test", True)
gen_trace()