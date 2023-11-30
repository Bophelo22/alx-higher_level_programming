#!/usr/bin/python3
if __name__ == "__main__":
    import dis
    filename = 'hidden_4.pyc'  # Replace with the actual filename
    
    with open(filename, 'rb') as file:
        bytecode = file.read()
    # Disassemble the bytecode
    dis.dis(bytecode)
