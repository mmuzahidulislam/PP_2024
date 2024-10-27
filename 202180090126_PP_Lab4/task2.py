import re
import pint

ureg = pint.UnitRegistry()

print("Welcome to the Metric-to-English Conversion Assistant!")
print("Question Format: How many <unit> are in <number> <unit>?")
def converter():
    while True:
        question = input("\nEnter your question (or type 'quit' to exit): ").strip().lower()

        if question == 'quit':
            print("Goodbye!")
            break

        pattern = r"how many (\w+) are in ([\d\.]+) (\w+)\?"
        match = re.search(pattern, question)

        if not match:
            print("Invalid question format. Please follow the question format on top.")
            continue

        to_unit = match.group(1)
        amount = float(match.group(2))
        from_unit = match.group(3)

        try:
            from_quantity = amount * ureg[from_unit]
            converted_quantity = from_quantity.to(to_unit)
            print(f"{amount} {from_unit} is equal to {converted_quantity.magnitude:.2f} {to_unit}.")
        except pint.DimensionalityError:
            print(f"Error: Cannot convert from {from_unit} to {to_unit} (different dimensions).")
        except Exception as e:
            print(f"Error: {str(e)}")

converter()
