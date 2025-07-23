print("Welcome to the pattern Generator and number Analyzer!")
print("")
print("select an option:")
print("1. Right-angled Triangle")
print("2. Pyramid")
print("3. Left-angled Triangle")
print("4. Analyze a range of Number")
print("")
Pattern =int (input("Enter your pattern:"))
if Pattern ==1:
    rows = int (input ("Enter the number of rows for the pattern: "))
    print ("Pattern:")
    for i in range(1, rows + 1):
        print("*" * i)
else:
    print("Invalid choice.")


"""
Welcome to the pattern Generator and number Analyzer!

select an option:
1. Right-angled Triangle
2. Pyramid
3. Left-angled Triangle
4. Analyze a range of Number

Enter your pattern:1
Enter the number of rows for the pattern: 5
Pattern:
*
**
***
****
*****
"""
