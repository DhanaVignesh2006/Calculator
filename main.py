# Importing Modules
import math
import locale
import sys
from decimal import Decimal
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(310, 555)
        self.setWindowIcon(QIcon("assets/icons/calculator.png"))
        self.setObjectName("main_window")
        with open("design.qss", "r") as f:
            stylesheet = f.read()
        self.setStyleSheet(stylesheet)
        self.ui()
        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_9:
            self.nine()
        if event.key() == Qt.Key_8:
            self.eight()
        if event.key() == Qt.Key_7:
            self.seven()
        if event.key() == Qt.Key_6:
            self.six()
        if event.key() == Qt.Key_5:
            self.five()
        if event.key() == Qt.Key_4:
            self.four()
        if event.key() == Qt.Key_3:
            self.three()
        if event.key() == Qt.Key_2:
            self.two()
        if event.key() == Qt.Key_1:
            self.one()
        if event.key() == Qt.Key_0:
            self.zero()
        if event.key() == Qt.Key_Period:
            self.dot()
        if event.key() == Qt.Key_C:
            self.clear()
        if event.key() == Qt.Key_Escape:
            self.all_clear()
        if event.key() == Qt.Key_Backspace:
            self.back_space()
        if event.key() == Qt.Key_Asterisk:
            self.multiply()
        if event.key() == Qt.Key_Plus:
            self.addition()
        if event.key() == Qt.Key_Minus:
            self.subtraction()
        if event.key() == Qt.Key_Slash:
            self.divide()
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.equals()
        if event.key() == Qt.Key_M:
            self.mod()
        if event.key() == Qt.Key_Percent:
            self.percent()
        if event.key() == Qt.Key_F2:
            self.sqr()
        if event.key() == Qt.Key_F3:
            self.cube()
        if event.key() == Qt.Key_F1:
            self.x_custom()
        if event.key() == Qt.Key_S:
            self.square_root()
        if event.key() == Qt.Key_Percent:
            self.percent()
        if event.key() == Qt.Key_ParenLeft:
            self.left_brace()
        if event.key() == Qt.Key_ParenRight:
            self.right_brace()
        if event.key() == Qt.Key_L:
            self.lcm()
        if event.key() == Qt.Key_Z:
            self.clear_side_display()

    def ui(self):
        self.button()
        self.display()
        self.menu()

    def menu(self):
        menu = self.menuBar()
        menu.setObjectName("menuBar")
        file = menu.addMenu("&File")
        file.setObjectName("file")
        log_out = QAction(QIcon("assets/icons/logout.png"), "Exit", self)
        log_out.triggered.connect(self.log_out)
        help_menu = menu.addMenu("&Help")
        help_menu.setObjectName("help")
        help_action = QAction(QIcon("assets/icons/help.png"), "Help", self)
        help_action.triggered.connect(self.help_dialog)
        about = QAction(QIcon("assets/icons/about.png"), "About", self)
        about.triggered.connect(self.about_dialog)
        help_menu.addAction(help_action)
        help_menu.addAction(about)
        file.addAction(log_out)

    def display(self):
        # ------------------side display------------------ #
        self.dis_side = QLabel(self)
        self.dis_side.setFont(QFont("Calibri", 14))
        self.dis_side.setAlignment(Qt.AlignRight)
        self.dis_side.setText("0")
        self.dis_side.setWordWrap(True)
        self.dis_side.setObjectName("side_display")
        self.dis_side.move(10, 30)
        self.dis_side.resize(290, 60)
        # ------------------main display------------------ #
        self.dis_main = QLabel(self)
        self.dis_main.setFont(QFont("Calibri", 18))
        self.dis_main.setAlignment(Qt.AlignRight)
        self.dis_main.setText("0")
        self.dis_main.setWordWrap(True)
        self.dis_main.setObjectName("main_display")
        self.dis_main.move(10, 100)
        self.dis_main.resize(290, 60)

    def button(self):
        # Button for AC
        self.btn_all_clear = QPushButton(self)
        self.btn_all_clear.setText("AC")
        self.btn_all_clear.setFont(QFont("Calibri", 14))
        self.btn_all_clear.move(10, 195)
        self.btn_all_clear.resize(50, 50)
        self.btn_all_clear.setObjectName("all_clear")
        self.btn_all_clear.clicked.connect(self.all_clear)
        # Button for C
        self.btn_clear = QPushButton(self)
        self.btn_clear.setText("C")
        self.btn_clear.setFont(QFont("Calibri", 14))
        self.btn_clear.move(70, 195)
        self.btn_clear.resize(50, 50)
        self.btn_clear.setObjectName("clear")
        self.btn_clear.clicked.connect(self.clear)
        # Button for backspace
        self.btn_backspace = QPushButton(self)
        self.btn_backspace.setText("←")
        self.btn_backspace.setFont(QFont("Calibri", 14))
        self.btn_backspace.move(130, 195)
        self.btn_backspace.resize(50, 50)
        self.btn_backspace.setObjectName("backspace")
        self.btn_backspace.clicked.connect(self.back_space)
        # Button for plus minus
        self.btn_plus_minus = QPushButton(self)
        self.btn_plus_minus.setText("+/-")
        self.btn_plus_minus.setFont(QFont("Calibri", 20))
        self.btn_plus_minus.move(190, 195)
        self.btn_plus_minus.resize(50, 50)
        self.btn_plus_minus.setObjectName("plus_minus")
        self.btn_plus_minus.clicked.connect(self.plus_minus)
        # Button for plus
        self.btn_plus = QPushButton(self)
        self.btn_plus.setText("+")
        self.btn_plus.setFont(QFont("Calibri", 20))
        self.btn_plus.move(250, 195)
        self.btn_plus.resize(50, 50)
        self.btn_plus.setObjectName("plus")
        self.btn_plus.clicked.connect(self.addition)
        # Button for multiply
        self.btn_multiply = QPushButton(self)
        self.btn_multiply.setText("X")
        self.btn_multiply.setFont(QFont("Calibri", 14))
        self.btn_multiply.move(250, 315)
        self.btn_multiply.resize(50, 50)
        self.btn_multiply.setObjectName("multiply")
        self.btn_multiply.clicked.connect(self.multiply)
        # Button for minus
        self.btn_minus = QPushButton(self)
        self.btn_minus.setText("-")
        self.btn_minus.setFont(QFont("Calibri", 30))
        self.btn_minus.move(250, 255)
        self.btn_minus.resize(50, 50)
        self.btn_minus.setObjectName("minus")
        self.btn_minus.clicked.connect(self.subtraction)
        # Button for nine
        self.btn_nine = QPushButton(self)
        self.btn_nine.setText("9")
        self.btn_nine.setFont(QFont("Calibri", 14))
        self.btn_nine.move(10, 255)
        self.btn_nine.resize(50, 50)
        self.btn_nine.setObjectName("nine")
        self.btn_nine.clicked.connect(self.nine)
        # Button for eight
        self.btn_eight = QPushButton(self)
        self.btn_eight.setText("8")
        self.btn_eight.setFont(QFont("Calibri", 14))
        self.btn_eight.move(70, 255)
        self.btn_eight.resize(50, 50)
        self.btn_eight.setObjectName("eight")
        self.btn_eight.clicked.connect(self.eight)
        # Button for seven
        self.btn_seven = QPushButton(self)
        self.btn_seven.setText("7")
        self.btn_seven.setFont(QFont("Calibri", 14))
        self.btn_seven.move(130, 255)
        self.btn_seven.resize(50, 50)
        self.btn_seven.setObjectName("seven")
        self.btn_seven.clicked.connect(self.seven)
        # Button for six
        self.btn_six = QPushButton(self)
        self.btn_six.setText("6")
        self.btn_six.setFont(QFont("Calibri", 14))
        self.btn_six.move(190, 255)
        self.btn_six.resize(50, 50)
        self.btn_six.setObjectName("six")
        self.btn_six.clicked.connect(self.six)
        # Button for five
        self.btn_five = QPushButton(self)
        self.btn_five.setText("5")
        self.btn_five.setFont(QFont("Calibri", 14))
        self.btn_five.move(10, 315)
        self.btn_five.resize(50, 50)
        self.btn_five.setObjectName("five")
        self.btn_five.clicked.connect(self.five)
        # Button for four
        self.btn_four = QPushButton(self)
        self.btn_four.setText("4")
        self.btn_four.setFont(QFont("Calibri", 14))
        self.btn_four.move(70, 315)
        self.btn_four.resize(50, 50)
        self.btn_four.setObjectName("four")
        self.btn_four.clicked.connect(self.four)
        # Button for three
        self.btn_three = QPushButton(self)
        self.btn_three.setText("3")
        self.btn_three.setFont(QFont("Calibri", 14))
        self.btn_three.move(130, 315)
        self.btn_three.resize(50, 50)
        self.btn_three.setObjectName("three")
        self.btn_three.clicked.connect(self.three)
        # Button for two
        self.btn_two = QPushButton(self)
        self.btn_two.setText("2")
        self.btn_two.setFont(QFont("Calibri", 14))
        self.btn_two.move(190, 315)
        self.btn_two.resize(50, 50)
        self.btn_two.setObjectName("two")
        self.btn_two.clicked.connect(self.two)
        # Button for one
        self.btn_one = QPushButton(self)
        self.btn_one.setText("1")
        self.btn_one.setFont(QFont("Calibri", 14))
        self.btn_one.move(10, 375)
        self.btn_one.resize(50, 50)
        self.btn_one.setObjectName("one")
        self.btn_one.clicked.connect(self.one)
        # Button for one
        self.btn_zero = QPushButton(self)
        self.btn_zero.setText("0")
        self.btn_zero.setFont(QFont("Calibri", 14))
        self.btn_zero.move(70, 375)
        self.btn_zero.resize(50, 50)
        self.btn_zero.setObjectName("zero")
        self.btn_zero.clicked.connect(self.zero)
        # Button for dot
        self.btn_dot = QPushButton(self)
        self.btn_dot.setText(".")
        self.btn_dot.setFont(QFont("Calibri", 20))
        self.btn_dot.move(130, 375)
        self.btn_dot.resize(50, 50)
        self.btn_dot.setObjectName("dot")
        self.btn_dot.clicked.connect(self.dot)
        # Button for lcm
        self.btn_lcm = QPushButton(self)
        self.btn_lcm.setText("lcm")
        self.btn_lcm.setFont(QFont("Calibri", 14))
        self.btn_lcm.move(190, 375)
        self.btn_lcm.resize(50, 50)
        self.btn_lcm.setObjectName("lcm")
        self.btn_lcm.clicked.connect(self.lcm)
        # Button for divide
        self.btn_divide = QPushButton(self)
        self.btn_divide.setText("÷")
        self.btn_divide.setFont(QFont("Calibri", 14))
        self.btn_divide.move(250, 375)
        self.btn_divide.resize(50, 50)
        self.btn_divide.setObjectName("divide")
        self.btn_divide.clicked.connect(self.divide)
        # Button for mod
        self.btn_mod = QPushButton(self)
        self.btn_mod.setText("mod")
        self.btn_mod.setFont(QFont("Calibri", 14))
        self.btn_mod.move(10, 435)
        self.btn_mod.resize(50, 50)
        self.btn_mod.setObjectName("violet")
        self.btn_mod.clicked.connect(self.mod)
        # Button for sqrt
        self.btn_sqrt = QPushButton(self)
        self.btn_sqrt.setText("√")
        self.btn_sqrt.setFont(QFont("Calibri", 20))
        self.btn_sqrt.move(70, 435)
        self.btn_sqrt.resize(50, 50)
        self.btn_sqrt.setObjectName("violet")
        self.btn_sqrt.clicked.connect(self.square_root)
        # Button for square
        self.btn_sqr = QPushButton(self)
        self.btn_sqr.setText("X²")
        self.btn_sqr.setFont(QFont("Calibri", 14))
        self.btn_sqr.move(130, 435)
        self.btn_sqr.resize(50, 50)
        self.btn_sqr.setObjectName("violet")
        self.btn_sqr.clicked.connect(self.sqr)
        # Button for cube
        self.btn_cube = QPushButton(self)
        self.btn_cube.setText("X³")
        self.btn_cube.setFont(QFont("Calibri", 14))
        self.btn_cube.move(190, 435)
        self.btn_cube.resize(50, 50)
        self.btn_cube.setObjectName("violet")
        self.btn_cube.clicked.connect(self.cube)
        # Button for x custom
        self.btn_custom = QPushButton(self)
        self.btn_custom.setText("Xⁿ")
        self.btn_custom.setFont(QFont("Calibri", 14))
        self.btn_custom.move(10, 495)
        self.btn_custom.resize(50, 50)
        self.btn_custom.setObjectName("violet")
        self.btn_custom.clicked.connect(self.x_custom)
        # Button for Left Bracket
        self.btn_left_brac = QPushButton(self)
        self.btn_left_brac.setText("(")
        self.btn_left_brac.setFont(QFont("Calibri", 14))
        self.btn_left_brac.move(70, 495)
        self.btn_left_brac.resize(50, 50)
        self.btn_left_brac.setObjectName("violet")
        self.btn_left_brac.clicked.connect(self.left_brace)
        # Button for right bracket
        self.btn_right_brac = QPushButton(self)
        self.btn_right_brac.setText(")")
        self.btn_right_brac.setFont(QFont("Calibri", 14))
        self.btn_right_brac.move(130, 495)
        self.btn_right_brac.resize(50, 50)
        self.btn_right_brac.setObjectName("violet")
        self.btn_right_brac.clicked.connect(self.right_brace)
        # Button for percentage
        self.btn_per = QPushButton(self)
        self.btn_per.setText("%")
        self.btn_per.setFont(QFont("Calibri", 14))
        self.btn_per.move(190, 495)
        self.btn_per.resize(50, 50)
        self.btn_per.setObjectName("violet")
        self.btn_per.clicked.connect(self.percent)
        # Button for equals
        self.btn_equals = QPushButton(self)
        self.btn_equals.setText("=")
        self.btn_equals.setFont(QFont("Calibri", 30))
        self.btn_equals.move(250, 435)
        self.btn_equals.resize(50, 110)
        self.btn_equals.setObjectName("equals")
        self.btn_equals.clicked.connect(self.equals)

    # ------------------Main Functions------------------ #
    def help_dialog(self):
        string = """Shortcuts:
    i)You can use the number keys which are in the keyboard to enter numbers and this is also applicable for the signs like plus, minus, multiply, divide, dot and parenthesis.
    ii) Use escape button to clear all the things in calculator.
    iii)Use C button to clear the main display.
    iv)Use backspace button to clear the last thing in the main display.
    v)Use Return or enter button to calculate the values.
    vi)use M button to find mod.
    vii)Use Percentage sign to find the Percentage.
    viii)use F2 button to find x² of the number.
    ix) Use F3 button to find x³ of the number.
    x)Use F1 button to find xⁿ of the number.
    xi)Use S button to find the square root of the number.
    xii)Use L button to find LCM for infinite of numbers.
    xiii)Use Z button to clear the side display.

    If you have more doubts please mail me the doubt
    Mail Id: tsdhanv@gmail.com

    Thank you for using this calculator...."""
        dialog = QDialog(self)
        dialog.setWindowTitle("Help")
        dialog.setWindowIcon(QIcon("assets/icons/help.png"))
        dialog.resize(400, 500)
        editor = QTextEdit(dialog)
        editor.setReadOnly(True)
        editor.wordWrapMode()
        editor.setText(string)
        editor.resize(350, 420)
        editor.setObjectName("editor")
        editor.setFont(QFont("Comicsans", 14))
        editor.move(25, 35)
        dialog.setObjectName("help_dialog")
        dialog.exec_()

    def about_dialog(self):
        dialog = QDialog(self)
        dialog.setObjectName("about_dialog")
        dialog.setWindowIcon(QIcon("assets/icons/about.png"))
        dialog.setWindowTitle("About")
        dialog.resize(500, 250)
        label = QLabel(dialog)
        label.setText("Calculator")
        label.move(175, 20)
        label.setFont(QFont("Arial", 25))
        label.setObjectName("about_label")
        label_1 = QLabel(dialog)
        label_1.setFont(QFont("Calibri", 18))
        label_1.setText("""This is the calculator made with Python using the
        \nmodule PyQt5.This is the application made
        by Master.T.S.DhanaVignesh......""")
        label_1.move(20, 90)
        label_1.setObjectName("about_label_1")
        label_2 = QLabel(dialog)
        label_2.setFont(QFont("Calibri", 18))
        label_2.setText("Calculator")
        label_2.move(175, 190)
        label_2.setObjectName("about_label_2")
        label_3 = QLabel(dialog)
        label_3.setFont(QFont("Calibri", 8))
        label_3.setText("2021.1.1")
        label_3.move(275, 205)
        label_3.setObjectName("about_label_3")
        btn_ok = QPushButton(dialog)
        btn_ok.setText("OK")
        btn_ok.setObjectName("about_btn_ok")
        btn_ok.move(420, 200)
        btn_ok.setFont(QFont("Arial", 12))
        btn_ok.resize(70, 30)
        btn_ok.clicked.connect(dialog.close)
        dialog.exec_()


    def convert_to_int(self, string):
        try:
            for i in range(0, len(string)):
                string[i] = int(string[i])
        except:
            return string


    def Format_string(self, string):
        return '{0:n}'.format(string)


    def check_commas(self):
        string = self.dis_main.text()
        number = string
        locale.setlocale(locale.LC_ALL, 'en_in')
        string = string.replace(",", "").replace(".", "").replace("-", '')
        formatted_string = self.Format_string(Decimal(string))
        self.dis_main.setText(formatted_string)

        if "-" in number:
            self.dis_main.setText(f"- {formatted_string}")

        if "." in number:
            splitted_string = number.split(".")
            formatted_first_string = self.Format_string(Decimal(splitted_string[0].replace(",", "").replace(".", "").replace("-", '')))
            formatted_string_dot = f"{formatted_first_string}.{splitted_string[1]}"
            if "-" in number:
                self.dis_main.setText(f"- {formatted_string_dot}")
            else:
                self.dis_main.setText(formatted_string_dot)


    def show_dialog(self, frame, text):
        dialog = QDialog(self)
        lab = QLabel(dialog)
        lab.setText(frame + text)
        lab.setObjectName("show_lab")
        lab.setFont(QFont("Calibri", 18))
        lab.move(20, 50)
        dialog.setWindowTitle("Power of")
        dialog.resize(800, 150)
        if dialog.close():
            self.dis_main.setText(" - ")
        dialog.exec()

    def x_custom_dialog(self):
        self.d = QDialog(self)
        self.d.setWindowIcon(QIcon("assets/icons/superscript.png"))
        self.label_1 = QLabel(self.d)
        self.label_1.setText("Number :")
        self.label_1.setObjectName("x_label_1")
        self.label_1.setFont(QFont("Calibri", 10))
        self.label_1.move(10, 10)
        self.label_2 = QLabel(self.d)
        self.label_2.setText("Number that you want to multiply : ")
        self.setObjectName("x_label_1")
        self.label_2.setFont(QFont("Calibri", 10))
        self.label_2.move(10, 40)
        validator = QDoubleValidator(self)
        self.first = QLineEdit(self.d)
        self.first.resize(180, 25)
        self.first.move(210, 4)
        self.first.setMaxLength(6)
        self.first.setFont(QFont("Calibri", 12))
        self.first.setObjectName("lcm_first_edit")
        self.first.setValidator(validator)
        self.second = QLineEdit(self.d)
        self.second.resize(180, 25)
        self.second.move(210, 35)
        self.second.setFont(QFont("Calibri", 12))
        self.second.setValidator(validator)
        self.second.setObjectName("lcm_first_edit")
        self.second.setMaxLength(8)
        self.second.setMaxLength(4)
        ok_btn = QPushButton("OK", self.d)
        ok_btn.clicked.connect(self.ok)
        ok_btn.move(170, 70)
        ok_btn.setObjectName("ok")
        ok_btn.resize(70, 25)
        ok_btn.setFont(QFont("Calibri", 12))
        cancel_btn = QPushButton("Cancel", self.d)
        cancel_btn.clicked.connect(self.cancel)
        cancel_btn.move(260, 70)
        cancel_btn.setObjectName("cancel")
        cancel_btn.resize(70, 25)
        cancel_btn.setFont(QFont("Calibri", 12))
        self.d.resize(400, 100)
        self.d.setObjectName("dialog")
        self.d.setWindowTitle("X-Custom")
        self.d.exec_()

    def ok(self):
        first = self.first.text()
        second = self.second.text()
        if first == "" or second == "":
            return None
        if "," in first or "," in second:
            return None
        ans = int(first) ** int(second)
        if len(str(ans)) > 20:
            str_ans = str(ans)
            minus = 10 - int(str_ans[-1])
            min_result = int(str_ans) + minus
            lis = list(str(min_result))
            lis.insert(1, ".")
            join_dot = "".join(lis)
            split = join_dot.split(".")
            split_1 = split[1]
            iterate_list = [iterate_split_1 for iterate_split_1 in split_1]
            eight = iterate_list[:8]
            len_join = "".join(split[0])
            len_eight = "".join(eight)
            length = len(iterate_list)
            large_to_e = len_join + "." + len_eight + "E+" + str(length)
            self.d.close()
            self.dis_main.setText(large_to_e)
        else:
            self.d.close()
            ans = int(first) ** int(second)
            self.dis_main.setText(str(ans))

    def cancel(self):
        self.d.close()

    def lcm_dialog(self):
        self.dialog = QDialog(self)
        self.label_1_edit = QLabel(self.dialog)
        self.label_1_edit.setText("Enter the number :")
        self.label_1_edit.setObjectName("x_label_1")
        self.label_1_edit.setFont(QFont("Calibri", 10))
        self.label_1_edit.move(10, 10)
        validator = QDoubleValidator(self)
        self.first_edit = QLineEdit(self.dialog)
        self.first_edit.resize(270, 25)
        self.first_edit.move(120, 4)
        self.first_edit.setFont(QFont("Calibri", 12))
        self.first_edit.setObjectName("lcm_first_edit")
        self.first_edit.setValidator(validator)
        self.second_label = QLabel(self.dialog)
        self.second_label.setText("Please insert the commas to separate the respective\n numbers")
        self.second_label.move(10, 32)
        self.second_label.setFont(QFont("Calibri", 12))
        self.second_label.setObjectName("lcm_snd_label")
        ok_btn = QPushButton("OK", self.dialog)
        ok_btn.clicked.connect(self.ok_btn)
        ok_btn.move(170, 70)
        ok_btn.setObjectName("lcm_ok_btn")
        ok_btn.resize(70, 25)
        ok_btn.setFont(QFont("Calibri", 12))
        cancel_btn = QPushButton("Cancel", self.dialog)
        cancel_btn.clicked.connect(self.cancel_btn)
        cancel_btn.move(260, 70)
        cancel_btn.setObjectName("lcm_cancel")
        cancel_btn.resize(70, 25)
        cancel_btn.setFont(QFont("Calibri", 12))
        self.dialog.resize(400, 100)
        self.dialog.setObjectName("lcm_dialog")
        self.dialog.setWindowIcon(QIcon("assets/icons/lcm.png"))
        self.dialog.setWindowTitle("LCM")
        self.dialog.exec_()

    def ok_btn(self):
        fText = self.first_edit.text()
        if fText == "":
            return None
        lcm = self.compute_lcm(fText)
        if len(str(lcm)) > 20:
            self.show_dialog("This cannot be shown in the display\n", f"{str(lcm)}")
        else:
            self.dis_main.setText(str(lcm))
            self.dialog.close()

    def cancel_btn(self):
        self.dialog.close()

    def check_dis(self):
        string = self.dis_main.text()
        string = string.replace(",", '').replace('.', '').replace("-", '')
        length = len(string)
        if length > 18:
            return True
        else:
            return False

    def count(self, character, string):
        count = 0
        for e in string:
            if e == character:
                count += 1

        return count

    def check_sign(self):
        stri = self.dis_side.text()
        lis = [sign for sign in stri]
        try:
            if "*" in lis[-2]:
                return True
            if "/" in lis[-2]:
                return True
            if "+" in lis[-2]:
                return True
            if "-" in lis[-2]:
                return True
        except:
            return False

    def insert(self, element):
        string = self.dis_main.text()
        stri = self.dis_side.text()
        if string == "0" or string == " - ":
            self.dis_main.setText(element)
        elif " = " in stri:
            self.dis_main.setText(element)
            self.dis_side.setText("0")
        elif string != "0" and string != " - ":
            self.dis_main.setText(string + element)
        else:
            print("none")

    def log_out(self):
        self.close()

    def all_clear(self):
        self.dis_main.setText("0")
        self.dis_side.setText("0")

    def clear(self):
        stri = self.dis_side.text()
        if stri == "0":
            self.dis_main.setText("0")
        else:
            self.dis_main.setText(" - ")

    def back_space(self):
        string = self.dis_main.text()
        stri = self.dis_side.text()
        insert = string[:-1]
        if string == " - ":
            return None
        if string == "":
            return None
        if len(string) == 1 and stri == "0":
            self.dis_main.setText("0")
        elif stri != "0" and len(string) == 1:
            self.dis_main.setText(" - ")
        else:
            self.dis_main.setText(insert)
            self.check_commas()

    def plus_minus(self):
        string = self.dis_main.text()
        lis = [elem for elem in string]
        if "E" in string:
            return None
        if string == " - ":
            return None
        if lis[0] == "-":
            st = "".join(lis)
            replace = st.replace("- ", "")
            self.dis_main.setText(replace)
        else:
            self.dis_main.setText("- " + string)

    def addition(self):
        string = self.dis_main.text()
        stri = self.dis_side.text()
        sign = self.check_sign()
        if "E" in string:
            return None
        if sign and string == " - ":
            lis = [elem for elem in stri]
            lis[-2] = "+"
            join = "".join(lis)
            self.dis_side.setText(join)
        if stri[-1] == ")":
            self.dis_side.setText(stri + " + ")
        if stri == "0":
            self.dis_side.setText(string + " + ")
        if string == " - ":
            return None
        if "=" in stri:
            self.dis_side.setText("")
            self.dis_side.setText(string + " + ")
            self.dis_main.setText(" - ")
        elif stri != "0" and stri[-1] != ")":
            self.dis_side.setText(stri + string + " + ")
        if stri[-1] == "(":
            self.dis_main.setText(" - ")
            return None
        if stri != "0" and stri[-2] == "+":
            self.dis_side.setText(stri + string + " + ")
        self.dis_main.setText(" - ")

    def multiply(self):
        string = self.dis_main.text()
        stri = self.dis_side.text()
        sign = self.check_sign()
        if "E" in string:
            return None
        if sign and string == " - ":
            lis = [elem for elem in stri]
            lis[-2] = "*"
            join = "".join(lis)
            self.dis_side.setText(join)
        if stri[-1] == ")":
            self.dis_side.setText(stri + " * ")
        if stri == "0":
            self.dis_side.setText(string + " * ")
        if string == " - ":
            return None
        if "=" in stri:
            self.dis_side.setText("")
            self.dis_side.setText(string + " * ")
            self.dis_main.setText(" - ")
        elif stri != "0" and stri[-1] != ")":
            self.dis_side.setText(stri + string + " * ")
        if stri != "0" and stri[-1] == "*":
            self.dis_side.setText(stri + string + " * ")
        self.dis_main.setText(" - ")

    def subtraction(self):
        string = self.dis_main.text()
        stri = self.dis_side.text()
        sign = self.check_sign()
        lis = [elem for elem in stri]
        if "E" in string:
            return None
        if sign and string == " - ":
            lis[-2] = "-"
            join = "".join(lis)
            self.dis_side.setText(join)
        if stri[-1] == ")":
            self.dis_side.setText(stri + " - ")
        if stri == "0":
            self.dis_side.setText(string + " - ")
        if string == " - ":
            return None
        if "=" in stri:
            self.dis_side.setText("")
            self.dis_side.setText(string + " - ")
            self.dis_main.setText(' - ')
        elif stri != "0" and stri[-1] != ")":
            self.dis_side.setText(stri + string + " - ")
        if stri != "0" and stri[-1] == "-":
            self.dis_side.setText(stri + string + " - ")
        self.dis_main.setText(" - ")

    def divide(self):
        string = self.dis_main.text()
        stri = self.dis_side.text()
        sign = self.check_sign()
        elem = [elem for elem in string]
        if "E" in string:
            return None
        if string == "0":
            return None
        if sign and string == " - ":
            lis = [elem for elem in stri]
            lis[-2] = "/"
            join = "".join(lis)
            self.dis_side.setText(join)
        if elem[-1] == ".":
            return None
        if sign and string == " - ":
            lis = [elem for elem in stri]
            lis[-2] = "/"
            join = "".join(lis)
            self.dis_side.setText(join)
        if stri[-1] == ")":
            self.dis_side.setText(stri + " / ")
        if stri == "0":
            self.dis_side.setText(string + " / ")
        if string == " - ":
            return None
        if "=" in stri:
            self.dis_side.setText("")
            self.dis_side.setText(string + " / ")
            self.dis_main.setText(' - ')
        elif stri != "0" and stri[-1] != ")":
            self.dis_side.setText(stri + string + " / ")
        if stri != "0" and stri[-1] == "/":
            self.dis_side.setText(stri + string + " / ")
        self.dis_main.setText(" - ")

    def clear_side_display(self):
        self.dis_side.setText("0")

    def nine(self):
        check_dis = self.check_dis()
        string = self.dis_main.text()
        if not check_dis:
            self.insert("9")
            self.check_commas()
        if string == "Overflow":
            self.dis_main.setText("9")
            self.check_commas()
        if check_dis:
            pass

    def eight(self):
        string = self.dis_main.text()
        check_dis = self.check_dis()
        if not check_dis:
            self.insert("8")
            self.check_commas()
        if string == "Overflow":
            self.dis_main.setText("8")
        if check_dis:
            pass

    def seven(self):
        string = self.dis_main.text()
        check_dis = self.check_dis()
        if not check_dis:
            self.insert("7")
            self.check_commas()
        if check_dis:
            pass

    def six(self):
        string = self.dis_main.text()
        check_dis = self.check_dis()
        if not check_dis:
            self.insert("6")
            self.check_commas()
        if check_dis:
            pass

    def five(self):
        string = self.dis_main.text()
        check_dis = self.check_dis()
        if not check_dis:
            self.insert("5")
            self.check_commas()
        if check_dis:
            pass

    def four(self):
        string = self.dis_main.text()
        check_dis = self.check_dis()
        if not check_dis:
            self.insert("4")
            self.check_commas()
        if check_dis:
            pass

    def three(self):
        string = self.dis_main.text()
        check_dis = self.check_dis()
        if not check_dis:
            self.insert("3")
            self.check_commas()
        if check_dis:
            pass

    def two(self):
        string = self.dis_main.text()
        check_dis = self.check_dis()
        if not check_dis:
            self.insert("2")
            self.check_commas()
        if check_dis:
            pass

    def one(self):
        string = self.dis_main.text()
        check_dis = self.check_dis()
        if not check_dis:
            self.insert("1")
            self.check_commas()
        if check_dis:
            pass

    def zero(self):
        string = self.dis_main.text()
        check_dis = self.check_dis()
        if not check_dis:
            self.insert("0")
            self.check_commas()
        if check_dis:
            pass

    def dot(self):
        string = self.dis_main.text()
        lis = [element for element in string]
        if string == "0" or string == " - ":
            self.dis_main.setText("0.")
        if "." in lis or string == " - ":
            pass
        else:
            self.dis_main.setText(string + ".")

    def compute_lcm(self, string):
        a = string.split(",")
        a = self.convert_to_int(a)
        lcm = a[0]
        for i in a[1:]:
            lcm = lcm * i // math.gcd(lcm, i)

        return lcm

    def lcm(self):
        self.lcm_dialog()

    def mod(self):
        string = self.dis_main.text()
        stri = self.dis_side.text()
        if stri == "0":
            self.dis_side.setText(string + " %")
        if string == " - ":
            return None
        if "=" in stri:
            self.dis_side.setText("")
            self.dis_side.setText(string + " % ")
            self.dis_main.setText(' - ')
        elif stri != "0":
            self.dis_side.setText(stri + string + " % ")
        if stri != "0" and stri[-1] == "%":
            self.dis_side.setText(stri + string + "%")
        self.dis_main.setText(" - ")

    def square_root(self):
        string = self.dis_main.text()
        sqRt = math.sqrt(float(string))
        split = str(sqRt).split(".")
        if split[1] == "0":
            roun = round(sqRt)
            self.dis_main.setText(str(roun))
        if split[1] != "0":
            self.dis_main.setText(str(sqRt))

    def sqr(self):
        string = self.dis_main.text()
        formatted = string.replace(",", "")
        if "." in string:
            sqr = float(formatted) ** 2
            self.dis_main.setText(str(sqr))
        if string != " - " and "." not in string:
            sqr = int(formatted) ** 2
            self.dis_main.setText(str(sqr))
        if string == " - ":
            return None
        square = str(sqr)
        length = len(square)
        if length > 20:
            result = str(sqr)
            minus = 10 - int(result[-1])
            min_result = sqr + minus
            list_min = list(str(min_result))
            list_min.insert(1, ".")
            join_dot = "".join(list_min)
            split = join_dot.split(".")
            split_1 = split[1]
            iterate_list = [iterate_split_1 for iterate_split_1 in split_1]
            eight = iterate_list[:8]
            len_join = "".join(split[0])
            len_eight = "".join(eight)
            length = len(iterate_list)
            large_to_e = len_join + "." + len_eight + "E+" + str(length)
            self.dis_main.setText(large_to_e)

    def cube(self):
        string = self.dis_main.text()
        formatted = string.replace(",", "")
        if "." in string:
            cube = float(formatted) ** 3
            self.dis_main.setText(str(cube))
        if string != " - " and "." not in string:
            cube = int(formatted) ** 3
            self.dis_main.setText(str(cube))
        if string == " - ":
            return None
        length = len(string)
        if length > 18:
            result = str(cube)
            minus = 10 - int(result[-1])
            min_result = cube + minus
            list_min = list(str(min_result))
            list_min.insert(1, ".")
            join_dot = "".join(list_min)
            split = join_dot.split(".")
            split_1 = split[1]
            iterate_list = [iterate_split_1 for iterate_split_1 in split_1]
            eight = iterate_list[:8]
            len_join = "".join(split[0])
            len_eight = "".join(eight)
            length = len(iterate_list)
            large_to_e = len_join + "." + len_eight + "E+" + str(length)
            self.dis_main.setText(large_to_e)

    def x_custom(self):
        self.x_custom_dialog()

    def left_brace(self):
        stri = self.dis_side.text()
        if stri == "0":
            self.dis_side.setText("(")
        if stri != "0":
            self.dis_side.setText(stri + "(")
        if " = " in stri:
            self.dis_side.setText("(")

    def right_brace(self):
        string = self.dis_main.text()
        stri = self.dis_side.text()
        count_left = self.count("(", stri)
        count_right = self.count(")", stri)
        if stri == "0":
            self.dis_side.setText(")")
        if stri != "0":
            self.dis_side.setText(stri + ")")
        if string == " - ":
            self.dis_side.setText(stri)
        if stri[-1] == ")":
            self.dis_side.setText(stri + ")")
        if string != " - " and stri[-1] != ")":
            self.dis_side.setText(stri + string + ")")
        if count_left == count_right:
            self.dis_side.setText(stri)

    def percent(self):
        string = self.dis_main.text()
        stri = self.dis_side.text()
        if string == "":
            return None
        if stri == "0":
            return None
        if stri[-2] == "*":
            percent = int(string) / 100
            self.dis_main.setText(str(percent))
        else:
            return None

    def equals(self):
        string = self.dis_main.text()
        stri = self.dis_side.text()
        # try:
        if "()" in stri:
            return None
        if string == " - ":
            return None
        if string == "0":
            return None
        if stri == "0":
            return None
        count_left = self.count("(", stri)
        count_right = self.count(")", stri)
        if count_left > count_right:
            sub = count_left - count_right
            self.dis_side.setText(stri + ")" * sub)
        if stri[-1] == ")":
            result = eval(stri)
            int_ans = str(result)
            self.dis_side.setText(stri + " = ")
            self.dis_main.setText(int_ans)
        else:
            self.evaluate()

    def evaluate(self):
        string = self.dis_main.text()
        stri = self.dis_side.text()
        string_r = string.replace(",", "")
        stri_r = stri.replace(",", "")
        total = eval(stri_r + string_r)
        self.dis_side.setText(stri + string + ' = ')
        result = str(total)
        if "." in result:
            split = result.split(".")
            if split[1] == "0":
                del split[1]
                join = "".join(split)
                self.dis_main.setText(join)
                self.check_commas()
            else:
                self.dis_main.setText(result)
                self.check_commas()
        if len(result) > 18:
            minus = 10 - int(result[-1])
            min_result = int(result) + minus
            lis = list(str(min_result))
            lis.insert(1, ".")
            join_dot = "".join(lis)
            split = join_dot.split(".")
            split_1 = split[1]
            iterate_list = [iterate_split_1 for iterate_split_1 in split_1]
            eight = iterate_list[:8]
            len_join = "".join(split[0])
            len_eight = "".join(eight)
            length = len(iterate_list)
            large_to_e = len_join + "." + len_eight + "E+" + str(length)
            self.dis_main.setText(large_to_e)
        else:
            self.dis_main.setText(result)
            self.check_commas()


app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())