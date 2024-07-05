import numpy as np
import matplotlib.pyplot as plt

class PID:
    def __init__(self, kp, ki, kd, setpoint):
        self.kp = kp  # 比例增益
        self.ki = ki  # 积分时间
        self.kd = kd  # 微分时间
        self.setpoint = setpoint  # 设定值

        self.prev_error = 0  # 上一次误差
        self.integral = 0  # 积分项

    def update(self, process_variable):
        error = self.setpoint - process_variable  # 当前误差
        self.integral += error  # 更新积分项

        # 计算PID控制输出
        output = self.kp * error + self.ki * self.integral + self.kd * (error - self.prev_error)

        # 更新上一次误差
        self.prev_error = error

        return output

    def set_setpoint(self, setpoint):
        self.setpoint = setpoint

    def set_parameters(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd

if __name__ == "__main__":
    # 设置控制参数和设定值
    kp = 0.42
    ki = 0.05
    kd = 0.58
    setpoint = 100

    # 创建PID控制器对象
    pid_controller = PID(kp, ki, kd, setpoint)

    # 模拟过程变量
    process_variable = 0

    # 用于可视化的数据记录
    setpoints = [setpoint]
    process_variables = [process_variable]
    control_outputs = []

    # 模拟控制循环
    for _ in range(100):
        # 更新控制器设定值
        pid_controller.set_setpoint(setpoint)

        # 更新过程变量（模拟实际过程中的测量）
        process_variable += pid_controller.update(process_variable)

        #加入噪音（可不加）
        process_variable -=5

        # 记录数据用于可视化
        setpoints.append(setpoint)
        process_variables.append(process_variable)
        control_outputs.append(pid_controller.update(process_variable))

    # 可视化结果
    plt.figure(figsize=(10, 5))#创建了一个新的图形窗口，并指定了图形的大小为宽度10英寸，高度5英寸
    plt.subplot(2, 1, 1)#创建了一个2行1列的子图网格，并选择了网格中的第1个子图来绘制
    plt.plot(setpoints, label='Setpoint')#绘制了设定值随时间的变化曲线，并设置了标签为'Setpoint'
    plt.plot(process_variables, label='Process Variable')#绘制了过程变量随时间的变化曲线，并设置了标签为'Process Variable'
    plt.xlabel('Time')#设置了X轴的标签为'Time'
    plt.ylabel('Value')#设置了Y轴的标签为'Value'
    plt.title('PID Control')#设置了图形的标题为'PID Control'
    plt.legend()

    plt.subplot(2, 1, 2)#创建了一个2行1列的子图网格，并选择了网格中的第2个子图来绘制
    plt.plot(control_outputs, label='Control Output', color='r')
    plt.xlabel('Time')#设置了X轴的标签为'Time'
    plt.ylabel('Control Output')#设置了Y轴的标签为'Value'
    plt.legend()

    plt.tight_layout()#调整子图的布局，使它们更加紧凑
    plt.show()#显示了绘制好的图形，将其展示在屏幕上
