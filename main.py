import sys

def main():
    argv = sys.argv[1]

    memory_size = 30000
    memory = [0 for i in range(memory_size)]
    pointer = 0
    head = 0

    while head < len(argv):
        if argv[head] == '+':
            memory[pointer] += 1

        elif argv[head] == '-':
            memory[pointer] -= 1

        elif argv[head] == '[':
            if memory[pointer] == 0:
                nest = 1
                while nest != 0:
                    head += 1
                    if head == len(argv):
                        print("']' is missing")
                        sys.exit(1)
                    if argv[head] == '[':
                        nest += 1
                    elif argv[head] == ']':
                        nest -= 1
        elif argv[head] == ']':
            if memory[pointer] != 0:
                nest = 1
                while nest != 0:
                    head -= 1
                    if head < 0:
                        print("'[' is missing")  
                    if argv[head] == ']':
                        nest += 1
                    elif argv[head] == '[':
                        nest -= 1
        elif argv[head] == '.':
            print(chr(memory[pointer]),end = "")
        elif argv[head] == ',':
            memory[pointer] = ord(sys.stdin.buffer.read(1))
        elif argv[head] == '>':
            pointer += 1       
            if pointer > memory_size:
                print("overflow!")
                sys.exit(1)
        elif argv[head] == "<":
            if pointer == 0:
                print("Can't decrement anymore")
            pointer -= 1
        else:
            pass

        head += 1  

main() if __name__ == '__main__' else None
