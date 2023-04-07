import sys

def convert_to_ascii_code(n):
    return chr(n)

def syntax_match(input_argv):
    memory_size = 2048
    pointer = [0 for i in range(memory_size)]
    current_pointer = 0
    string_stack = []

    for i, n in enumerate(input_argv):
        match n:
            case '>': # ポインタをインクリメント（右にずらす）
                current_pointer += 1
            case '<': # ポインタをデクリメント（左にずらす）
                current_pointer -= 1
            case '+': # ポインタの値をインクリメント
                pointer[current_pointer] += 1
            case '-': # ポインタの値をデクリメント
                pointer[current_pointer] -= 1
            case '.': # ポインタの値を出力
                string_stack.append(convert_to_ascii_code(pointer[current_pointer]))
            case ',': # 入力から1byte読み込んで、ポインタが指す値に代入
                pass
            case '[': # ポインタの指す値が0なら、後の]までジャンプ(要するにWhile) 
                pass
            case ']': # ポインタが指す値が0でないなら、対応する [ （の直後[注釈 1]）にジャンプする
                pass
            case _: # その他の入力が来た場合
                pass

    return string_stack

def main():
    # TODO 途中入力にも対応する
    input_argv = sys.argv[1]
    result = syntax_match(input_argv)

    print(''.join(result))

main() if __name__ == '__main__' else None