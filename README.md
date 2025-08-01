# 💰 Budget App

A Python utility to manage budget categories with deposits, withdrawals, transfers, and to visualize spending via a percentage chart.

---

## Objective

Implement the class:

<pre><code class="language-python">
class Category:
    def __init__(self, name):
        """Create a budget category with an empty ledger."""
        ...
</code></pre>

Methods to implement:
- **deposit(amount, description='')**  
  Record a positive amount with an optional description.
- **withdraw(amount, description='')**  
  Record a negative amount if funds are sufficient; return `True`/`False`.
- **get_balance()**  
  Return the current balance (sum of ledger amounts).
- **transfer(amount, other_category)**  
  Move funds between categories, adding matching ledger entries; return `True`/`False`.
- **check_funds(amount)**  
  Return `False` if `amount` exceeds balance, otherwise `True`.

Printing a `Category` instance should produce:

<pre>
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
</pre>

---

## Spend Chart

Implement the function:

<pre><code class="language-python">
def create_spend_chart(categories):
    """Return a bar chart of percentage spent per category."""
</code></pre>

- Calculate each category’s withdrawal total.
- Compute percentage of total spending, rounded **down** to the nearest 10.
- Build a vertical bar chart using `o` markers and labels 0–100.
- Draw a horizontal line and write category names vertically below.

Example:

<pre>
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
</pre>

---

## Constraints

- **No external libraries**—pure Python.
- Start times and inputs are assumed valid.
- Chart supports up to **4 categories**.
- Minutes in transactions < 60; hours ≥ 0.
