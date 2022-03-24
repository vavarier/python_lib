from moulitek.mt_print import *
import subprocess
import glob

moulitek_script_trace = ""

def check_makefile():
    makefile_test = Category("Preriquires Tests", "Looking for mandatory preriquires of the project.", info=True)
    make_rules = makefile_test.add_sequence("Make rules", "Check all makefile's mandatory rules.")
    mandatory = ["all", "re", "clean", "fclean"]
    for phony in mandatory:
        make_rules.add_test("Make %s." % phony)
        ret = subprocess.call("timeout 15s make -q %s 1> /dev/null 2> /dev/null" % phony, shell=True)
        if ret == 2:
            make_rules.set_status("Make %s." % phony, False, BADOUTPUT, "Rule make %s" % phony, "No rule in Makefile")
        else:
            make_rules.set_status("Make %s." % phony, True)

def init_moulitek():
    """Initialize moulitek for testing
    """
    global moulitek_script_trace
    if not "Makefile" in glob.glob("*"):
        moulitek_script_trace += "[BUILD SUCCESS]\n"
        return
    ret = subprocess.call(
        "timeout 15s make -q tests_run 1> /dev/null 2> /dev/null", shell=True)
    if ret != 2:
        subprocess.call(
            "timeout 15s make tests_run 1> /dev/null 2> /dev/null", shell=True)
        proc = subprocess.Popen("timeout 15s gcovr --exclude=tests", shell=True,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        coverage, _ = proc.communicate()
        moulitek_script_trace += "[covr]\n%s[/covr]\n" % coverage.decode()
        proc = subprocess.Popen("timeout 15s gcovr --exclude=tests -b",
                                shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        branches, _ = proc.communicate()
        moulitek_script_trace += "[branch]\n%s[/branch]\n" % branches.decode()
    check_makefile()
    ret = subprocess.call(
        "timeout 15s make fclean && make 1> /dev/null 2> /dev/null", shell=True)
    if (ret == 0):
        moulitek_script_trace += "[BUILD SUCCESS]\n"
    else:
        exit(0)

def success(name):
    global moulitek_script_trace
    moulitek_script_trace += "[OK] " + name + " [/OK]\n"
    moulitek_script_trace += "_____________________________________\n\n"


def category(name, description, info):
    global moulitek_script_trace
    if info:
        moulitek_script_trace += "[i] " + name + " [/i]\n\n"
    else:
        moulitek_script_trace += "[##] " + name + " [/##]\n\n"
    if (description != None):
        moulitek_script_trace += "[desc]\n" + description + "\n[/desc]\n"
    moulitek_script_trace += "_____________________________________\n\n"


def sequence(name, description):
    global moulitek_script_trace
    moulitek_script_trace += "[#] " + name + " [/#]\n\n"
    if (description != None):
        moulitek_script_trace += "[desc]\n" + description + "\n[/desc]\n"
    moulitek_script_trace += "_____________________________________\n\n"


def error(name, flag, description, expected, got):
    global moulitek_script_trace
    if (flag == SEGFAULT):
        moulitek_script_trace += "[KO] [segfault] " + name + " [/KO]\n\n"
    if (flag == TIMEOUT):
        moulitek_script_trace += "[KO] [timeout] " + name + " [/KO]\n\n"
    if (flag == NEVER_RUN):
        return
    if (flag == RETVALUE):
        moulitek_script_trace += "[KO] [retvalue] " + name + " [/KO]\n\n"
    if (flag == BADOUTPUT):
        moulitek_script_trace += "[KO] [badoutput] " + name + " [/KO]\n\n"
    if (description != None):
        moulitek_script_trace += "[desc]\n" + description + "\n[/desc]\n\n"
    moulitek_script_trace += "[expected]\n" + expected + "\n[/expected]\n\n"
    moulitek_script_trace += "[got]\n" + got + "\n[/got]\n\n"
    moulitek_script_trace += "_____________________________________\n\n"


def gen_trace():
    for cat in moulitek_all_categories:
        category(cat.name, cat.desc, cat.info)
        for seq in cat.sequences:
            sequence(seq.name, seq.desc)
            for test in seq.tests:
                if test["passed"]:
                    success(test["name"])
                else:
                    error(test["name"], test["reason"],
                          test["desc"], test["expected"], test["got"])
    open("trace.txt", "w+").write(moulitek_script_trace)
