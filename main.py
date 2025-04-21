from tkinter import *
#screen
screen=Tk()
screen.title("BMI Calculator")
screen.minsize(width=400,height=300)

#input height
input_height=Entry()
input_height.place(relx=0.5, rely=0.35, anchor="center") #Slightly above the midpoint

#input weight
input_weight=Entry()
input_weight.place(relx=0.5,rely=0.55,anchor="center") #Slightly below the midpoint.relx and rely values must be between 0 and 1!

def calculation_values():
    try:
        input_1=float(input_height.get())/100
        input_2=float(input_weight.get())
        calculation_result=float(input_2/(input_1**2))
        if calculation_result < 18.5:
            comment="Underweight"
        elif 18.5 <= calculation_result <= 24.9:
            comment="Healthy weight"
        elif 25.0<= calculation_result <=29.9:
            comment="Overweight"
        elif 30.0<= calculation_result <= 34.9:
            comment="Class 1 obesity"
        elif 35.0 <= calculation_result <=39.9:
            comment="Class 2 obesity"
        elif calculation_result >= 40:
            comment="Class 3 obesity"

        result_label.config(text=f"Height: {input_1*100}cm, Weight: {input_2}kg,\n BMI: {calculation_result:.2f} - {comment}") # Label'ı güncelle:

    except:

        result_label.config(text="Please enter true values.Only numbers!")

#weight_button
calculate_button=Button(text="Calculate",command=calculation_values)
calculate_button.place(relx=0.5,rely=0.70,anchor="center")

#Label for height
hight_label=Label(text="Please enter your height in cm!",font=("Arial", 14))
hight_label.place(relx=0.5,rely=0.27,anchor="center")

#Label for weight
weight_label=Label(text="Please enter your weight in kg!",font=("Arial", 14))
weight_label.place(relx=0.5,rely=0.47,anchor="center")


#Label for result
result_label=Label()
result_label.config(font=("Arial", 14, "bold"))
result_label.place(relx=0.5,rely=0.83,anchor="center")

screen.mainloop()
