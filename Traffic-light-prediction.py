import random
import time 


lights = ["Green"  ,"Red " , "Yellow"]

while True:
    traffic_right = random.randint(1 , 100)
    time.sleep(1)
    traffic_left = random.randint(1 , 100)
    time.sleep(1)
    # traffic_Forward = random.randint(1 , 100)
    # time.sleep(1)
    # traffic_Backward = random.randint(1 , 100)
    # time.sleep(1)
    print(f"The traffic of left side is {traffic_left}\n The traffic of right side is {traffic_right}\n")

    for light in lights:
        if traffic_right > traffic_left:
            time.sleep(3)
            print("Yellow light is on, Kindely start your vehicles...")
            time.sleep(3)
            print("Green light is on move Steight Forward")

        elif traffic_left > traffic_right:
            time.sleep(3)
            print("Yellow light is on, Kindely start your vehicles...")
            time.sleep(3)
            print("Green light is on move Steight Forward")
        elif traffic_right == traffic_left:
            print("Too Little Chance...")

# import os
# import random
# import time
# import platform
# from enum import Enum

# class TrafficLight(Enum):
#     GREEN = "🟢 GREEN"
#     YELLOW = "🟡 YELLOW"
#     RED = "🔴 RED"

# class TrafficController:
#     """Efficient Traffic Light Controller"""
    
#     def __init__(self, duration: int = 10):
#         self.duration = duration
#         self.clear_cmd = 'cls' if platform.system() == 'Windows' else 'clear'
#         self.cycle_count = 0
    
#     def clear_screen(self):
#         """Screen clear karo"""
#         os.system(self.clear_cmd)
    
#     def get_traffic_density(self) -> tuple:
#         """Traffic density measure karo (1-100)"""
#         right_traffic = random.randint(1, 100)
#         left_traffic = random.randint(1, 100)
#         return right_traffic, left_traffic
    
#     def determine_direction(self, right: int, left: int) -> str:
#         """Kaunsi side ko priority do"""
#         if right > left + 10:  # Right mein zyada traffic
#             return "right"
#         elif left > right + 10:  # Left mein zyada traffic
#             return "left"
#         else:
#             return "balanced"
    
#     def show_yellow_light(self):
#         """Yellow light dikhao"""
#         self.clear_screen()
#         print("=" * 50)
#         print(f"🟡 YELLOW LIGHT 🟡")
#         print("=" * 50)
#         print("⚠️  Kindly prepare your vehicles...")
#         print("=" * 50)
#         time.sleep(3)
    
#     def show_green_light(self, direction: str):
#         """Green light dikhao"""
#         self.clear_screen()
#         print("=" * 50)
#         print(f"🟢 GREEN LIGHT 🟢")
#         print("=" * 50)
        
#         if direction == "right":
#             print("→ RIGHT SIDE: Move ahead! 🚗")
#         elif direction == "left":
#             print("← LEFT SIDE: Move ahead! 🚗")
#         else:
#             print("↔️  BOTH SIDES: Move ahead! 🚗")
        
#         print("=" * 50)
#         time.sleep(5)
    
#     def show_red_light(self):
#         """Red light dikhao"""
#         self.clear_screen()
#         print("=" * 50)
#         print(f"🔴 RED LIGHT 🔴")
#         print("=" * 50)
#         print("⛔ STOP! Wait for next signal...")
#         print("=" * 50)
#         time.sleep(2)
    
#     def display_traffic_status(self, right: int, left: int, direction: str):
#         """Traffic status display karo"""
#         self.clear_screen()
#         self.cycle_count += 1
        
#         print("\n" + "=" * 50)
#         print(f"🚦 TRAFFIC CONTROL SYSTEM - Cycle #{self.cycle_count}")
#         print("=" * 50)
#         print(f"\n📊 Traffic Density:")
#         print(f"   Right Side: {right}% {'█' * (right // 10)}")
#         print(f"   Left Side:  {left}% {'█' * (left // 10)}")
#         print(f"\n🎯 Priority: {direction.upper()}")
#         print("=" * 50 + "\n")
#         time.sleep(2)
    
#     def run(self, cycles: int = 5):
#         """System ko run karo"""
#         for _ in range(cycles):
#             # Traffic density check karo
#             right_traffic, left_traffic = self.get_traffic_density()
#             direction = self.determine_direction(right_traffic, left_traffic)
            
#             # Status display karo
#             self.display_traffic_status(right_traffic, left_traffic, direction)
            
#             # Signal sequence
#             self.show_yellow_light()
#             self.show_green_light(direction)
#             self.show_red_light()
        
#         self.clear_screen()
#         print("=" * 50)
#         print("🚦 Traffic Control System STOPPED")
#         print(f"Total Cycles Completed: {self.cycle_count}")
#         print("=" * 50)

# # Use karo
# if __name__ == "__main__":
#     controller = TrafficController()
#     controller.run(cycles=5)  # 5 cycles ke liye chalao