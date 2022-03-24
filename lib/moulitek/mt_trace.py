from mt_print import *

def success(name):
    print("[OK] " + name + " [/OK]")
    print("_____________________________________\n")

def category(name, description):
    print("[##] " + name + " [/##]\n")
    if (description != None):
        print("[desc]\n" + description + "\n[/desc]")
    print("_____________________________________\n")

def sequence(name, description):
    print("[#] " + name + " [/#]\n")
    if (description != None):
        print("[desc]\n" + description + "\n[/desc]")
    print("_____________________________________\n")

def error(name, flag, description, expected, got):
    if (flag == SEGFAULT):
        print("[KO] [segfault] " + name + " [/KO]\n")
    if (flag == TIMEOUT):
        print("[KO] [timeout] " + name + " [/KO]\n")
    if (flag == NEVER_RUN):
        return ;
    if (flag == RETVALUE):
        print("[KO] [retvalue] " + name + " [/KO]\n")
    if (flag == BADOUTPUT):
        print("[KO] [badoutput] " + name + " [/KO]\n")
    if (description != None):
        print("[desc]\n" + description + "\n[/desc]\n")
    print("[expected]\n" + expected + "\n[/expected]\n")
    print("[got]\n" + got + "\n[/got]\n")
    print("_____________________________________\n")


def gen_trace():
    for cat in moulitek_all_categories:
        category(cat.name, cat.desc)
        for seq in cat.sequences:
            sequence(seq.name, seq.desc)
            for test in seq.tests:
                if test["passed"]:
                    success(test["name"])
                else:
                    error(test["name"], test["reason"], test["desc"], test["expected"], test["got"])