class Calculator:

    def judge_input_type(self, num1, num2):
        # 验证输入数据类型
        if num1 is None or num2 is None:
            # 判断输入是否为空
            # print("输入的值不能为空")
            return None
        elif (type(num1) == int or type(num1) == float or type(num1) == complex) and (
                type(num2) == int or type(num2) == float or type(num2) == complex):
            # 判断输入是否为数值类型
            return num1, num2
        else:
            # print("输入的值数据类型错误")

            return False

    def judge_input_len(self, num1, num2):
        # 验证输入数据长度
        num_list = [num1, num2]
        is_beyond = False
        # # python里数值对象为动态长度
        # return num_list[0], num_list[1]

        # c#
        # java
        # c++
        for num_value in num_list:
            if type(num_value) is int and -2147483647 <= num_value <= 2147483647:
                # 判断c++整型长度
                pass
            elif type(num_value) is float and -3.4E38 <= num_value <= 3.4E38:
                # 判断c++浮点数长度
                pass
            elif type(num_value) is complex:
                # 判断c++复数长度
                pass
            else:
                is_beyond = True
                break
        if is_beyond:
            # print("输入的值超出范围")
            return None
        else:
            return num_list[0], num_list[1]

    def judge_output_len(self, num_value):
        # 计算结果长度验证
        if type(num_value) is int and -2147483647 <= num_value <= 2147483647:
            # 判断c++整型长度
            return num_value
        elif type(num_value) is float and 3.4E-38 <= num_value <= 3.4E38:
            # 判断c++浮点数长度
            return num_value
        elif type(num_value) is complex:
            # 判断c++复数长度
            return num_value
        else:
            # print("计算结果的值超出范围")
            return "计算结果的值超出范围"

    def judge_add(self, num1, num2):
        tag_type = self.judge_input_type(num1, num2)
        tag_len = self.judge_input_len(num1, num2)
        if tag_type:
            if tag_len is not None:
                sum_number = num1 + num2
                tag_sum_len = self.judge_output_len(sum_number)
                if tag_sum_len == "计算结果的值超出范围":
                    return "output oversize error"
                else:
                    return sum_number
            else:
                print("input oversize error")
                return "input oversize error"
        elif tag_type is False:
            return "input type error"
        elif tag_type is None:
            return "input None error"


class Div:
    def div(self, a, b):
        return a/b

print(type(1+5j))
