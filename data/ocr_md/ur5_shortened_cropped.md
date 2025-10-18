# 2. Your Robot 

Introduction Congratulations on the purchase of your new Universal Robots robot, which consists of the robot arm (manipulator), Control Box and the Teach Pendant.

Originally designed to mimic the range of motion of a human arm, the robot arm is composed of aluminium tubes, articulated by six joints, allowing for a high range of flexibility in your automation installation.
The Universal Robots patented programming interface, PolyScope, allows you to create, load and run your automation applications.

In the boxes

- Robot arm
- Control Box
- Teach Pendant or a 3PE Teach Pendant
- Mounting bracket for the Control Box
- Mounting bracket for the 3PE Teach Pendant
- Key for opening the Control Box
- Cable for connecting the robot arm and the Control Box (multiple options available depending on robot size)
- Mains cable or power cable compatible with your region
- Round sling or lifting sling (depending on robot size)
- Tool cable adapter (depending on robot version)
- This manual

About the robot arm

The Joints, Base and Tool Flange are the main components of the robot arm. The controller coordinates joint motion to move the robot arm.

Attaching an end effector (tool) to the Tool Flange at the end of the robot arm, allows the robot to manipulate a workpiece. Some tools have a specific purpose beyond manipulating a part, for example, QC inspection, applying adhesives and welding.
![img-0.jpeg](img-0.jpeg)
1.1: The main components of the robot arm.

- Base: where the robot arm is mounted.
- Shoulder and Elbow: make larger movements.
- Wrist 1 and Wrist 2: make finer movements.
- Wrist 3: where the tool is attached to the Tool Flange.

The robot is partly completed machinery, as such a Declaration of Incorporation is provided. A risk assessment is required for each robot application.

About the manual

This manual contains safety information, guidelines for safe use, and instructions to mount the robot arm, Control Box and Teach Pendant. You can also find instructions for how to begin to install and how to start programming the robot.

Read and adhere to the intended uses. Perform a risk assessment. Install and use in accordance with the electrical and mechanical specifications provided in this user manual.

Risk assessment requires an understanding of the hazards, risks and risk reduction measures for the robot application. Robot integration can require a basic level of mechanical and electrical training.

|  Contentdisclaimer | Universal Robots A/Scontinues to improve the reliability and performance of its products, and as such reserves the right to upgrade products, and product documentation, without prior warning. Universal Robots A/S takes every care to ensure the content of the User Manual/s is precise and correct, but takes no responsibility for any errors or missing information.This manual does not contain warranty information.  |
| --- | --- |
|  myUR | The myUR portal allows you to register all your robots, keep track of service cases and answer general support questions.Sign into myur.universal-robots.com to access the portal.In the myUR portal, your cases are handled either by your preferred distributor, or escalated to Universal Robots Customer Service teams.You can also subscribe to robot monitoring and manage additional user accounts in your company.  |
|  Support | The support sitewww.universal-robots.com/support contains other language versions of this manual  |
|  UR+ | The online showroom UR+www.universal-robots.com/plus provides cutting-edge products to customize your UR robot application. You can find everything you need in one place – from tools and accessories to software.UR+ products connect to and work with UR robots to ensure simple set-up and an overall smooth user experience. All UR+ products are tested by UR.  |
|   | You can also access the UR+ Partner Program via our software platformplus.universal-robots.com to design more user-friendly products for UR robots.  |
|  UR forums | The UR Forumforum.universal-robots.com allows robot enthusiasts of all skill levels to connect to UR and each other, to ask questions and to exchange information. While the UR Forum was created by UR+ and our admins are UR employees, the majority of the content is created by you, the UR Forum user.  |
|  Academy | The UR Academy siteacademy.universal-robots.com offers a variety of training opportunities.  |
|  Developer suite | The UR Developer Suiteuniversal-robots.com/products/ur-developer-suite is a collection of all the tools needed to build an entire solution, including developing URCaps, adapting end-effectors, and integrating hardware.  |

|  Online | Manuals, guides and handbooks can be read online. We have gathered a large number of  |
| --- | --- |
|  manuals | documents at https://www.universal-robots.com/manuals  |
|   | • PolyScope Software Handbook with descriptions and instructions for the software  |
|   | • The Service Handbook with instructions for troubleshooting, maintenance and repair  |
|   | • The Script Directory with scripting for in depth programming  |

# 2.1. Technical Specifications UR5e

|  |   |
| --- | --- |
|  Robot type | UR5e  |
|  Robot weight | $20.7 \mathrm{~kg} / 45.7 \mathrm{lb}$  |
|  Maximum payload | $5 \mathrm{~kg} / 11 \mathrm{lb}$  |
|  Reach | $850 \mathrm{~mm} / 33.5$ in  |
|  Joint ranges | Unlimited rotation of tool flange, $\pm 360^{\circ}$ for all other joints $\pm 360^{\circ}$ for all joints  |
|  Speed | Joints: Max $180^{\circ} / \mathrm{s}$.
Tool: Approx. $1 \mathrm{~m} / \mathrm{s} /$ Approx. $39.4 \mathrm{in} / \mathrm{s}$.  |
|  System update frequency | 500 Hz  |
|  Force Torque sensor accuracy | 4 N  |
|  Pose repeatability | $\pm 0.03 \mathrm{~mm} / \pm 0.0011$ in (1.1 mils)per ISO 9283  |
|  Footprint | Ø149 mm / 5.9 in  |
|  Degrees of freedom | 6 rotating joints  |
|  Control Box size ( $\mathrm{W} \times \mathrm{H} \times \mathrm{D}$ ) | $460 \mathrm{~mm} \times 449 \mathrm{~mm} \times 254 \mathrm{~mm} / 18.2$ in $\times 17.6$ in $\times 10$ in  |
|  Control Box I/O ports | 16 digital in, 16 digital out, 2 analog in, 2 analog out  |
|  Tool I/O ports | 2 digital in, 2 digital out, 2 analog in  |
|  Tool Communication | RS  |
|  Tool I/O power supply \& voltage | 12 V/24 V 1.5 A (Dual pin) 1 A (Single pin)  |
|  Control Box I/O power supply | 24 V 2 A in Control Box  |
|  Communication | TCP/IP 1000 Mbit: IEEE 802.3ab, 1000BASE-T Ethernet socket, MODBUS TCP \& EtherNet/IP Adapter, Profinet  |
|  Programming | PolyScope graphical user interface on 12" touchscreen  |
|  Noise | Robot Arm: Less than 60dB(A) Control Box: Less than 50dB(A)
Robot Arm: Less than 65dB(A) Control Box: Less than 50dB(A)  |
|  IP classification | IP54  |
|  Cleanroom classification | Robot Arm: ISO Class 5, Control Box: ISO Class 6  |
|  Power consumption (average) | 570 W  |
|  Power consumption | Approx. 250 W using a typical program  |
|  Short-Circuit Current Rating (SCCR) | 200A  |
|  Collaboration operation | 17 advanced safety functions. In compliance with: EN ISO 13849-1, PLd, Cat. 3 and EN ISO 10218-1  |
|  Materials | Aluminium, PC/ASA plastic  |
|  Ambient temperature range | $0-50^{\circ} \mathrm{C}$. At ambient temperatures above $35^{\circ} \mathrm{C}$, the robot may operate at reduced speed and performance.  |
|  Control Box power source | 100-240 VAC, 47-440 Hz  |
|  TP cable: Teach Pendant to Control Box | $4.5 \mathrm{~m} / 177$ in  |
|  Robot Cable: Robot Arm to Control Box (options) | Standard (PVC) $6 \mathrm{~m} / 236$ in $\times 13.4 \mathrm{~mm}$
Standard (PVC) $12 \mathrm{~m} / 472.4$ in $\times 13.4 \mathrm{~mm}$
Hiflex (PUR) $6 \mathrm{~m} / 236$ in $\times 12.1 \mathrm{~mm}$
Hiflex (PUR) $12 \mathrm{~m} / 472.4$ in $\times 12.1 \mathrm{~mm}$  |

# 2.2. Maximum Payload 

Description The rated robot arm payload depends on the center of gravity (CoG) offset of the payload, as shown below. The CoG offset is defined as the distance from the center of the tool flange to the center of gravity of the attached payload.

The robot arm can accommodate a long center of gravity offset, if the payload is placed below the tool flange. For example when computing the payload mass in a pick and place application, consider both the gripper and the workpiece.

The robot's capacity to accelerate can be reduced if the payload CoG exceeds the robot's reach and payload. You can verify the reach and payload of your robot in the Technical Specifications.

Payload $[\mathrm{kg}]$
![img-1.jpeg](img-1.jpeg)

The relationship between the rated payload and the center of gravity offset.

## Payload

inertia

You can configure payloads with high inertia, if the payload is set correctly. The controller software automatically adjusts accelerations when the following parameters are correclty configured:

- Payload mass
- Center of gravity
- Inertia

You can use the URSim to evaluate the accelerations and cycle times of the robot motions with a specific payload.

# 2.3. Stopping Time and Stopping Distance 

## Description

![img-2.jpeg](img-2.jpeg)

## NOTICE

You can set user-defined safety rated maximum stopping time and distance.
If user-defined settings are used, the program speed is dynamically adjusted to always comply with the selected limits.

The graphical data provided for Joint 0 (base), Joint 1 (shoulder) and Joint 2 (elbow) is valid for stopping distance and stopping time:

- Category 0
- Category 1
- Category 2

The Joint 0 test was carried out using a horizontal movement, where the rotational axis was perpendicular to the ground. For the Joint 1 and Joint 2 tests, the robot followed a vertical trajectory, where the rotational axes were parallel to the ground, and the stop was done while the robot was moving downward.
The $Y$-axis is the distance from where the stop is initiated to the final position.
The payload CoG is at the tool flange.

Joint 0
(BASE)
Stopping distance in meters for $33 \%$ of 5 kg
![img-3.jpeg](img-3.jpeg)

Stopping distance in meters for $66 \%$ of 5 kg
![img-4.jpeg](img-4.jpeg)

## Joint 0

(BASE)
Stopping time in seconds for $33 \%$ of 5 kg
![img-5.jpeg](img-5.jpeg)

Stopping time in seconds for $66 \%$ of 5 kg
![img-6.jpeg](img-6.jpeg)

Stopping time in seconds for maximum payload of 5 kg

![img-7.jpeg](img-7.jpeg)

## Joint 1 (SHOULDER)

Stopping distance in meters for $33 \%$ of 5 kg

![img-8.jpeg](img-8.jpeg)

Stopping distance in meters for $66 \%$ of 5 kg

![img-9.jpeg](img-9.jpeg)

Stopping distance in meters for maximum payload of 5 kg

![img-10.jpeg](img-10.jpeg)

# Joint 1 (SHOULDER) 

Stopping time in seconds for $33 \%$ of 5 kg

Stopping time in seconds for $66 \%$ of 5 kg

Stopping time in seconds for maximum payload of 5 kg

Joint 2
(ELBOW)
Stopping distance in meters for $33 \%$ of 5 kg
![img-11.jpeg](img-11.jpeg)

Stopping distance in meters for $66 \%$ of 5 kg
![img-12.jpeg](img-12.jpeg)

## Joint 2

(ELBOW)
Stopping time in seconds for $33 \%$ of 5 kg
![img-13.jpeg](img-13.jpeg)

Stopping time in seconds for $66 \%$ of 5 kg
![img-14.jpeg](img-14.jpeg)

Stopping time in seconds for maximum payload of 5 kg
![img-15.jpeg](img-15.jpeg)

# 3. Safety 

Description Review the content here to understand the key safety guidelines, including important safety messages and your responsibilities when working with the robot. Note that system design and installation are not covered here.

### 3.1. General

Description Read the general safety information and the instructions and guidance pertaining to the risk assessment and intended use provided. Give particular attention to text accompanied by warning symbols. Subsequent sections describe and define safetyrelated functions particularly relevant for collaborative applications.

Read and understand the specific engineering data relevant to mounting and installation, in order to understand the integration of UR robots before the robot is powered on for the first time.

It is essential to observe and follow all assembly instructions in the following sections of this manual.

## NOTICE

Universal Robots disclaims any and all liability if the robot (arm Control Box with or without Teach Pendant) is damaged, changed or modified in any way. Universal Robots cannot be held responsible for any damages caused to the robot or any other equipment due to programming errors, unauthorized access to the UR robot and its contents, or malfunctioning of the robot.

# 3.2. Safety Message Types 

Description Safety messages are used to emphasize important information. Read all the messages to help ensure safety and to prevent injury to personnel and product damage. The safety message types are defined below.

## WARNING

Indicates a hazardous situation that, if not avoided, can result in death or serious injury.

## WARNING: ELECTRICITY

Indicates a hazardous electrical situation that, if not avoided, can result in death or serious injury.

## WARNING: HOT SURFACE

Indicates a hazardous hot surface where injury can result from contact and non-contact proximity.

## CAUTION

Indicates a hazardous situation that, if not avoided, can result in injury.

## GROUND

Indicates grounding.

## PROTECTIVE GROUND

Indicates protective grounding.

## NOTICE

Indicates the risk of damage to equipment and/or information to be noted.

## READ MANUAL

Indicates more detailed information that should be consulted in the manual.

# 3.3. General Warnings and Cautions 

Description The following warnings messages can be repeated, explained or detailed in subsequent sections.

## WARNING

Failure to adhere to the general safety practices, listed below, can result in injury or death.

- Verify the robot arm and tool/end effector are properly and securely bolted in place.
- Verify the robot application has ample space to operate freely.
- Verify the personnel are protected during the lifetime of the robot application including transport, installation, commissioning, programming/ teaching, operation and use, dismantling and disposing.
- Verify robot safety configuration parameters are set to protect personnel, including those who can be within reach of the robot application.
- Avoid using the robot if it is damaged.
- Avoid wearing loose clothing or jewelry when working with the robot. Tie back long hair.
- Avoid placing any fingers behind the internal cover of the Control Box.
- Inform users of any hazardous situations and the protection that is provided, explain any limitations of the protection and the residual risks.
- Inform users of the location of the emergency stop button(s) and how to activate the emergency stop in case of an emergency or an abnormal situation.
- Warn people to keep outside the reach of the robot, including when the robot application is about to start-up.
- Be aware of robot orientation to understand the direction of movement when using the Teach Pendant.
- Adhere to the requirements and guidance in ISO 10218-2.


## WARNING

Handling tools/end effectors with sharp edges and/or pinch points can result in injury.

- Make sure tools/end effectors have no sharp edges or pinch points.
- Protective gloves and/or protective eyeglasses could be required.

# WARNING: HOT SURFACE 

Prolonged contact with the heat generated by the robot arm and the Control Box, during operation, can lead to discomfort resulting in injury.

- Do not handle or touch the robot while in operation or immediately after operation.
- Check the temperature on the log screen before handling or touching the robot.
- Allow the robot to cool down by powering it off and waiting one hour.


## CAUTION

Failure to perform a risk assessment prior to integration and operation can increase risk of injury.

- Perform a risk assessment and reduce risks prior to operation.
- If determined by the risk assessment, do not enter the range of the robot movement or touch the robot application during operation. Install safeguarding.
- Read the risk assessment information.


## CAUTION

Using the robot with untested external machinery, or in an untested application, can increase the risk of injury to personnel.

- Test all functions and the robot program separately.
- Read the commissioning information.


## NOTICE

Very strong magnetic fields can damage the robot.

- Do not expose the robot to permanent magnetic fields.


## READ MANUAL

Verify all mechanical and electrical equipment is installed according to relevant specifications and warnings.

# 3.4. Integration and Responsibility 

Description The information in this manual does not cover designing, installing, integrating and operating a robot application, nor does it cover all peripheral equipment that can influence the safety of the robot application. The robot application must be designed and installed in accordance with the safety requirements set forth in the relevant standards and regulations of the country where the robot is installed.

The person/s integrating the UR robot are responsible for ensuring that the applicable regulations in the country concerned are observed and that any risks in the robot application are adequately reduced. This includes, but is not limited to:

- Performing a risk assessment for the complete robot system
- Interfacing other machines and additional safeguarding if required by the risk assessment
- Setting the correct safety settings in the software
- Ensuring safety measures are not modified
- Validating the robot application is designed, and installed and integrated
- Specifying instructions for use
- Marking the robot installation with relevant signs and contact information of the integrator
- Retaining all documentation; including the application risk assessment, this manual and additional relevant documentation.


### 3.5. Stop Categories

Description Depending on the circumstances, the robot can initiate three types of stop categories defined according to IEC 60204-1. These categories are defined in the following table.

| Stop <br> Category | Description |
| :-- | :-- |
| 0 | Stop the robot by immediate removal of power. |
| 1 | Stop the robot in an orderly, controlled manner. Power is removed once <br> the robot is stopped. |
| 2 | *Stop the robot with power available to the drives, while maintaining the <br> trajectory. Drive power is maintained after the robot is stopped. |

*Universal Robots robots' Category 2 stops are further described as SS1 or as SS2 type stops according to IEC 61800-5-2.

# 4. Risk Assessment 

Description The risk assessment is a requirement that shall be performed for the application. The application risk assessment is the responsibility of the integrator. The user can also be the integrator.

The robot is partly completed machinery, as such the safety of the robot application depends on the tool/end effector, obstacles and other machines. The party performing the integration must use ISO 12100 and ISO 10218-2 to conduct the risk assessment. Technical Specification ISO/TS 15066 can provide additional guidance for collaborative applications. The risk assessment shall consider all tasks throughout the lifetime of the robot application, including but not limited to:

- Teaching the robot during set-up and development of the robot application
- Troubleshooting and maintenance
- Normal operation of the robot application

A risk assessment must be conducted before the robot application is powered on for the first time. The risk assessment is an iterative process. After physically installing the robot, verify the connections, then complete the integration. A part of the risk assessment is to determine the safety configuration settings, as well as the need for additional emergency stops and/or other protective measures required for the specific robot application.

Safety configuration settings

Identifying the correct safety configuration settings is a particularly important part of developing robot applications. Unauthorized access to the safety configuration must be prevented by enabling and setting password protection.

# WARNING 

Failure to set password protection can result in injury or death due to purposeful or inadvertent changes to configuration settings.

- Always set password protection.
- Set up a program for managing passwords, so that access is only by persons who understand the effect of changes.

Some safety functions are purposely designed for collaborative robot applications. These are configurable through the safety configuration settings. They are used to address risks identified in the application risk assessment.

The following limit the robot and as such can affect the energy transfer to a person by the robot arm, end effector and workpiece.

- Force and power limiting: Used to reduce clamping forces and pressures exerted by the robot in the direction of movement in case of collisions between the robot and the operator.
- Momentum limiting: Used to reduce high transient energy and impact forces in case of collisions between robot and operator by reducing the speed of the robot.
- Speed limitation: Used to ensure the speed is less that the configured limit.

The following orientation settings are used to avoid movements and reduce exposure of sharp edges and protrusions to a person.

- Joint, elbow and tool/end effector position limiting: Used to reduce risks associated with certain body parts: Avoid movement towards head and neck.
- Tool/end effector orientation limiting: Used to reduce risks associated with certain areas and features of the tool/end effector and work-piece: Avoid sharp edges being pointed towards the operator, by turning the sharp edges inward towards the robot.

Stopping performance risks

Some safety functions are purposely designed for any robot application. These features are configurable through the safety configuration settings. They are used to address risks associated with the stopping performance of the robot application.

The following limit the robot stopping time and stopping distance to ensure stopping will occur before reaching the configured limits. Both settings automatically affect the speed of the robot to ensure the limit is not exceeded.

- Stopping Time Limit: Used to limit the stopping time of the robot.
- Stopping Distance Limit: Used to limit the stopping distance of the robot.

If either of the above is used, there is no need for manually performed periodic stopping performance testing. The robot safety control does continuous monitoring.

If the robot is installed in a robot application where hazards cannot be reasonably eliminated or risks cannot be sufficiently reduced by use of the built-in safety-related functions (e.g. when using a hazardous tool/end effector,or hazardous process), then safeguarding is required. See ISO 10218-2.

# WARNING 

Failure to conduct a application risk assessment can increase risks.

- Always conduct an application risk assessment for foreseeable risks and reasonably foreseeable misuse.

For collaborative applications, the risk assessment includes the foreseeable risks due to collisions and to reasonably foreseeable misuse.

The risk assessment shall address:

- Severity of harm
- Likelihood of occurrence
- Possibility to avoid the hazardous situation

Potential
Hazards

Universal Robots identifies the potential significant hazards listed below for consideration by the integrator. Other significant hazards can be associated with a specific robot application.

- Penetration of skin by sharp edges and sharp points on tool/end effector or tool/end effector connector.
- Penetration of skin by sharp edges and sharp points on nearby obstacles.
- Bruising due to contact.
- Sprain or bone fracture due to impact.
- Consequences due to loose bolts that hold the robot arm or tool/end effector.
- Items falling out of, or flying from the tool/end effector, e.g. due to a poor grip or power interruption.
- Mistaken understanding of what is controlled by multiple emergency stop buttons.
- Incorrect setting of the safety configuration parameters.
- Incorrect settings due to unauthorized changes to the safety configuration parameters.


### 4.1. Pinch Hazard

|  Description | You can avoid pinching hazards by removing obstacles in these areas, by placing the robot differently, or by using a combination of safety planes and joint limits to eliminate the hazards by preventing the robot moving into this area of its workspace.  |
| --- | --- |
|   | CAUTION  |
|   | Placing the robot in certain areas can create pinching hazards that can lead to injury.  |
|   | Due to the physical properties of the robot arm, certain workspace areas require attention regarding pinching hazards. One area (left) is defined for radial motions when the wrist 1 joint is at least 750 mm from the base of the robot. The other area (right) is within 200 mm of the base of the robot, when moving tangentially.  |

# 6.1. Workspace and Operating Space 

Description The workspace is the range of the fully extended robot arm, horizontally and vertically. The operating space is the location where the robot is expected to function.

## NOTICE

Disregard for the robot workspace and operating space can result in the damage to property.

- Consider the information below when choosing the operating space for the robot.


## NOTICE

Moving the tool close to the cylindrical volume can cause the joints to move too fast, leading to loss of functionality and damage to property.

- Do not move the tool close to the cylindrical volume, even when the tool is moving slowly.

The cylindrical volume is both directly above and directly below the robot base. The robot extends 850 mm from the base joint.
![img-16.jpeg](img-16.jpeg)

# 6.8. Mains Connections 

Description
The mains cable from the Control Box has a standard IEC plug at the end. Connect a country specific mains plug, or cable, to the IEC plug.

## NOTICE

- IEC 61000-6-4:Chapter 1 scope: "This part of IEC 61000 for emission requirement applies to electrical and electronic equipment intended for use within the environment of existing at industrial (see 3.1.12) locations."
- IEC 61000-6-4:Chapter 3.1.12 industrial location: "Locations characterized by a separate power network, supplied from a high- or medium-voltage transformer, dedicated for the supply of the installation"

Mains connections

To power the robot, the Control Box shall be connected to the mains via the supplied power cord. The IEC C13 connecter on the power cord connects to the IEC C14 appliance inlet at the bottom of the Control Box.

## NOTICE

Always use a power cord with a country specific wall plug when connecting to the Control Box. Do not use an adapter.

As a part of the electrical installation, provide the following:

- Connection to ground
- Main fuse
- Residual current device
- A lockable (in the OFF position) switch

A main switch shall be installed to power off all equipment in the robot application as an easy means for lockout. The electrical specifications are shown in the table below.

| Parameter | Min | Typ | Max | Unit |
| :-- | :--: | :--: | :--: | :--: |
| Input voltage | 90 | - | 264 | VAC |
| External mains fuse (90-200V) | 8 | - | 16 | A |
| External mains fuse (200-264V) | 8 | - | 16 | A |
| Input frequency | 47 | - | 440 | Hz |
| Stand-by power | - | - | $<1.5$ | W |
| Nominal operating power | 90 | 150 | 325 | W |

# WARNING: ELECTRICITY 

Failure to follow any of the below can result in serious injury or death due to electrical hazards.

- Ensure the robot is grounded correctly (electrical connection to ground). Use the unused bolts associated with grounding symbols inside the Control Box to create common grounding of all equipment in the system. The grounding conductor shall have at least the current rating of the highest current in the system.
- Ensure the input power to the Control Box is protected with a Residual Current Device (RCD) and a correct fuse.
- Lockout all power for the complete robot installation during service.
- Ensure other equipment shall not supply power to the robot I/O when the robot is locked out.
- Ensure all cables are connected correctly before the Control Box is powered. Always use the original power cord.

# 7.1. Freedrive 

Description
Freedrive allows the robot arm to be manually pulled into desired positions and/or poses.
The joints move with little resistance because the brakes are released. While the robot arm is being moved manually, it is in Freedrive.
As the robot arm in Freedrive approaches a predefined limit or plane (see Software Safety Restrictions), resistance increases.
This makes pulling the robot into position feel heavy.

## WARNING

Injury to personnel can occur due to unexpected motion.

- Verify the configured payload is the payload being used.
- Verify the correct payload is securely attached to the tool flange.

Enabling
Freedrive
You can enable Freedrive in the following ways:

- Use the 3PE Teach Pendant.
- Use the Freedrive on robot.
- Use I/O Actions.


## NOTICE

Enabling Freedrive while you are moving the robot arm, can cause it to drift leading to faults.

- Do not enable Freedrive while you are pushing or touching the robot.

3PE Teach
Pendant
To use the 3PE TP button to freedrive the robot arm:

1. Rapidly light-press, release, light-press again and keep holding the 3PE button in this position.

Now you can pull the robot arm into a desired position, while the light-press is maintained.

|  Freedrive on | To use Freedrive on robot to freedrive the robot arm:  |
| --- | --- |
|  robot |   |
|   | 1. Press-and-hold the button of switch configured for Freedrive on robot.  |
|   | 2. When the Freedrive panel appears in PolyScope, select the desired movement type for the robot arm’s joints. Or use the list of axes to customize the movement type.  |
|   | 3. You can define the type of feature if required, by selecting an option from the Feature dropdown list.  |
|   | The robot arm can stop moving if it approaches a singularity scenario. Tap All axes are free in the Freedrive panel to resume movement.  |
|   | 4. Move the robot arm as desired.  |
|  Backdrive | During initialization of the robot arm, minor vibrations may be observed when the robot brakes are released. In some situations, such as when the robot is close to collision, these vibrations are undesirable. Use Backdrive to force specific joints to a desired position without releasing all brakes in the robot arm.  |

# 7.1.1. Freedrive Panel 

Description When the robot arm is in Freedrive, a panel appears on PolyScope, as illustrated below.
![img-17.jpeg](img-17.jpeg)

The LED on the status bar of the Freedrive panel indicates:

- When one or more joints are approaching their joint limits.
- When the robot arm's positioning is approaching singularity. Resistance increases as the robot approaches singularity, making it feel heavy to position.
![img-18.jpeg](img-18.jpeg)

Icons
You can lock one or more of the axes allowing the TCP to move in a particular direction, as defined in the table below.

| All axes are free | Movement is allowed through all axes. |
| :--: | :--: |
| Plane | Movement is only allowed through the X-axis and Y-axis. |
| Translation | Movement is allowed through all axes, without rotation. |
| Rotation | Movement is allowed through all axes, in a spherical motion, around the TCP. |

# CAUTION 

Moving the robot arm in some axes when a tool is attached, can present a pinch point.

- Use caution when moving the robot arm in any axis.

# 8. Installation 

Description Installing the robot can require the configuration and use of input and output signals (I/Os). These different types of I/Os and their uses are described in the following sections.

### 8.1. Electrical Warnings and Cautions

Warnings
Observe the following warnings for all the interface groups, including when you design and install an application.

## WARNING

Failure to follow any of the below can result in serious injury or death, as the safety functions could be overridden.

- Never connect safety signals to a PLC that is not a safety PLC with the correct safety level. It is important to keep safety interface signals separated from the normal I/O interface signals.
- All safety-related signals shall be constructed redundantly (two independent channels).
- Keep the two independent channels separate so a single fault cannot lead to loss of the safety function.


## WARNING: ELECTRICITY

Failure to follow any of the below can result in serious injury or death due to electrical hazards.

- Make sure all equipment not rated for water exposure remain dry. If water is allowed to enter the product, lockout-tagout all power and then contact your local Universal Robots service provider for assistance.
- Only use the original cables supplied with the robot only. Do not use the robot for applications where the cables are subject to flexing.
- Use caution when installing interface cables to the robot I/O. The metal plate in the bottom is intended for interface cables and connectors. Remove the plate before drilling holes. Make sure that all shavings are removed before reinstalling the plate. Remember to use correct gland sizes.

# CAUTION 

Disturbing signals with levels higher than those defined in the specific IEC standards can cause unexpected behaviors from the robot. Be aware of the following:

- The robot has been tested according to international IEC standards for ElectroMagnetic Compatibility (EMC). Very high signal levels or excessive exposure can damage the robot permanently. EMC problems are found to happen usually in welding processes and are normally prompted by error messages in the log. Universal Robots cannot be held responsible for any damages caused by EMC problems.
- I/O cables going from the Control Box to other machinery and factory equipment may not be longer than 30 m , unless additional tests are performed.


## GROUND

Negative connections are referred to as Ground (GND) and are connected to the casing of the robot and the Control Box. All mentioned GND connections are only for powering and signalling. For PE (Protective Earth) use the M6-size screw connections marked with earth symbols inside the Control Box. The grounding conductor shall have at least the current rating of the highest current in the system.

## READ MANUAL

Some I/Os inside the Control Box can be configured for either normal or safetyrelated I/O. Read and understand the complete Electrical Interface chapter.

# 8.2. Safety I/O 

Safety I/O This section describes dedicated safety input (Yellow terminal with red text) and configurable I/O (Yellow terminals with black text) when configured as safety I/O.
Safety devices and equipment must be installed according to the safety instructions and the risk assessment in chapter Safety.
All safety I/O are paired (redundant), so a single fault does not cause loss of the safety function. However, the safety I/O must be kept as two separate branches.

The permanent safety input types are:

- Robot Emergency Stop for emergency stop equipment only
- Safeguard Stop for protective devices
- 3PE Stop for protective devices

Table The functional difference is shown below.

|  | Emergency <br> Stop | Safeguard Stop | 3PE Stop |
| :-- | :--: | :--: | :--: |
| Robot stops moving | Yes | Yes | Yes |
| Program execution | Pauses | Pauses | Pauses |
| Drive power | Off | On | On |
| Reset | Manual | Automatic or <br> manual | Automatic or <br> manual |
| Frequency of use | Infrequent | Every cycle to <br> infrequent | Every cycle to <br> infrequent |
| Requires re-initialization | Brake release <br> only | No | No |
| Stop Category (IEC 60204-1) | 1 | 2 | 2 |
| Performance level of monitoring <br> function (ISO 13849-1) | PLd | PLd | PLd |

Safety Use the configurable I/O to set up additional safety I/O functionality, e.g. Emergency Stop caution Output. Configuring a set of configurable I/O for safety functions are done through the GUI, (see part Part II PolyScope Manual).

## CAUTION

Failure to verify and test the safety functions regularly can lead to hazardous situations.

- Safety functions shall be verified before putting the robot into operation.
- Safety functions shall be tested regularly.

OSSD signals

OSSD Safety Signals

All configured and permanent safety inputs are filtered to allow the use of OSSD safety equipment with pulse lengths under 3 ms . The safety input is sampled every millisecond and the state of the input is determined by the most frequently seen input signal over the last 7 milliseconds.

You can configure the Control Box to output OSSD pulses when a safety output is inactive/high. OSSD pulses detect the ability of the Control Box to make safety outputs active/low. When OSSD pulses are enabled for an output, a 1 ms low pulse is generated on the safety output once every 32 ms . The safety system detects when an output is connected to a supply and shuts down the robot.
The illustration below shows: the time between pulses on a channel ( 32 ms ), the pulse length (1ms) and the time from a pulse on one channel to a pulse on the other channel (18ms)
![img-19.jpeg](img-19.jpeg)

To enable OSSD for Safety Output

1. In the Header, tap Installation and select Safety.
2. Under Safety, select I/O.
3. On the I/O screen, under Output Signal, select the desired OSSD checkbox. You must assign the output signal to enable the OSSD checkboxes.

Default safety configuration

The robot is delivered with a default configuration, which enables operation without any additional safety equipment (see illustration below).
![img-20.jpeg](img-20.jpeg)

Connecting emergency stop buttons

Most applications require one or more extra emergency stop buttons. The illustration below shows how one or more emergency stop buttons can be connected.
![img-21.jpeg](img-21.jpeg)

Sharing the Emergency Stop with other machines

You can set up a shared emergency stop function between the robot and other machines by configuring the following I/O functions via the GUI. The Robot Emergency Stop Input cannot be used for sharing purposes. If more than two UR robots or other machines need to be connected, a safety PLC must be used to control the emergency stop signals.

- Configurable input pair: External emergency stop.
- Configurable output pair: System emergency stop.

The illustration below shows how two UR robots share their emergency stop functions. In this example the configured I/Os used are CIO-CI1 and CO0-CO1.
![img-22.jpeg](img-22.jpeg)

Safeguard stop with automatic resume

This configuration is only intended for applications where the operator cannot go through the door and close it behind him. The configurable I/O is used to setup a reset button outside the door to reactivate robot motion. The robot resumes movement automatically when the signal is re-established.

# WARNING 

Do not use this configuration if signal can be re-established from the inside of the safety perimeter.
![img-23.jpeg](img-23.jpeg)

This example illustrates a door switch is a basic safeguard device where the robot is stopped when the door is opened.

This example illustrates a safety mat is a safety device where automatic resume is appropriate. This example is also valid for a safety laser scanner.

Safeguard
Stop with reset button

If the safeguard interface is used to interact with a light curtain, a reset outside the safety perimeter is required. The reset button must be a two channel type. In this example the I/O configured for reset is CIO-CI1 (see below).
![img-24.jpeg](img-24.jpeg)

Description The I/O are divided between inputs and outputs and are paired up so that each function provides a Category 3 and PLd I/O.
![img-25.jpeg](img-25.jpeg)

Input The following Safety Functions can be used with the input signals:
Signals

| System <br> Emergency <br> Stop | This is an emergency stop button alternative to the one on the Teach <br> Pendant, providing the same functionality if the device complies with <br> ISO 13850. |
| :-- | :-- |
|  | All safety limits can be applied while the robot is using a Normal <br> configuration, or a Reduced configuration (see Software Safety <br> Modes). When configured, a low signal sent to the inputs causes the <br> safety system to transition to the reduced configuration. The robot arm <br> decelerates to satisfy the reduced parameters. <br> The safety system guarantees the robot is within reduced limits less <br> than 0.5s after the input is triggered. If the robot arm continues to <br> violate any of the reduced limits, a Stop Category 0 is triggered. Trigger <br> planes can also cause a transition to the reduced configuration. The <br> safety system transitions to the normal configuration in the same way. |
| Reduced | In Manual Mode, an external 3-Position Enabling Device must be <br> pressed and held in the center-on position to move the robot. If you are <br> using a built-in 3-Position Enabling Device, the button must be pressed <br> and held in the mid position to move the robot. |
| 3-Position <br> Enabling <br> Device | You can configure the Freedrive input to enable and use Freedrive <br> without pressing the Freedrive button on a standard TP, or without <br> having to press-and-hold any of the buttons on the 3PE TP in the light- <br> press position. |

Input
Signals

| Operational <br> Mode | When defined, this input can be used to switch between Automatic <br> Mode and Manual Mode. |
| :-- | :-- |
| Safeguard <br> Reset | When a Safeguard Stop occurs, this output ensures that the <br> Safeguard Stop state continues until a reset is triggered. |
| Automatic <br> Mode <br> Safeguard <br> Stop | Once configured, an Automatic Mode Safeguard Stop performs a <br> Safeguard Stop when the input pins are low and ONLY when the <br> robot is in Automatic mode. |

# WARNING 

- If you disable the default Safeguard Reset input, the Robot Arm is no longer Safeguard Stop stopped as soon as the input is high. A program paused only by the Safeguard stop resumes.
- Similar to the Safeguard Reset, if the default Automatic Mode Safeguard Reset is disabled, the Robot Arm is no longer Safeguard Stop stopped once the Automatic Mode Safeguard Stop input is high. A program paused only by the Automatic Mode Safeguard Stop resumes.

|  Output | You can apply the following Safety functions for output signals. All signals return to low when the  |
| --- | --- |
|  Signals | state which triggered the high signal has ended:  |
|  System | Signal is Low when the safety system has been triggered into an  |
|  Emergency Stopped state by the Robot Emergency Stop input or the |   |
|  Emergency Stop Button. To avoid deadlocks, if the Emergency |   |
|  Stopped state is triggered by the System Emergency Stop input, low |   |
|  signal will not be given. |   |
|  Robot Moving | Signal is Low if the robot is moving, otherwise high.  |
|  Robot Not | Signal is High when the robot is stopped or in the process of stopping  |
|  Stopping | due to an emergency stop or safeguard stop. Otherwise it will be logic  |
|   | low.  |
|  Reduced | Signal is Low when the robot arm uses reduced parameters or if the  |
|   | safety input is configured with a reduced input and the signal is  |
|   | currently low. Otherwise the signal is high.  |
|  Not Reduced | This is the inverse of Reduced, defined above.  |
|  Safe Home | Signal is High if the Robot Arm is stopped in the configured Safe  |
|   | Home Position. Otherwise, the signal is Low.  |

# NOTICE

Any external machinery receiving its Emergency Stop state from the robot through the System Emergency Stop output must comply with ISO 13850. This is particularly necessary in setups where the Robot Emergency Stop input is connected to an external Emergency Stop device. In such cases, the System Emergency Stop output becomes high when the external Emergency Stop device is released. This implies that the emergency stop state at the external machinery will be reset with no manual action needed from the robot's operator. Hence, to comply with safety standards, the external machinery must require manual action in order to resume.

Description Use the I/O Setup screen to define I/O signals and configure actions with the I/O tab control. The types of I/O signals are listed under Input and Output.
You can use a fieldbus, for example, Profinet and EtherNet/IP, to access the general purpose registers.
If you enable the Tool Communication Interface (TCI), the tool analog input becomes unavailable.
![img-26.jpeg](img-26.jpeg)

# NOTICE 

When starting programs from an I/O or fieldbus input, the robot can begin movement from the position it has, there will not be any manual movement to the first waypoint via PolyScope required.

I/O Signal To limit the number of signals listed under Input and Output, use the View drop-down menu Type to change the displayed content based on signal type.

Assigning
User-defined
Names

You can name the Input and Output signals to easily identify the ones being used.

1. Select the desired signal.
2. Tap the text field to type a name for the signal.
3. To reset the name to default, tap Clear.

You must provide a user-defined name for a general purpose register to make it available in the program (i.e., for a Wait command or the conditional expression of an If command). The Wait and If commands are described in (Wait) and (If), respectively. You can find named general purpose registers in the Input or Output selector on the Expression Editor screen.

|  I/O Actions | You can use Physical and Fieldbus digital I/Os to trigger actions or react to the status of a program.  |
| --- | --- |
|  and I/O Tab | |   |
|  Control |   |

I/O Tab Control to specify whether an output is controlled on the I/O tab (by either programmers, or both operators and programmers), or if it is controlled by the robot programs.

Available Input Actions

|  Command | Action  |
| --- | --- |
|  Start | Starts or resumes the current program on a rising edge (only enabled
in Remote Control, see Settings)  |
|  Stop | Stops the current program on a rising edge  |
|  Pause | Pauses the current program on a rising edge  |
|  Freedrive | When the input is high, the robot goes into freedrive (similar to the
freedrive button).
The input is ignored if other conditions disallow freedrive.  |

# WARNING

If the robot is stopped while using the Start input action, the robot slowly moves to the first waypoint of the program before executing that program. If the robot is paused while using the Start input action, the robot slowly moves to the position from where it was paused before resuming that program.

Available Output Actions

| Action | Output <br> state | Program state |
| :-- | :-- | :-- |
| Low when not running | Low | Stopped or <br> paused |
| High when not running | High | Stopped or <br> paused |
| High when running, low when stopped | Low <br> High | Running, <br> Stopped or <br> paused |
| Low on unscheduled stop | Low | Program <br> terminated <br> unscheduled |
| Low on unscheduled stop, otherwise High | Low <br> High | Program <br> terminated <br> unscheduled <br> Running, <br> stopped or <br> paused |
| Continuous Pulse | Alternates <br> between <br> high and <br> low | Running <br> (pause or stop <br> the program to <br> maintain the <br> pulse state) |

Program Termination Cause

An unscheduled program termination can occur for any of the reasons listed below:

- Robot stop
- Fault
- Violation
- Runtime exception

# 8.3. Control Box Connection Ports 

Description
The underside of the I/O interface groups is equipped with external connection ports, as illustrated below. There are capped openings at the base of the Control Box cabinet to run external connector cables to access the ports.

The Mini Displayport supports monitors using Displayport. This requires an active Mini Display to DVI or HDMI converter. Passive converters do not work with DVI/HDMI ports. The Fuse must be a UL marked, Mini Blade type with maximum current rating: 10A and minimum voltage rating: 32 V
![img-27.jpeg](img-27.jpeg)

## NOTICE

Connecting or disconnecting a Teach Pendant while the Control Box is powered on can cause damage.

- Do not connect a Teach Pendant while the Control Box is on.
- Power off the Control Box before you connect a Teach Pendant. Do not connect or disconnect the Teach Pendant while Control Box is powered on. This can cause damage to Control Box.


## NOTICE

Failure to plug in the active adapter before powering on the Control Box can hinder the display output.

- Plug in the active adapter before powering on the Control Box.
- In some cases the external monitor must be powered on before the Control Box.
- Use an active adapter that supports revision 1.2 as not all adapters function out-of-the-box.

# 8.7. End Effector Integration 

Description The end effector can also be referred to as the tool and the workpiece in this manual.

## NOTICE

UR provides documentation for the end effector to be integrated with the robot arm.

- Refer to the documentation specific to the end effector/tool/workpiece for mounting and connection.

# 8.7.1. Tool I/O 

Tool
Connector

The tool connector illustrated below provides power and control signals for the grippers and sensors used on a specific robot tool. The tool connector has eight holes and is located next to the tool flange on Wrist 3.
The eight wires inside the connector have different functions, as listed in the table:

|  | Pin \# | Signal | Description |
| :-- | :-- | :--: | :-- |
|  | 1 | AI3 / RS485- | Analog in 3 or RS485- |
|  | 2 | AI2 / RS485+ | Analog in 2 or RS485+ |
|  | 3 | TOO/PWR | Digital Outputs 0 or 0V/12V/24V |
|  | 4 | TO1/GND | Digital Outputs 1 or Ground |
|  | 5 | POWER | 0V/12V/24V |
|  | 6 | TI0 | Digital Inputs 0 |
|  | 7 | TI1 | Digital Inputs 1 |
|  | 8 | GND | Ground |

![img-28.jpeg](img-28.jpeg)

## NOTICE

The Tool Connector must be manually tightened up to a maximum of 0.4 Nm .

Tool I/O
Accessories

The UR20 tool I/O can require an accessory element to facilitate connection with tools. Depending on the tool, you can use the following tool I/O accessories: Tool Flange Adapter (see Tool Flange Accessories) and/or Tool Cable Adapter.

Tool Cable Adapter

The Tool Cable Adapter is the electronic accessory that allows compatibility between the tool I/O and e-Series tools.
![img-29.jpeg](img-29.jpeg)

1 Connects to the tool/end effector.
2 Connects to the robot.

# WARNING 

Connecting the Tool Cable Adapter to a robot that is powered on can lead to injury.

- Connect the adapter to the tool/end effector before connecting the adapter to the robot.
- Do not power on the robot if the Tool Cable Adapter is not connected to the tool/end effector.

The eight wires inside the Tool Cable Adapter have different functions, as listed in the table below:

| Pin \# | Signal | Description |
| :--: | :--: | :--: |
| 1 | AI2 / RS485+ | Analog in 2 or RS485+ |
| 2 | AI3 / RS485- | Analog in 3 or RS485- |
| 3 | TI1 | Digital Inputs 1 |
| 4 | TI0 | Digital Inputs 0 |
| 5 | POWER | 0V/12V/24V |
| 6 | TO1/GND | Digital Outputs 1 or Ground |
| 7 | TO0/PWR | Digital Outputs 0 or 0V/12V/24V |
| 8 | GND | Ground |

## GROUND

The tool flange is connected to GND (Ground).

Description
The analog I/O interface is the green terminal. It is used to set or measure voltage (010 V ) or current $(4-20 \mathrm{~mA})$ to and from other equipment.
The following directions is recommended to achieve the highest accuracy.

- Use the AG terminal closest to the I/O. The pair share a common mode filter.
- Use the same GND (0V) for equipment and Control Box. The analog I/O is not galvanically isolated from the Control Box.
- Use a shielded cable or twisted pairs. Connect the shield to the GND terminal at the terminal called Power.
- Use equipment that works in current mode. Current signals are less sensitive to interferences.

Electrical Specifications

In the GUI you can select input modes (see part Part II PolyScope Manual). The electrical specifications are shown below.

| Terminals | Parameter | Min | Typ | Max | Unit |
| :--: | :--: | :--: | :--: | :--: | :--: |
| Analog Input in current mode |  |  |  |  |  |
| [AIx - AG] | Current | 4 | - | 20 | mA |
| [AIx - AG] | Resistance | - | 20 | - | ohm |
| [AIx - AG] | Resolution | - | 12 | - | bit |
| Analog Input in voltage mode |  |  |  |  |  |
| [AIx - AG] | Voltage | 0 | - | 10 | V |
| [AIx - AG] | Resistance | - | 10 | - | Kohm |
| [AIx - AG] | Resolution | - | 12 | - | bit |
| Analog Output in current mode |  |  |  |  |  |
| [AOx - AG] | Current | 4 | - | 20 | mA |
| [AOx - AG] | Voltage | 0 | - | 24 | V |
| [AOx - AG] | Resolution | - | 12 | - | bit |
| Analog Output in voltage mode |  |  |  |  |  |
| [AOx - AG] | Voltage | 0 | - | 10 | V |
| [AOx - AG] | Current | $-20$ | - | 20 | mA |
| [AOx - AG] | Resistance | - | 1 | - | ohm |
| [AOx - AG] | Resolution | - | 12 | - | bit |

Analog Output and Analog Input
![img-30.jpeg](img-30.jpeg)

This example illustrates controlling a conveyor belt with an analog speed control input.
![img-31.jpeg](img-31.jpeg)

This example illustrates connecting an analog sensor.

# 8.7.3. General Purpose Digital I/O 

Description
The Startup screen contains settings for automatically loading and starting a default program, and for auto-initializing the Robot arm during power up.

General
This section describes the general purpose 24V I/O (Gray terminals) and the configurable I/O purpose digital I/O (Yellow terminals with black text) when not configured as safety I/O. The common specifications in section 8.7.3 General Purpose Digital I/O above must be observed.

The general purpose I/O can be used to drive equipment like pneumatic relays directly or for communication with other PLC systems. All Digital Outputs can be disabled automatically when program execution is stopped, see part Part II PolyScope Manual.
In this mode, the output is always low when a program is not running. Examples are shown in the following subsections.
These examples use regular Digital Outputs but any configurable outputs could also have be used if they are not configured to perform a safety function.
![img-32.jpeg](img-32.jpeg)

Communication
This example shows how a load is controlled from a Digital Outputs when connected.

This example shows how a simple button is connected to a Digital Input.

Communication
You can use the digital I/O to communicate with other equipment if a common GND with other machines or PLCs
(0V) is established and if the machine uses PNP technology, see below.
![img-33.jpeg](img-33.jpeg)

# 8.7.4. Remote ON/OFF control 

Description Use remote ON/OFF control to turn the Control Box on and off without using the Teach Pendant. It is typically used:

- When the Teach Pendant is inaccessible.
- When a PLC system must have full control.
- When several robots must be turned on or off at the same time.

Remote The remote ON/OFF control provides a auxiliary 12 V supply, kept active when the Control Box Control is turned off. The ON input is intended only for short time activation and works in the same way as the POWER button. The OFF input can be held down as desired. Use a software feature to load and start programs automatically (see part Part II PolyScope Manual).
The electrical specifications are shown below.

| Terminals | Parameter | Min | Typ | Max | Unit |
| :-- | :-- | :--: | :--: | :--: | :--: |
| $[12 \mathrm{~V}-$ GND $]$ | Voltage | 10 | 12 | 13 | V |
| $[12 \mathrm{~V}-$ GND $]$ | Current | - | - | 100 | mA |
| $[$ ON / OFF $]$ | Inactive voltage | 0 | - | 0.5 | V |
| $[$ ON / OFF $]$ | Active voltage | 5 | - | 12 | V |
| $[$ ON / OFF $]$ | Input current | - | 1 | - | mA |
| $[$ ON $]$ | Activation time | 200 | - | 600 | ms |

![img-34.jpeg](img-34.jpeg)

This example illustrates connecting a remote
ON button.
![img-35.jpeg](img-35.jpeg)

This example illustrates connecting a remote OFF button.

## CAUTION

Maintaining a press and hold on the power button switches the Control Box OFF without saving.

- Do not press and hold the ON input or the POWER button without saving.
- Use the OFF input for remote off control to allow the Control Box to save open files and shut down correctly.

# 8.7.5. Securing Tool 

Description The tool or workpiece is mounted to the tool output flange (ISO) at the tip of the robot.
![img-36.jpeg](img-36.jpeg)

Dimensions and hole pattern of the tool flange. All measurements are in millimeters.

Tool flange The tool output flange (ISO 9409-1) is where the tool is mounted at the tip of the robot. It is recommended to use a radially slotted hole for the positioning pin to avoid over-constraining, while keeping precise position.

## CAUTION

Very long M8 bolts can press against the bottom of the tool flange and short circuit the robot.

- Do not use bolts that extend beyond 10 mm to mount the tool.


## WARNING

Failure to tighten bolts properly cause injury due to loss of the adapter flange and/or end effector.

- Ensure the tool is properly and securely bolted in place.
- Ensure the tool is constructed such that it cannot create a hazardous situation by dropping a part unexpectedly.

# 8.7.6. Tool I/O Installation Specifications

Description The electrical specifications are shown below. Access Tool I/O in the Installation Tab (see part Part II PolyScope Manual) to set the internal power supply to 0V, 12V or 24V.

|  Parameter | Min | Typ | Max | Unit  |
| --- | --- | --- | --- | --- |
|  Supply voltage in 24 V mode | 23.5 | 24 | 24.8 | V  |
|  Supply voltage in 12V mode | 11.5 | 12 | 12.5 | V  |
|  Supply current (single pin)* | - | 600 | $2000^{ }$ | mA  |
|  Supply current (dual pin)* | - | 600 | $2000^{ }$ | mA  |
|  Supply capacitive load | - | - | $8000^{ *** }$ | uF  |

- It is highly recommended to use a protective diode for inductive loads. ** Peak for max 1 second, duty cycle max: 10\%. Average current over 10 seconds must not exceed typical current. *** When tool power is enabled, a 400 ms soft start time begins allowing a capacitive load of 8000 uF to be connected to the tool power supply at start-up. Hot-plugging the capacitive load is not allowed.

# 8.7.7. Tool Power Supply 

## Description

Access Tool I/O in the Installation Tab to set the internal power supply to 0V, 12V or 24V.
![img-37.jpeg](img-37.jpeg)

Dual Pin
Power
Supply

In Dual Pin Power mode, the output current can be increased as listed in Tool I/O.

1. In the Header, tap Installation.
2. In the list on the left, tap General.
3. Tap Tool IO and select Dual Pin Power.
4. Connect the wires Power (gray) to TOO (blue) and Ground (red) to TO1 (pink).
![img-38.jpeg](img-38.jpeg)

## NOTICE

Once the robot makes an Emergency Stop, the voltage is set to 0 V for both Power Pins (power is off).

# 8.7.8. Tool Digital Outputs

**Distribution**

Digital Outputs support three different modes:

|  Mode | Active | Inactive  |
| --- | --- | --- |
|  Sinking (NPN) | Low | Open  |
|  Sourcing (PNP) | High | Open  |
|  Push / Pull | High | Low  |

Access Tool I/O in the Installation Tab to configure the output mode of each pin. The electrical specifications are shown below:

|  Parameter | Min | Typ | Max | Unit  |
| --- | --- | --- | --- | --- |
|  Voltage when open | -0.5 | - | 26 | V  |
|  Voltage when sinking 1A | - | 0.08 | 0.09 | V  |
|  Current when sourcing/sinking | 0 | 600 | 1000 | mA  |
|  Current through GND | 0 | 1000 | 3000* | mA  |

**NOTICE**

Once the robot makes an Emergency Stop, the Digital Outputs (DO0 and DO1) are deactivated (High Z).

**CAUTION**

The Digital Outputs in the tool are not current-limited. Overriding the specified data can cause permanent damage.

**Using Tool Digital Outputs**

This example illustrates turning on a load using the internal 12V or 24V power supply. The output voltage at the I/O tab must be define. There is voltage between the POWER connection and the shield/ground, even when the load is turned off.

![img-39.jpeg](img-39.jpeg)

It is recommended to use a protective diode for inductive loads, as shown below.

![img-40.jpeg](img-40.jpeg)

Description The Startup screen contains settings for automatically loading and starting a default program, and for auto-initializing the Robot arm during power up.

Table The Digital Inputs are implemented as PNP with weak pull-down resistors. This means that a floating input always reads as low. The electrical specifications are shown below.

| Parameter | Min | Type | Max | Unit |
| :-- | :--: | :--: | :--: | :--: |
| Input voltage | -0.5 | - | 26 | V |
| Logical low voltage | - | - | 2.0 | V |
| Logical high voltage | 5.5 | - | - | V |
| Input resistance | - | 47 k | - | $\Omega$ |

Using the This example illustrates connecting a simple button. Tool Digital Inputs
![img-41.jpeg](img-41.jpeg)

# 8.7.10. Tool Analogue Inputs 

Description Tool Analogue Input are non-differential and can be set to either voltage (0-10V) or current (4-20mA) on the I/O tab. The electrical specifications are shown below.

| Parameter | Min | Type | Max | Unit |
| :-- | :--: | :--: | :--: | :--: |
| Input voltage in voltage mode | -0.5 | - | 26 | V |
| Input resistance @ range 0V to 10V | - | 10.7 | - | $\mathrm{k} \Omega$ |
| Resolution | - | 12 | - | bit |
| Input voltage in current mode | -0.5 | - | 5.0 | V |
| Input current in current mode | -2.5 | - | 25 | mA |
| Input resistance @ range 4mA to 20mA | - | 182 | 188 | $\Omega$ |
| Resolution | - | 12 | - | bit |

Two examples of using Analog Input are shown in the following subsections.

Description This section describes how you get started using the robot. Among other things, it covers easy start-up, an overview of the Polyscope user interface and how to set up your first program. Additionally, it covers free drive mode and basic operation.

# 10.1. Quick System Start-up 

## Quick System Start

## MANDATORY ACTION

Before using the PolyScope, verify the robot arm and Control Box are correctly installed.

This is how you quickly start up the robot.

1. On the Teach Pendant, press the emergency stop button.
2. On the Teach Pendant, press the power button and allow the system to start, displaying text on the PolyScope.
3. A popup appears on the touch screen indicating that the system is ready and that the robot must be initialized.
4. In the popup dialog, tap Go to Initialize Screen to access the Initialize screen.
5. Unlock the emergency stop button to change robot state from Emergency Stopped to Power off.
6. Step outside the reach (workspace) of the robot.
7. On the Initialize Robot screen, tap the ON button and allow robot state to change to Idle.
8. In the Payload field, in Active Payload, verify the payload mass. You can also verify the mounting position is correct, in the Robot field.
9. Tap the Start button, for the robot to release its brake system. The robot vibrates and makes clicking sounds indicating it is ready to be programmed.

## NOTICE

Learn to program your Universal Robots robot on www.universalrobots.com/academy/

# 10.2. Safety-related Functions and Interfaces 

Description Universal Robots robots are equipped with a range of built-in safety functions as well as safety I/O, digital and analog control signals to or from the electrical interface, to connect to other machines and additional protective devices. Each safety function and I/O is constructed according to EN ISO13849-1 (see Certifications) with Performance Level d (PLd) using a category 3 architecture.
See Software Safety Configuration for configuration of the safety functions, inputs and outputs in the user interface. See Safety I/O for descriptions on how to connect safety devices to I/O.

## WARNING

The use of safety configuration parameters different from those determined as necessary for risk reduction, can result in hazards that are not reasonably eliminated, or risks that are not sufficiently reduced.

- Ensure tools and grippers are connected correctly to avoid hazards due to interruption of power.


## WARNING: ELECTRICITY

Programmer and/or wiring errors can cause the voltage to change from 12 V to 24 V leading to fire damage to equipment.

- Verify the use of 12 V and proceed with caution.


## Additional Information

## NOTICE

- The use and configuration of safety functions and interfaces must follow the risk assessment procedures for each robot application. (see chapter Safety section Safety-related Functions and Interfaces)
- The stopping time should be taken into account as part of the application risk assessment
- If the robot detects a fault or violation in the safety system (e.g. if one of the wires in the Emergency Stop circuit is cut or a safety limit is exceeded), then a Stop Category 0 is initiated.


## NOTICE

The end effector is not protected by the UR safety system. The functioning of the end effector and/or connection cable is not monitored

Description Universal Robots robot safety functions, as listed in the table below, are in the robot but are meant to control the robot system i.e. the robot with its attached tool/end effector. The robot safety functions are used to reduce robot system risks determined by the risk assessment. Positions and speeds are relative to the base of the robot.

| Safety <br> Function | Description |
| :-- | :-- |
| Joint Position <br> Limit | Sets upper and lower limits for the allowed joint positions. |
| Joint Speed <br> Limit | Sets an upper limit for joint speed. |
| Safety <br> Planes | Defines planes, in space, that limit robot position. Safety planes limit <br> either the tool/end effector alone or both the tool/end effector and the <br> elbow. |
| Tool <br> Orientation | Defines allowable orientation limits for the tool. |
| Speed Limit | Limits maximum robot speed. The speed is limited at the elbow, at the <br> tool/end effector flange, and at the center of the user-defined tool/end <br> effector positions. |
| Force Limit | Limits maximum force exerted by the robot tool/end effector and elbow <br> in clamping situations. The force is limited at the tool/end effector, <br> elbow flange and center of the user-defined tool/end effector positions. |
| Momentum <br> Limit | Limits maximum momentum of the robot. |
| Power Limit | Limits mechanical work performed by the robot. |
| Stopping <br> Time Limit | Limits maximum time the robot uses for stopping after a robot stop is <br> initiated. |
| Stopping <br> Distance <br> Limit | Limits maximum distance travelled by the robot after a robot stop is <br> initiated. |

Safety
Function

When performing the application risk assessment, it is necessary to take into account the motion of the robot after a stop has been initiated. In order to ease this process, the safety functions Stopping Time Limit and Stopping Distance Limit can be used.
These safety functions dynamically reduces the speed of the robot motion such that it can always be stopped within the limits. The joint position limits, the safety planes and the tool/end effector orientation limits take the expected stopping distance travel into account i.e. the robot motion will slow down before the limit is reached.

The functional safety can be summarized as:

[^0]
[^0]:    ${ }^{1}$ Robot stop was previously known as "Protective stop".

| Safety Function | Accuracy | Performance Level | Category |
| :-- | :-- | :-- | :-- |
| Emergency Stop | - | d | 3 |
| Safeguard Stop | - | d | 3 |
| Joint Position Limit | $5^{\circ}$ | d | 3 |
| Joint Speed Limit | $1.15^{\circ} / \mathrm{s}$ | d | 3 |
| Safety Planes | 40 mm | d | 3 |
| Tool Orientation | $3^{\circ}$ | d | 3 |
| Speed Limit | $50 \mathrm{~mm} / \mathrm{s}$ | d | 3 |
| Force Limit | 25 N | d | 3 |
| Momentum Limit | $3 \mathrm{~kg} \mathrm{~m} / \mathrm{s}$ | d | 3 |
| Power Limit | 10 W | d | 3 |
| Stopping Time Limit | 50 ms | d | 3 |
| Stopping Distance Limit | 40 mm | d | 3 |
| Safe Home | $1.7^{\circ}$ | d | 3 |

# Warnings 

## CAUTION

Failure to configure the maximum speed limit can result in hazardous situations.

- If the robot is used in manual hand-guiding applications with linear movements, the speed limit must be set to maximum $250 \mathrm{~mm} / \mathrm{s}$ for the tool/end effector and elbow unless a risk assessment shows that higher speeds are acceptable. This will prevent fast movements of the robot elbow near singularities.


## NOTICE

There are two exceptions to the force limiting function that are important when designing an application.
As the robot stretches out, the knee-joint effect can give high forces in the radial direction (away from the base) at low speeds. Similarly, the short leverage arm, when the tool/end effector is close to the base and moving around the base, can cause high forces at low speeds.

![img-42.jpeg](img-42.jpeg)

Due to the physical properties of the robot arm, certain workspace areas require attention regarding pinching hazards. One area (left) is defined for radial motions when the wrist 1 joint is at least 450 mm from the base of the robot. The other area (right) is within 200 mm of the base of the robot, when moving tangentially.

Placing the robot in certain areas can create pinching hazards that can lead to injury.

|  Safety Input | Description  |
| --- | --- |
|  Emergency Stop Button | Performs a Stop Category 1 (IEC 60204-1) informing other machines using the System Emergency Stop output, if that output is defined. A stop is initiated in anything connected to the output.  |
|  Robot Emergency Stop | Performs a Stop Category 1 (IEC 60204-1) via Control Box input, informing other machines using the System Emergency Stop output, if that output is defined.  |
|  System Emergency Stop | Performs a Stop Category 1 (IEC 60204-1) on robot only, in all modes and takes precedence over all other commands.  |
|  Safeguard Stop | Performs a Stop Category 2 (IEC 60204-1) in all modes, except when using a 3-Position Enabling Device and a mode selector - then when in Manual Mode, the Safeguard Stop can be set to only function in Automatic Mode.  |
|  Automatic Mode Safeguard Stop | Performs a Stop Category 2 (IEC 60204-1) in Automatic mode ONLY. Automatic Mode Safeguard Stop can only be selected when a Three-Position Enabling Device is configured and installed.  |
|  Safeguard Reset | Returns from the Safeguard Stop state, when a rising edge on the Safeguard Reset input occurs.  |
|  Reduced Mode | Transitions the safety system to use the Reduced mode limits.  |
|  Three-Position Enabling Device | Initiates a Stop Category 2 (IEC 60204-1) when the enabling device is fully pressed or fully released in manual mode only. Three-Position Enabling Device Stop is triggered when an input goes low. It is unaffected by a Safeguard Reset.  |
|  Freedrive on robot | Enables freedrive, when the robot is not in Automatic Mode.  |
|  Operational Mode | Switches between Operational modes. The robot is in Automatic mode when input is low, Manual mode when input is high.  |
|  Automatic Mode Safeguard Reset | Returns from the Automatic Mode Safeguard Stop state, when a rising edge on the Automatic Mode Safeguard Reset input occurs.  |

Safety outputs

For interfacing with other machines, the robot is equipped with the following safety outputs:

| Safety <br> Output | Description |
| :-- | :-- |
| System <br> Emergency <br> Stop | While this signal is logic low, the Robot Emergency Stop input is logic low <br> or the Emergency Stop button is pressed. |
| Robot <br> Moving | While this signal is logic high, no single joint of the robot moves more than <br> $0.1 \mathrm{rad} / \mathrm{s}$. |
| Robot Not <br> Stopping | Logic high when the robot is stopped or in the process of stopping due to <br> an Emergency Stop or Safeguard Stop. Otherwise it will be logic low. |
| Reduced | Logic low when the safety system is in Reduced Mode. |
| Not Reduced | Logic low when the system is not in Reduced Mode. |
| Safe Home | Logic high when robot is in the configured Safe Home Position. |

All safety I/O are dual channel, meaning they are safe when low (e.g., the Emergency Stop is active when the signals are low).

# 10.2.2. Safety Functions 

Description The safety system acts by monitoring if any of the safety limits are exceeded or if an Emergency Stop or a Safeguard Stop is initiated.
The reactions of the safety system are:

| Trigger | Reaction |
| :-- | :-- |
| Emergency Stop | Stop Category 1 |
| Safeguard Stop | Stop Category 2 |
| 3PE Stop (if a 3-Position Enabling device is connected) | Stop Category 2 |
| Limit Violation | Stop Category 0 |
| Fault Detection | Stop Category 0 |

## NOTICE

If the safety system detects any fault or violation, all safety outputs reset to low.

Description The safety system has the following set of configurable safety parameters:

- Normal
- Reduced

Normal and Reduced

You can set up the safety limits for each set of safety parameters, creating distinct configurations for normal, or higher settings, and reduced. The reduced configuration is active when the tool/end effector is positioned on the reduced side of a Trigger Reduced Plane, or when the reduced configuration is externally triggered by a safety input. Using a plane to trigger the Reduced configuration: When the robot arm moves from the side of the trigger plane configured with reduced safety parameters, to the side that is configured with normal safety parameters, there is a 20 mm area around the trigger plane where both normal and reduced limits are allowed. This area around the trigger plane prevents nuisance safety stops when the robot is exactly at the limit.
Using an input to trigger the Reduced configuration: When a safety input starts, or stops, the reduced configuration, up to 500 ms can elapse before the new limit values become active. This can happen in either of the following circumstances:

- Switching from the reduced configuration to normal
- Switching from the normal configuration to reduced

The robot arm adapts to the new safety limits within the 500 ms .

Recovery When a safety limit is exceeded, the safety system must be restarted. For example, if a joint position limit is outside a safety limit, at start-up, Recovery is activated.
You cannot run programs for the robot when recovery is activated, but the robot arm can be manually moved back within limits using Freedrive, or by using the Move tab in PolyScope. The safety limits for Recovery are:

| Safety Function | Limit |
| :-- | :-- |
| Joint Speed Limit | $30^{\circ} / \mathrm{s}$ |
| Speed Limit | $250 \mathrm{~mm} / \mathrm{s}$ |
| Force Limit | 100 N |
| Momentum Limit | $10 \mathrm{~kg} \mathrm{~m} / \mathrm{s}$ |
| Power Limit | 80 W |

The safety system issues a Stop Category 0 if a violation of these limits appears.

# WARNING 

Failure to use caution when moving the robot arm in recovery mode can lead to hazardous situations.

- Use caution when moving the robot arm back within the limits, as limits for the joint positions, the safety planes, and the tool/end effector orientation are all disabled in recovery mode.

# 10.3. Software Safety Configuration 

Description This section covers how to access the robot safety settings. It is made up of items that help you set up the robot Safety Configuration.

## WARNING

Before you configure your robot safety settings, your integrator must conduct a risk assessment to guarantee the safety of personnel and equipment around the robot. A risk assessment is an evaluation of all work procedures throughout the robot lifetime, conducted in order to apply correct safety configuration settings. You must set the following in accordance with the integrator's risk assessment.

1. The integrator must prevent unauthorized persons from changing the safety configuration e.g. installing password protection.
2. Use and configuration of the safety-related functions and interfaces for a specific robot application.
3. Safety configuration settings for set-up and teaching before the robot arm is powered on for the first time.
4. All safety configuration settings accessible on this screen and sub-tabs.
5. The integrator must ensure that all changes to the safety configuration settings comply with the risk assessment. See Hardware Installation Manual.

Accessing Safety Settings are password protected and can only be configured once a password is set and subsequently used.

# To access the software safety settings 

1. In your PolyScope header, tap the Installation icon.
2. In the Side Menu on the left of the screen, tap Safety.
3. Observe that the Robot Limits screen displays, but settings are inaccessible.
4. If a Safety password was previously set, enter the password and press Unlock to make settings accessible. Note: Once Safety settings are unlocked, all settings are now active.
5. Press Lock tab or navigate away from the Safety menu to lock all Safety item settings again.
![img-43.jpeg](img-43.jpeg)

# 10.3.1. Setting a Software Safety Password 

Description
You must set a password to Unlock all safety settings that make up your Safety Configuration. If no safety password is applied, you are prompted to set it up.

To set a
Software
Safety password

You can tap the Lock tab to lock all Safety settings again or simply navigate to a screen outside of the Safety menu.

1. In your PolyScope header right corner, press the Hamburger menu and select Settings.
2. On the left of the screen, in the blue menu, press Password and select Safety.
3. In New password, type a password.
4. Now, in Confirm new password, type the same password and press Apply.
5. In the bottom left of the blue menu, press Exit to return to previous screen.

|  Description | Changes to the Safety Configuration settings must comply with the risk assessment conducted by the integrator.  |
| --- | --- |
|  Recommended procedure for the integrator: | To change the safety configuration  |
|   | 1. Verify that changes comply with the risk assessment conducted by the integrator.  |
|   | 2. Adjust safety settings to the appropriate level defined by the risk assessment conducted by the integrator.  |
|   | 3. Verify that the settings are applied.  |
|   | 4. Place following text in the operators’ manuals:  |
|   | Before working near the robot, make sure that the safety configuration is as expected. This can be verified e.g. by inspecting the Safety Checksum in the top right corner of PolyScope for any changes. (See Safety Checksum).  |

Description The robot is powered off while you make changes to the configuration. Your changes only take effect after you tap the Apply button.
The robot cannot be powered on again until you select Apply and Restart to visually inspect your robot Safety Configuration which, for safety reasons, is displayed in SI Units in a popup.
You can select Revert Changes to return to the previous configuration. When your visual inspection is complete you can select Confirm Safety Configuration and the changes are automatically saved as part of the current robot installation.

# Safety Checksum 

Description
The Safety Checksum icon displays your applied robot safety configuration.

It could be four or eight digits.
A four-digit Checksum should be read from top to bottom and left to right, while an eightdigit Checksum is read left to right, top row first. Different text and/or colors indicate changes to the applied safety configuration.

The Safety Checksum changes if you change the Safety Functions settings, because the Safety Checksum is only generated by the safety settings.
You must apply your changes to the Safety Configuration for the Safety Checksum to reflect your changes.

.

Description You can use the robot without attaching the Teach Pendant. Removing the Teach Pendant requires defining another Emergency Stop source. You must specify if the Teach Pendant is attached to avoid triggering a safety violation.

# CAUTION 

If the Teach Pendant is detached or disconnected from the robot, the Emergency Stop button is no longer active. You must remove the Teach Pendant from the vicinity of the robot.

To safely remove the Teach Pendant

The robot can be used without PolyScope as the programming interface. To configure the robot without a Teach Pendant

1. In the Header tap Installation.
2. In the Side Menu on left tap Safety and select Hardware.
3. Input Safety password and Unlock the screen.
4. Deselect Teach Pendant to use robot without PolyScope interface.
5. Press Save and restart to implement changes.

Description Under normal conditions, i.e. when no robot stop is in effect, the safety system operates in a Safety Mode associated with a set of safety limits ${ }^{1}$ :

- Normal mode is the safety mode that is active by default
- Reduced mode is active when the robot Tool Center Point (TCP) is positioned beyond a Trigger Reduced mode plane (see Software Safety Restrictions), or when triggered using a configurable input.
- Recovery mode activates when a safety limit from the active limit set is violated, the robot arm performs a Stop Category 0. If an active safety limit, such as a joint position limit or a safety boundary, is violated already when the robot arm is powered on, it starts up in Recovery mode. This makes it possible to move the robot arm back within the safety limits. While in Recovery mode, the movement of the robot arm is restricted by a fixed limit that you cannot customize.


# WARNING 

Limits for joint position, tool position and tool orientation are disabled in Recovery mode, so take caution when moving the robot arm back within the limits.

The menu of the Safety Configuration screen enables the user to define separate sets of safety limits for Normal and Reduced mode. For the tool and joints, Reduced mode limits for speed and momentum are required to be more restrictive than their Normal mode counterparts.

### 10.3.6. Software Safety Limits

Description In the Safety Configuration the safety system limits are specified. The Safety System receives the values from the input fields and detects any violation if any these values are exceeded. The robot controller attempts to prevent any violations by making a robot stop or by reducing the speed.

## Robot Limits

Description Robot Limits restrict general robot movements. The Robot Limits screen has two configuration options: Factory Presets and Custom.

[^0]
[^0]:    ${ }^{1}$ Robot stop was previously known as "Protective Stop" for Universal Robots robots.

Factory Presets is where you can use the slider to select a predefined safety setting. The values in the table are updated to reflect the preset values ranging from Most Restricted to Least Restricted

NOTICE
Slider values are only suggestions and do not substitute a proper risk assessment.
![img-44.jpeg](img-44.jpeg)

Custom
Custom is where you can set Limits on how the robot functions and monitor the associated
Tolerance.

Power
Limits maximum mechanical work produced by the robot in the
environment. This limit considers the payload a part of the robot and
not of the environment.
Momentum
Limits maximum robot momentum.
Stopping
Time
Limits maximum time it takes the robot to stop e.g. when an
emergency stop is activated.
Stopping
Distance
Limits maximum distance the robot tool or elbow can travel while
stopping.

NOTICE
Restricting stopping time and distance affect overall
robot speed. For example, if stopping time is set to
300 ms, the maximum robot speed is limited
allowing the robot to stop within 300 ms.
Tool Speed
Tool Force
Limits maximum robot tool speed.
Limits maximum force that the robot tool exerts on the environment to
prevent clamping situations.
Elbow Speed
Elbow Force
Limits maximum robot elbow speed.
Limits maximum force that the elbow exerts on the environment to
prevent clamping situations.

The tool speed and force are limited at the tool flange and the center of the two user-defined tool positions, (see Tool Position Restriction).
![img-45.jpeg](img-45.jpeg)

NOTICE
You can switch back to Factory Presets for all robot limits to reset to their default settings.

# Joint Limits 

## Description

Joint limits allow you to restrict individual robot joint movements in joint space i.e. joint rotational position and joint rotational speed. Joint limiting can also be called software based axis limiting. The joint limit options are: Maximum speed and Position range.
![img-46.jpeg](img-46.jpeg)

.

Description
Safe Home is a return position defined by using the user-defined Home Position. Safe Home I/Os are active when the Robot Arm is in the Safe Home Position and a Safe Home I/O is defined.
The Robot Arm is in the Safe Home Position if the joint positions are at the specified joint angles or a multiple of 360 degrees thereof.
The Safe Home Safety Output is active when the robot is standing still at the Safe Home Position.
![img-47.jpeg](img-47.jpeg)

Syncing
from Home

## Safe Home Output

Defining Safe Home Output

To sync from Home

1. In the Header, tap Installation.
2. In the Side Menu on the left of the screen, tap Safety and select Safe Home.
3. Under Safe Home, tap Sync from Home.
4. Tap Apply and in the dialog box that appears, select Apply and restart.

The Safe Home Position must be defined before the Safe Home Output (see I/O).

To define Safe Home Output

1. In the Header, tap Installation.
2. In the Side Menu on the left of the screen, under Safety, select I/O.
3. On the I/O screen in the Output Signal, under Function Assignment, in drop-down menu, select Safe Home.
4. Tap Apply and in the dialog box that appears, select Apply and restart.

|  Editing Safe | To edit Safe Home  |
| --- | --- |
|  Home | Editing Home does not automatically modify a previously defined Safe Home position. While these values are out of sync, Home program node is undefined.  |
|   | 1. In the Header, tap Installation.  |
|   | 2. In the Side Menu on the left of the screen, under General, select Home.  |
|   | 3. Tap Edit Position and set the new robot arm position and tap OK.  |
|   | 4. In the Side Menu, under Safety, select Safe Home. You need a Safety password to Unlock the Safety Settings (See Setting a Software Safety Password).  |
|   | 5. Under Safe Home, tap Sync from Home  |

Description

# NOTICE 

Configuring planes is entirely based on features. We recommend you create and name all features before editing the safety configuration, as the robot is powered off once the Safety Tab has been unlocked and moving the robot will be impossible.

Safety planes restrict robot workspace. You can define up to eight safety planes, restricting the robot tool and elbow. You can also restrict elbow movement for each safety plane and disable by deselecting the checkbox. Before configuring safety planes, you must define a feature in the robot installation. The feature can then be copied into the safety plane screen and configured.

## WARNING

Defining safety planes only limits the defined Tool spheres and elbow, not the overall limit for the robot arm. This means that specifying a safety plane, does not guarantee that other parts of the robot arm will obey this restriction.

Saf You can configure each plane with restrictive Modes using the icons listed below. ety Pla nes Mod es

|  | Disabled | The safety plane is never active in this state. |
| :--: | :--: | :--: |
| 囚 | Normal | When the safety system is in Normal mode, a normal plane is active and it acts as a strict limit on the position. |
|  | Reduced | When the safety system is in Reduced mode, a reduced mode plane is active and it acts as a strict limit on the position. |
| 园 | Normal \& Reduced | When the safety system is either in Normal or Reduced mode, a normal and reduced mode plane is active and acts as a strict limit on the position. |
|  | Trigger Reduced Mode | The safety plane causes the safety system to switch to Reduced mode if the robot Tool or Elbow is positioned beyond it. |
|  | Show | Pressing this icon hides or shows the safety plane in the graphics pane. |
|  | Delete | Deletes the created safety plane. There is no undo/redo action. If a plane is deleted in error, it must be remade. |
|  | Rename | Pressing this icon allows you to rename the plane. |

## Configuring safety planes

1. In your PolyScope header, tap Installation.
2. In the Side Menu on the left of the screen, tap Safety and select Planes.
3. On the top right of the screen, in the Planes field, tap Add plane.
4. On the bottom right of the screen, in the Properties field, set up Name, Copy Feature and Restrictions.

Copy Feature

In Copy Feature, only Undefined and Base are available. You can reset a configured safety plane by selecting Undefined
If the copied feature is modified in the Features screen, a warning icon appears to the right of the Copy Feature text. This indicates that the feature is out of sync i.e. the information in the properties card is not updated to reflect the modifications that may have been made to the Feature.
![img-48.jpeg](img-48.jpeg)

| Gray | Plane is configured but disabled (A) |
| :-- | :-- |
| Yellow \& Black | Normal Plane (B) |
| Blue \& Green | Trigger Plane (C) |
| Black Arrow | The side of the plane the tool and/or elbow is allowed to be on (For <br> Normal Planes) |
| Green Arrow | The side of the plane the tool and/or elbow is allowed to be on (For <br> Trigger Planes) |
| Gray Arrow | The side of the plane the tool and/or elbow is allowed to be on (For <br> Disabled Planes) |

![img-49.jpeg](img-49.jpeg)

Elbow
Restriction

You can enable Restrict Elbow to prevent robot elbow joint from passing through any of your defined planes. Disable Restrict Elbow for elbow to pass through planes. The diameter of the ball that restricts the elbow is different for each size of robot.

| UR3e | 0.1 m |
| :-- | :-- |
| UR5e | 0.13 m |
| UR10e / UR16e | 0.15 m |
| UR20 / UR30 | 0.19 m |

The information about the specific radius can be found in the urcontrol.conf file on the robot under the section [Elbow].
![img-50.jpeg](img-50.jpeg)

Tool Flange Restriction

Restricting the tool flange prevents the tool flange and the attached tool from crossing a safety plane. When you restrict the tool flange, the unrestricted area is the area inside of the safety plane, where the tool flange can operate normally.
The tool flange cannot cross the restricted area, outside of the safety plane.

Removing the restriction allows the tool flange to go beyond the safety plane, to the restricted area, while the attached tool remains inside of the safety plane.

You can remove the tool flange restriction when working with a large tool off-set. This will allow extra distance for the tool to move.

Restricting the tool flange requires the creation of a plane feature. The plane feature is used to set up a safety plane later in the safety settings.

Adding a Displacement offsets the plane in either the positive or negative direction along the plane plane feature
example normal (Z-axis of the plane feature).
Deselect the checkbox for the Elbow and the Tool Flange so they do not trigger the safety plane. The Elbow can remain checked as needed by your application.
![img-51.jpeg](img-51.jpeg)

The unrestricted tool flange can cross a safety plane, even when no tool is defined. If no tool is added, a warning on the Tool Position button prompts you to correctly define the tool.
When working with an unrestricted tool flange and a defined tool, it is ensured that the dangerous part of the tool can't go above and/or beyond certain area. The unrestricted tool flange can be used for any application where safety planes are needed, like Welding or Assembly.

In this example, an X-Y-plane is created with an offset of 300 mm along the positive Z-axis with reference to the base feature.
The Z-axis of the plane can be thought of as "pointing" towards the restricted area. If the safety plane is needed on e.g., the surface of a table, rotate the plane 3.142 rad or $180^{\circ}$ around either the $X$ - or $Y$-axis so the restricted area is under the table. (TIP: Change the display of rotation from "Rotation Vector [rad]" to "RPY ["]")
![img-52.jpeg](img-52.jpeg)

If needed it is possible to offset the plane in either positive or negative Z-direction later in the safety settings.
When satisfied with the position of the plane, tap OK.

# 10.4.1. Tool Direction Restriction 

Description
The Tool Direction screen can be used to restrict the angle in which the tool is pointing. The limit is defined by a cone that has a fixed orientation with respect to the robot arm Base. As the robot arm moves around, tool direction is restricted so it remains within the defined cone. The default direction of the tool coincides with the Z-axis of the tool output flange. It can be customized by specifying tilt and pan angles.
Before configuring the limit, you must define a point or plane in the robot installation. The feature can then be copied and its Z axis used as the center of the cone defining the limit.

## NOTICE

Configuration of the tool direction is based on features. We recommend you create desired feature(s) before editing the safety configuration, as once the Safety Tab has been unlocked, the robot arm powers off making it impossible to define new features.
![img-53.jpeg](img-53.jpeg)

Limit The Tool Direction limit has three configurable properties:
Prope

1. Cone center: You can select a point or plane feature from the drop-down menu, to define the center of the cone. The $Z$ axis of the selected feature is used as the direction around which the cone is centred.
2. Cone angle: You can define how many degrees the robot is allowed to deviate from center.

| Disabled Tool direction limit | Never active |
| :-- | :-- |
| Normal Tool direction limit | Active only when safety system is in Normal mode |
| Reduced Tool direction limit | Active only when the safety system is in Reduced mode |
| Normal \& Reduced Tool <br> direction limit | Active when the safety system is in Normal mode as <br> well as when it is in Reduced mode. |

You can reset the values to default or undo the Tool Direction configuration by setting the copy feature back to "Undefined".

Tool By default, the tool points in the same direction as the $Z$ axis of the tool output flange. This can be Prope modified by specifying two angles:
rties

- Tilt angle: How much to tilt the $Z$ axis of the output flange towards the $X$ axis of the output flange
- Pan angle: How much to rotate the tilted $Z$ axis around the original output flange $Z$ axis.

Alternatively, the $Z$ axis of an existing TCP can be copied by selecting that TCP from the drop-down menu.

# 10.4.2. Tool Position Restriction 

Description The Tool Position screen enables more controlled restriction of tools and/or accessories placed on the end of the robot arm.

- Robot is where you can visualize your modifications.
- Tool is where you can define and configure a tool up to two tools.
- Tool_1 is the default tool defined with values $x=0.0, y=0.0, z=0.0$ and radius $=0.0$. These values represent the robot tool flange.

Under Copy TCP, you can also select Tool Flange and cause the tool values to go back to 0 .
A default sphere is defined at the tool flange.
![img-54.jpeg](img-54.jpeg)

- Radius to change the radius of the tool sphere. The radius is considered when using safety planes. When a point in the sphere passes a reduced mode trigger plane, the robot switches to Reduced mode. The safety system prevents any point on the sphere from passing a safety plane (see Software Safety Restrictions).
- Position to change the position of the tool with respect to the tool flange of the robot. The position is considered for the safety functions for tool speed, tool force, stopping distance and safety planes.

You can use an existing Tool Center Point as a base for defining new tool positions. A copy of the existing TCP, predefined in General menu, in TCP screen, can be accessed in Tool Position menu, in Copy TCP drop-down list.
When you edit or adjust the values in the Edit Position input fields, the name of the TCP visible in the drop down menu changes to custom, indicating that there is a difference between the copied TCP and the actual limit input. The original TCP is still available in the drop down list and can be selected again to change the values back to the original position. The selection in the copy TCP drop down menu does not affect the tool name.
Once you apply your Tool Position screen changes, if you try to modify the copied TCP in the TCP configuration screen, a warning icon appears to the right of the Copy TCP text. This indicates that the TCP is out of sync i.e. the information in the properties field is not updated to reflect modifications that may have been made to the TCP. The TCP can be synced by pressing the sync icon (see ).
The TCP does not have to be synced in order to define and use a tool successfully. You can rename the tool by pressing the pencil tab next to the displayed tool name. You can also determine the Radius with an allowed range of 0-300 mm. The limit appears in the graphics pane as either a point or a sphere depending on radius size.
![img-55.jpeg](img-55.jpeg)

Tool Position You must set a Tool Position within the safety settings, for the safety plane to trigger Warning correctly when the tool TCP approaches the safety plane.
The warning remains on the Tool Position if:

- You fail to add a new tool under Tool Flange.

To configure the tool position

1. In the Header tap Installation.
2. On the left side of the screen, under Safety, tap Tool Position.
3. On the right side of the screen, select Add Tool.

- The newly added tool has a default name: Tool_x.

4. Tap the edit button to rename Tool_x to something more identifiable.
5. Edit the Radius and Position to match that of the tool you are currently using, or use the Copy TCP drop-down and choose a TCP from the General>TCP settings if such is defined.

Tool Position Warning example

In this example, a Radius of 0.8 mm is set and the TCP position to XYZ [20, 0, 400] in millimeters respectively. Optionally you can choose to "Copy TCP" by using the drop-down menu if one has already been set in the ->General/TCP settings. Once the Apply is tapped in the bottom right corner of the screen, you are DONE.

The warning on the Tool Position button indicates a tool is not added under Tool Flange.
![img-56.jpeg](img-56.jpeg)

Tool Position button without the warning indicates a tool (other than the Tool Flange) is added.
![img-57.jpeg](img-57.jpeg)

# 13. Emergency Events 

Description
Follow the instructions here to handle emergency situations, such as activating the emergency stop using the red push-button. This section also describes how to manually move the system without power.

### 13.1. Emergency Stop

Description
The Emergency Stop or E-stop is the red push-button located on the Teach Pendant. Press the emergency stop push-button to stop all robot motion. Activating the emergency stop push-button causes a stop category one (IEC 60204-1). Emergency stops are not safeguards (ISO 12100).

Emergency stops are complementary protective measures that do not prevent injury. The risk assessment of the robot application determines if additional emergency stop push-buttons are required. The emergency stop function and the actuating device must comply with ISO 13850.
After an emergency stop is actuated, the push-button latches in that setting. As such, each time an emergency stop is activated, it must be manually reset at the push-button that initiated the stop.
Before resetting the emergency stop push-button, you must visually identify and assess the reason the E-stop was first activated. Visual assessment of all the equipment in the application is required. Once the problem is solved, reset the emergency stop pushbutton.

## To reset the emergency stop push-button

1. Hold the push-button and twist clockwise until the latching disengages.

You should feel when the latching is disengaged, indicating the push-button is reset.
2. Verify the situation and whether to reset the emergency stop.
3. After resetting the emergency stop, restore power to the robot and resume operation.

# 13.2. Movement Without Drive Power 

Description In the unlikely event of an emergency, when powering the robot is either impossible or unwanted, you can use forced back-driving to move the robot arm.

To perform forced back-driving you must push, or pull, the robot arm hard to move the joint. Each joint brake has a friction clutch that enables movement during high forced torque.

Performing forced back-driving requires high force and cannot be performed by one person alone. In clamping situations, two or more people are required to do the forced back-driving. In some situations, two or more people are required to disassemble the robot arm.

See the Service Manual for information about how to disassemble the robot.

## WARNING

Risks due to an unsupported robot arm breaking or falling can cause injury or death.

- Support the robot arm before removing power.


## NOTICE

Moving the robot arm manually is intended for emergency and service purposes only. Unnecessary moving of the robot arm can lead to property damage.

- Do not move the joint more than 160 degrees, to ensure the robot can find its original physical position.
- Do not move any joint more than necessary.

Description You access and activate different modes using Teach Pendant or the Dashboard Server. If an external mode selector is integrated, it control the modes - not PolyScope or the Dashboard Server.

Automatic Mode Once activated, the robot can only execute a program of pre-defined tasks. You cannot modify or save programs and installations.
Manual Mode Once activated, you can program the robot. You can modify and save programs and installations.

High Speed Manual Mode can be used. It allows both tool speed and elbow speed to temporarily exceed $250 \mathrm{~mm} / \mathrm{s}$, while a hold-to-run is used.
Hold-to-run is performed by continuous contact with the Speed Slider.
The robot performs a Safeguard Stop in Manual mode, if a Three-Position Enabling Device is configured, and either released (not pressed) or it is fully compressed.

Switching between Automatic mode to Manual mode requires the Three-Position Enabling Device to be fully released and pressed again to allow the robot to move. When using High Speed Manual Mode, use safety joint limits (see Joint Limits) or safety planes (see Safety Planes) to restrict the robot's moving space.

Mode switching

| Operational mode | Manual | Automatic |
| :-- | :-- | :--: |
| Freedrive | $x$ | $*$ |
| Move robot with arrows on Move Tab | $x$ | $*$ |
| Edit \& save program \& installation | $x$ |  |
| Execute Programs | Reduced <br> speed** | $*$ |
| Start program from selected node | $x$ |  |
| *Only when no Three-Position Enabling Device is configured. <br> ** If a Three-Position Enabling Device is configured, the robot operates at Manual <br> Reduced Speed unless High Speed Manual Mode is activated. |  |  |

Notice when switching mode

## NOTICE

- Some UR robot sizes might not be equipped with a Three-Position Enabling Device. If the risk assessment requires the enabling device, a 3PE Teach Pendant must be used.


# WARNING 

- Any suspended safeguards must be returned to full functionality before selecting Automatic Mode.
- Wherever possible, Manual Mode shall only be used with all persons located outside the safeguarded space.
- If an external mode selector is used, it must be placed outside the safeguarded space.
- No-one is to enter, or be within, the safeguarded space in Automatic Mode, unless safeguarding is used or the collaborative application is validated for power and force limiting (PFL).

To Switch
Modes: PolyScope

1. In the Header, select the profile icon.

- Automatic indicates the operational mode of the robot is set to Automatic.
- Manual indicates the operational mode of the robot is set to Manual.

Using the Dashboard Server

1. Connect to the Dashboard server.
2. Use the Set Operational Mode commands.

- Set Operational Mode Automatic
- Set Operational Mode Manual
- Clear Operational Mode

Three-Position
Enabling
Device

When a Three-Position Enabling Device is used and the robot is in Manual Mode, movement requires pressing the Three-Position Enabling Device to the center-on position. The Three-Position Enabling Device has no effect in Automatic Mode.

A 3PE Teach Pendant is recommended for programming. If another person can be within the safeguarded space when in Manual Mode, an additional device can be integrated and configured for the additional person's use.

Description

When a safety limit is exceeded, Recovery Mode is automatically activated, allowing the robot arm to be moved. Recovery Mode is a type of Manual Mode . You cannot run robot programs when Recovery Mode is active.

During Recovery Mode, the robot arm is moved to be within joint limits, using either Freedrive or the Move tab in PolyScope.

| Safety limits <br> of Recovery <br> Mode | Safety Function | Limit |
| :-- | :-- | :-- |
|  | Joint Speed Limit | $30^{\circ} / \mathrm{s}$ |
|  | Speed Limit | $250 \mathrm{~mm} / \mathrm{s}$ |
|  | Force Limit | 100 N |
| Momentum Limit | $10 \mathrm{~kg} \mathrm{~m} / \mathrm{s}$ |  |
| Power Limit | 80 W |  |

The safety system issues a Stop Category 0 if a violation of these limits appears.

# WARNING 

Failure to use caution when moving the robot arm in recovery mode can lead to hazardous situations.

- Use caution when moving the robot arm back within the limits, as limits for the joint positions, the safety planes, and the tool/end effector orientation are all disabled in recovery.


### 13.3.2. Backdrive

Description Backdrive is a Manual Mode used to force specific joints to a desired position without releasing all brakes in the robot arm.
This is sometimes necessary if the robot arm is close to collision and the vibrations that accompany a full restart are not desired.
The robot joints feel heavy to move, while Backdrive is in use.
You can use any of the following sequences to enable Backdrive:

- 3PE Teach Pendant
- 3PE device/switch
- Freedrive on robot

3PE Teach
Pendant

3PE
device/switch

## Freedrive on

robot

To use the 3PE TP button to backdrive the robot arm.

1. On the Initialize screen, tap ON to start the power up sequence.
2. When the robot state is Teach Pendant 3PE Stop, light-press, then light-press-and-hold, the 3PE TP button.
The robot state changes to Backdrive.
3. Now you can apply significant pressure to release the brake in a desired joint to move the robot arm.
As long as light-press is maintained on the 3PE button, Backdrive is enabled, allowing the arm to move.

To use a 3PE device/switch to backdrive the robot arm.

1. On the Initialize screen, tap ON to start the power up sequence.
2. When the robot state is Teach Pendant 3PE Stop, light-press, then light-press-and-hold, the 3PE TP button.
The robot state changes to System 3PE Stop.
3. Press and hold the 3PE device/switch. The robot state changes to Backdrive.
4. Now you can apply significant pressure to release the brake in a desired joint to move the robot arm.
As long as the hold is maintained on both the 3PE device/switch and the 3PE TP button, Backdrive is enabled, allowing the arm to move.

To use Freedrive on robot to backdrive the robot arm.

1. On the Initialize screen, tap ON to start the power up sequence.
2. When the robot state is Teach Pendant 3PE Stop, press and hold the Freedrive on robot.
The robot state changes to Backdrive.
3. Now you can apply significant pressure to release the brake in a desired joint to move the robot arm.
As long as the hold is maintained on the Freedrive on robot, Backdrive is enabled, allowing the arm to move.

# Backdrive Inspection 

Description If the robot is close to colliding with something, you can use Backdrive to move the robot arm to a safe position before initializing.

3PE Teach Pendant
![img-58.jpeg](img-58.jpeg)

# Enable Backdrive

1. Press **ON** to enable power. Status changes to **Robot Active**.

   ![img-59.jpeg](img-59.jpeg)

2. Press and hold **Freedrive**. Status changes to **Backdrive**.

   ![img-60.jpeg](img-60.jpeg)

3. Move robot as in **Freedrive** mode. Joint brakes are released where needed once the **Freedrive** button is activated.

   ![img-61.jpeg](img-61.jpeg)

**NOTICE**

In **Backdrive** Mode the robot is "heavy" to move around.

**MANDATORY ACTION**

You must test **Backdrive** mode on all joints.

|  Safety settings | Verify the robot safety settings comply with the robot installation risk assessment.  |
| --- | --- |
|  |   |

**Additional safety inputs and outputs are still functioning**

Check which safety inputs and outputs are active and that they can be triggered via **PolyScope** or external devices.

# 15. Maintenance and Repair 

Description Perform any inspection in compliance with all safety instructions in this manual and according with local requirements.
Conduct all maintenance, inspection, calibration and repair work according to the latest version of Service Manual on the documentation website: http://www.universalrobots.com/manuals
Repair work should only be done by Universal Robots. Client designated, trained individuals can do repair work, provided they follow the Service Manual. See the Service Manual: Chapter 5 for full inspection plan for trained individuals
All parts returned to Universal Robots shall be returned according to terms in the Service Manual.

Safety for
Maintenance

After maintenance and repair work, checks must be done to ensure the required safety level. Checks must adhere to valid national or regional work safety regulations. The correct functioning of all safety functions shall also be tested.
The purpose of maintenance and repair work is to ensure that the system is kept operational or, in the event of a fault, to return the system to an operational state. Repair work includes troubleshooting in addition to the actual repair itself.
When working on the robot arm or control box, you must observe the procedures and warnings below.

Warning

## WARNING

Failure to adhere to any of the safety practices, listed below, can result in injury.

- Unplug the main power cable from the bottom of the Control Box to ensure that it is completely unpowered. Power off any other source of energy connected to the robot arm or Control Box. Take necessary precautions to prevent other persons from powering on the system during the repair period.
- Check the earth connection before re-powering the system.
- Observe ESD regulations when parts of the robot arm or Control Box are disassembled.
- Prevent water and dust from entering the robot arm or Control Box.

Warning: Electricity

## WARNING: ELECTRICITY

Disassembling the Control Box power supply too quickly after switching off, can result in injury due to electrical hazards.

- Avoid disassembling the power supply inside the Control Box, as high voltages (up to 600 V ) can be present inside these power supplies for several hours after the Control Box has been switched off.

# 15.1. Testing Stopping Performance 

Description Test periodically to determine if stopping performance is degraded. Increased stopping times can require safeguarding to be modified, possibly with changes to the installation. If stop time and/or stop distance safety functions are used and are the basis of the risk reduction strategy, no monitoring or testing of stopping performance is required. The robot does continuous monitoring.

### 15.2. Robot Arm Cleaning and Inspection

Description
As part of regular maintenance the robot arm can be cleaned, in accordance with the recommendations in this manual and local requirements.

Cleaning
To address the dust, dirt, or oil on the robot arm and/or Teach Pendant, simply use a cloth Methods alongside one of the cleaning agents provided below.

Surface Preparation: Before applying the below solutions, surfaces may need to be prepared by removing any loose dirt or debris.

## Cleaning agents:

- Water
- 70\% Isopropyl alcohol
- 10\% Ethanol alcohol
- 10\% Naphtha (Use to remove grease.)

Application: The solution is typically applied to the surface that needs cleaning using a spray bottle, brush, sponge, or cloth. It can be applied directly or diluted further depending on the level of contamination and the type of surface being cleaned.
Agitation: For stubborn stains or heavily soiled areas, the solution may be agitated using a brush, scrubber, or other mechanical means to help loosen the contaminants.
Dwell Time: If necessary, the solution is allowed to dwell on the surface for a up to 5 minutes to penetrate and dissolve the contaminants effectively.
Rinsing: After the dwell time, the surface is typically rinsed thoroughly with water to remove the dissolved contaminants and any remaining cleaning agent residue. It's essential to ensure thorough rinsing to prevent any residue from causing damage or posing a safety hazard.
Drying: Finally, the cleaned surface may be left to air dry or dried using towels.

## WARNING

DO NOT USE BLEACH in any diluted cleaning solution.

# WARNING 

Grease is an irritant and can cause an allergic reaction. Contact, inhalation or ingestion can cause illness or injury. To prevent illness or injury, adhere to the following:

- PREPARATION:
- Ensure that the area is well ventilated.
- Have no food or beverages around the robot and cleaning agents.
- Ensure that an eye wash station is nearby.
- Gather the required PPE (gloves, eye protection)
- WEAR :
- Protective gloves: Oil resistant gloves (Nitrile) impermeable and resistant to product.
- Eye protection is recommended to prevent accidental contact of grease with eyes.
- DO NOT INGEST.
- In the event of
- contact with skin, wash with water and a mild cleaning agent
- a skin reaction, get medical attention
- contact with the eyes, use an eyewash station, get medical attention.
- inhalation of vapors or ingestion of grease, get medical attention
- After grease work
- clean contaminated work surfaces.
- dispose responsibly of any used rags or paper used for cleaning.
- Contact with children and animals is prohibited.

Robot Arm Inspection Plan

The table below is a checklist of the type of inspections recommended by Universal Robots. Perform inspections regularly as advised in the table. Any referenced parts found to be in an unacceptable state must be rectified or replaced.

|  Inspection action type |  |  | Timeframe |  |   |
| --- | --- | --- | --- | --- | --- |
|   |  |  | Monthly | Biannually | Annually  |
|  1 | Check flat rings | V |  | $x$ |   |
|  2 | Check robot cable | V |  | $x$ |   |
|  3 | Check robot cable connection | V |  | $x$ |   |
|  4 | Check Robot Arm mounting bolts | F | $x$ |  |   |
|  5 | Check Tool mounting bolts * | F | $x$ |  |   |
|  6 | Round Sling | F |  |  | $x$  |

Robot Arm Inspection Plan

NOTICE
Using compressed air to clean the robot arm can damage the robot arm components.

- Never use compressed air to clean the robot arm.
![img-62.jpeg](img-62.jpeg)

Robot Arm Inspection Plan

1. Move the Robot Arm to ZERO position, if possible.
2. Turn off and disconnect the power cable from Control Box.
3. Inspect the cable between Control Box and Robot Arm for any damage.
4. Check the base mounting bolts are properly tightened.
5. Check the tool flange bolts are properly tightened.
6. Inspect the flat rings for wear and damage.

- Replace the flat rings if they are worn out or damaged.


# NOTICE 

If any damage is observed on a robot within the warranty period, contact the distributor where the robot was purchased.

Inspection

1. Unmount any tool/s or attachment/s or set the TCP/Payload/CoG according to tool specifications.
2. To move the robot arm in Freedrive:

- On a 3PE Teach Pendant, rapidly light-press, release, light-press again and keep holding the 3PE button in this position.
![img-63.jpeg](img-63.jpeg)
3. Pull/Push the robot to a horizontally elongated position and release.
![img-64.jpeg](img-64.jpeg)

4. Verify the robot arm can maintain the position without support and without activating Freedrive.

# 15.3. Log Tab 

Description
The Log tab displays information about the robot arm and Control Box.
![img-65.jpeg](img-65.jpeg)

Readings
and Joint
Load

The Readings pane displays Control Box information. The Joint Load pane displays information for each robot arm joint.
Each joint displays:

- Temperature
- Load
- Status
- Voltage

Date Log
The first column displays log entries, categorized by the severity. The second column shows a paperclip if there is an Error Report associated with the log entry. The next two columns display the messages' time of arrival and the source of the message. The last column shows a short description of the message itself.
Some log messages are designed to provide more information that is displayed on the right side, after selecting the log entry.

Message
Severity

You can filter messages by selecting the toggle buttons that correspond to the severity of the log entry or by whether an attachment is present. The following table describes message severity.

| $\Theta$ | Provides general information, such as status of a program, changes of <br> the controller and controller version. |
| :-- | :-- |
| $\Delta$ | Issues that may have occurred but the system was able to recover. |
| $\Delta$ | A violation occurs if the safety limit is exceeded. This causes the robot <br> to perform a safety rated stop. |
| $\Delta$ | A fault occurs if there is an unrecoverable error in the system. This <br> causes the robot to perform a safety rated stop. |

When you select a log entry, additional information appears on the right side of the screen. Selecting the attachments filter either displays entry attachments exclusively or, displays all entries.

Saving Error A detailed status report is available when a paper clip icon appears on the log line. Reports

# NOTICE 

The oldest report is deleted when a new one is generated. Only the five most recent reports are stored.

1. Select a log line and tap the Save Report button to save the report to a USB drive.

You can save the report while a program is running.
You can track and export the following list of errors:

- Emergency stop
- Fault
- Internal PolyScope exceptions
- ¹Robot Stop
- Unhandled exception in URCap
- Violation

The exported report contains: a user program, a history log, an installation and a list of running services.

[^0]
[^0]:    ${ }^{1}$ Robot stop was previously known as "Protective Stop" for Universal Robots robots.

|  Technical | The report file contains information that is helpful to diagnose and reproduce issues. The file contains records of previous robot failures, as well as current robot configurations, programs and installations. The report file can be saved to external USB drive. On the Log screen, tap Support file and follow the on-screen instructions to access the function.  |
| --- | --- |
|  Support File | |   |
|  NOTICE | |   |
|  The export process can take up to 10 minutes depending on USB drive speed and the size of files collected from robot file system. The report is saved as a regular zip file, that is not password protected, and can be edited before sending to technical support. | |   |

# 15.4. Program and Installation Manager 

Description The Program and Installation Manager refers to three icons that allow you to create, load and configure Programs and Installations:

- New... Allows you to create a new Program and/or Installation.
- Open... Allows you to load a Program and/or Installation.
- Save... Offers saving options for a Program and/or Installation.

The File Path displays your current loaded Program name and the type of Installation. File Path changes when you create or load a new Program or Installation. You can have several installation files for a robot. Programs created load and use the active installation automatically.
![img-66.jpeg](img-66.jpeg)

To load a program

1. In the Program and Installation Manager, tap Open... and select Program.
2. On the Load Program screen, select an existing program and tap Open.
3. In the File Path, verify that the desired program name is displayed.
![img-67.jpeg](img-67.jpeg)

To load an installat ion

To create a new program

1. In the Program and Installation Manager, tap Open... and select Installation.
2. On the Load Robot Installation screen, select an existing installation and tap Open.
3. In the Safety Configuration box, select Apply and restart to prompt robot reboot.
4. Select Set Installation to set installation for the current Program.
5. In the File Path, verify that the desired installation name is displayed.
6. In the Program and Installation Manager, tap New... and select Program.
7. On the Program screen, configure your new program as desired.
8. In the Program and Installation Manager, tap Save... and select Save All or Save Program As...
9. On the Save Program As screen, assign a file name and tap Save.
10. In the File Path, verify that the new program name is displayed.
![img-68.jpeg](img-68.jpeg)

To create a new installation

Save your installation for use after powering down the robot.

1. In the Program and Installation Manager, tap New... and select Installation.
2. Tap Confirm Safety Configuration.
3. On the Installation screen, configure your new installation as desired.
4. In the Program and Installation Manager, tap Save... and select Save Installation As...
5. On the Save Robot Installation screen, assign a file name and tap Save.
6. Select Set Installation to set installation for the current Program.
7. In File Path, verify that the new installation name is displayed.

To use the Save options

Save...Depending on the program/installation you load-create, you can:

- Save All to save the current Program and Installation immediately, without the system prompting to save to a different location or different name. If no changes are made to the Program or Installation, the Save All... button appears deactivated.
- Save Program As... to change the new Program name and location. The current Installation is also saved, with the existing name and location.
- Save Installation As... to change the new Installation name and location. The current Program is saved, with the existing name and location.
![img-69.jpeg](img-69.jpeg)


# 15.5. Accessing Robot Data 

Description Use the About option to access and display different types of data about the robot. You can display the following types of robot data:

- General
- Version
- Legal

|  To display | 1. | In the Header, tap the Hamburger menu.  |
| --- | --- | --- |
|  data about | 2. | Select About.  |
|  the robot | 3. | Tap General to access the robot's software version, network settings and serial number.For the other data types you can:  |
|   |  | • Tap Version to display more detailed data about the robot's software version.  |
|   |  | • Tap Legal to display data about the robot's software license/s.  |
|   | 4. | Tap Close to return to your screen.  |