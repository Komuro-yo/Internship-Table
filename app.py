import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Load Table 1
    table1 = pd.read_csv('Table_Input.csv')

    # For Table 2 Calculations
    a5_value = int(table1[table1.iloc[:, 0] == 'A5'].iloc[0, 1])
    a20_value = int(table1[table1.iloc[:, 0] == 'A20'].iloc[0, 1])
    a15_value = int(table1[table1.iloc[:, 0] == 'A15'].iloc[0, 1])
    a7_value = int(table1[table1.iloc[:, 0] == 'A7'].iloc[0, 1])
    a13_value = int(table1[table1.iloc[:, 0] == 'A13'].iloc[0, 1])
    a12_value = int(table1[table1.iloc[:, 0] == 'A12'].iloc[0, 1])

    # Perform Calculations
    alpha = a5_value + a20_value
    beta = a15_value / a7_value
    charlie = a13_value * a12_value

    # Create Table 2
    table2 = [
        {"Category": "Alpha", "Value": alpha},
        {"Category": "Beta", "Value": beta},
        {"Category": "Charlie", "Value": charlie}
    ]

    return render_template('index.html', table1=table1.to_dict(orient='records'), table2=table2)

if __name__ == '__main__':
    app.run(debug=True)
