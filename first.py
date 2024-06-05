#SALES PREDICTION USING PYTHON

import tkinter as tk

def predict_sales():
    try:
        # Get the input values
        tv_ads = float(entry_tv.get())
        radio_ads = float(entry_radio.get())
        newspaper_ads = float(entry_newspaper.get())
        
        # Define coefficients for linear regression
        tv_coef = 0.05
        radio_coef = 0.08
        newspaper_coef = 0.02
        intercept = 50
        
        # Calculate predicted sales using predetermined coefficients
        predicted_sales = intercept + tv_coef * tv_ads + radio_coef * radio_ads + newspaper_coef * newspaper_ads
        
        # Display the predicted sales
        result_label.config(text=f"Predicted Sales: {predicted_sales}")
    except Exception as e:
        result_label.config(text=f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Sales Prediction")

# Create labels and entry fields for input
tk.Label(root, text="TV Advertising:").grid(row=0, column=0)
entry_tv = tk.Entry(root)
entry_tv.grid(row=0, column=1)

tk.Label(root, text="Radio Advertising:").grid(row=1, column=0)
entry_radio = tk.Entry(root)
entry_radio.grid(row=1, column=1)

tk.Label(root, text="Newspaper Advertising:").grid(row=2, column=0)
entry_newspaper = tk.Entry(root)
entry_newspaper.grid(row=2, column=1)

# Create predict button
predict_button = tk.Button(root, text="Predict Sales", command=predict_sales)
predict_button.grid(row=3, column=0, columnspan=2)

# Create label to display result
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

# Run the main event loop
root.mainloop()