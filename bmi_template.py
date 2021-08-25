# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# BMI

from tkinter import *


class Userinterface:

    def __init__(self):
        self.__mainwindow = Tk()

        # TODO: Change the title of the main window to be "BMI calculator"
        self.__mainwindow.title("BMI calculator")

        # TODO: Add GUI components to make the GUI understandable for the
        # user, for example labels to indicate what the user should write
        # in the Entry-components.
        self.label_weight= Label(self.__mainwindow, text="Enter your Weight(KG)")
        self.label_height = Label(self.__mainwindow, text="Enter your Height(CM)")

        # TODO: Create an Entry-component for the weight.
        self.__weight_value = Entry(self.__mainwindow,width=50)

        # TODO: Create an Entry-component for the height.

        self.__height_value = Entry(self.__mainwindow,width=50)

        # TODO: Create a Button that will call the calculate_BMI-method.
        # TODO: Change the colour of the Button to something else than
        # the default colour.
        self.__calculate_button = Button(self.__mainwindow, bg='red',text='Click to BMI calculate', command=self.calculate_BMI)
        # TODO: Create a Label that will show the decimal value of the BMI 
        # after it has been calculated.
        self.__result_text =  Label(self.__mainwindow,text='')
        # TODO: Create a Label that will show a verbal description of the BMI
        # after the BMI has been calculated.
        self.__explanation_text = Label(self.__mainwindow,text='')
        # TODO: Create a button that will call the stop-method.
        self.__stop_button = Button(self.__mainwindow,text='Quit!',command=self.stop)

        # TODO: Place the components in the GUI as you wish.
        # If you read the Gaddis book, you can use pack here instead of grid!

        self.__weight_value.grid(row=1, column=0)
        self.label_weight.grid(row=2,column=0)
        self.__height_value.grid(row=4, column=0)
        self.label_height.grid(row=5,column=0)


        self.__result_text.grid(row=7, column=0)
        self.__explanation_text.grid(row=8, column=0)

        self.__calculate_button.grid(row=10, column=0)
        self.__stop_button.grid(row=11, column=0)




    # TODO: Implement this method.
    def calculate_BMI(self):
        """ Section b) This method calculates the BMI of the user and
            displays it. First the method will get the values of
            height and weight from the GUI components
            self.__height_value and self.__weight_value.  Then the
            method will calculate the value of the BMI and show it in
            the element self.__result_text. 
            
            Section e) Last, the method will display a verbal
            description of the BMI in the element
            self.__explanation_text. 
        """
        try:
            weight = float(self.__weight_value.get())
            height = float(self.__height_value.get())

            if weight < 0 or height < 0:
                raise TypeError

            bmi = weight / (height / 100) ** 2
            self.__result_text['text'] = str(format(bmi, ',.2f'))

            if 18.5 < bmi < 25:
                self.__explanation_text['text']='Your weight is normal.'

            elif bmi>25:
                self.__explanation_text['text']='You are overweight.'


            else:
                self.__explanation_text['text']='You are underweight.'

        except TypeError:
            self.reset_fields()
            self.__explanation_text['text'] = 'Error: height and weight must be positive.'


        except ValueError:
            self.reset_fields()
            self.__explanation_text['text']='Error: height and weight must be numbers.'





    # TODO: Implement this method.
    def reset_fields(self):
        """ In error situations this method will zeroize the elements
            self.__result_text, self.__height_value, and self.__weight_value.

        """
        self.__weight_value.delete(0,100)
        self.__height_value.delete(0,100)







    def stop(self):
        """ Ends the execution of the program.
        """
        self.__mainwindow.destroy()

    def start(self):
        """ Starts the mainloop. 
        """
        self.__mainwindow.mainloop()


def main():
    ui = Userinterface()
    ui.start()


main()
