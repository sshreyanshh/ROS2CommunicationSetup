# ROS 2 Communication Setup

A beginner-friendly ROS 2 Publisher--Subscriber communication demo built using Python and `rclpy`.

This project is part of **TechBlocks 12.1 - Day 3**, where we learn the basics of ROS 2 Nodes, Topics, Publishers, Subscribers, Messages, and Callbacks.

------------------------------------------------------------------------

## What Are We Building?

Two independent Python programs communicate with each other using ROS 2.

``` text
Publisher
    |
    |  "LEFT"
    v
/robot_command
    |
    v
Subscriber
    |
    v
Callback -> Robot Action
```

The publisher sends a robot command such as:

-   `LEFT`
-   `RIGHT`
-   `CENTER`
-   `STOP`

The subscriber receives the command and performs the corresponding
action.

------------------------------------------------------------------------

## Project Structure

``` text
ROS2CommunicationSetup/
|
├── publisher.py
├── subscriber.py
└── README.md
```

### `publisher.py`

Creates a ROS 2 publisher and continuously publishes commands to:

``` text
/robot_command
```

### `subscriber.py`

Creates a ROS 2 subscriber that listens to:

``` text
/robot_command
```

Whenever a message arrives, its callback function is executed.

------------------------------------------------------------------------

## Requirements

-   Ubuntu / WSL
-   ROS 2 Jazzy
-   Python 3
-   `rclpy`
-   `std_msgs`

Make sure ROS 2 is installed and configured in your WSL environment.

------------------------------------------------------------------------

## Setup

Open WSL and source the ROS 2 environment:

``` bash
source /opt/ros/jazzy/setup.bash
```

Verify that `rclpy` is available:

``` bash
python3 -c 'import rclpy; print("rclpy works!")'
```

Expected output:

``` text
rclpy works!
```

------------------------------------------------------------------------

## Running the Publisher

Open Terminal 1.

Navigate to the project directory:

``` bash
cd /path/to/ROS2CommunicationSetup
```

Run:

``` bash
python3 publisher.py
```

You should see:

``` text
Publishing: LEFT
Publishing: LEFT
Publishing: LEFT
```

Keep this terminal running.

------------------------------------------------------------------------

## Checking ROS 2 Communication

Open another WSL terminal.

First source ROS 2 again:

``` bash
source /opt/ros/jazzy/setup.bash
```

### Check running nodes

``` bash
ros2 node list
```

You should see:

``` text
/robot_publisher
```

### Check available topics

``` bash
ros2 topic list
```

You should see:

``` text
/robot_command
```

### View messages being published

``` bash
ros2 topic echo /robot_command
```

Expected output:

``` text
data: LEFT
---
data: LEFT
---
```

------------------------------------------------------------------------

## Running the Subscriber

Open another WSL terminal.

Source ROS 2:

``` bash
source /opt/ros/jazzy/setup.bash
```

Run:

``` bash
python3 subscriber.py
```

You should see:

``` text
Received: LEFT
Action: Turning LEFT

Received: LEFT
Action: Turning LEFT
```

------------------------------------------------------------------------

## Publisher -\> Topic -\> Subscriber

The publisher and subscriber do not directly communicate with each
other.

Instead:

``` text
+-------------+
|  Publisher  |
| publisher.py|
+------+------+
       |
       | publish()
       v
+------------------+
|  /robot_command  |
|      Topic       |
+--------+---------+
         |
         | message
         v
+----------------+
|   Subscriber   |
| subscriber.py  |
+-------+--------+
        |
        v
 command_callback()
        |
        v
   Robot Action
```

The publisher and subscriber only need to agree on:

1.  The topic name
2.  The message type

------------------------------------------------------------------------

## Message Example

The publisher creates a ROS 2 `String` message:

``` python
msg = String()
msg.data = "LEFT"
```

and publishes it:

``` python
self.publisher.publish(msg)
```

ROS 2 does not know what `"LEFT"` means.

It simply transports the message.

The subscriber decides what the command means:

``` python
if msg.data == "LEFT":
    print("Action: Turning LEFT")
```

------------------------------------------------------------------------

## ROS 2 Concepts Covered

  Concept          Meaning
  ---------------- -----------------------------------------------
  Node             A program participating in the ROS 2 system
  Publisher        Sends messages
  Topic            Communication channel
  Subscriber       Receives messages
  Message          Data being transmitted
  Callback         Function executed when a message arrives
  `rclpy.spin()`   Keeps the node alive and processes ROS events

------------------------------------------------------------------------

## Try It Yourself

Change this line in `publisher.py`:

``` python
msg.data = "LEFT"
```

Try:

``` python
msg.data = "RIGHT"
```

or:

``` python
msg.data = "CENTER"
```

or:

``` python
msg.data = "STOP"
```

Restart the publisher and observe how the subscriber responds.

------------------------------------------------------------------------

## Tech Stack

-   Python
-   ROS 2
-   `rclpy`
-   `std_msgs`
-   WSL / Ubuntu

------------------------------------------------------------------------

## TechBlocks 12.1

**Day 3 - ROS 2 Hands-on**

A beginner-friendly demonstration of ROS 2 communication using a simple robot-command example.
