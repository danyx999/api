import tkinter as tk
from tkinter import ttk

GEOMETRY = "550x140"


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Graphical Calculator")
        self.geometry(GEOMETRY)
        self.mainFrame = tk.Frame(self)
        self.mainFrame.grid(column=0, row=0)
        self.label = tk.Label(
            self.mainFrame,
            text="Enter your numbers (you can enter 2 or 3 numbers separated with ',')",
        )
        self.label.grid(column=0, row=0)
        self.numberEntry = tk.Entry(self.mainFrame, width=60)
        self.numberEntry.grid(column=0, row=1)

        self.resultLabel = tk.Label(self.mainFrame, text="Results")
        self.resultLabel.grid(column=0, row=2)
        self.resultText = tk.Text(self.mainFrame, width=45, height=3, state="disabled")
        self.resultText.grid(column=0, row=3)

        self.radioButtonFrame = tk.Frame(self)
        self.radioButtonFrame.grid(column=1, row=0)
        self.choiceLabel = tk.Label(
            self.radioButtonFrame, text="Choose from the options"
        )
        self.choiceLabel.grid(column=0)
        self.modeChoice = tk.IntVar(value=0)
        self.radioButtonText = ["LCM", "GCD", "Prime number product"]
        for value, text in enumerate(self.radioButtonText):
            self.modeChoiceRadioButton = tk.Radiobutton(
                self.radioButtonFrame,
                variable=self.modeChoice,
                value=value,
                text=text,
                compound="left",
            )
            self.modeChoiceRadioButton.grid(column=0, sticky="W")

        self.enterButton = tk.Button(
            self, text="Enter", command=self.getChoiceAndNumbers
        )
        self.enterButton.grid(column=0, row=2)
        self.deleteButton = tk.Button(self, text="Delete", command=self.deleteText)
        self.deleteButton.grid(column=0, row=2, columnspan=2)
        self.quitButton = tk.Button(self, text="Quit", command=quit)
        self.quitButton.grid(column=1, row=2)

    def getChoiceAndNumbers(self) -> None:
        pass

    def deleteText(self) -> None:
        self.numberEntry.delete("1.0", "end")
        self.resultText.config(state="normal")
        self.resultText.delete("1.0", "end")
        self.resultText.config(state="disabled")


class PrimeNumberProduct:
    ProductList: list[int]

    def getPrimeNumberProduct(self, numberToConvert: int) -> None:
        primeNumbers = []
        tempNum = numberToConvert

        for num in range(2, numberToConvert + 1):
            for divisor in range(2, num):
                if num % divisor == 0:
                    break
            else:
                primeNumbers.append(num)

        primeNumbers.reverse()

        while tempNum > 1:
            for primeNum in primeNumbers:
                if tempNum % primeNum == 0:
                    self.ProductList.append(primeNum)
                    tempNum /= primeNum

    def __str__(self) -> str:
        pass


class Gcd:
    Result: int

    def getGcd(self, num1: int, num2: int) -> int:
        if num2 > num1:
            temp = num1
            num1 = num2
            num2 = temp

        for divisor in range(2, num1):
            if num1 % divisor == 0 and num2 % divisor == 0:
                return divisor
        else:
            return 1

    def getGcd2Nums(self, nums: list[int]) -> None:
        num1, num2 = nums
        self.Result = self.getGcd(num1, num2)

    def getGcd3Nums(self, nums: list[int]) -> None:
        num1, num2, num3 = nums
        self.Result = self.getGcd(self.getGcd(num1, num2), num3)

    def __str__(self) -> str:
        pass


class Lcm:
    Result: int

    def getLcm2Nums(self, nums: list[int]) -> None:
        num1, num2 = nums

    def getLcm3Nums(self, nums: list[int]) -> None:
        num1, num2, num3 = nums

    def __str__(self) -> str:
        pass


def main() -> None:
    app = App()
    app.mainloop()


main()
