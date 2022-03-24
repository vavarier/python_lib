from mt_print import *

moulitek_script_trace = ""

def success(name):
    global moulitek_script_trace
    moulitek_script_trace += "[OK] " + name + " [/OK]"
    moulitek_script_trace += "_____________________________________\n"

def category(name, description):
    global moulitek_script_trace
    moulitek_script_trace += "[##] " + name + " [/##]\n"
    if (description != None):
        moulitek_script_trace += "[desc]\n" + description + "\n[/desc]"
    moulitek_script_trace += "_____________________________________\n"

def sequence(name, description):
    global moulitek_script_trace
    moulitek_script_trace += "[#] " + name + " [/#]\n"
    if (description != None):
        moulitek_script_trace += "[desc]\n" + description + "\n[/desc]"
    moulitek_script_trace += "_____________________________________\n"

def error(name, flag, description, expected, got):
    global moulitek_script_trace
    if (flag == SEGFAULT):
        moulitek_script_trace += "[KO] [segfault] " + name + " [/KO]\n"
    if (flag == TIMEOUT):
        moulitek_script_trace += "[KO] [timeout] " + name + " [/KO]\n"
    if (flag == NEVER_RUN):
        return ;
    if (flag == RETVALUE):
        moulitek_script_trace += "[KO] [retvalue] " + name + " [/KO]\n"
    if (flag == BADOUTPUT):
        moulitek_script_trace += "[KO] [badoutput] " + name + " [/KO]\n"
    if (description != None):
        moulitek_script_trace += "[desc]\n" + description + "\n[/desc]\n"
    moulitek_script_trace += "[expected]\n" + expected + "\n[/expected]\n"
    moulitek_script_trace += "[got]\n" + got + "\n[/got]\n"
    moulitek_script_trace += "_____________________________________\n"


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
