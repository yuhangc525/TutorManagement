from datetime import datetime


class Utils:
    def __init__(self):
        self.state_map = {
            0: "未出",
            1: "已推荐",
            2: "试讲",
            3: "已出",
            4: "废弃"
        }
        self.is_wechat_map = {
            0: "是",
            1: "否"
        }
        self.dim_is_wechat = 4
        self.dim_in_date = 5
        self.dim_state = 7
        self.dim_out_date = 8

    def dealState(self, state):
        return self.state_map.get(state)

    def dealDate(self, date):
        return date.strptime("%Y-%m-%d")

    def deal(self, turtle):
        result = []
        for one in turtle:
            one = list(one)
            one[self.dim_is_wechat] = self.is_wechat_map.get(one[self.dim_is_wechat])
            # one[self.dim_in_date] = self.dealDate(one[self.dim_in_date])
            # one[self.dim_out_date] = self.dealDate(one[self.dim_out_date])
            one[self.dim_state] = self.dealState(one[self.dim_state])
            one.pop(0)
            result.append(one)
        return result
