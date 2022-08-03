import re, sys, json, openpyxl
import time, random #, testlink
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from random import choice
from openpyxl import Workbook

import NQ_HR_appium
from NQ_HR_appium import execution_log, fail_log, error_log, Logging

def MyExecution():
    error_menu = []

    try:
        NQ_HR_appium.execution()
    except:
        Logging("Cannot continue execution")
        error_menu.append("NQ_HR_appium.execution")  

    nhuquynh_log = {
        "execution_log": execution_log,
        "fail_log": fail_log,
        "error_log": error_log,
        "error_menu": error_menu
    }

    return nhuquynh_log
    
def My_Execution():
    NQ_HR_appium.execution()

    nhuquynh_log = {
        "execution_log": execution_log,
        "fail_log": fail_log,
        "error_log": error_log
    }

    return nhuquynh_log

My_Execution()
