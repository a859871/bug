import vending_machine.vending_service as machine

flag = True # 控制迴圈是否執行
balance = 0
while flag:
    print('\n====================')
    select = eval(input('1. 儲值\n2. 購買\n3. 查詢餘額\n4. 離開\n請選擇 :'))
    if select == 1:  # 儲值
        machine.deposit()

    elif select == 2:
        machine.buy()
    elif select == 3:
        print(f'目前餘額為 {balance}元')
    elif select == 4:
        print('bye')
        flag = 0
        break
    else:
        print('====請輸入1-4之間====')
        continue
weight1 = 100
weight2 = 80

def add_weight(w1, w2=1):
    result = w1 +w2
    return result

x = add_weight(weight1,weight2)
y = add_weight(weight1)
#出錯因為函式規定要兩個變數除非將def add_weight(w1, w2=1)設定預設值
print(x,y)