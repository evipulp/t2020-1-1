def calculator(a, b, typeOfOperation):
  if (typeOfOperation == "add") :
    return a + b;
  elif (typeOfOperation == "sub") :
    return a - b;
  elif (typeOfOperation == "multi") :
    return a * b;
  elif typeOfOperation == 'div' :
        return a / b;
  else:
        return 'Please provide valid input!'

a = float(input("Please enter argument a:"));
b = float(input("Please enter argument b:"));
typeOfOperation = input("Please enter type of operation:");

result = calculator(a, b, typeOfOperation);
print(result);
