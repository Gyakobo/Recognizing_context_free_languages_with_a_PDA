# Global Functions
def accept_string():
    print("String is accepted!")
def reject_string():
    print("String is rejected!")


# STATE Q1 - Create the stack and append '$'   
stack = ['$']

# STATE Q10
def Q10():
    if stack.pop() == '$':
        print("ε: Q10")
        print("Read 'ε'")
        print("Popped '$' from stack")
        print("Pushed 'ε' to stack\n")
        #print(f"Current stack: {stack}")
        accept_string()
    else:
        print("error")
        return

# STATE Q9
def Q9(input_str):
    cnt = 0
    for c in input_str:
        if c == 'b' and stack.pop() == 'b':
            cnt += 1
            print("b: Q9")
            print("Read 'b'")
            print("Popped 'b' from stack")
            print("Pushed 'ε' to stack")
            print("Moving to state Q9\n")
            #print(f"Current stack: {stack}\n")
        else:
            break

    if input_str[cnt] == 'a' and stack.pop() == 'a':
        print("a: Q9")
        print("Read 'a'")
        print("Popped 'a' from stack")
        print("Pushed 'ε' to stack")
        print("Moving to state Q10\n")
        #print(f"Current stack: {stack}\n")
        Q10()
    else:
        reject_string()
        return


# STATE Q4
def Q4(input_str):
    cnt = 0
    for c in input_str:
        if c == '(':
            stack.append('(')
            print("(: Q4")            
            print("Read '('")
            print("Popped 'ε' from stack")
            print("Pushed '(' to stack")
            print("Moving to state Q4\n")
            #print(f"Current stack: {stack}\n")
            cnt += 1
        else:
            break

    if input_str[cnt].isdigit():
        print(f"{input_str[cnt]}: Q4")
        print(f"Read '{input_str[cnt]}'")
        print("Popped 'ε' from stack")
        print("Pushed 'ε' to stack")
        print("Moving to state Q5\n")
        # print(f"Current stack: {stack}\n")
        Q5(input_str[cnt+1:])
    elif input_str[cnt] == '.':
        print(".: Q4")
        print("Read '.'")
        print("Popped 'ε' from stack")
        print("Pushed 'ε' to stack")
        print("Moving to state Q6\n")
        #print(f"Current stack: {stack}\n")
        Q6(input_str[cnt+1:])
    else:
        reject_string()
        return

# STATE Q8
def Q8(input_str):
    cnt = 0
    for c in input_str:
        if input_str[cnt] == ')' and stack.pop() == '(':
            cnt += 1
            print("): Q8")
            print("Read ')'")
            print("Popped '(' from stack")
            print("Pushed 'ε' to stack")
            print("Moving to state Q8\n")
            #print(f"Current stack: {stack}\n")
        else:
            break
    
    if input_str[cnt] == 'a' and stack.pop() == 'a': 
        print("a: Q8")
        print("Read 'a'")
        print("Popped 'a' from stack")
        print("Pushed 'ε' to stack")
        print("Moving to state Q9\n")
        #print(f"Current stack: {stack}\n")
        Q9(input_str[cnt+1:])
    elif input_str[cnt] in [ '+', '-', '/', '*' ]:
        print(f"{input_str[cnt]}: Q8")
        print(f"Read '{input_str[cnt]}'")
        print("Popped 'ε' from stack")
        print("Pushed 'ε' to stack")
        print("Moving to state Q4\n")
        #print(f"Current stack: {stack}\n")
        Q4(input_str[cnt+1:])
    else:
        reject_string()
        return

# STATE Q7
def Q7(input_str):
    cnt = 0
    for c in input_str:
        if c.isdigit():
            print(f"{c}: Q7")
            print(f"Read '{c}'")
            print("Popped 'ε' from stack")
            print("Pushed 'ε' to stack")
            print("Moving to state Q7\n")
            #print(f"Current stack: {stack}\n")
            cnt += 1
        else:
            break
    
    if input_str[cnt] == 'a' and stack.pop() == 'a':
        print("a: Q7")
        print(f"Read 'a'")
        print("Popped 'a' from stack")
        print("Pushed 'ε' to stack")
        print("Moving to state Q9\n")
        #print(f"Current stack: {stack}\n")
        Q9(input_str[cnt+1:])
    elif input_str[cnt] == ')' and stack.pop() == '(':
        print("): Q7")
        print(f"Read ')'")
        print("Popped '(' from stack")
        print("Pushed 'ε' to stack")
        print("Moving to state Q8\n")
        #print(f"Current stack: {stack}\n")
        Q8(input_str[cnt+1:]) 
    elif input_str[cnt] in [ '+', '-', '/', '*' ]:
        print(f"{input_str[cnt]}: Q7")
        print(f"Read '{input_str[cnt]}'")
        print("Popped 'ε' from stack")
        print("Pushed 'ε' to stack")
        print("Moving to state Q4\n")
        #print(f"Current stack: {stack}\n")
        Q4(input_str[cnt+1:]) 
    else:
        reject_string()
        return

# STATE Q6
def Q6(input_str):
    if input_str[0].isdigit:
        print(f"{input_str[0]}: Q6")
        print(f"Read '{input_str[0]}'")
        print("Popped 'ε' from stack")
        print("Pushed 'ε' to stack")
        print("Moving to state Q7\n")
        #print(f"Current stack: {stack}\n")
        Q7(input_str[1:])
    else:
        reject_string()
        return
        
# STATE Q5
def Q5(input_str):
    cnt = 0
    for c in input_str:
        if c.isdigit():
            cnt += 1
            print(f"{c}: Q5")
            print(f"Read '{c}'")
            print("Popped 'ε' from stack")
            print("Pushed 'ε' to stack")
            print("Moving to state Q5\n")
            #print(f"Current stack: {stack}\n")
        else:
            break

    if input_str[cnt] == '.':
        print(f"{input_str[cnt]}: Q5")
        print("Read '.'")
        print("Popped 'ε' from stack")
        print("Pushed 'ε' to stack")
        print("Moving to state Q7\n")
        # print(f"Current stack: {stack}\n")
        Q7(input_str[cnt+1:])
    else:
        reject_string()
        return


# STATE Q3
def Q3(input_str):
    cnt = 0
    for c in input_str:
        if c == 'b':
            stack.append('b')
            print("b: Q3")
            print("Read 'b'")
            print("Popped 'ε' from stack")
            print("Pushed 'b' to stack")
            print("Moving to state Q3\n")
            #print(f"Current stack: {stack}\n")
            cnt += 1
        else:
            break
    
    if input_str[cnt] == 'a':
        stack.append('a')
        print("a: Q3")
        print("Read 'a'")
        print("Popped 'ε' from stack")
        print("Pushed 'a' to stack")
        print("Moving to state Q4\n")
        #print(f"Current stack: {stack}\n")
        Q4(input_str[cnt+1:])
    else:
        reject_string()
        return

# STATE Q2
def Q2(input_str):
    if input_str[0] == 'a':
        stack.append('a')
        print("a: Q2")
        print("Read 'a'")
        print("Popped 'ε' from stack")
        print("Pushed 'a' to stack")
        print("Moving to state Q3\n")

        #print(f"Current stack: {stack}\n")        
        Q3(input_str[1:])
    else:
        reject_string()
        return


# Start of the program
n = int(input("Please enter number of iterations: "))
print(f"Processing {n} string(s)", end="\n")

# This block of code iterates through every letter in the string and runs them through the state machine
for i in range(n):
    stack = ['$']
    str_ = input(f'\nEnter string {i+1} of {n}: ')
    print(str_)
    print(f"Starting on State Q1")
    
    print("$: Q1")
    print("Read '$'")
    print("Popped 'ε' from stack")
    print("Pushed '$' to stack")
    print("Moving to state Q2\n")
    #print(f"Current stack: {stack}\n")
    Q2(str_)