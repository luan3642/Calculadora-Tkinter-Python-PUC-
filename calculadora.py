import tkinter as tk


class Calc():
    def __init__(self, parent=tk.Tk()):
        self.parent = parent
        self.parent.title("Calculadora")
        self.parent.option_add("*Font", "Verdana 12 normal")
        self.parent.iconbitmap("icones/Wineass-Ios7-Redesign-Calculator.ico")
        self.math_expression = None
        menu_bar = tk.Menu(self.parent)
        self.parent.config(menu=menu_bar)
        self.display_stringvar = tk.StringVar()
        display_entry_validate = (self.parent.register(self.only_number_entry), '%S', '%d')
        self.display = tk.Entry(self.parent, font=("Verdana", 20, "normal"), validate="key",
                                validatecommand=display_entry_validate, textvariable=self.display_stringvar)
        self.display.bind('<Return>', self.command_calc)
        self.bt0 = tk.Button(self.parent, text="0", command=lambda: self.button_press('0'))
        self.bt1 = tk.Button(self.parent, text="1", command=lambda: self.button_press('1'))
        self.bt2 = tk.Button(self.parent, text="2", command=lambda: self.button_press('2'))
        self.bt3 = tk.Button(self.parent, text="3", command=lambda: self.button_press('3'))
        self.bt4 = tk.Button(self.parent, text="4", command=lambda: self.button_press('4'))
        self.bt5 = tk.Button(self.parent, text="5", command=lambda: self.button_press('5'))
        self.bt6 = tk.Button(self.parent, text="6", command=lambda: self.button_press('6'))
        self.bt7 = tk.Button(self.parent, text="7", command=lambda: self.button_press('7'))
        self.bt8 = tk.Button(self.parent, text="8", command=lambda: self.button_press('8'))
        self.bt9 = tk.Button(self.parent, text="9", command=lambda: self.button_press('9'))
        self.bt_addition = tk.Button(self.parent, text="+", command=lambda: self.button_press('+'))
        self.bt_subtraction = tk.Button(self.parent, text="-", command=lambda: self.button_press('-'))
        self.bt_mutiplication = tk.Button(self.parent, text="*", command=lambda: self.button_press('*'))
        self.bt_division = tk.Button(self.parent, text="/", command=lambda: self.button_press('/'))
        self.bt_decimal_point = tk.Button(self.parent, text=".", command=lambda: self.button_press('.'))
        self.bt_equal = tk.Button(self.parent, text="=", command=lambda: self.button_press("="))
        self.bt_clear = tk.Button(self.parent, text="Limpar", command=self.clear)
        self.bt_quit = tk.Button(self.parent, text="Sair", command=self.parent.destroy)
        self.bt_delete = tk.Button(self.parent, text="Del", command=lambda: self.button_press('Delete'))
        self.parent.bind("<Escape>", lambda event=None: self.parent.destroy())

    def run(self):
        self.mount_gui()
        self.parent.mainloop()

    def mount_gui(self):
        self.display.grid(row=0, column=0, columnspan=4, sticky="ewns", ipady=5, padx=2, pady=2)
        self.bt0.grid(row=4, column=0, sticky="ewns", padx=2, pady=2)
        self.bt1.grid(row=3, column=0, sticky="ewns", padx=2, pady=2)
        self.bt2.grid(row=3, column=1, sticky="ewns", padx=2, pady=2)
        self.bt3.grid(row=3, column=2, sticky="ewns", padx=2, pady=2)
        self.bt4.grid(row=2, column=0, sticky="ewns", padx=2, pady=2)
        self.bt5.grid(row=2, column=1, sticky="ewns", padx=2, pady=2)
        self.bt6.grid(row=2, column=2, sticky="ewns", padx=2, pady=2)
        self.bt7.grid(row=1, column=0, sticky="ewns", padx=2, pady=2)
        self.bt8.grid(row=1, column=1, sticky="ewns", padx=2, pady=2)
        self.bt9.grid(row=1, column=2, sticky="ewns", padx=2, pady=2)
        self.bt_addition.grid(row=3, column=3, sticky="ewns", padx=2, pady=2)
        self.bt_subtraction.grid(row=2, column=3, sticky="ewns", padx=2, pady=2)
        self.bt_division.grid(row=4, column=3, sticky="ewns", padx=2, pady=2)
        self.bt_mutiplication.grid(row=1, column=3, sticky="ewns", padx=2, pady=2)
        self.bt_decimal_point.grid(row=4, column=1, sticky="ewns", padx=2, pady=2)
        self.bt_equal.grid(row=4, column=2, sticky="ewns", padx=2, pady=2)
        self.bt_delete.grid(row=5, column=3, sticky="wens", padx=2, pady=2)
        self.bt_clear.grid(row=5, column=1, columnspan=2, sticky="ewns", padx=2, pady=2)
        self.bt_quit.grid(row=5, column=0, sticky="ewns", padx=2, pady=2)

    def clear(self):
        self.display_stringvar.set("")
        self.math_expression = None

    def only_number_entry(self, button, operation):
        isvalid = False
        numbers = "0123456789"
        operators = "+-*/"
        string = self.display_stringvar.get()
        index = len(string)
        str_size = index

        if operation == '0':
            index -= 1
            isvalid = True

        if str_size == 0:
            isvalid = button in numbers
        else:
            last_char = string[index - 1]
            if last_char in numbers and button in numbers or last_char in numbers and button in operators or last_char in numbers and button == ".":
                isvalid = True
            elif last_char == "." and button in numbers:
                isvalid = True
            elif last_char in operators and button in numbers:
                isvalid = True
        return isvalid

    def button_press(self, button):
        index = len(self.display_stringvar.get())
        if button == "Delete":
            index -= 1
            self.display.delete(index, 'end')
        elif button == "=" and self.expression_check():
            self.calc_expression()
        else:
            self.display.insert(index, button)

    def command_calc(self, event=None):
        if self.expression_check():
            self.calc_expression()

    def expression_check(self):
        isvalid = False
        string = self.display_stringvar.get()
        index = len(string)
        if index == 0:
            isvalid = False
        else:
            index -= 1
            last_char = string[index]
            if last_char in "+-*/.":
                isvalid = False
            elif last_char in "0123456789":
                isvalid = True
        return isvalid

    def prepare_expression(self):
        elements = []
        index = 0
        operators = "+-*/"
        for char in self.display_stringvar.get():
            if len(elements) == 0 and char in "0123456789":
                elements.append(char)
            elif len(elements) > 0 and char in operators:
                elements.append(char)
                index += 1
            elif elements[index] in operators:
                elements.append(char)
                index += 1
            else:
                elements[index] += char
        self.math_expression = elements

    def calc_expression(self, event=None):
        self.prepare_expression()
        while "*" in self.math_expression or "/" in self.math_expression:
            index = 0
            for element in self.math_expression:
                if element in '/*':
                    value1 = float(self.math_expression[index - 1])
                    value2 = float(self.math_expression[index + 1])
                    if element == '*':
                        result = str(value1 * value2)
                    elif element == '/':
                        result = str(value1 / value2)
                    self.math_expression[index] = result
                    self.math_expression.pop(index + 1)
                    self.math_expression.pop(index - 1)
                    break
                index += 1
        while len(self.math_expression) > 1:
            index = 0
            for element in self.math_expression:
                if element in '+-':
                    value1 = float(self.math_expression[index - 1])
                    value2 = float(self.math_expression[index + 1])
                    if element == '+':
                        result = str(value1 + value2)
                    elif element == '-':
                        result = str(value1 - value2)
                    self.math_expression[index] = result
                    self.math_expression.pop(index + 1)
                    self.math_expression.pop(index - 1)
                    break
                index += 1
        final_result = round(float(self.math_expression[0]), 1)
        if final_result % 1 == 0:
            final_result = int(final_result)
        final_result = str(final_result)

        self.display_stringvar.set(final_result)


if __name__ == "__main__":
    calc = Calc()
    calc.run()
