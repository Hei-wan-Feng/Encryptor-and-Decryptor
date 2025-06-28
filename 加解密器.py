    #作者:Hei_wan_Feng
#辅助AI:Kimi
#详情见最后

# 头文件
import string
import random
import ast

# 定义字符
all_characters = string.ascii_letters + string.digits + string.punctuation + ' '

# Hei_wan_Feng的生成随机的字符映射表
def generate_mapping():
    characters = list(all_characters)
    shuffled_characters = characters.copy()
    random.shuffle(shuffled_characters)
    return dict(zip(characters, shuffled_characters))

# Hei_wan_Feng的生成解密映射表
def inverse_mapping(mapping):
    return {v: k for k, v in mapping.items()}

# Hei_wan_Feng的检查映射表是否有效
def validate_mapping(mapping):
    if len(mapping) != len(all_characters):
        return False
    if len(set(mapping.values())) != len(all_characters):
        return False
    return True

# Hei_wan_Feng的加密函数
def encrypt(text, mapping):
    return ''.join(mapping.get(char, char) for char in text)

# Hei_wan_Feng的解密函数
def decrypt(text, inverse_mapping):
    return ''.join(inverse_mapping.get(char, char) for char in text)

# 凯撒密码加密函数
def caesar_encrypt(plaintext, shift):
    return ''.join(
        chr((ord(char) - 65 + shift) % 26 + 65) if 'A' <= char <= 'Z'
        else chr((ord(char) - 97 + shift) % 26 + 97) if 'a' <= char <= 'z'
        else char
        for char in plaintext
    )

# 凯撒密码解密函数
def caesar_decrypt(ciphertext, shift):
    return ''.join(
        chr((ord(char) - 65 - shift) % 26 + 65) if 'A' <= char <= 'Z'
        else chr((ord(char) - 97 - shift) % 26 + 97) if 'a' <= char <= 'z'
        else char
        for char in ciphertext
    )

# Hei_wan_Feng的主程序
if __name__ == "__main__":
    en_contains = False
    de_contains = False
    judge_use_predef_mapping = None
    caesar_shift = None
    easter_egg_crashed_triggered = 0
    easter_egg_b_a_permiss_triggered = 0

    # 生成映射表
    while True:
        judge_use_predef_mapping = input("你想要使用预制的字符映射表吗？(y/n): ").strip().lower()
        if judge_use_predef_mapping.lower() == "y":
            while True:
                try:
                    input_for_mapping = input("请输入映射字符表（字典格式）: ")
                    # 清理输入字符串中的多余空格
                    input_for_mapping = input_for_mapping.strip()
                    mapping = ast.literal_eval(input_for_mapping)
                    if not isinstance(mapping, dict):
                        raise ValueError("输入的映射表必须是字典格式")
                    if not validate_mapping(mapping):
                        raise ValueError("映射表验证失败")
                    break  # 输入正确，跳出循环
                except (ValueError, SyntaxError) as e:
                    print(f"输入格式错误：{e}，请重新输入。")
            break
        elif judge_use_predef_mapping.lower() == "n":
            print("正常继续...")
            mapping = generate_mapping()
            break
        else:
            print("没有这个选项")
            continue


    # 打印字符映射表
    print("字符映射表为:\n\n")
    print(mapping)
    print("\n\n小提示:\n格式:{'字符': <-这是空格'字符', <-这是空格}\n")
    print("记得把大括号也复制上！\n\n\n")
    
    # 生成解密映射表
    inverse_map = inverse_mapping(mapping)

    while True:
        print("\n1. 加密")
        print("2. 解密")
        print("3. 退出")
        choice = input("请选择操作（1/2/3）：")

        if choice == '1':
            input_text = input("请输入要加密的文本：")
            try:
                caesar_shift = int(input("输入凯撒密码的加密移动位数:"))
            except ValueError:
                print("输入的位移量无效，请输入一个整数。")
                continue
            encrypted_text = encrypt(input_text, mapping)
            final_result_en = caesar_encrypt(encrypted_text, caesar_shift)
            if input_text != final_result_en:
                print("加密后的文本：")
                print("\n" + final_result_en)
                print("\n小提示：如果你输入了加密或解密，但是结果是一样的，那么这个字符串不能被加解密\n")
            elif input_text == final_result_en:
                print("\n无法转换。")
                continue
        elif choice == '2':
            input_text = input("请输入要解密的文本：")
            try:
                caesar_shift = int(input("输入凯撒密码的解密移动位数:"))
            except ValueError:
                print("输入的位移量无效，请输入一个整数。")
                continue
            decrypted_text = caesar_decrypt(input_text, caesar_shift)
            final_result_de = decrypt(decrypted_text, inverse_map)
            if input_text != final_result_de:
                print("解密后的文本：")
                print("\n" + final_result_de)
                print("\n小提示：如果你输入了加密或解密，但是结果是一样的，那么这个字符串不能被加解密\n")
            elif input_text == final_result_de:
                print("\n无法转换。")
                continue
        elif choice == '3':
            input("按任意键继续...")
            break
        elif choice == '4':
            print('There is(are) a() py subject(s) has(have) crashed:加解密器.py show details(type "sd" to show youself crashed details.)')
            easter_egg_crashed_triggered = 1
            continue
        elif choice == 'sd':
            if easter_egg_crashed_triggered == 1:
                print("details:\nat.com.System.has.not.triggered.is.************, These're only BETTER ADMINSTRATORS can see.")
                easter_egg_b_a_permiss_triggered = 1
                continue
            else:
                print("you haven't permissions to continue")
                continue
        elif choice == 'uuddlrlrbaba':
            if easter_egg_b_a_permiss_triggered == 1:
                print("恭喜你发现彩蛋！\n作者qq:732226024")
                continue
            else:
                print("you haven't open konami(old games cheat) code.")
                continue
        else:
            print("无效的选择，请重新输入。")

#informations:
#auther:Hei_wan_Feng
#help AI:kimi.normal
#the AI's website:https://kimi.com
# #Hei_wan_Feng's bilibili uid:3537107096176812