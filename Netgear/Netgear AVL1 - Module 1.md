Module 1

Please
Do
Not
Throw
Salami
Pizza
Away

## Hardware Levels

### 1 Physical (copper, fiber, rf) Raw signal 
- via PHY converter
	- like a sampler
	- Physical Layer Chip
		- cables, connectors, voltages, data rates, transmission distances
	- bridge physical system and the digital medium
	- TOPOLOGY
	- BIT TRANSMISSION
		- 1's and 0's
	- BIT SYCNHRONIZATION
		- clocks
	- TRANSMISSION MODE
		- simplex, full or half duplex
	- cables, hubs, repeaters, NICS, modems

### 2 Data Link (Digital Data)
- PHY units MAC ADDRESS
	- Media Access Control
- 12-digti hex number AA:BB:CC:DD:EE:01
- uniquely identifies a device on a network
![[Pasted image 20250624185905.png]]
- Manages error detection and correction between PHY's
- Need to ID the broadcast domain
- SEGMENTED INTO FRAMES
- ERROR CONTROL
- FLOW CONTROL
- Sender and destination MAC Addresses Added
	- PHYSICAL ADDRESSIN (MAC)

OSI model is two lane highway
- full duplex
![[Pasted image 20250624190327.png]]
- No requirement to understand layer 3 o4 IP information
- All transaction completed at layer 2
- Layer 2 Switches works by examining the MAC Address of each PACKET that passes thru it

![[Pasted image 20250624190356.png]]

### 3 Network (Layer 3)
Managed or Layer 3 switches operate at both layers 2 & 3 of the OSI model
- perform layer 2 functions plus
	- static and dynamic ROUTING 
- This layer responsible for routing PACKETS across different networks
- uses LOGICAL ADDRESSING to ID source and destination of data packets

![[Pasted image 20250624191118.png]]
- IP (Internet Protocol) is most common set of rules contained in Layer 3
- IP is connectionless
	- communication between endpoints can occur without 1st ensuring either endpoint is available and ready to receive data
- higher level protocols required to manage this connection orientation
	- I.E. TCP or UDP which reside on Layer 4
- FRAGMENTATION 
	- Data segmented into packets 
- Send and destination IP Addresses added

### 4 Transport 
- TCP = Transmission Control Protocol
- UDP = User Datagram Protocol
- ensures complete data transmission and packet recovery, flow control, & data integrity 
- error free and in sequence
- TCP 
	- most common protocol that allows devices and applications to exchange messages over a network
	- underlying protocol for web servers and web sites, email applications, FTP, & peer-to-peer apps 
	- receiving site acknowledges receiving data
	- in correct order (1,2.3,...)
	- connection based protocol
	- requires ACK
	- slower
	- consumes more bandwidth
- UDP
	- sequential
	- time sensitive networks (TSN)
	- gaming, DNS lookups, AV over IP
	- datagrams sent in order
	- No ACK
	- loss of a couple of frames are bearable
	- connectionless
	- packets in order with NO ACK
	- less reliable but works quicker
	- choice for AVoIP, media streaming and other TSN
- SEGMENTING and REASSEMBLY
- ERROR CONTROL
- FLOW CONTROL
- PORT ADDRESSING
- TCP or USP
	- CONNECTION ORIENTED (TCP)
	- CONNECTIONLESS (UDP)

## Software Levels

### 5 Session
- manages connection and data flow
- establishes, maintains and terminated connections
- ensure data streams are properly synchronized
- SESSION
- SYNC
- DIALOG
- AUTHENTICATION/RECONNECTION

### 6 Presentation
- translates data for application and the network itself
- handles data encryption, compression, & translation
- ensure data from application layer is readable by the receiving application
- home of network security
- TRANSLATION
- ENCRYPTION
- COMPRESSION

### 7 Application
- handles interaction with applications
- closest layer to the end user
- common protocols are HTTP for web browsing
- FTP for file transfer
- DHCP for managing network addresses
- POP or SMTP for email applications
- Are resources available (I.E. a network?, bandwidth?)
- Sync's communication

![[Pasted image 20250624193816.png]]

Full Stack

![[Pasted image 20250624193917.png]]

## Encapsulation

 ![[Pasted image 20250624194136.png]]

![[Pasted image 20250624200553.png]]

![[Pasted image 20250624200857.png]]

Packet Switching
-  find best route

Routers use to provide additional network management functions instead of switches
- i.e. DHCP Server for IP Distribution
- common to disable on the switcher to let the router perform this function
- Routing tables
- communicate across networks
- common to have imbedded applications and wizards to take away the complexity of advanced switch configurations
- failover and load balancing

![[Pasted image 20250624201110.png]]


![[Pasted image 20250624201523.png]]

## Module 1 Takeaways

![[Pasted image 20250624201846.png]]





