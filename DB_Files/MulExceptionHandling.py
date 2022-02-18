# list1 =  [2,4,0,'a',5,7,'f',9,0]
# x = int(input("enter range"))
# for i in range(x):
#     try:
#         y= 30/list1[i]
#         print(y)
#     except ZeroDivisionError:
#         print("Error:Division by zero")
#     except TypeError:
#         print("Error: dividing number with character is not possible")
#     except IndexError:
#         print("Error: index out of range ")
#
## -----------------
# x= int(input("enter a number\n"))
# try:
#     if x > 18:
#         raise ValueError(x)
# except ValueError: if x>18 condition is true it raises error and goes to except block
#     print(x,"is age of adult")
# else: # if x>18 condition is false then it goes to else block
#     print(x,"is not adult age")
#
## -----------------
# y = int(input("enter a number to divide"))
# try:
#     x = 10/y
#     print(x)
# except ZeroDivisionError:
#     print("division by zero error")

## -----------------
# try:
#     # F = open("text1","w")
#     F = open("text1","r") # opening file in read mode
#     F.write("printing the content") #trying to write into the file but it is opened only in read mode so it gives an error
#     # print(F.read())
# except IOError:
#     print("Error: error while opening file or  write to it")
# finally: #whether try block as error or not finally block executes every time
#     F.close() #when ever file is opened e need to close the file so we use finally.
## -----------------
#
# list1 =  [2,4,0,'a',5,7,'f',9,0]
# x = int(input("enter range"))
# try:
#     if x>15:
#         raise ValueError(x)
# except ValueError:
#     print(x,"is greater than length of list")
#
#     try:
#         for i in range(x): #when ever it gets error it goes to except block and terminates
#             y= 30/list1[i]
#             print(y)
#     except ZeroDivisionError:
#         print("Error:Division by zero")
#     except TypeError:
#         print("Error: dividing number with character is not possible")
#     except IndexError:
#         print("Error: index out of range ")
#     except ValueError:
#         print("Error: Value exceed index range ")

## -----------------
# list1 =  [2,4,0,'a',5,7,'f',9,0]
# x = int(input("enter range"))
# try:
#     if x>15:
#         raise ValueError(x)
# except ValueError:
#     print(x,"is greater than length of list")
#     for i in range(x):
#         try:
#             # for i in range(x): #when ever it gets error it goes to except block and terminates
#             y= 30/list1[i]
#             print(y)
#         except ZeroDivisionError:
#             print("Error:Division by zero")
#         except TypeError:
#             print("Error: dividing number with character is not possible")
#         except IndexError:
#             print("Error: index out of range ")
#         except ValueError:
#             print("Error: Value exceed index range ")