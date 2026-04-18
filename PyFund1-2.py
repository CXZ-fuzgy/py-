def box_print(msg):
    width = len(msg) + 28          # 两边各留一个空格
    print("┌" + "─" * width + "┐")
    print("│" + msg + " │")
    print("└" + "─" * width + "┘")

物料列表 = []

while True:
    name = input("请输入物料名称（输入q退出）：")
    if name == "q":
        break
    print("\n请选择物料类别：")
    print("1-金属类 2-橡胶类 3-电子电器类 4-纺织类 5-玻璃化学品类 6-其他")
    AutoMaterialCategory = input(f'请输入{name}的类别（输入数字1-6）')

    类别字典 = {
        '1':"金属类",
        '2':"橡胶类",
        '3':"电子电器类",
        '5':"玻璃化学品类",
        '4':"纺织类",
        '6':"其他"
    }
    类别 = 类别字典.get(AutoMaterialCategory,'未分类')

    入库时间 = int(input(f'请输入物料{name}在库时间（天）：'))

    单个物料 =[name,类别,入库时间]
    物料列表.append(单个物料)


print("\n=========所有物料信息=========")

for 物料 in 物料列表:
    name = 物料[0]
    类别 = 物料[1]
    入库时间 = 物料[2]

    if 入库时间 > 10:
        状态 = '回收！'
    else:
        状态 = '可以继续使用。'

    box_print(f" | 物料名称：{物料[0]} | 入库时间：{入库时间}天 | 类别：{类别} | 状态：{状态}")
