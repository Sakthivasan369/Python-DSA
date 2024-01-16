class motor_bike:
    def __init__(self,frame_weight,engine_weight,wheels_weight):
        self.frame_weight=frame_weight
        self.engine_weight=engine_weight
        self.wheels_weight=wheels_weight
    def calculate_total_weight(self):
        total_weight=self.frame_weight+self.engine_weight+self.wheels_weight
        return total_weight
frame_weight =float(input("Enter The weight of the frame(in kg):"))
engine_weight =float(input("Enter the weight of the engine in kg: "))
wheels_weight =float(input("ENter The weight of the wheels in kg :"))
bike=motor_bike(frame_weight,engine_weight,wheels_weight)
total_weight=bike.calculate_total_weight()
print(f"The Total Weight Of the motor bike is {total_weight}kg.")
-----------------------------------------------------------------------------------------------------
Output
Enter The weight of the frame(in kg):100
Enter the weight of the engine in kg: 49
ENter The weight of the wheels in kg :12
The Total Weight Of the motor bike is 161.0kg.
