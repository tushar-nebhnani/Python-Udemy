"""
Questions:
1. What happens if an exception occurs inside the try block and there is no corresponding except block to handle it?
2. What is a ValueError?
3. What's the difference between a bare except statement (except:) and catching a specific exception (except ValueError:)?
4. What will be the output of this codes?
    1. def my_function():
        try:
            return 'success'
        except:
            return 'error'
        finally:
            print('cleanup')


    2. def my_func():
        try:
            print('Start')
        raise ValueError('Something is wrong')
        except TypeError:
            print('TypeError')
        except:
            print('Something else')

    3.  try:
            print('hello' + 5)
        except TypeError:
            print('Type error occurred')
        except:
        print('Some other error')

    4.  try:
            print(1 / 'a')
        except (ValueError, TypeError) as e:
            print(e)

    5.  def check_value(x):
            if x < 0:
                raise ValueError('Value cannot be negative')
            return x

        try:
            check_value(-5)
        except ValueError as e:
            print(e)

    6.  try:
            print('try')
        raise Exception('An error')
            except Exception as e:
            print('except')
            raise e
        finally:
            print('finally')

    7.  try:
            print('try block')
            raise IndexError('This is an index error')
        except ValueError:
            print('ValueError caught')
        finally:
            print('finally block')

Points to remenber:
1. You're right that the program will crash. If an exception occurs in the try block and there's no matching except block to catch it, the program terminates and displays a traceback, which is a detailed report of the error. Python does allow for a single try block without an except block, but it must be followed by a finally or else block. However, for the purpose of handling exceptions and preventing a crash, you need an except block.

2. A ValueError is raised when a function receives an argument of the correct type but an inappropriate value. For example, trying to convert the string 'hello' into an integer using int('hello') will raise a ValueError, because 'hello' is a string but doesn't contain a valid integer representation.

3. An IndentationError is a specific type of SyntaxError that arises when the spacing or indentation of your code is incorrect. Python relies on indentation to define code blocks (like those inside functions, loops, or conditional statements), so incorrect indentation is a critical syntax violation.

4. The as keyword does create an alias, but its primary purpose is not just to "write faster." It's used to assign the exception object itself to a variable (in your example, e). This variable then holds all the information about the exception, such as the error message, which you can then access and use within your except block. This allows you to handle the error more dynamically and provide more informative feedback to the user.

5. The raise statement is used to forcefully trigger an exception. While it can be used to raise custom exceptions you've defined, it's also commonly used to re-raise a built-in exception after you've handled it, or to raise a built-in exception under a specific condition in your code.

6.  The try block starts, and print('Start') is executed.
    The raise ValueError('Something is wrong') statement is encountered, and a ValueError is raised.
    The program looks for an except block that can handle a ValueError.
    The first except block is except TypeError, which doesn't match ValueError, so it's skipped.
    The second except block is a bare except (or it could also be except Exception), which catches any exception. It catches the ValueError.
    The code in this second except block is executed, printing Something else.
"""