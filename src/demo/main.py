from ib_insync import IB, util

def main():
    # 创建 IB 实例
    ib = IB()
    
    try:
        # 添加连接状态检查
        print('before connecting...')
        ib.connect('127.0.0.1', 4001, clientId=2, readonly=True)
        print('connected.')
        if not ib.isConnected():
            print("无法连接到 IB Gateway，请检查:")
            print("1. IB Gateway 是否已启动")
            print("2. 端口号是否正确")
            print("3. 客户端 ID 是否被占用")
            return

        # 添加错误处理
        def get_account_info():
            try:
                account_summary = ib.accountSummary()
                print("账户摘要:")
                for item in account_summary:
                    print(f"{item.tag}: {item.value} {item.currency}")
            except Exception as e:
                print(f"获取账户信息时出错: {str(e)}")

        def get_positions():
            try:
                positions = ib.positions()
                print("\n账户持仓:", 'Stocks: '+str(len(positions)))
                for pos in positions:
                    print(f"合约: {pos.contract.symbol}, 持仓: {pos.position}, 平均成本: {pos.avgCost}")
            except Exception as e:
                print(f"获取持仓信息时出错: {str(e)}")

        # 执行函数
        # get_account_info()
        # get_positions()

    except Exception as e:
        print(f"程序执行出错: {str(e)}")
    finally:
        if ib.isConnected():
            ib.disconnect()


if __name__ == "__main__":
    main() 

