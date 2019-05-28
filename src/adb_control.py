import os

class AdbControl:
    hander = 'adb'

    def get_devices(self):
        stdout = self.exec('devices')
        result = []
        for line in stdout.split('\n'):
            if line != 'List of devices attached ' and line:
                result.append(line.split('\t')[0])
        print(result)

    def exec(self, cmd):
        return os.popen(f'{self.hander} {cmd}').read()

    def tap(self, x, y):
        self.exec(f'shell input tap {x} {y}')

    def swipe(self, startX, startY, endX, endY, timeout):
        self.exec(f'shell input swipe {startX} {startY} {endX} {endY} {timeout}')