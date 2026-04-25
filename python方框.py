# box_text.py  —— 直接复制即可运行
import unicodedata

def disp_len(s: str) -> int:
    """返回字符串在终端里的显示宽度（全角=2，半角=1）"""
    return sum(2 if unicodedata.east_asian_width(ch) in 'FWA' else 1 for ch in s)

def box_text(text: str) -> str:
    lines = text.splitlines()
    if not lines:                      # 防空输入
        return '++\n||\n++'
    max_w = max(disp_len(line) for line in lines)
    top = bottom = '+' + '=' * (max_w + 2) + '+'
    boxed = [top]
    for line in lines:
        pad = max_w - disp_len(line)
        boxed.append('| ' + line + ' ' * pad + ' |')
    boxed.append(bottom)
    return '\n'.join(boxed)

# ---------------- 演示 ----------------
if __name__ == '__main__':
    demo = """文件存在？False
Traceback (most recent call last):
File "d:/VS cold.py/ar_lesson/质检.py"， line 7， in <module>
print('文件大小（字节）：', os.path.getsize(path))
FileNotFoundError：[WinError 2]系统找不到指定的文件。：'standard.jpg'"""
    print(box_text(demo))


