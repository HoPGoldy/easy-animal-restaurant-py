from adb_control import AdbControl
import time
import json

class RestaurantControl:
    # 当前所在的场景编号
    screen_code = 1
    # 场景枚举
    SCREEN_MAP = {
        'garden': 0,
        'hall': 1,
        'kitchen': 2
    }
    
    # 获取参数以及adb控制
    def __init__(self):
        self.adb = AdbControl()
        self._get_config()
    
    # 获取参数
    def _get_config(self):
        try:
            with open("./src/config.json", 'r', encoding='utf-8') as load_f:
                self.config = json.load(load_f)
        except:
            print('错误，未发现config.json')

    # 移动至指定场景
    def go_to(self, screen_name):
        if screen_name in self.SCREEN_MAP:
            step = self.SCREEN_MAP[screen_name] - self.screen_code

            if step < 0:
                for i in range(0, -step):
                    self.adb.tap(self.config['leftScreen']['x'], self.config['leftScreen']['y'])
                    time.sleep(1)
            elif step > 0:
                for i in range(0, step):
                    self.adb.tap(self.config['rightScreen']['x'], self.config['rightScreen']['y'])
                    time.sleep(1)
            
            self.screen_code = self.SCREEN_MAP[screen_name]
            return True
        else:
            return False

    # 拾取座位旁饭钱
    def pick_site_money(self):
        for i in range(0, 2):
            for j in range(0, 3):
                x = self.config['firstMoney']['x'] + self.config['siteOffset']['x'] * j
                y = self.config['firstMoney']['y'] + self.config['siteOffset']['y'] * i

                print(f'拾取第 {(i * 3) + (j + 1)} 桌扔钱')

                self.adb.tap(x, y)
                time.sleep(1)
        return True

    # 点击大厅的订单
    def order(self):
        for i in range(0, 2):
            for j in range(0, 3):
                x = self.config['firstSite']['x'] + self.config['siteOffset']['x'] * j
                y = self.config['firstSite']['y'] + self.config['siteOffset']['y'] * i

                print(f'点击第 {(i * 3) + (j + 1)} 桌订单')

                self.adb.tap(x, y)
                time.sleep(1)
        return True
    
    # 拾取大厅其他地方的钱
    def pick_hall_money(self):
        for key in self.config['hallMoney']:
            item = self.config['hallMoney'][key]
            print(f'正在拾取 {item["info"]} 的收入')

            self.adb.tap(item['x'], item['y'])
            time.sleep(0.5)
        return True

    # 拾取厨房其他地方的钱
    def pick_kitchen_money(self):
        for key in self.config['kitchenMoney']:
            item = self.config['kitchenMoney'][key]
            print(f'正在拾取 {item["info"]} 的收入')

            self.adb.tap(item['x'], item['y'])
            time.sleep(0.5)
        return True

    # 点击 number 次宣传按钮
    def click_propaganda(self, number):
        print(f'\n点击 {number} 次宣传按钮\n')
        for i in range(0, number):
            self.adb.tap(self.config['propaganda']['x'], self.config['propaganda']['y'])
            time.sleep(0.5)