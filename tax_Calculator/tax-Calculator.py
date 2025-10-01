import customtkinter as ctk


class TaxCalculator:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title('Tax Calculator')
        self.window.geometry('350x200')
        self.window.resizable(False, False)

        self.padding: dict = {'padx': 20, 'pady': 10}

        self.income_lable = ctk.CTkLabel(self.window, text='Income')
        self.income_lable.grid(row=0, column=0, **self.padding)

        self.income_entry = ctk.CTkEntry(self.window)
        self.income_entry.grid(row=0, column=1, **self.padding)

        self.tax_rate_lable = ctk.CTkLabel(self.window, text='Percent')
        self.tax_rate_lable.grid(row=1, column=0, **self.padding)

        self.tax_rate_entry = ctk.CTkEntry(self.window)
        self.tax_rate_entry.grid(row=1, column=1, **self.padding)

        self.result_lable = ctk.CTkLabel(self.window, text='Tax')
        self.result_lable.grid(row=2, column=0, **self.padding)

        self.result_entry = ctk.CTkEntry(self.window)
        self.result_entry.grid(row=2, column=1, **self.padding)

        self.calculate_btn = ctk.CTkButton(self.window, text='Calculate', command=self.calculate_tax)
        self.calculate_btn.grid(row=3, column=1, **self.padding)

        self.clear_input_btn = ctk.CTkButton(self.window, text='Clear Inputs', command=self.clear_input)
        self.clear_input_btn.grid(row=3, column=0, padx=10, pady=5)

    def update_result(self, text: str):
        self.result_entry.delete(0, ctk.END)
        self.result_entry.insert(0, text)

    def calculate_tax(self):
        try:
            income: float = float(self.income_entry.get())

            tax_rate: float = float(self.tax_rate_entry.get())

            self.update_result(f'{income * (tax_rate / 100):,.2f}')

        except ValueError:
            self.update_result('Invalid Input ')

    def clear_input(self):
        self.result_entry.delete(0, ctk.END)
        self.tax_rate_entry.delete(0, ctk.END)
        self.income_entry.delete(0, ctk.END)

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    tc = TaxCalculator()
    tc.run()
