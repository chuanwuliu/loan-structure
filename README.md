# Home Loan Restructuring

## Introduction

When you borrow a home loan from bank. There are usually two types of mortgage products:
fixed rate loan and variable rate loan. A fixed rate loan usually has a lower interest rate fixed
for a number of years, while a variable rate loan has a fluctuate interest rate.
The advantage of having a variable rate loan is that you can link it to an offset bank account.
Your saving in the offset account will be used to deduct the principle that generates interest.
You usually need to pay a annual fee for having an offset account.

Given the mount of borrowing, you can choose either all fixed rate or all variable rate or partial-partial.
This is the loan structure. This software is a light-weight productive model that help you to determine the best
split between fixed rate and variable rate.

## Requirements
1. The software is running on Python 3.6.
2. (Optional) Create and activate a virtual environment
    ```bash
    python -m venv venvname
    source venvname/bin/activate
    ```
3. Install dependencies with pip
    ```bash
    pip install -r requirements.txt
    ```

## Net wealth depending loan structure.
Before running the code you can configure your variables such as interest rate, monthly salary
and living cost in `config.py`. Then setup the total loan amount in `plot.py`. To plot the relationship
between the net wealth and the amount of variable rate loan, simply execute
```bash
python plot.py
```
