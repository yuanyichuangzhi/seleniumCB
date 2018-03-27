from Util import *
from test_case.src.cb.payments.paymentsPage import PaymentPage

# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: MakeAPaymentPage.py
@time: 2018/3/21 15:47
'''


class MakeAPaymentPage(PaymentPage):

    # VN Make a Payment 的Account 定位
    account_ux_loc = (By.XPATH, "//p-auto-complete[@formcontrolname='fromAccount']/div/input")
    account_value_ux_loc = (By.XPATH, "//p-auto-complete[@formcontrolname='fromAccount']/div/div/ul/li[1]/div/span")

    # VN Make a Payment 的Payment Currency 定位
    payment_currency_ux_loc = (By.XPATH, "//p-auto-complete[@formcontrolname='currency']/div/div[1]/span")
    payment_currency_textbox_ux_loc = (By.XPATH, "//p-auto-complete[@formcontrolname='currency']/div/input")
    payment_currency_value_ux_loc = (By.XPATH, "//p-auto-complete[@formcontrolname='currency']/div/div/ul/li/div/span")
    # VN Make a Payment amount 定位
    amount_ux_loc = (By.XPATH, "//dbs-input[@formcontrolname='amount']/span/div/input")
    # VN 选择Telegraphic Transfer的beneficiary的定位
    beneficiary_ux_loc = (By.XPATH, "//auto-complete[@formcontrolname='payee']/div/input")
    beneficiary_value_ux_loc = (By.XPATH, "//auto-complete[@formcontrolname='payee']/div/div[2]/div/span")
    # VN 选择Telegraphic Transfer的purpose code下拉框中第一个元素的定位
    purpose_code_ux_loc = (By.XPATH, "//multi-level-dropdown[@formcontrolname='purposeCode']/div/div[1]")
    purpose_code_value_ux_loc = (By.XPATH, "//multi-level-dropdown[@formcontrolname='purposeCode']/div/div[2]/div/span")
    # VN Telegraphic Transfer的bank charge定位
    bank_charges_ux_loc = (By.XPATH, "//dbs-radio-group[@formcontrolname='bankCharge']/div/dbs-radio/div")
    # VN Telegraphic Transfer的payment details定位
    payment_details_ux_loc = (By.XPATH, "//dbs-textarea[@formcontrolname='paymentDetail']/div/textarea")
    # VN Telegraphic Transfer的Next按钮定位
    next_button_ux_loc = (By.XPATH, "//button[@name = 'next']")
    # VN Telegraphic Transfer的Submit按钮定位
    submit_button_ux_loc = (By.XPATH, "//button[@name = 'submit']")

    def select_account_ux(self, value):
        self.find_element(self.account_ux_loc, clickable=True).click()
        self.find_element(self.account_ux_loc, clickable=True).send_keys(value)
        self.double_click(loc=self.account_value_ux_loc)

    def select_payment_currency_ux(self, currency):
        self.find_element(self.payment_currency_ux_loc, clickable=True).click()
        self.find_element(self.payment_currency_textbox_ux_loc, clickable=True).send_keys(currency)
        self.double_click(loc=self.payment_currency_value_ux_loc)

    def enter_amount_ux(self, value):
        self.find_element(self.amount_ux_loc, clickable=True).send_keys(value)

    def select_beneficiary_ux(self, value):
        self.find_element(self.beneficiary_ux_loc, clickable=True).click()
        self.find_element(self.beneficiary_ux_loc, clickable=True).send_keys(value)
        self.double_click(loc=self.beneficiary_value_ux_loc)
        # self.find_element(self.beneficiary_value_ux_loc).click()

    def select_purpose_code_ux(self):
        self.find_element(self.purpose_code_ux_loc, clickable=True).click()
        self.find_element(self.purpose_code_value_ux_loc).click()

    def select_bank_charges_ux(self):
        self.find_element(self.bank_charges_ux_loc, clickable=True).click()

    def enter_payment_details_ux(self, value):
        self.find_element(self.payment_details_ux_loc, clickable=True).send_keys(value)

    def click_next_button_ux(self):
        self.find_element(self.next_button_ux_loc, clickable=True).click()

    def click_submit_button_ux(self):
        self.find_element(self.submit_button_ux_loc, clickable=True).click()
