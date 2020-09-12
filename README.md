# EPAi session8 assignment
---

The following requirements need to be met to successfully run the code : 
Dependencies  :   python > = 3.7.4 \
Python packages  :   refer to requirements.txt

---
## Session8 objectives
This assignment, helps to code the concepts that are learnt in the session 8 of the EPAi module. 
In particular, this assignment focuses on the following topics  : 

---

The test cases can be executed by executing _pytest_, from python shell
 - Global and Local Scopes
 - Non Local Scopes
 - Closures
 
---

### Functions


**q1_check_doc_str_length()**

    Global Function
    Task :  Write a closure that takes a function and then check whether the function passed has a docstring with more
    than 50 characters. 50 is stored as a free variable.
    print - "Valid Docstring" when condition is satisfied and "Invalid Docstring" otherwise
     : param func :  Any function
     : return :  local function check_doc_str_length

**check_doc_str_length(func :  'any function') -> bool**

        Local Function
        Check length of doc string
         : param func :  Any function
         : return :  bool

**q2_get_next_fib_number()**

    Global Function
    Task :  Write a closure that gives you the next Fibonacci number
     : return :  local function generate_fib_sequence

**generate_fib_sequence()**

        Local Function :  Generates fib sequence
         : return :  next fib number based on the previous two (non-local) free variables

**add(a, b)**

    Generic method to add two objects, on which + is defined
     : param a :  object 1
     : param b :  object 2
     : return :  the sum of a and b

**mul(a, b)**

    Generic method to multiply two objects, on which * is defined
     : param a :  object 1
     : param b :  object 2
     : return :  the product of a and b

**div(a, b)**

    Generic method to divide two objects, on which / is defined
     : param a :  object 1
     : param b :  object 2
     : return :  the div of a and b

**q3_update_local_counts()**

    Task :  Write a closure that can keep a track of how many times add/mul/div functions were called, and update a
    global dictionary variable with the counts
     : return :  local function count

**count(func, \*args, \*\*kwargs)**

        Call any function
         : param func :  function name
         : param args :  positional arguments of func
         : param kwargs :  keyword arguments of func
         : return :  function result, dictionary of counts

**q4_update_counts_global(count_dict=None)**

    Task :  Modify above such that now we can pass in different dictionary variables to update different dictionaries
     : return :  local function count

**count(func, \*args, \*\*kwargs)**

        Call any function
         : param func :  function name
         : param args :  positional arguments of func
         : param kwargs :  keyword arguments of func
         : return :  function result, dictionary of counts


---

### Unit Tests

**test_readme_exists()**

    Check if the README file exists
     : return :  None

**test_readme_contents()**

    Test the length of the README file
     : return :  None

**test_readme_file_for_formatting()**

    Tests the formatting for the README file
     : return :  None

**test_function_name_had_cap_letter()**

    Checking PEP-8 guidelines for function names. Pass if all alphabets(a-z) are in small case.
     : return :  None

**test_q1_check_doc_str_length()**

    Test the closure q1_check_doc_str_length
     : return :  None

**test_q2_get_next_fib_number()**

    Test the closure q2_get_next_fib_number
     : return :  None

**test_q3_update_local_counts()**

    Test the closure q3_update_local_counts
     : return :  None

**test_q4_update_counts_global()**

    Test the closure q4_update_counts_global
     : return :  None

---

#### 