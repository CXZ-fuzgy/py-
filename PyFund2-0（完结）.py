# ================= 物流物料管理系统 =================
# 包含 Python 基础全部核心知识点
# 变量、数据类型、条件、循环、函数、列表、字典、文件、异常处理

materials = []  # 全局物料列表，每个元素是一个字典

def show_menu():
    """打印主菜单"""
    print("\\n" + "=" * 35)
    print("       物流物料管理系统")
    print("=" * 35)
    print("1. 添加新物料")
    print("2. 查看所有物料")
    print("3. 查找物料")
    print("4. 修改物料数量")
    print("5. 删除物料")
    print("6. 库存统计")
    print("7. 保存数据到文件")
    print("8. 从文件读取数据")
    print("9. 退出系统")
    print("=" * 35)

def add_material():
    """添加新物料"""
    print("\\n--- 添加新物料 ---")
    name = input("物料名称: ")
    code = input("物料编号: ")
    quantity = int(input("初始数量: "))
    location = input("存放位置: ")
    
    material = {
        "name": name,
        "code": code,
        "quantity": quantity,
        "location": location
    }
    materials.append(material)
    print(f"✅ 物料 '{name}' 已添加。")

def view_all():
    """查看所有物料"""
    if not materials:
        print("📭 仓库暂无物料。")
        return
    print("\\n--- 当前库存物料 ---")
    print(f"{'序号':<4} {'名称':<10} {'编号':<10} {'数量':<6} {'位置':<10}")
    print("-" * 45)
    for idx, m in enumerate(materials, start=1):
        print(f"{idx:<4} {m['name']:<10} {m['code']:<10} {m['quantity']:<6} {m['location']:<10}")

def search_material():
    """查找物料（名称或编号）"""
    if not materials:
        print("📭 仓库暂无物料。")
        return
    keyword = input("请输入物料名称或编号: ")
    found = []
    for m in materials:
        if keyword == m['name'] or keyword == m['code']:
            found.append(m)
    if found:
        print(f"\\n🔍 找到 {len(found)} 条记录:")
        for m in found:
            print(f"名称: {m['name']}, 编号: {m['code']}, 数量: {m['quantity']}, 位置: {m['location']}")
    else:
        print(f"❌ 未找到 '{keyword}'。")

def update_quantity():
    """修改物料数量"""
    if not materials:
        print("📭 仓库暂无物料。")
        return
    code = input("请输入要修改的物料编号: ")
    for m in materials:
        if m['code'] == code:
            print(f"当前 {m['name']} 数量: {m['quantity']}")
            new_qty = int(input("新数量: "))
            m['quantity'] = new_qty
            print(f"✅ 数量已更新为 {new_qty}。")
            return
    print(f"❌ 未找到编号 '{code}'。")

def delete_material():
    """删除物料"""
    if not materials:
        print("📭 仓库暂无物料。")
        return
    code = input("请输入要删除的物料编号: ")
    for idx, m in enumerate(materials):
        if m['code'] == code:
            confirm = input(f"确定删除 '{m['name']}'? (y/n): ")
            if confirm.lower() == 'y':
                deleted = materials.pop(idx)
                print(f"✅ '{deleted['name']}' 已删除。")
            else:
                print("操作取消。")
            return
    print(f"❌ 未找到编号 '{code}'。")

def statistics():
    """库存统计"""
    if not materials:
        print("📭 仓库暂无物料。")
        return
    total_qty = 0
    for m in materials:
        total_qty += m['quantity']
    count = len(materials)
    avg = total_qty / count
    print("\\n--- 库存统计 ---")
    print(f"物料种类: {count}")
    print(f"总库存量: {total_qty}")
    print(f"平均库存: {avg:.2f}")

def save_to_file():
    """保存到文件"""
    if not materials:
        print("⚠️ 无数据可保存。")
        return
    with open("materials.txt", "w", encoding="utf-8") as f:
        for m in materials:
            f.write(f"{m['name']},{m['code']},{m['quantity']},{m['location']}\\n")
    print("💾 已保存到 materials.txt")

def load_from_file():
    """从文件读取"""
    global materials
    try:
        with open("materials.txt", "r", encoding="utf-8") as f:
            materials = []
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    if len(parts) == 4:
                        name, code, qty, loc = parts
                        materials.append({
                            "name": name,
                            "code": code,
                            "quantity": int(qty),
                            "location": loc
                        })
        print("📂 已从文件加载数据。")
    except FileNotFoundError:
        print("❌ 文件不存在。")
    except Exception as e:
        print(f"❌ 读取出错: {e}")

def main():
    """主程序"""
    while True:
        show_menu()
        choice = input("请输入操作编号 (1-9): ")
        if choice == "1":
            add_material()
        elif choice == "2":
            view_all()
        elif choice == "3":
            search_material()
        elif choice == "4":
            update_quantity()
        elif choice == "5":
            delete_material()
        elif choice == "6":
            statistics()
        elif choice == "7":
            save_to_file()
        elif choice == "8":
            load_from_file()
        elif choice == "9":
            print("👋 再见！")
            break
        else:
            print("⚠️ 无效输入，请输入 1-9。")

if __name__ == "__main__":
    main()