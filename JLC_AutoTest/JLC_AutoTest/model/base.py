from JLC_AutoTest.globalvar import platform
# from JLC_AutoTest.model.ShamElement import ShamElement
import time,os
from xml.etree.ElementTree import ElementTree

from macaca import WebDriverException


class Base(object):
    """
    基本类
    """

    def __init__(self, driver):
        """
        初始化构造器
        :param driver: WebDriver对象
        """
        self.driver = driver
        self.platform = platform

    def selector(self, location):
        """
        根据平台与定位方式的字典查找元素
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'xpath',
            'android_value': '//*[@text="总资产"]',
        :param location: {
            'ios_by': 'ios_by',
            'ios_value': 'ios_value',
            'android_by': 'android_by',
            'android_value': 'android_value',
        }
        :return: WebDriver对象
        """
        by = None
        value = None
        if 'by' in location:
            by = location['by']
            value = location['value']
        elif platform == 'ios':
            by = location['ios_by']
            value = location['ios_value']
        elif platform == 'android':
            by = location['android_by']
            value = location['android_value']
        else:
            pass
        if by == 'xpath':
            return self.xpath(value)
        elif by == 'id':
            return self.id(value)
        elif by == 'wait_id':
            return self.wait_id(value)
        elif by == 'name':
            return self.name(value)
        elif by == 'wait_name':
            return self.wait_name(value)
        elif by == 'class_name':
            return self.class_name(value)
        elif by == 'wait_xpath':
            return self.wait_xpath(value)
        elif by=='rect':
            return self.rect(value)
        else:
            pass

    def xpath(self, xpath):
        """
        通过XMLPath查找元素
        :param xpath: 元素的XMLPath
        :return: WebElement对象
        """
        return self.driver.element_by_xpath(xpath)



    def id(self, _id):
        """
        通过ID查找元素
        :param _id: 元素的ID
        :return: WebElement对象
        """
        return self.driver.element_by_id(_id)

    def wait_id(self, _id):
        """
        通过ID查找元素，默认等待10秒，每次间隔1秒
        :param _id: 元素的ID
        :return: WebElement对象
        """
        return self.driver.wait_for_element_by_id(_id)

    def name(self, name):
        """
        通过文本查找元素
        :param name: 元素的文本
        :return: WebElement对象
        """
        return self.driver.element_by_name(name)

    def wait_name(self, name):
        """
        通过文本查找元素，默认等待10秒，每次间隔1秒
        :param name: 元素的文本
        :return: WebElement对象
        """
        return self.driver.wait_for_element_by_name(name)

    def class_name(self, class_name):
        """
        通过[伪类名称,索引]查找元素
        :param class_name: ['class_name', index]
        :return: WebElement对象
        """
        return self.driver.elements_by_class_name(class_name[0])[class_name[1]]

    def wait_xpath(self, xpath):
        """
        通过xpath寻找元素
        :param xpath:
        :return:
        """
        return self.driver.wait_for_element_by_xpath(xpath)

    def to_back(self):
        """
            返回操作
        :return:
        """
        return self.driver.back()

    def by_rect(self):
        """
            返回矩形
        :return:
        """
        return self.driver.rect()

    def _get_window_size(self):
        window = self.driver.get_window_size()
        x = int(window['width'])
        y = int(window['height'])

        return x, y

    @staticmethod
    def _get_element_size(element):
        rect = element.rect

        x_center = rect['x'] + rect['width'] / 2
        y_center = rect['y'] + rect['height'] / 2
        x_left = rect['x']
        y_up = rect['y']
        x_right = rect['x'] + rect['width']
        y_down = rect['y'] + rect['height']

        return x_left, y_up, x_center, y_center, x_right, y_down

    def _swipe(self, fromX, fromY, toX, toY, steps):
        self.driver \
            .touch('drag', {'fromX': fromX, 'fromY': fromY, 'toX': toX, 'toY': toY, 'steps': steps})

  #滑动的最新方法用duration

    def _swipenew(self, fromX, fromY, toX, toY, duration):
        self.driver \
            .touch('drag', {'fromX': fromX, 'fromY': fromY, 'toX': toX, 'toY': toY, 'duration': duration})

    #向上滑动的最新方法，用duration

    def swipe_up_new(self, element=None, duration=3):
        """
        swipe up
        :param element: WebElement of Macaca, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :return: None
        """
        if element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(element)

            fromX = x_center
            fromY = y_center
            toX = x_center
            toY = y_up
        else:
            x, y = self._get_window_size()
            fromX = 0.2* x
            fromY = 0.8* y
            toX = 0.2* x
            toY = 0.3* y

        self._swipenew(fromX, fromY, toX, toY, duration)



    def swipe_up(self, element=None, steps=10):
        """
        swipe up
        :param element: WebElement of Macaca, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :return: None
        """
        if element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(element)

            fromX = x_center
            fromY = y_center
            toX = x_center
            toY = y_up
        else:
            x, y = self._get_window_size()
            fromX = 0.8*x
            fromY = 0.2*y
            toX = 0.8*x
            toY = 0.1*y

        self._swipe(fromX, fromY, toX, toY, steps)

    def swipe_up_android(self, element=None, steps=10):
        """
        swipe up
        :param element: WebElement of Macaca, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :return: None
        """
        if element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(element)

            fromX = x_center
            fromY = y_center
            toX = x_center
            toY = y_up
        else:
            x, y = self._get_window_size()
            fromX = 0.5*x
            fromY = 0.81*y
            toX = 0.5*x
            toY = 0.4*y

        self._swipe(fromX, fromY, toX, toY, steps)

    def swipe_down(self, element=None, steps=10):
        """
        swipe down
        :param element: WebElement of Macaca, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :return: None
        """
        if element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(element)

            fromX = x_center
            fromY = y_center
            toX = x_center
            toY = y_down
        else:
            x, y = self._get_window_size()
            fromX = 0.5*x
            fromY = 0.5*y
            toX = 0.5*x
            toY = 0.75*y

        self._swipe(fromX, fromY, toX, toY, steps)

    #最新的向上滑动的方法

    def swipe_down_new(self, element=None, duration=3):
        """
        swipe down
        :param element: WebElement of Macaca, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :return: None
        """
        if element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(element)

            fromX = x_center
            fromY = y_center
            toX = x_center
            toY = y_down
        else:
            x, y = self._get_window_size()
            fromX = 0.5*x
            fromY = 0.3*y
            toX = 0.5*x
            toY = 0.8*y

        self._swipenew(fromX, fromY, toX, toY, duration)

    def swipe_left(self, element=None, steps=10):
        """
        swipe left
        :param element: WebElement of Macaca, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :return: None
        """
        if element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(element)

            fromX = x_center
            fromY = y_center
            toX = x_left
            toY = y_center
        else:
            x, y = self._get_window_size()
            print(x,y)
            fromX = 0.9*x
            fromY = 0.8*y
            toX = 0.25*x
            toY = 0.8*y

        self._swipe(fromX, fromY, toX, toY, steps)

    def swipe_left_android(self, element=None, duration=1):
        """
        swipe left
        :param element: WebElement of Macaca, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :return: None
        """
        if element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(element)

            fromX = x_center
            fromY = y_center
            toX = x_left
            toY = y_center
        else:
            x, y = self._get_window_size()
            print(x, y)
            fromX = 0.9 * x
            fromY = 0.8 * y
            toX = 0.25 * x
            toY = 0.8 * y

        self._swipe(fromX, fromY, toX, toY, duration)

    def swipe_right(self, element=None, steps=10):
        """
        swipe right
        :param element: WebElement of Macaca, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :return: None
        """
        if element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(element)

            fromX = x_center
            fromY = y_center
            toX = x_right
            toY = y_center
        else:
            x, y = self._get_window_size()
            fromX = 0.5*x
            fromY = 0.5*y
            toX = 0.75*x
            toY = 0.5*y

        self._swipe(fromX, fromY, toX, toY, steps)

    def _find_element_by_swipe(self, direction, using, value, element=None, steps=10, max_swipe=6):
        times = max_swipe

        stability_width = 0
        stability_height = 0
        for i in range(times):
            try:
                e = self.driver.element(using, value)

                width = e.rect['width']
                height = e.rect['height']
                if stability_width != width or stability_height != height:
                    stability_width = width
                    stability_height = height
                    raise WebDriverException
                else:
                    return e
            except WebDriverException:
                if direction == 'up':
                    self.swipe_up(element=element, steps=steps)
                elif direction == 'down':
                    self.swipe_down(element=element, steps=steps)
                elif direction == 'left':
                    self.swipe_left(element=element, steps=steps)
                elif direction == 'right':
                    self.swipe_right(element=element, steps=steps)

                if i == times - 1:
                    raise WebDriverException

    def find_element_by_swipe_up(self, using, value, element=None, steps=10, max_swipe=6):
        """
        find element by swipe up
        :param using: The element location strategy.
                      "id","xpath","link text","partial link text","name","tag name","class name","css selector"
        :param value: The value of the location strategy.
        :param element: WebElement of Macaca, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :param max_swipe: the max times of swipe
        :return: WebElement of Macaca

        Raises:
            WebDriverException.
        """
        return self._find_element_by_swipe('up', using, value,
                                           element=element, steps=steps, max_swipe=max_swipe)

    def find_element_by_swipe_down(self, using, value, element=None, steps=10, max_swipe=6):
        """
        find element by swipe down
        :param using: The element location strategy.
                      "id","xpath","link text","partial link text","name","tag name","class name","css selector"
        :param value: The value of the location strategy.
        :param element: WebElement of Macaca, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :param max_swipe: the max times of swipe
        :return: WebElement of Macaca

        Raises:
            WebDriverException.
        """
        return self._find_element_by_swipe('down', using, value,
                                           element=element, steps=steps, max_swipe=max_swipe)

    def find_element_by_swipe_left(self, using, value, element=None, steps=10, max_swipe=6):
        """
        find element by swipe left
        :param using: The element location strategy.
                      "id","xpath","link text","partial link text","name","tag name","class name","css selector"
        :param value: The value of the location strategy.
        :param element: WebElement of Macaca, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :param max_swipe: the max times of swipe
        :return: WebElement of Macaca

        Raises:
            WebDriverException.
        """
        return self._find_element_by_swipe('left', using, value,
                                           element=element, steps=steps, max_swipe=max_swipe)

    def find_element_by_swipe_right(self, using, value, element=None, steps=10, max_swipe=6):
        """
        find element by swipe right
        :param using: The element location strategy.
                      "id","xpath","link text","partial link text","name","tag name","class name","css selector"
        :param value: The value of the location strategy.
        :param element: WebElement of Macaca, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :param max_swipe: the max times of swipe
        :return: WebElement of Macaca

        Raises:
            WebDriverException.
        """
        return self._find_element_by_swipe('right', using, value,
                                           element=element, steps=steps, max_swipe=max_swipe)

    def find_element_on_horizontal(self, using, value, element=None, steps=10, max_swipe=6):
        """
        find element on horizontal
        :param using: The element location strategy.
                      "id","xpath","link text","partial link text","name","tag name","class name","css selector"
        :param value: The value of the location strategy.
        :param element: WebElement of Macaca, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :param max_swipe: the max times of swipe
        :return: WebElement of Macaca

        Raises:
            WebDriverException.
        """
        try:
            return self.find_element_by_swipe_left(using, value,
                                                   element=element, steps=steps, max_swipe=max_swipe)
        except WebDriverException:
            pass

        return self.find_element_by_swipe_right(using, value,
                                                element=element, steps=steps, max_swipe=max_swipe)

    def find_element_on_vertical(self, using, value, element=None, steps=10, max_swipe=6):
        """
        find element on vertical
        :param using: The element location strategy.
                      "id","xpath","link text","partial link text","name","tag name","class name","css selector"
        :param value: The value of the location strategy.
        :param element: WebElement of Macaca, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :param max_swipe: the max times of swipe
        :return: WebElement of Macaca

        Raises:
            WebDriverException.
        """
        try:
            return self.find_element_by_swipe_up(using, value,
                                                 element=element, steps=steps, max_swipe=max_swipe)
        except WebDriverException:
            pass

        return self.find_element_by_swipe_down(using, value,
                                               element=element, steps=steps, max_swipe=max_swipe)

    def _tap(self, x, y):
        self.driver.touch('tap', {'x': x, 'y': y})

    def _press(self, x, y):
        self.driver.touch('press', {'x': x, 'y': y, 'steps': 100})

    def _side_of_element(self, direction, element, rate):
        rect = element.rect

        width = rect['width']
        height = rect['height']

        x_center = rect['x'] + rect['width'] / 2
        y_center = rect['y'] + rect['height'] / 2

        x_left = rect['x']
        y_up = rect['y']
        x_right = rect['x'] + rect['width']
        y_down = rect['y'] + rect['height']

        x = y = 0
        if direction == 'above':
            x = x_center
            y = y_up - rate * height
        elif direction == 'under':
            x = x_center
            y = y_down + rate * height
        elif direction == 'left':
            x = x_left - rate * width
            y = y_center
        elif direction == 'right':
            x = x_right + rate * width
            y = y_center

        return x, y

    def _click_side_of_element(self, direction, element, rate):
        x, y = self._side_of_element(direction, element, rate)

        self._tap(x, y)

    def _press_side_of_element(self, direction, element, rate):
        x, y = self._side_of_element(direction, element, rate)

        self._press(x, y)

    def click_above_of_element(self, element, rate=1):
        """
        click above the gaven element
        :param element: WebElement of Macaca
        :param rate: rate of the width or height of the element
        :return: None
        """
        self._click_side_of_element('above', element, rate)

    def click_under_of_element(self, element, rate=1):
        """
        click under the gaven element
        :param element: WebElement of Macaca
        :param rate: rate of the width or height of the element
        :return: None
        """
        self._click_side_of_element('under', element, rate)

    def click_left_of_element(self, element, rate=1):
        """
        click the left of the gaven element
        :param element: WebElement of Macaca
        :param rate: rate of the width or height of the element
        :return: None
        """
        self._click_side_of_element('left', element, rate)

    def click_right_of_element(self, element, rate=1):
        """
        click the right of the gaven element
        :param element: WebElement of Macaca
        :param rate: rate of the width or height of the element
        :return: None
        """
        self._click_side_of_element('right', element, rate)

    def press_above_of_element(self, element, rate=1):
        """
        press above the gaven element
        :param element: WebElement of Macaca
        :param rate: rate of the width or height of the element
        :return: None
        """
        self._press_side_of_element('above', element, rate)

    def press_under_of_element(self, element, rate=1):
        """
        press under the gaven element
        :param element: WebElement of Macaca
        :param rate: rate of the width or height of the element
        :return: None
        """
        self._press_side_of_element('under', element, rate)

    def press_left_of_element(self, element, rate=1):
        """
        press the left of the gaven element
        :param element: WebElement of Macaca
        :param rate: rate of the width or height of the element
        :return: None
        """
        self._press_side_of_element('left', element, rate)

    def press_right_of_element(self, element, rate=1):
        """
        press the right of the gaven element
        :param element: WebElement of Macaca
        :param rate: rate of the width or height of the element
        :return: None
        """
        self._press_side_of_element('right', element, rate)

    def wait_string(self, string, timeout=10000, interval=1000):
        """
        wait string between the gaven time
        :param string: string
        :param timeout: timeout(ms) that wait the gaven strings
        :param interval: interval(ms)
        :return: True or False
        """
        times = int(timeout / interval) + 1
        interval_s = interval / 1000

        for i in range(times):
            time.sleep(interval_s)

            source = self.driver.source
            if string in source:
                return True

            if i == times - 1:
                return False

    def wait_string_use_and(self, *args, timeout=10000, interval=1000):
        """
        wait all strings between the gaven time
        :param args: strings
        :param timeout: timeout(ms) that wait the gaven strings
        :param interval: interval(ms)
        :return: True or False
        """
        times = int(timeout / interval) + 1
        interval_s = interval / 1000

        for i in range(times):
            time.sleep(interval_s)

            source = self.driver.source
            previous = False
            for j in range(len(args)):
                if args[j] in source:
                    if j != 0 and not previous:
                        return False

                    previous = True

                    if j == len(args) - 1:
                        return True
                else:
                    if previous:
                        return False

            if i == times - 1:
                return False

    def wait_string_use_or(self, *args, timeout=10000, interval=1000):
        """
        wait anyone string between the gaven time
        :param args: strings
        :param timeout: timeout(ms) that wait the gaven strings
        :param interval: interval(ms)
        :return: True or False
        """
        times = int(timeout / interval) + 1
        interval_s = interval / 1000

        for i in range(times):
            time.sleep(interval_s)

            source = self.driver.source
            for string in args:
                if string in source:
                    return True

            if i == times - 1:
                return False

    def _find_element_in_nodes(self, nodes, using, value):
        for node in nodes:
            result = self._find_element_in_node(node, using, value)
            if result is not None:
                return result

    def _find_element_in_node(self, node, using, value):
        if node.get(using) == value:
            return node

        child_nodes = node.findall('node')
        if len(child_nodes):
            return self._find_element_in_nodes(child_nodes, using, value)
        else:
            return None

    @staticmethod
    def _parse_bounds(bounds_str):
        bounds = bounds_str.split(',')
        x_left = int(bounds[0].strip('['))
        y_up = int(bounds[1].split(']')[0])
        x_right = int(bounds[1].split(']')[1].strip('['))
        y_down = int(bounds[2].strip(']'))

        x_center = (x_left + x_right) / 2
        y_center = (y_up + y_down) / 2

        return x_center, y_center

    @staticmethod
    def _delete_file(filename):
        if os.path.exists(filename):
            os.remove(filename)

    def _wait_element(self, using, value, timeout=10000, interval=1000):
        times = int(timeout / interval) + 1
        interval_s = interval / 1000

        stability_flag = ''
        for i in range(times):
            time.sleep(interval_s)

            file = 'source.xml'
            with open(file, 'wt', encoding='utf-8') as f:
                f.write(self.driver.source)

            try:
                tree = ElementTree()
                tree.parse(file)
                root = tree.getroot()

                nodes = root.findall('node')
                result = self._find_element_in_nodes(nodes, using, value)
                if result is not None:
                    bounds_str = result.get('bounds')
                    if stability_flag != bounds_str:
                        stability_flag = bounds_str
                    else:
                        self._delete_file(file)
                        return result

                if i == times - 1:
                    self._delete_file(file)
                    return None
            except Exception:
                self._delete_file(file)
                raise Exception

    def wait_element_by_accessibility_id(self, value, timeout=10000, interval=1000):
        """
        wait element by accessibility id. in android, wait content-desc
        :param value: value
        :param timeout: timeout(ms) that wait the gaven strings
        :param interval: interval(ms)
        :return: True or False
        """
        result = self._wait_element('content-desc', value=value, timeout=timeout, interval=interval)
        if result is not None:
            return ShamElement(result)
        else:
            return None

    def click_element_by_accessibility_id(self, value, timeout=10000, interval=1000):
        """
        click element by accessibility id. in android, wait content-desc
        :param value: value
        :param timeout: timeout(ms) that wait the gaven strings
        :param interval: interval(ms)
        :return:

        raise:
            WebDriverException
        """
        result = self._wait_element('content-desc', value=value, timeout=timeout, interval=interval)
        if result is not None:
            x, y = self._parse_bounds(result.get('bounds'))
            self._tap(x, y)
        else:
            raise WebDriverException('No such accessibility id that value was you gaven.')

    def public(self, driver):
        '''

        :param driver:驱动
        :return: 一个屏幕像素list
        '''
        # 获取屏幕像素,返回一个list坐标
        self.driver = driver
        window = self.driver.get_window_size()

        width = int(window[u'width'])
        height = int(window[u'height'])
        zuobiao = [width, height]
        return zuobiao

    def left_swipe(self, driver):
        '''

        :param driver: 驱动
        :return:
        '''
        # 左划动
        # self.driver = driver
        a = {"direction": "left"}
        return self.driver.execute_script('mobile: swipe', a)
