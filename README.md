# 🐢 TurtleSim ROS2 Project

## 📌 Project Overview
This project is a **TurtleSim simulation** built using **ROS2 Humble** and **Python**. The goal of this project is to help beginners understand the basics of ROS2 by controlling a virtual turtle in a simulated environment.

## 🛠 Features
✅ Move the turtle using ROS2 topics
✅ Publish velocity commands to control movement
✅ Learn ROS2 package creation and execution
✅ Hands-on experience with `rclpy` and `geometry_msgs`

## 🚀 Getting Started

### 1️⃣ Prerequisites
Make sure you have the following installed:
- **Ubuntu 22.04** (Recommended for ROS2 Humble)
- **ROS2 Humble** ([Installation Guide](https://docs.ros.org/en/humble/Installation.html))
- **Python3**
- **colcon** (For building ROS2 packages)

### 2️⃣ Clone the Repository
```bash
cd ~/ros2_ws/src  # Navigate to your ROS2 workspace
git clone https://github.com/KunalJadhao/TurtleSim_ROS2_Project.git
cd ..
colcon build  # Build the package
source install/setup.bash  # Source the workspace
```

### 3️⃣ Run the Simulation
#### 🏁 Start the ROS2 TurtleSim Node
```bash
ros2 run turtlesim turtlesim_node
```

#### 🎮 Move the Turtle Using a ROS2 Publisher
```bash
ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist '{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.0}}'
```

### 4️⃣ Control the Turtle Manually
You can create a custom Python script to move the turtle programmatically using ROS2 nodes.

```bash
ros2 run my_package my_turtle_controller.py  # Replace with actual package and script name
```

## 📂 Project Structure
```
TurtleSim_ROS2_Project/
├── my_turtle_controller/   # Custom Python scripts for turtle movement
├── turtlesim/              # ROS2 TurtleSim package
├── README.md               # Project documentation
└── LICENSE                 # License file
```

## 🏆 Key Learnings
- How to **publish** and **subscribe** to ROS2 topics
- How to send velocity commands to a robot
- Basics of `rclpy` and `geometry_msgs`
- Running and debugging ROS2 nodes

## 🤝 Contributing
Feel free to **fork** this repository, submit **issues**, and send **pull requests**! Your contributions are always welcome. 😊

## 📜 License
This project is licensed under the **MIT License**.

## 🌍 Connect with Me
📌 **GitHub:** [KunalJadhao](https://github.com/KunalJadhao)  
📌 **LinkedIn:** www.linkedin.com/in/kunaljadhav07
