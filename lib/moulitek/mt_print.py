SEGFAULT = 1
BADOUTPUT = 2
RETVALUE = 3
TIMEOUT = 4
NEVER_RUN = 5

moulitek_all_categories = []

class Sequence:
    def __init__(self, category, name, desc = None):
        self.name = name
        self.desc = desc
        self.category = category
        self.tests = []

    def test_exist(self, name):
        for i, test in enumerate(self.tests):
            if test["name"] == name:
                return i
        return -1

    def add_test(self, name, desc = None):
        if self.test_exist(name) != -1:
            return False
        test = {"name": name, "desc": desc, "passed": False, "reason": NEVER_RUN, "expected": None, "got": None}
        self.tests.append(test)
        return True

    def set_status(self, name, passed = True, reason = 0, expected = None, got = None):
        existing_test = self.test_exist(name)
        if existing_test == -1:
            return False
        if not passed and (reason == 0 or expected == None or got == None):
            return False
        self.tests[existing_test]["passed"] = passed
        self.tests[existing_test]["reason"] = reason
        self.tests[existing_test]["expected"] = expected
        self.tests[existing_test]["got"] = got
        return True

class Category:
    def __init__(self, name, desc = None):
        self.name = name
        self.desc = desc
        self.sequences = []
        moulitek_all_categories.append(self)

    def add_sequence(self, name, desc = None):
        sequence = Sequence(self, name, desc)
        self.sequences.append(sequence)
        return sequence
