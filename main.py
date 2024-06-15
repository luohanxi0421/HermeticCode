from datetime import datetime


def calculate_days_of_life(birth_date, retirement_age=60):
    """
    计算从出生日期到今天活了多少天，以及距离退休还有多少天。

    :param birth_date: 出生日期，格式为 'YYYY-MM-DD'
    :param retirement_age: 退休年龄，默认为60岁
    :return: 一个元组，第一个元素是活了多少天，第二个元素是距离退休还有多少天
    """
    # 将字符串日期转换为datetime对象
    birth_date_obj = datetime.strptime(birth_date, '%Y-%m-%d')
    # 获取当前日期
    today = datetime.today()
    # 计算活了多少天
    days_lived = (today - birth_date_obj).days
    # 计算退休日期
    retirement_date = birth_date_obj.replace(year=birth_date_obj.year + retirement_age)
    # 如果退休日期小于今天，则认为已经退休
    if retirement_date < today:
        days_until_retirement = 0
    else:
        # 计算距离退休还有多少天
        days_until_retirement = (retirement_date - today).days
    return days_lived, days_until_retirement


def main():
    # 用户输入出生日期
    user_birth_date = input("请输入您的出生日期 (格式 YYYY-MM-DD): ")
    try:
        # 调用函数并接收结果
        days_lived, days_until_retirement = calculate_days_of_life(user_birth_date)
        # 打印结果
        print(f"您已经出生了 {days_lived} 天。")
        if days_until_retirement > 0:
            print(f"您距离退休还有 {days_until_retirement} 天。")
        else:
            print("您已经退休了。")
    except ValueError:
        print("输入的日期格式不正确，请确保使用 YYYY-MM-DD 格式。")


if __name__ == "__main__":
    main()