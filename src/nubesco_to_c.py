import sys
import os
import re   

REPLACEMENTS = {
    "ベルミッティスモゲロン": "int main() ",
    "ヌベ": "{ ",
    "ヌゾ": "} ",
    "ｗｗｗｗｗｗ": "} ",
    "ｗｗｗ": "} ",
    "ｗｗ": "} ",
    "ボョ": "return ",
    "イヒヒ": "; ",
}

def convert_printf_blocks(text):
    result = ""
    result += "#include <stdio.h>\n"
    result += "#include <stdlib.h>\n\n"
    while "プリチョ" in text:
        pre, rest = text.split("プリチョ", 1)
        args, rest = rest.split("イヒー", 1)
        result += pre + f'printf({args}); '
        text = rest
    return result + text

def convert_nubesco_to_c(nube_code):
    # まずプリチョを特殊処理
    nube_code = convert_printf_blocks(nube_code)

    # 通常の置換処理
    for nube, c_code in REPLACEMENTS.items():
        nube_code = nube_code.replace(nube, c_code)

    # 整形（簡易）
    nube_code = nube_code.replace("{", "{\n    ")
    nube_code = nube_code.replace(";", ";\n    ")
    nube_code = nube_code.replace("}", "\n}\n")
    return nube_code.strip()



def main():
    if len(sys.argv) != 2:
        print("使い方: python nubesco_to_c.py input.nube")
        return

    input_path = sys.argv[1]
    if not input_path.endswith(".nube"):
        print("エラー: .nubeファイルを指定してください")
        return

    output_path = os.path.splitext(input_path)[0] + ".c"

    with open(input_path, "r", encoding="utf-8") as f:
        nube_code = f.read()

    c_code = convert_nubesco_to_c(nube_code)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(c_code)

    print(f"変換完了: {output_path}")

if __name__ == "__main__":
    main()
