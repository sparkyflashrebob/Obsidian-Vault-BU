The OSI (Open Systems Interconnection) model is a conceptual framework that standardizes the functions of a telecommunication or computing system into seven distinct layers.1 Each layer performs specific functions to ensure data is transmitted effectively and efficiently across a network.2 Data flows down the layers on the sender's side and up the layers on the receiver's side.3

Here's a breakdown of the functions performed at each layer:

**7. Application Layer**

- **Function:** This is the layer closest to the end-user.4 It provides network services directly to end-user applications.5
    
- **Activities:**
    
    - Identifies communication partners (e.g., determining if another device has the required communication capability).6
        
    - Determines resource availability (e.g., checking for sufficient network resources for a data transfer).
        
    - Synchronizes communication.7
        
    - Provides services like file transfer, email, remote access, web Browse, and database access.8
        
- **Examples of Protocols:** HTTP, HTTPS, FTP, SMTP, DNS, POP3.9
    

**6. Presentation Layer**

- **Function:** This layer is responsible for the translation, encryption/decryption, and compression/decompression of data to ensure that data is presented in a format that the Application Layer can understand.10 It acts as a data translator.11
    
- **Activities:**
    
    - **Translation:** Converts data formats (e.g., ASCII to EBCDIC).12
        
    - **Encryption/Decryption:** Encrypts data for secure transmission and decrypts it upon reception.13
        
    - **Compression/Decompression:** Reduces the number of bits to be transmitted, improving efficiency.14
        
- **Examples of Formats/Protocols:** JPEG, MPEG, ASCII, EBCDIC, TLS/SSL (partially).
    

**5. Session Layer**

- **Function:** This layer establishes, manages, and terminates communication sessions between applications. It controls the dialogues between communicating processes.
    
- **Activities:**
    
    - **Session Establishment, Maintenance, and Termination:** Allows two processes to set up, use, and tear down a connection.15
        
    - **Synchronization:** Inserts checkpoints into the data stream, so if a session fails, it can be resumed from the last checkpoint rather than starting over.
        
    - **Dialog Control:** Determines which party transmits data at what time (e.g., full-duplex or half-duplex communication).16
        
    - **Authentication and Reconnection:** Manages user authentication and allows for re-establishing broken connections.
        
- **Examples of Protocols:** NetBIOS, RPC, Sockets, NFS, SMB.17
    

**4. Transport Layer**

- **Function:** This layer provides reliable and transparent transfer of data between end systems (end-to-end communication). It segments data from the Session Layer and reassembles it at the destination.
    
- **Activities:**
    
    - **Segmentation and Reassembly:** Breaks data into smaller segments for transmission and reassembles them at the receiving end.
        
    - **Error Control:** Ensures that data arrives without errors, duplicates, or loss, and requests retransmission of corrupted or missing segments.18
        
    - **Flow Control:** Manages the data transmission rate between a sender and receiver to prevent a fast sender from overwhelming a slow receiver.19
        
    - **Service-point Addressing (Port Addressing):** Uses port numbers to identify which application process data should be delivered to.
        
    - **Connection-oriented vs. Connectionless Communication:** Provides both reliable (e.g., TCP) and unreliable (e.g., UDP) data transfer services.
        
- **Examples of Protocols:** TCP (Transmission Control Protocol), UDP (User Datagram Protocol).
    

**3. Network Layer**

- **Function:** This layer is responsible for logical addressing, routing, and forwarding of data packets across different networks (inter-network communication).
    
- **Activities:**
    
    - **Logical Addressing:** Assigns unique logical addresses (e.g., IP addresses) to devices to identify them on the network.
        
    - **Routing:** Determines the best path for data packets to travel from the source to the destination across interconnected networks.
        
    - **Packetizing:** Encapsulates segments from the Transport Layer into packets.
        
    - **Fragmentation:** Divides large packets into smaller ones if necessary for transmission across certain network links.20
        
- **Examples of Protocols:** IP (Internet Protocol), ICMP (Internet Control Message Protocol), OSPF, RIP.
    

**2. Data Link Layer**

- **Function:** This layer provides node-to-node data transfer and handles framing, physical addressing, error detection, and flow control within a local network segment. It ensures error-free transmission over the physical link.
    
- **Activities:**
    
    - **Framing:** Divides data packets from the Network Layer into frames for transmission.
        
    - **Physical Addressing (MAC Addressing):** Adds physical (MAC) addresses to frames to identify the source and destination devices on the local network.
        
    - **Error Control:** Detects and potentially corrects errors that may occur during transmission over the physical medium.21
        
    - **Flow Control:** Regulates the rate of data flow between two directly connected devices.22
        
    - **Media Access Control (MAC):** Manages access to the shared physical medium.23
        
- **Examples of Protocols:** Ethernet, PPP (Point-to-Point Protocol), Frame Relay.24
    

**1. Physical Layer**

- **Function:** This is the lowest layer of the OSI model and deals with the physical characteristics of the network, including the electrical, mechanical, procedural, and functional specifications for activating, maintaining, and deactivating the physical link between devices.
    
- **Activities:**
    
    - **Bit Transmission:** Transmits raw bit streams (1s and 0s) over the physical medium (e.g., electrical signals, light pulses, radio waves).
        
    - **Hardware Specifications:** Defines cabling types, connectors, voltage levels, data rates, and transmission distances.
        
    - **Topology:** Specifies how devices are physically arranged in a network (e.g., bus, star, ring).
        
    - **Bit Synchronization:** Ensures that the sender and receiver's clocks are synchronized for accurate data transmission.25
        
    - **Transmission Mode:** Defines how data flows (simplex, half-duplex, full-duplex).26
        
- **Examples of Hardware:** Cables (Ethernet, fiber optic), hubs, repeaters, network interface cards (NICs), modems.
