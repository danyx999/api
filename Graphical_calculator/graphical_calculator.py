import tkinter as tk
from tkinter import ttk

GEOMETRY = "575x170"


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Graphical Calculator")
        self.geometry(GEOMETRY)
        self.mainFrame = tk.Frame(self)
        self.mainFrame.grid(column=0, row=0)
        self.label = tk.Label(
            self.mainFrame,
            text="Enter your numbers as integers (you can enter 2 or 3 numbers separated with ',')\nFor prime number product you can enter 1 number",
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
        self.choiceLabel.grid(column=0, pady=10)
        self.menu = {
            "LCM": self.doLcm,
            "GCD": self.doGcd,
            "Prime number product": self.doPrimeNumberProduct,
        }
        self.modeChoice = tk.StringVar(value="LCM")
        for text in self.menu.keys():
            self.modeChoiceRadioButton = tk.Radiobutton(
                self.radioButtonFrame,
                variable=self.modeChoice,
                value=text,
                text=text,
                compound="left",
            )
            self.modeChoiceRadioButton.grid(column=0, sticky="W")

        self.buttonFrame = tk.Frame(self)
        self.buttonFrame.grid(row=1, columnspan=2, pady=15)
        self.enterButton = tk.Button(
            self.buttonFrame, text="Enter", command=self.startChosenFunction
        )
        self.enterButton.grid(column=0, row=0, padx=55)
        self.deleteButton = tk.Button(
            self.buttonFrame, text="Delete", command=self.deleteText
        )
        self.deleteButton.grid(column=1, row=0, padx=55)
        self.quitButton = tk.Button(self.buttonFrame, text="Quit", command=quit)
        self.quitButton.grid(column=2, row=0, padx=55)

    def startChosenFunction(self) -> None:
        chosenFunction = self.menu.get(self.modeChoice.get())
        chosenFunction()

    def doLcm(self) -> None:
        numbers = self.getEnteredValues()
        if len(numbers) < 2 or len(numbers) > 3:
            return
        self.result = Lcm(numbers)
        self.displayResult()

    def doGcd(self) -> None:
        numbers = self.getEnteredValues()
        if len(numbers) <= 1:
            return
        self.result = Gcd(numbers)
        self.displayResult()

    def doPrimeNumberProduct(self) -> None:
        numberToConvert = self.getValueForPrimeNumberProduct()
        if numberToConvert is None:
            return
        self.result = PrimeNumberProduct()
        self.result.getPrimeNumberProduct(numberToConvert)
        self.displayResult()

    def getEnteredValues(self) -> list[int]:
        numbers = []
        temp = self.numberEntry.get()
        splitValues = temp.split(",")

        for num in splitValues:
            if self.checkNumber(num):
                numbers.append(int(num))
            else:
                self.displayErrorMessage()
                break

        return numbers

    def getValueForPrimeNumberProduct(self) -> int:
        enteredNumber = self.numberEntry.get()
        if self.checkNumber(enteredNumber):
            return int(enteredNumber)
        else:
            self.displayErrorMessage()

    def checkNumber(self, number: int) -> bool:
        try:
            int(number)
            return True
        except ValueError:
            return False

    def displayResult(self) -> None:
        self.deleteText()
        self.resultText.config(state="normal")
        self.resultText.insert("0.0", self.result)
        self.resultText.config(state="disabled")

    def displayErrorMessage(self) -> None:
        self.deleteText()
        self.resultText.config(state="normal")
        self.resultText.insert("0.0", "Incorrectly entered or separated numbers")
        self.resultText.config(state="disabled")

    def deleteText(self) -> None:
        self.resultText.config(state="normal")
        self.resultText.delete("1.0", "end")
        self.resultText.config(state="disabled")


class PrimeNumberProduct:
    ProductList: list[int] = []
    NumberToConvert: int

    def getPrimeNumberProduct(self, numberToConvert: int) -> None:
        self.NumberToConvert = numberToConvert

        while numberToConvert > 1:
            for primeNum in range(2, numberToConvert + 1):
                if numberToConvert % primeNum == 0:
                    self.ProductList.append(primeNum)
                    numberToConvert //= primeNum
                    break

        self.ProductList.sort()

    def __str__(self) -> str:
        numbers = []
        for num in self.ProductList:
            numbers.append(str(num))
        return f"{self.NumberToConvert} = {' x '.join(numbers)}"


class MyMath:
    Numbers: list[int]
    Result: int

    def __init__(self, nums: list[int]) -> None:
        self.Numbers = nums

    def getGcd(num1: int, num2: int) -> int:
        while num2 > 0:
            num1, num2 = num2, num1 % num2
        return num1

    def getLcm(num1, num2) -> float:
        return num1 * num2 / MyMath.getGcd(num1, num2)


class Gcd(MyMath):
    def __init__(self, nums: list[int]) -> None:
        super().__init__(nums)
        if len(self.Numbers) == 2:
            self.getGcd2Nums()
        else:
            self.getGcd3Nums()

    def getGcd2Nums(self) -> None:
        num1, num2 = self.Numbers
        self.Result = MyMath.getGcd(num1, num2)

    def getGcd3Nums(self) -> None:
        num1, num2, num3 = self.Numbers
        self.Result = MyMath.getGcd(MyMath.getGcd(num1, num2), num3)

    def __str__(self) -> str:
        numbers = []
        for num in self.Numbers:
            numbers.append(str(num))
        return f"GCD({', '.join(numbers)}) = {self.Result}"


class Lcm(MyMath):
    def __init__(self, nums: list[int]) -> None:
        super().__init__(nums)
        if len(self.Numbers) == 2:
            self.getLcm2Nums()
        else:
            self.getLcm3Nums()

    def getLcm2Nums(self) -> None:
        num1, num2 = self.Numbers
        self.Result = int(MyMath.getLcm(num1, num2))

    def getLcm3Nums(self) -> None:
        num1, num2, num3 = self.Numbers
        self.Result = int(MyMath.getLcm(MyMath.getLcm(num1, num2), num3))

    def __str__(self) -> str:
        numbers = []
        for num in self.Numbers:
            numbers.append(str(num))
        return f"LCM({', '.join(numbers)}) = {self.Result}"


def main() -> None:
    app = App()
    app.mainloop()


main()
