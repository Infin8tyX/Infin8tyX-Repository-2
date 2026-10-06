
# Python Lesson: Dictionaries

## What is a dictionary?

A **dictionary** (`dict`) is a way to store data as **key–value pairs**. Instead of accessing items by position (like a list, using `0`, `1`, `2`...), you access them by a **name** you choose — the "key."

Think of it like a real dictionary: you look up a *word* (the key) to find its *definition* (the value). Or think of a product label: you look up `"price"` to find `699.99`.

```python
{
    "key1": value1,
    "key2": value2,
}
```

Dictionaries use **curly braces** `{ }`, and each key is connected to its value with a colon `:`. Pairs are separated by commas.

---

## Part 1: A single dictionary

Let's start with one item — a vacuum for sale:

```python
vac = {
    "name": "Dyson V15 Cordless Vacuum",
    "price": 699.99,
    "department": "Appliances",
    "description": "High-powered cordless vacuum with laser dust detection."
}
```

Here, `vac` is a dictionary with **four keys**: `"name"`, `"price"`, `"department"`, and `"description"`. Each key points to a value — some are strings, one is a number (a `float`).

### Accessing values

To get a value out of a dictionary, use square brackets with the key name (as a string):

```python
print(vac["name"])
print(vac["price"])
```

**Output:**
```
Dyson V15 Cordless Vacuum
699.99
```

You can also combine multiple lookups in one `print()` call:

```python
print(vac["name"], vac["price"])
```

**Output:**
```
Dyson V15 Cordless Vacuum 699.99
```

### Important: keys vs. values

- The **key** (`"name"`, `"price"`, etc.) is always a fixed label you use to look something up.
- The **value** (`"Dyson V15 Cordless Vacuum"`, `699.99`, etc.) is the actual data.
- If you try to access a key that doesn't exist — like `vac["color"]` — Python will raise a `KeyError`, because that key was never defined.

### Try it yourself

```python
print(vac["department"])
print(vac["description"])
```

What do you think each line will print? Run it and check.

### Changing a value

Dictionaries are **mutable**, meaning you can change their values after creating them:

```python
vac["price"] = 649.99
print(vac["price"])
```

**Output:**
```
649.99
```

---

## Part 2: A list of dictionaries

One dictionary can represent one item. But what if you have a whole *store* full of items? You can put many dictionaries into a **list**, giving you a list of dictionaries:

```python
best_buy_items = [
    {
        "name": "Samsung 55\" 4K UHD TV",
        "price": 429.99,
        "department": "Televisions",
        "description": "55-inch Ultra HD Smart TV with HDR and built-in streaming apps."
    },
    {
        "name": "Sony Noise Cancelling Headphones",
        "price": 299.99,
        "department": "Audio",
        "description": "Wireless over-ear headphones with industry-leading noise cancellation."
    },
    {
        "name": "Apple iPhone 15",
        "price": 999.99,
        "department": "Mobile Phones",
        "description": "Latest Apple smartphone with A17 chip and advanced camera system."
    }
]
```

Now `best_buy_items` is a **list**, and each *element* of that list is a **dictionary**. This is a very common pattern in real-world programming — think of it like a spreadsheet, where each row is one dictionary and the whole spreadsheet is the list.

### Accessing one item in the list

Since it's a list, you can use a normal index to grab one dictionary:

```python
print(best_buy_items[0])
```

**Output:**
```
{'name': 'Samsung 55" 4K UHD TV', 'price': 429.99, 'department': 'Televisions', 'description': '55-inch Ultra HD Smart TV with HDR and built-in streaming apps.'}
```

That prints the *whole dictionary*. To get just one value from it, you combine list indexing **and** dictionary key access:

```python
print(best_buy_items[0]["name"])
print(best_buy_items[0]["price"])
```

**Output:**
```
Samsung 55" 4K UHD TV
429.99
```

Read this left to right: "Get item `0` from the list, then get the `"name"` key from that dictionary."

---

## Part 3: Displaying all items with `enumerate`

Printing one item at a time by typing out `best_buy_items[0]`, `best_buy_items[1]`, etc. doesn't scale. Instead, we can loop through the whole list — and use `enumerate()` to keep track of each item's index as we go.

### What does `enumerate` do?

Normally, a `for` loop over a list just gives you each item:

```python
for item in best_buy_items:
    print(item["name"])
```

But if we also want to know the **position** of each item (so a user can type a number to choose one), we wrap the list in `enumerate()`:

```python
for index, item in enumerate(best_buy_items):
    print(index, item["name"])
```

`enumerate()` hands back two things each time through the loop: the **index** (starting at 0) and the **item** itself. That's why we write `index, item` instead of just `item`.

### Putting it in a function

```python
def show_items(items):
    for index, item in enumerate(items):
        print(index, ":", item["name"])

show_items(best_buy_items)
```

**Output:**
```
0 : Samsung 55" 4K UHD TV
1 : Sony Noise Cancelling Headphones
2 : Apple iPhone 15
```

Now a user browsing this list can see a numbered menu of every item.

---

## Part 4: Letting the user choose an item

Now let's combine everything: show the numbered list, ask the user to type a number, and look up the item they picked.

```python
def choose_item():
    show_items(best_buy_items)
    x = int(input("Which item number do you want to buy? "))
    print(best_buy_items[x])

choose_item()
```

### How it works, step by step

1. `show_items(best_buy_items)` prints the numbered menu.
2. `input("Which item number do you want to buy? ")` pauses and waits for the user to type something. `input()` always returns a **string**, even if the user types a number.
3. `int(...)` converts that string into an actual integer, so we can use it as a list index.
4. `best_buy_items[x]` uses that number to look up the matching dictionary in the list, and we print the whole thing.

### A word of caution

What happens if the user types `99` (a number with no matching item), or types `"television"` instead of a number? Try it and see what error you get. This is a great example of why real programs need to **validate input** — we'll cover that (`try`/`except`) in a later lesson.

---

## Summary

| Concept | Example | What it does |
|---|---|---|
| Create a dict | `vac = {"name": "Dyson", "price": 699.99}` | Stores key–value pairs |
| Access a value | `vac["name"]` | Looks up the value for a given key |
| Change a value | `vac["price"] = 649.99` | Updates the value for a key |
| List of dicts | `best_buy_items = [ {...}, {...} ]` | Stores many dicts together |
| Access nested | `best_buy_items[0]["name"]` | Index into the list, then key into the dict |
| `enumerate()` | `for i, item in enumerate(items):` | Loops with both index and item |
