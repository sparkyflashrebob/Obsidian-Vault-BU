---
tags:
  - notebooklm-import
notebook: "H_Netgear Certification Level 1"
category: "research"
---

NETGEAR AV Certification Level 1
Table of Contents
COURSE INTRODUCTION .................................................................................................................. 4
COURSE AGENDA .......................................................................................................................................... 5 LEARNING OBJECTIVES ................................................................................................................................... 5 CERTIFICATION OVERVIEW .............................................................................................................................. 6
MODULE 1 – THE OSI MODEL ............................................................................................................ 7
THE 7-LAYER OSI MODEL .............................................................................................................................. 7 Hardware Layers vs. Software Layers .................................................................................................. 7 Detailed Overview of the OSI Layers .................................................................................................. 8
ENCAPSULATION AND PACKET SWITCHING ................................................................................................... 10 THE ROLE OF THE PHY ................................................................................................................................. 11 ROUTERS AND ADVANCED FUNCTIONS ......................................................................................................... 11
MODULE 02 – DEFINING A NETWORK ............................................................................................ 13
TYPES OF NETWORKS ................................................................................................................................... 14 MEDIA ACCESS CONTROLLER (MAC) ........................................................................................................... 16 BROADCAST DOMAINS ................................................................................................................................. 17 SUBNETS ...................................................................................................................................................... 18 CLASSLESS INTER-DOMAIN ROUTING (CIDR) ............................................................................................... 19 IPV4 VS. IPV6 ............................................................................................................................................... 20
MODULE 03 – TOPOLOGY AND DESIGN ........................................................................................ 22
NETWORK TOPOLOGY .................................................................................................................................. 23 Spine and Leaf Topology .................................................................................................................... 24 Stacked Core Topology ...................................................................................................................... 25
NETWORK SPEEDS ........................................................................................................................................ 26 COPPER VS. FIBER ........................................................................................................................................ 26 MANAGING BANDWIDTH .............................................................................................................................. 28
Network Security ................................................................................................................................. 28
MODULE 04: UNICAST, MULTICAST, AND BROADCAST ............................................................... 29
UNDERSTANDING UNICASTING ..................................................................................................................... 30 EXPLORING BROADCASTING ......................................................................................................................... 31 THE EFFICIENCY OF MULTICASTING ............................................................................................................... 32
Internet Group Management Protocol (IGMP) ................................................................................ 33 Protocol Independent Multicast (PIM) .............................................................................................. 33
INTRODUCING IGMP PLUS™ ....................................................................................................................... 34 Benefits of IGMP Plus™ ...................................................................................................................... 34 How IGMP Plus™ Works ..................................................................................................................... 35
MODULE 05: UNDERSTANDING VLANS ......................................................................................... 37
WHAT IS A VLAN? ....................................................................................................................................... 37 Benefits of VLANs ................................................................................................................................ 38
VLAN PORTS ............................................................................................................................................... 39 VLAN TAGGING .......................................................................................................................................... 40 CONTROL VLANS ........................................................................................................................................ 40
MODULE 06: UNDERSTANDING TERMINOLOGY ........................................................................... 42
NETGEAR AV Certification Level 1
LINK AGGREGATION ..................................................................................................................................... 42 SPANNING TREE PROTOCOL (STP) ................................................................................................................ 43 MULTI-CHASSIS LINK AGGREGATION (MLAG) .............................................................................................. 44 BLOCKING VS. NON-BLOCKING NETWORKS .................................................................................................. 45 AV NETWORK EXAMPLE ............................................................................................................................... 46
MODULE 7 – NETGEAR ENTERPRISE SWITCHES ............................................................................ 47
SPECIFICATION SHEETS ................................................................................................................................. 47 POWER BAYS ................................................................................................................................................ 48 POWER OVER ETHERNET (POE) .................................................................................................................... 49 PORT CONFIGURATION ................................................................................................................................. 50 CHOOSING YOUR SWITCH ............................................................................................................................ 51
Office Example .................................................................................................................................... 52 ADDITIONAL FEATURES ................................................................................................................................ 53
MODULE 8 – ENGAGE CONTROLLER .............................................................................................. 54
REDUCING NETWORK COMPLEXITY .............................................................................................................. 55 KEY FEATURES OF ENGAGE CONTROLLER ..................................................................................................... 55 INSTALLATION AND SETUP ............................................................................................................................ 56 DEVICE SETUP AND PROFILE MANAGEMENT ................................................................................................. 59
MODULE 9 – SPECIFYING NETGEAR SWITCHES ............................................................................ 61
UNDERSTANDING THE NEEDS OF THE PROJECT ............................................................................................. 62 Switch Example: 96-Port Network ..................................................................................................... 63
REDUNDANCY CONSIDERATIONS .................................................................................................................. 64 Example: ST2110 Broadcast Network .............................................................................................. 65
IDENTIFYING BANDWIDTH REQUIREMENTS .................................................................................................... 67 COMMUNICATING WITH CUSTOMERS ............................................................................................................ 67 NETGEAR ENGAGE IS KEY WHEN PITCHING YOUR PROJECT ......................................................................... 68
REVIEW THE CONTENT AND TAKE THE TEST ................................................................................. 69
DISCLAIMER:
This guidebook is intended to support your AV over IP learning journey and includes visual references to graphics from our on-demand video lessons, which are available at
www.netgear.academy
For a more comprehensive learning experience, we encourage you to explore the full video content at the provided link.
NETGEAR, the NETGEAR logo, NETGEAR AV, Engage and IGMP Plus are trademarks and/or registered trademarks of NETGEAR, Inc. and/or its subsidiaries in the United States and/or other countries. Other brand names mentioned herein are for identification purposes only and may be trademarks of their respective holder(s). Information is subject to change without notice.
© 2024 NETGEAR, Inc. All rights reserved.
NETGEAR AV Certification Level 1

##### Course Introduction

Welcome to the NETGEAR AV Level One Certification course! It’s a pleasure for us to guide you through this learning journey.
In the AV industry, there’s a growing need to standardize a minimum core level of networking competency across all job functions. This course is designed to address that need. Over the next nine modules, you’ll gain a comprehensive understanding of AV networking. We’ll break down complex terminology, explain the vital roles of various network functions, and demonstrate how to efficiently transmit audio, video, and control signals over an Ethernet network.
We’ll also showcase NETGEAR Engage, a tool that simplifies network configuration and management, eliminating the need to manage individual user interfaces for each component. This course will equip you with the knowledge to navigate AV networking with confidence and efficiency.
NETGEAR AV Certification Level 1

##### Course Agenda

This course is structured to provide a step-by-step foundation for networking in the AV industry:

* Module 1: Refresh your understanding of the OSI Model—the foundational framework for networking.
* Module 2: Define what a network is and its essential components.
* Module 3: Explore network topologies and their role in identifying system requirements for AV projects.
* Module 4: Understand the differences between Unicast, Broadcast and Multicast.
* Module 5: Learn how networks are segmented into VLANs.
* Module 6: Dive into IT terminology related to AVoIP systems.
* Module 7: Interpret technical specifications of NETGEAR Enterprise Switches
* Module 8: Start your journey with Engage onboarding your first switches.
* Module 9: Combine everything you’ve learned to specify efficient switch configurations for AVoIP project.

##### Learning Objectives

By completing this Level 1 certification course, you will be able to:

1. Understand Basic Networking Terminology
   o Gain a clear understanding of key networking terms and their functions in a typical AV-over-IP project.
2. Identify Switch Configurations and Capabilities
   o Learn how to match switch configurations to specific project requirements.
3. Specify a Switching infrastructure for AVoIP
   o Determine the correct network infrastructure based on AVoIP requirements.
   NETGEAR AV Certification Level 1
   Advance to Higher Certification Levels
   Prepare for Level 2 certification, where you’ll take the lead on implementing NETGEAR switches in projects. Level 3 training is also available for managing large-scale deployments with hundreds or thousands of endpoints.
   Upon successful completion, you’ll earn AVIXA RU points and the title of NETGEAR Level 1 Certified, showcasing your qualifications to the industry. This certification positions you at the forefront of the Pro AV industry as AV-over-IP continues to become the standard infrastructure.

##### Certification Overview

The NETGEAR Certification Program is structured to help you progress through three levels of expertise:

* Level 1: Establish foundational knowledge and skills in networking for AV-over-IP projects.
* Level 2: Focus on advanced configurations and project implementation.
* Level 3: Prepare for managing large-scale deployments.
  This certification ensures you meet the competency standards required by global corporate IT teams, enabling you to successfully implement AV-over-IP solutions.
  Your journey begins here, where we’ll start by covering the basics and building a strong foundation for your future success.
  NETGEAR AV Certification Level 1

##### Module 1 – The OSI Model

The OSI Model (Open Systems Interconnection model) serves as the cornerstone of Ethernet-based communication. In simple terms, it transforms physical signals into application data. While this definition is straightforward, understanding how it accomplishes this is crucial to mastering AV networking.

##### The 7-Layer OSI Model

The OSI model comprises seven layers that enable seamless communication between devices. Physical signals, such as those carried by cables or Wi-Fi, enter at the bottom layer and emerge as application data at the top layer. Each OSI layer has a specific function, working collectively to facilitate data exchange.
Think of each networked device—routers, switches, phones, computers, and even smart appliances—as having its own OSI model. While we use these devices daily, understanding how they communicate ensures efficient AV network design and troubleshooting.
Hardware Layers vs. Software Layers
The OSI model can be divided into hardware layers (1–4) and software layers (5– 7):

* Hardware layers focus on the transmission and management of data at the physical level.
* Software layers handle application-specific tasks, such as data encryption, presentation, and session control.
  Professionals responsible for networking hardware typically focus on layers 1–4, while software developers concentrate on layers 5–7.
  NETGEAR AV Certification Level 1
  Detailed Overview of the OSI Layers

1. Physical Layer
   Handles the physical connection between devices, transmitting raw signals over mediums like cables, fiber optics, or radio frequencies. It relies on a component called the PHY (physical layer device) to convert signals into digital data for further processing.
2. Data Link Layer
   Ensures reliable data transfer between directly connected devices. It uses MAC (Media Access Control) addresses to identify devices and manage error detection and correction. At this layer, data packets are framed and checked for errors.
3. Network Layer
   Responsible for routing packets across networks using logical addresses. This layer supports advanced management, including multicasting and subnetting. Protocols like IP (Internet Protocol) manage connectionless communication between endpoints.
   NETGEAR AV Certification Level 1
4. Transport Layer
   Ensures complete and accurate data delivery using protocols like:

* TCP (Transmission Control Protocol) for reliable, ordered communication (e.g., emails).
* UDP (User Datagram Protocol) for high-speed, unordered data transfer (e.g., video streaming).

5. Session Layer
   Manages connections between devices, ensuring data streams are synchronized and organized. This is essential for continuous data flows, such as during video conferencing.
6. Presentation Layer
   Translates and formats data for network transmission, handling encryption, compression, and translation. This layer ensures secure and readable communication between applications.
7. Application Layer
   Closest to the end user, it provides network services directly to applications. Protocols like HTTP (web browsing), FTP (file transfer), and SMTP (email) operate here, ensuring smooth application-network interaction.
   For example, when accessing LinkedIn, your device creates data packets encapsulated with headers. These packets travel through the layers, ensuring error-free and secure delivery to the intended destination.
   NETGEAR AV Certification Level 1

##### Encapsulation and Packet Switching

When data travels across the OSI layers, each layer adds a specific protocol header. This encapsulation ensures the data is properly managed at each stage of its journey.
The process called packet switching, breaks data into smaller packets for transmission, making it resilient to network congestion or failure.
NETGEAR AV Certification Level 1

##### The Role of the PHY

The PHY (physical layer device) plays a critical role in data transmission by converting digital data into physical signals for transmission across different media.

##### Routers and Advanced Functions

While switches can handle many network functions, routers often manage tasks like:

* Routing traffic across multiple independent networks.
  NETGEAR AV Certification Level 1
* Managing DHCP (Dynamic Host Configuration Protocol) for address
  assignment
* Enabling features like failover and load balancing to ensure network reliability.
  Summary
  The OSI model separates hardware and software responsibilities across its seven layers:

1. Physical Layer: Handles raw signal transmission (via the PHY).
2. Data Link Layer: Ensures error-free data transfer using MAC addresses.
3. Network Layer: Routes packets using logical addresses (IP).
4. Transport Layer: Manages data delivery using protocols like TCP and UDP.
5. Session Layer: Synchronizes data streams between devices.
6. Presentation Layer: Encrypts, compresses, and translates data.
7. Application Layer: Interfaces directly with end-user applications.
   Understanding these layers provides the foundation for effective network design and troubleshooting.
   NETGEAR AV Certification Level 1

##### Module 02 – Defining a Network

Welcome back to the NETGEAR Level 1 Certification Course! In Module 1, we explored the OSI Model, answering the question: “How does the OSI model work?”—a foundational concept for any networking professional.
Today, we’ll expand on that foundation by answering another critical question: “What is a network?”
This module also unpacks broadcast domains and introduces the essentials of IP addressing, equipping you with the knowledge needed to design, implement, and manage efficient network infrastructures.
Let’s begin by understanding what we mean when we use the term network.
What is a Network?
A network is an interconnected collection of devices—such as computers, printers, servers, and switches—that communicate over a shared medium. Its primary purpose is to facilitate data exchange and communication, enhancing productivity and operational efficiency.
NETGEAR AV Certification Level 1

##### Types of Networks

Networks can be categorized by their size and purpose:

* LAN (Local Area Network): Connects devices within a small area, like an office or home.
* WAN (Wide Area Network): Links larger areas, such as cities or countries.
  NETGEAR AV Certification Level 1
* WLAN (Wireless LAN): Uses radio waves for connectivity, offering mobility
  without cables.
  Ethernet, introduced in the 1970s, is the global standard enabling communication across these networks. It transforms raw data streams into packets, which can be exchanged efficiently. Without Ethernet, modern networks simply wouldn’t exist.
  NETGEAR AV Certification Level 1

##### Media Access Controller (MAC)

In Module 1, we discussed the PHY (physical layer). Attached to the PHY is the Media Access Controller (MAC), which handles Ethernet Data Link layer tasks. This includes:

* Framing data packets.
* Passing frames between OSI layers.
  Every MAC has a unique address, forming the core of packet-based communication. This unique MAC address ensures packets are traceable, enabling seamless communication within the network.
  While the OSI model outlines networks starting at Layer 3, networks are actually constructed at Layer 2, within something called a broadcast domain.
  NETGEAR AV Certification Level 1

##### Broadcast Domains

A broadcast domain is a Layer 2 network where a broadcast frame sent by one device can reach all devices within the same domain. Broadcast domains are determined by physical connectivity.
Efficient management of broadcast domains is crucial to:

* Prevent data floods that degrade performance.
* Optimize resource usage.
  NETGEAR AV Certification Level 1

##### Subnets

At Layer 3 (the Network layer), we connect multiple broadcast domains using IP addresses.

* Broadcast Domains (Layer 2): Devices communicate directly.
* Subnets (Layer 3): Devices across networks communicate through routers.
  NETGEAR AV Certification Level 1

##### 

##### Subnet Masks

##### Classless Inter-Domain Routing (CIDR)

Traditional IP addressing used fixed classes (e.g., Class A, B, C), which were inefficient.
NETGEAR AV Certification Level 1
CIDR introduced variable-length subnet masks for flexible allocation based on network needs.
CIDR enables:

* Subnetting: Dividing large networks into smaller ones to enhance performance and security.
* Optimized Traffic Management: Reducing unnecessary data transmission.
* Applications like NETGEAR Engage simplify the complexities of subnetting, automating processes like routing table creation.

##### Subnetting with CIDR

Subnetting is the process of subdividing an entire network to reduce congestion and overload.
The subnet mask acts as a filter, allowing only a specific range of IP address to communicate in that subnet.
Note that Broadcast is always the last IP address on each subnet.
NETGEAR AV Certification Level 1

##### 

##### 

##### 

##### 

##### IPv4 vs. IPv6

An IP address consists of two parts:

1. Network Portion (shared by all devices on the subnet).
2. Host Portion (unique to each device).
   The Subnet Mask defines this division, ensuring devices within the same subnet can communicate. Devices in different subnets require routing.
   NETGEAR AV Certification Level 1

* IPv4:
  o 32-bit addressing (≈ 4 billion addresses).
  o Easier to manage manually or via DHCP.
* IPv6:
  o 128-bit addressing (virtually unlimited).
  o Supports autoconfiguration for easier management.
  Both protocols coexist, with IPv4 dominating private networks and IPv6 emerging in public networks.
  Summary
  In this module, we’ve explored:

1. The definition and purpose of networks.
2. Key concepts like broadcast domains, subnets, and IP addressing.
3. The transition from IPv4 to IPv6 and the benefits of CIDR.
   These foundational elements are critical for understanding network infrastructures. In the next module, we’ll delve into network topologies and design, emphasizing documentation best practices. Don’t forget to take the quiz to test your understanding! See you in the next session!

##### Module 03 – Topology and Design

So far, we've reviewed foundational networking concepts to align your knowledge with that of a Level 1 certified professional. Now, we’re ready to tackle the question, “What does a network design need to consider?” This module focuses on network speeds, cable types, and the architectural principles needed for robust, scalable network designs. Mastering these topics will equip you to manage networks that support seamless media streaming and high-definition communications.
NETGEAR AV Certification Level 1

##### Network Topology

Network topology defines how network elements, such as nodes and connections, are arranged. This arrangement determines both the physical layout and the logical data flow within a network. The efficiency and scalability of a network heavily depend on its topology. Common examples include:

* Star Topology: Each node connects to a central hub, simplifying problem isolation and network management.
* Ring Topology: Nodes form a closed loop, ideal for small networks with predictable data flow.
* Bus Topology: A single central cable connects all devices, a simple yet outdated approach.
* Mesh Topology: Nodes interconnect with multiple paths, offering redundancy and reliability in critical environments.
  Selecting the appropriate topology is crucial for balancing performance, reliability, and future expansion.
  NETGEAR AV Certification Level 1
  Spine and Leaf Topology
  Modern networks often adopt spine and leaf architecture, ideal for handling massive data loads in AV environments. This design:
* Reduces latency with direct connections between devices and switches.
* Prevents bottlenecks, ensuring high throughput for real-time AV processing.
* Supports flexible expansion and reconfiguration with minimal disruption.
  This topology is a go-to choice for dynamic, high-performance networks.
  NETGEAR AV Certification Level 1
  Stacked Core Topology
  For environments requiring enhanced reliability, stacked core configurations offer:
* Redundancy: Ensures no single point of failure.
* Manageability: Simplifies network control by consolidating switches into a single logical unit.
* Performance: Integrates traffic management strategies to handle high-demand operations seamlessly.
  This approach is essential for mission-critical networks, such as those in financial or emergency services.
  NETGEAR AV Certification Level 1

##### Network Speeds

Network speeds have evolved to meet increasing data demands:

* 1G Networks: Reliable for general tasks but insufficient for today’s high-data environments.
* 10G Networks: Becoming the standard for high-bandwidth applications such as live event streaming and real-time data processing. These networks support simultaneous high-definition video streams and extensive file transfers without performance degradation.
  For ProAV systems, 10G is often the baseline for ensuring seamless media delivery.

##### Copper vs. Fiber

Choosing the right cabling is pivotal for network design. Key differences include:

* Copper Cables (e.g., CAT5e to CAT8):
  o Cost-effective.
  o Suitable for short distances.
  o Supports up to 10Gbps speeds.
  NETGEAR AV Certification Level 1
* Fiber Optic Cables:
  o Ideal for long-distance, high-bandwidth applications.
  o Immune to electromagnetic interference.
  o Single-mode fiber supports kilometers of connectivity with minimal loss, while multi-mode fiber is optimal for data center backbones.
  Pro Tip: Fiber ensures reliable, high-speed data transmission, especially in AV setups requiring uninterrupted signal quality.
  NETGEAR AV Certification Level 1

##### Managing Bandwidth

Effective bandwidth management ensures optimal network performance by:

* Prioritizing critical traffic (e.g., video over general data).
* Using Quality of Service (QoS) to allocate resources to high-priority applications.
* Implementing techniques like traffic shaping and rate limiting.
  Network Security
  Robust network security is vital for protecting data and infrastructure against evolving cyber threats.
  NETGEAR AV Certification Level 1
  Key measures include:
* Advanced firewalls and intrusion detection systems.
* Regular security audits.
* Compliance with legal standards for sensitive industries like healthcare and government.
  Security considerations must be integrated into every stage of network design.
  Summary
  In this session, we’ve explored the essential components of network infrastructure:
* Topologies that define layout and performance.
* Speed and cable options for specific use cases.
* Architectural principles like spine-and-leaf and stacked core designs.
* Bandwidth management strategies and robust security measures.
  In the next module, we’ll dive into the nuances of Unicast, Broadcast, and Multicast networking, examining how these transmission methods enhance communication efficiency and scalability.
  Don’t forget to take the quiz to test your understanding, and I’ll see you in the next module!

##### Module 04: Unicast, Multicast, and Broadcast

This module explores the fundamental networking protocols that underpin modern network management. You’ll learn about Unicast, Broadcast, and Multicast communications, along with a deeper understanding of the Internet Group Management Protocol (IGMP) and an introduction to Protocol Independent Multicast (PIM). These protocols are essential for optimizing network efficiency, especially in environments demanding high data transfer rates, such as multimedia streaming and enterprise systems.
NETGEAR AV Certification Level 1

##### Understanding Unicasting

Unicasting can be compared to a one-on-one conversation between two network devices, where data flows directly from a single sender to a specific receiver. It is the backbone of most internet communications, making it ideal for secure, point-to-point data transfers such as:

* Sending emails
* Streaming a video to a particular user
* Requesting information from a server
  ProAV Applications
  In ProAV, unicasting is commonly used for transmitting control data. These control streams are typically small and bursty, existing only when needed. Once the task is complete, they stop.
  Challenges of Unicasting
  While unicast communication is efficient for one-to-one data transfers, it becomes bandwidth-intensive when the same data needs to be sent to multiple endpoints. For instance, in AV networks where the same video or audio content must reach hundreds or thousands of devices, unicasting can lead to inefficiencies and excessive resource consumption.
  NETGEAR AV Certification Level 1

##### Exploring Broadcasting

Broadcast communication is akin to making a public announcement where every device within a broadcast domain receives the same message.
ProAV Use Cases
Broadcasting is effective for:

* Device discovery via Address Resolution Protocol (ARP)
* Network-wide announcements
* Configuration updates
  Limitations of Broadcasting
  Broadcast communication presents challenges in dense network environments, including:

1. Network Congestion: Every device must process each broadcast packet, creating unnecessary traffic.
2. Security Risks: Broadcasting indiscriminately sends data to all devices, increasing vulnerability.
   Broadcasting is not suitable for large-scale video or audio streaming due to these drawbacks.
   NETGEAR AV Certification Level 1

##### The Efficiency of Multicasting

Multicasting strikes a balance between the exclusivity of unicasting and the broad reach of broadcasting. It allows data to be efficiently distributed to multiple selected recipients.
ProAV Benefits
In AV networks, multicasting is ideal for:

* Live event streaming
* Webinars
* Real-time data sharing, such as stock tickers
  How It Works
  Instead of duplicating unicast streams for each endpoint, multicasting uses network infrastructure to duplicate packets only when necessary. This ensures bandwidth efficiency while sending data only to endpoints that request it.
  NETGEAR AV Certification Level 1
  Internet Group Management Protocol (IGMP)
  IGMP is a critical component of multicast communication, enabling routers to manage and track multicast group memberships.
  Key Functions

1. Devices that want to receive multicast streams send IGMP join requests to the router.
2. Routers maintain a membership list of devices in the multicast group.
3. Routers periodically query devices to confirm membership, removing inactive members to optimize data transmission.
   This process ensures that multicast streams are sent only to active and interested recipients, preserving network performance and resources.
   Protocol Independent Multicast (PIM)
   is a routing protocol used to efficiently route multicast traffic across networks. It doesn't depend on any specific unicast routing protocol (hence "independent"), and it’s designed to handle multicast group management and delivery for applications like streaming video or data distribution.
   NETGEAR AV Certification Level 1
   Key Difference:

* PIM is a multicast routing protocol that works across multiple routers and networks to deliver multicast traffic efficiently. It focuses on the routing part of multicast.
* IGMP Plus works at the local level to manage multicast group memberships within a single network segment or switch, optimizing how multicast traffic is handled within a local area network (LAN).

##### Introducing IGMP Plus™

IGMP Plus™ is an enhancement implemented in NETGEAR switches to simplify multicast traffic management.
Key Features

* Monitors IGMP conversations between hosts and routers.
* Streamlines configuration for ProAV networks by eliminating the need for multiple command-line entries.
* Conserves bandwidth by limiting multicast traffic to the relevant ports.
  Benefits of IGMP Plus™

1. Simplified Configuration With traditional IGMP, configuring multicast VLANs requires several commands, increasing the likelihood of user errors. IGMP Plus simplifies this with a single command.
2. Optimized Traffic Flow IGMP Plus prevents multicast flooding by ensuring only requested traffic is forwarded.
   Use Case: Spine and Leaf Architectures
   In complex ProAV setups using multiple switches, IGMP Plus can be applied across all switches to streamline configuration. By enabling IGMP Plus on a VLAN, multicast streams are efficiently distributed, avoiding unnecessary traffic and bandwidth issues.
   NETGEAR AV Certification Level 1
   How IGMP Plus™ Works
   Consider two scenarios:
   Without IGMP Plus: Multicast traffic from transmitters is sent indiscriminately to all ports, leading to excess traffic and potential bottlenecks.
   With IGMP Plus: Only requested multicast traffic is forwarded to the correct decoder, significantly improving network efficiency.
   This streamlined approach ensures that ProAV and data traffic coexist seamlessly without compromising performance.
   NETGEAR AV Certification Level 1
   Summary
   In this module, we covered the roles of Unicast, Broadcast, and Multicast in networking, emphasizing their relevance to ProAV environments. We also explored the importance of IGMP and the advantages of IGMP Plus in managing multicast traffic efficiently.
   These concepts form the backbone of effective network design, ensuring systems are robust, scalable, and capable of meeting the demands of modern data-intensive applications. Take the module quiz to test your understanding.
   NETGEAR AV Certification Level 1

##### Module 05: Understanding VLANs

This module explores Virtual Local Area Networks (VLANs), a critical concept in modern networking. By the end of this lesson, you will understand:

1. The purpose and benefits of VLANs.
2. Different types of VLAN ports.
3. VLAN tagging and its role in traffic management.
4. Control VLANs and their importance in network optimization.
   Let’s begin by addressing the foundational question: What is a VLAN?

##### What is a VLAN?

A VLAN is a logical subdivision of a physical network, creating multiple isolated networks within a single infrastructure.

* VLANs group devices logically rather than physically.
* Devices within a VLAN communicate as if they’re on the same physical network, even if located on separate switches.
* VLANs improve security, network management, and broadcast traffic reduction.
  NETGEAR AV Certification Level 1
  For example, in an AV environment, VLANs help segregate multimedia streams, ensuring smoother operation and reduced interference.
  Benefits of VLANs
  VLANs provide numerous advantages:

1. Enhanced Security
   o Sensitive data, such as financial transactions, can be isolated from other network traffic.
   o Segments like the finance or HR department can be kept separate from general traffic.
2. Improved Performance
   o Each VLAN has its own broadcast domain, reducing unnecessary network-wide traffic.
3. Simplified Management
   o Devices can be grouped logically by function or department, making moves or policy updates simpler.
   o Access control becomes more efficient, supporting scalable growth.
   NETGEAR AV Certification Level 1

##### VLAN Ports

To implement VLANs effectively, understanding VLAN port types is crucial:
Access Ports
o Connect individual devices to a specific VLAN.
o Carry traffic for only one VLAN.
o Commonly used for endpoint devices like encoders or decoders.
Trunk Ports
o Carry traffic for multiple VLANs between switches or between a switch and a router.
o Use VLAN tagging to identify which VLAN each frame belongs to.
o Essential for inter-VLAN communication and extending VLANs across multiple switches.
NETGEAR AV Certification Level 1

##### VLAN Tagging

VLAN tagging uses the IEEE 802.1Q protocol to maintain traffic separation by adding a VLAN ID to Ethernet frames.

* This ID ensures traffic is directed to the correct VLAN.
* Trunk ports use VLAN tagging to manage traffic from multiple VLANs on a single link.
  For example:
* A switch handling control traffic and USB streams will tag packets to direct them to the correct VLAN.
* Tagging ensures that only relevant traffic reaches specific endpoints, maintaining security and reducing congestion.

##### Control VLANs

A Control VLAN is dedicated to network management and control traffic.
Key purposes:

* Isolates critical management functions (e.g., switch management, Spanning Tree Protocol) from general network traffic.
* Enhances security and ensures uninterrupted control of the network.
  NETGEAR AV Certification Level 1
  Example Usage: In a combined AV and data network:
* Separate VLANs are used for departmental traffic (e.g., HR, IT, and Sales) and AV streams.
* A Control VLAN handles network management, ensuring smooth operations.
* Access ports connect devices to specific VLANs, while trunk ports link switches to carry traffic for all VLANs.
  Summary
  VLANs are a powerful tool for enhancing network security, performance, and manageability. By mastering VLAN configuration, including port types, tagging, and Control VLANs, you can optimize your network for scalability and efficiency.
  In the next module, we’ll dive into essential networking terminology, building a strong foundation to tackle advanced networking concepts confidently. Don’t forget to complete the short quiz to test your understanding of VLANs. See you in the next lesson!
  NETGEAR AV Certification Level 1

##### Module 06: Understanding Terminology

In this module, we’ll cover critical networking concepts that bridge the gap between IT and AV. Whether you’re a beginner or a seasoned professional, understanding these terms will boost your confidence when discussing network requirements with IT professionals, ensuring seamless collaboration during AV network design and implementation.

##### Link Aggregation

Link Aggregation combines multiple physical network links into a single logical link, increasing bandwidth and providing redundancy.
Key benefits include:

1. Improved Performance: Traffic is balanced across multiple links for optimal bandwidth utilization.
2. Redundancy: If one link fails, others maintain network availability.
   To manage Link Aggregation effectively, networks utilize the Link Aggregation Control Protocol (LACP), which dynamically detects and configures compatible links.
   Auto LAG simplifies this process by automatically grouping links for efficient utilization and failover. Similarly, Auto Trunk automates the configuration of trunk ports to carry traffic for multiple VLANs, reducing setup complexity and minimizing errors.
   NETGEAR AV Certification Level 1

##### Spanning Tree Protocol (STP)

Spanning Tree Protocol (STP) ensures a loop-free topology in Layer 2 networks by blocking redundant paths while providing failover options.
How it works:

* STP builds a logical map of the network’s broadcast domain.
* A central switch, known as the root bridge, manages the topology.
* STP calculates the best path to the root bridge based on link costs, blocking alternative paths to prevent loops.
  STP safeguards network stability by preventing disruptions like broadcast storms and maintaining efficient data flow.
  NETGEAR AV Certification Level 1

##### Multi-Chassis Link Aggregation (MLAG)

MLAG extends the concept of Link Aggregation across multiple switches, treating them as a single logical switch.
This approach offers:

1. Redundancy: Traffic flows seamlessly even if one switch fails.
2. Load Balancing: Efficient distribution of traffic across multiple switches.
3. Simplified Management: Unified management of aggregated links.
   MLAG enhances resilience in complex network topologies, making it a cornerstone of high-availability networks.
   NETGEAR AV Certification Level 1

##### Blocking vs. Non-Blocking Networks

These terms refer to a network's ability to handle traffic without congestion:

1. Blocking Networks
   o Limited bandwidth may delay or drop traffic during peak times.
   o Suitable for bursty data communication with lower throughput demands.
2. Non-Blocking Networks
   o Sufficient bandwidth supports all traffic simultaneously.
   o Ideal for AV multicast streams with high data transfer demands.
   When designing AV networks, consider the maximum possible throughput to ensure uninterrupted traffic flow. For example, calculate bandwidth requirements based on maximum resolution and ensure enough links between switches.
   NETGEAR AV Certification Level 1

##### AV Network Example

Consider a high-demand AV network requiring reliable performance:

1. Auto LAG and Auto Trunk: Simplify link aggregation and VLAN configuration.
2. STP: Maintains a loop-free topology for smooth communication.
3. MLAG: Provides redundancy and failover for uninterrupted operation.
4. Non-Blocking Design: Eliminates congestion, ensuring seamless AV streams.
5. LACP: Dynamically manages link aggregation for optimal traffic distribution.
   These features collectively create a robust network infrastructure tailored to AV requirements. Later in the course, we’ll explore how NETGEAR Engage simplifies configuring these elements.
   Summary
   This module covered essential concepts in modern networking:

* Auto LAG and Auto Trunk streamline configurations.
* STP ensures loop-free operations.
* MLAG provides switch redundancy.
* Non-Blocking Networks eliminate congestion.
* LACP manages aggregated links dynamically.
  These terms are foundational to designing high-performance AV networks. With this knowledge, you’re better equipped to navigate complex scenarios confidently.
  NETGEAR AV Certification Level 1

##### Module 7 – NETGEAR Enterprise Switches

In this module, we’ll explore the key features of NETGEAR enterprise switches, focusing on power bays, Power over Ethernet (PoE), and port configurations. These are essential components that help support AV network projects. We’ll also refer to the switch specification sheet to understand how these features come together to meet the needs of AV systems. Let’s dive in and start preparing for the Level 2 certification, where we’ll go deeper into how each switch supports AV network projects.

##### Specification Sheets

As AV and IT professionals, we’re all familiar with the specification sheet of a product. It’s an essential resource when evaluating a switch for its capabilities, ensuring that it meets your network’s requirements. By understanding the specifications, you can make informed decisions and even exceed expectations based on what else the product can do. NETGEAR Enterprise Switches, specifically designed for AV over IP, feature the Engage platform for easy configuration, offering certified profiles for over 200 manufacturers. We’ll explore Engage in more detail in the next module. For now, let’s focus on the specifications we’re familiar with.
NETGEAR AV Certification Level 1

##### Power Bays

NETGEAR enterprise switches come with dual power supply configurations, providing critical redundancy to ensure maximum reliability and uptime. If one power supply fails, the other will seamlessly take over, preventing disruptions. These power supplies are also hot-swappable, allowing for replacement without downtime, which is essential in environments like data centers and mission-critical applications. Furthermore, these power supplies are energy-efficient, helping to reduce operational costs while supporting green IT initiatives.
NETGEAR AV Certification Level 1

##### Power Over Ethernet (PoE)

PoE is a feature that simplifies the deployment of network devices by delivering both data and power over a single Ethernet cable. NETGEAR switches support several PoE standards to meet varying power requirements.

* PoE (802.3af): Delivers up to 15.4W per port, suitable for devices like IP phones and wireless access points.
* PoE+ (802.3at): Delivers up to 30W per port, ideal for devices with moderate power needs.
* PoE++ (802.3bt): Provides up to 60W or 90W per port, designed for high-power devices like PTZ cameras and lighting systems.
  The total PoE power budget varies across models, offering flexibility for powering multiple devices, reducing cabling, and simplifying deployment.
  NETGEAR AV Certification Level 1

##### Port Configuration

NETGEAR enterprise switches offer a variety of port configurations to meet the diverse connectivity needs of modern networks.
These include:

* Gigabit Ethernet ports: Ideal for general connectivity at speeds of 10/100/1000 Mbps.
* 10-Gigabit SFP+ ports: Perfect for high-bandwidth applications, such as server connections or switch uplinks, supporting speeds of up to 10 Gbps.
* Multigigabit ports: Support speeds of 2.5G, 5G, and 10G, useful for high-performance devices like Wi-Fi 6 access points.
  This mix of ports ensures that the switch meets your current and future network needs, providing optimal performance and future-proofing.
  NETGEAR AV Certification Level 1

##### Choosing Your Switch

When selecting the right NETGEAR switch for your project, several factors need to be considered:

1. Power Requirements: Evaluate the number and types of devices that require PoE to choose a switch with the appropriate power budget.
2. Port Density and Types: Consider how many devices need connectivity and the types of ports required (e.g., 1 Gbps, 10 Gbps, or Multigigabit).
3. Redundancy: For critical applications, choose switches with dual, hot-swappable PSUs to ensure uninterrupted service in case of a failure.
4. Scalability: Ensure the switch can scale with your network demands, offering flexibility for future growth.
   NETGEAR AV Certification Level 1
   Office Example
   Let’s look at a practical example to illustrate how to choose the right switch. This AV project needs to connect and power:

* 12x PoE+ gooseneck mics
* 6x PoE++ ceiling speakers
* 2x Multi-Gig WiFi 7 PoE++ access points
* 4 PoE++ PTZ cameras
  The switch must support 2x 10G Fiber ports for a long backhaul and support high availability, making redundancy a critical factor.
  For such a setup, a NETGEAR M4350 44M4X4V switch would be ideal. It offers sufficient PoE budget for all devices, includes a mix of 1 Gbps and 10 Gbps ports, and features dual, hot-swappable PSUs for redundancy, meeting the high availability requirement of the project.
  NETGEAR AV Certification Level 1

##### Additional Features

NETGEAR enterprise switches also offer advanced features like:

* Quality of Service (QoS): Prioritizes critical network traffic to ensure optimal performance.
* VLAN Support: Helps segment network traffic for better traffic management.
* Security Features: Access control lists (ACLs) and network monitoring tools protect your network from threats and optimize traffic.
  These advanced features enhance network performance and security, ensuring smooth and efficient operation.
  Summary
  NETGEAR enterprise switches provide robust features tailored to modern network environments. Their advanced power bays ensure redundancy and efficiency, PoE capabilities simplify device deployment, and versatile port configurations meet all connectivity needs. Whether you’re building a small office or large enterprise network, NETGEAR switches offer flexibility and scalability. In the next module, we’ll explore how the Engage platform allows you to manage switch configurations seamlessly.
  NETGEAR AV Certification Level 1

##### Module 8 – Engage Controller

In this lesson, we will dive into the key aspects of the NETGEAR Engage Controller, focusing on installation, user interface navigation, and configuring your network for different applications such as Video, Audio, Lighting, and NDI. Engage is an invaluable tool that simplifies network management in AV-over-IP installations, so let's get started!
NETGEAR Engage™ Controller
The NETGEAR Engage™ Controller removes the complexity of network configuration and management in AV-over-IP installations using NETGEAR's M4250, M4350, M4300 and M4500 switches. This free, portable app for both Windows and MacOS automatically detects all switches, allowing you to upgrade firmware and configure settings across your network. The Engage Controller makes deploying AV networks straightforward and efficient.
NETGEAR AV Certification Level 1

##### Reducing Network Complexity

AV-over-IP installations often come with network configuration challenges. Managing Ethernet switches is critical to ensuring a successful AV-over-IP setup. With Engage, you can eliminate manual switch detection and firmware updates, as the software automatically handles these tasks. You can also configure switches for various AV applications such as Dante, AES67, AVB, and Lighting, which can otherwise be error-prone and difficult for those unfamiliar with networking.

##### Key Features of Engage Controller

* Switch Detection and Configuration: Engage automatically detects M4250,
  M4350, and M4500 switches and allows you to configure them with port-based profiles across the network.
* Network Topology Visualization: Engage provides a visual map of your network, showing all switches, ports, and connected devices. This helps ensure that your network design matches the physical setup.
* Centrally Manage Multiple Sites: Engage allows you to manage multiple AV networks or locations through the same controller. For example, a larger auditorium can be set up with different profiles than a smaller one, ensuring customization for each environment.
* Profile Management: You can create and assign network profiles to ports, including the Default network profile and any other custom profiles, such as those for Dante AV, ensuring that your switches are optimized for your AV needs.
  NETGEAR AV Certification Level 1

##### Installation and Setup

Download the Engage Controller: Instructions for downloading the controller are provided in the course resources. Ensure that your firewall and anti-virus programs are adjusted to avoid interference with the installation.
NETGEAR AV Certification Level 1

1. Initial Login and Admin Setup: The first time you log in to Engage, you will
   be prompted to set an admin password for security. You will also create a default site for your network configuration.
2. Configure Site Settings:
   o Set a site name and description.
   NETGEAR AV Certification Level 1
3. Configure Network Settings for Engage
   Decide on how the controller connects to your AV network (Dynamic IP, Static IP, or Static IP + DHCP).
4. Onboarding Switches
   After setting up your network connection, Engage will display all switches detected in the network. You can onboard each switch by entering its device
   NETGEAR AV Certification Level 1
   password and allow the controller to configure the devices.
5. Network Profile Setup: Review available profiles and assign the appropriate ones to each switch. You can create new profiles or modify existing ones, ensuring each switch is properly configured for its role.

##### Device Setup and Profile Management

During the onboarding process, Engage pulls the network profiles from your switches and pushes these profiles to onboarded devices. You can manage and
NETGEAR AV Certification Level 1
edit network profiles directly through the controller, changing their names, VLAN IDs, and colors for easier identification.
Finalizing the Setup
Once your network profiles are configured and switches are onboarded, your Engage network controller is ready to go. You can always make adjustments and updates as your network grows or changes.
Summary
NETGEAR’s Engage Controller simplifies the management of AV-over-IP installations by automatically detecting switches, streamlining firmware upgrades, and making profile configurations intuitive and efficient. It enables centralized control of your network setup, saving time and reducing the complexity of large-scale AV projects. With Engage, network configuration becomes a seamless part of your AV deployment.
In the next session, we’ll cover best practices for selling NETGEAR Enterprise Switches to your customers. Don’t forget to take the short quiz to check your understanding of this module!
NETGEAR AV Certification Level 1

##### Module 9 – Specifying NETGEAR Switches

In this module, we will explore how to specify the right NETGEAR switches for your AV projects. Properly selecting and applying the right switch lineup is critical to the success of your design. This guide will help you make informed decisions about which switch to use based on your project’s specific requirements.
Switches Overview
NETGEAR’s M4250, M4300, M4350, and M4500 switches are designed to support various AV over IP projects, offering flexibility and scalability to meet the needs of different applications. To effectively specify the right switch for your project, we’ll discuss:

* Understanding the project’s scope, budget, and infrastructure design.
* How to use specification sheets to determine the right equipment.
* Leveraging NETGEAR Engage for simplified configuration and management.
  NETGEAR AV Certification Level 1

##### Understanding the Needs of the Project

Selecting the appropriate switch may feel challenging, especially for those new to enterprise-level networking. The first step in this process is understanding your project’s requirements. Key considerations include:

* Number of devices to be connected.
* Type of devices (e.g., audio/video equipment, computers, etc.).
* Bandwidth requirements for each device and the overall system.
  For smaller deployments, the M4250 series is a cost-effective option. For larger-scale installations, the M4300 and M4350 series offer a balance of performance and value. For high-demand applications, the M4500 series provides top-tier performance and reliability.
  NETGEAR AV Certification Level 1
  Switch Example: 96-Port Network
  Let’s break down an example to understand how to match the right switch to the project needs. In this case, we look at a 96-port network using M4250 switches in a core-and-access topology.
* Core Switch (SW1): The M4250 core switch connects to access switches via 10G SFP fiber ports, utilizing Auto-LAG link aggregation to deliver 40Gb throughput between the core and each access switch.
* Access Switches: Each access switch offers 40x 1Gb copper ports, sufficient for a deployment with 96x 1Gb endpoints and additional headroom for 24 more endpoints.
  This configuration is ideal for smaller to mid-sized projects, providing a reliable, scalable solution with a total throughput capacity of 40Gb across the core
  NETGEAR AV Certification Level 1

##### Redundancy Considerations

Redundancy ensures that your system continues to operate even if part of the network fails. While redundancy is not always necessary, larger or mission-critical projects may require it.
In a stacked core configuration, two M4350 switches act as redundant core switches, with each connected to multiple M4250 access switches. If one core switch fails, the other maintains connectivity, and the system can still operate with 20Gb link aggregation. This redundancy is essential for high-availability systems where uptime is critical.
NETGEAR AV Certification Level 1
Example: ST2110 Broadcast Network
For projects requiring 10G infrastructure, such as SMPTE 2110 AV over IP deployments, the M4350 switches are ideal. In this example:

* Switches 2–5: M4350 switches support 10Gb endpoints, used to connect broadcast devices.
* Switches 6-7: M4250 switches manage 1Gb traffic on the same network.
* Core Switch (C3): An M4350 switch with 100G QSFP ports aggregates all traffic between the switches.
  This design supports high-performance 10Gb AV streams while maintaining cost-effectiveness for non-10Gb devices.
  NETGEAR AV Certification Level 1
  Choosing Your Switches
  Budget considerations are crucial when selecting the right switch for a project. NETGEAR offers options for various financial plans without sacrificing performance or reliability:
* The M4250 series is an affordable solution for small to medium-sized projects.
* The M4300 and M4350 series offer excellent performance for more demanding applications.
* The M4500 series is the premium option for mission-critical and large-scale deployments, offering the highest level of performance and scalability.
  Be sure to carefully review the technical specifications of each switch to ensure it matches the project’s requirements.
  NETGEAR AV Certification Level 1

##### Identifying Bandwidth Requirements

When determining the right switch, start by calculating the total throughput required for all devices in the system. This helps identify the link aggregation necessary to ensure sufficient bandwidth for all the devices.
Always refer to the specification sheets to make sure the switches meet the technical demands of your project. These documents outline each switch’s capabilities, features, and performance specifications.
With NETGEAR’s M4250, M4300, M4350, and M4500 series switches, you are equipped to handle any AV over IP project, ensuring high-quality, reliable audio and video streaming across your network.

##### Communicating with Customers

Once you’ve gained a deeper understanding of NETGEAR switches, you can effectively communicate with customers and align their needs with the right equipment. Here’s how to approach the conversation:

* Emphasize the value of AV over IP and how NETGEAR switches simplify cabling, centralize management, and improve scalability.
* Tailor your approach to the customer’s specific needs, budget, and existing infrastructure.
* Highlight the unique features of the NETGEAR switches and how they outperform competitors.
* Provide real-world examples and case studies to reinforce the benefits of NETGEAR switches.
  NETGEAR AV Certification Level 1

##### NETGEAR Engage is Key when Pitching your Project

With Engage, you can:

* Onboard switches into a project with ease.
* Assign devices to specific ports and configure the necessary services.
* Manage multicast streams for video and audio across multiple switches.
  Engage’s streamlined configuration process saves significant time and ensures your system is correctly set up the first time.
  Summary
  By thoroughly understanding project needs and selecting the appropriate NETGEAR switch, you ensure the success of your AV over IP deployment. NETGEAR switches provide reliability, scalability, and performance, making them a trusted choice for AV professionals worldwide.
  Remember:
* Choose the right switch based on the project’s scope, budget, and performance requirements.
* Use specification sheets to make informed decisions.
* Leverage NETGEAR Engage to simplify configuration and management.
* Emphasize the value of NETGEAR’s commitment to quality and support when communicating with clients.
  NETGEAR AV Certification Level 1

##### Review the Content and Take the Test

Congratulations on reaching the final module of the Level One Certification course! You’ve completed an important step in your journey to becoming a certified AV over IP (AVoIP) professional, and we’re excited to support you as you continue to grow and develop in this field.
Review of the Content
Before you take the final assessment, it’s important to review the material you’ve covered throughout this course.
Next Steps: Take the Test
You’re now ready to take the Level One Assessment. The assessment is designed to test your understanding of the material covered in the course. You can attempt the assessment as many times as you need to, and we encourage you to revisit any modules if you need a refresher.
Upon successfully completing the assessment, you will earn your Level 1 Certification. This certification will give you the foundation to move forward into Level 2, where you’ll expand your skills and dive deeper into how to implement and configure NETGEAR switches for more complex AV over IP projects.
Good Luck!
We wish you the best of luck on your assessment. We’re confident you have gained the knowledge and skills to succeed. When you complete the certification, you’ll be one step closer to mastering the world of AV over IP.
We look forward to seeing you in Level 2!
NETGEAR AV Certification Level 1