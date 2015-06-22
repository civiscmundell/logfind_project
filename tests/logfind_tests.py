from nose.tools import *
<<<<<<< HEAD
from logfind import logfind
import os 

def test_find_files():
    log_files = logfind.find_files(os.getcwd(), ['.log$'])
    bak_files = logfind.find_files(os.getcwd(), ['.bak$'])
    both_files = logfind.find_files(os.getcwd(),
            ['.log$','.bak$'])
    assert_equal(len(log_files),4)
    assert_equal(len(bak_files),3)
    assert_equal(len(both_files),7)
    
def test_find_pattern_matches():
    both_files = logfind.find_files(os.getcwd(), ['.log$','.bak$'])
    soc_match = logfind.find_pattern_matches(both_files,'Socrates', False)
    gla_match = logfind.find_pattern_matches(both_files,'Glaucon', False)
    assert_equal(len(soc_match),6) 
    assert_equal(len(gla_match),2)
    
    
def test_and_or_matching():
    both_files = logfind.find_files(os.getcwd(), ['.log$','.bak$'])
    soc_gla_Amatch = logfind.find_pattern_matches(both_files,'Socrates Glaucon', False)
    soc_gla_Omatch = logfind.find_pattern_matches(both_files,'Socrates Glaucon', True)
    assert_equal(len(soc_gla_Amatch),1)
    assert_equal(len(soc_gla_Omatch),7)
=======
import NAME

def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test_basic():
    print("I RAN!")
>>>>>>> 84b78a1258f03c65fe5825031c1f9485b07e0ad6
