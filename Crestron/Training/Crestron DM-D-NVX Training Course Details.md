# DMC Certified Designer - NVX Course

### **Part 1: Course Introduction & Housekeeping**

*   **Course Overview:** The session is the DMC-D-NVX Design class. The instructor clarifies that while it is an AV over IP design course, it is **not** a deep-dive networking class. The goal is to provide the necessary knowledge to effectively communicate design requirements with IT professionals.
*   **Class Logistics:**
    *   **Attendance:** Participants are reminded to ensure their Zoom display name matches their registered name for proper course credit.
    *   **Asking Questions:** Two methods are outlined: using the "Raise Hand" feature for verbal questions and using the dedicated **Q&A panel** for text-based questions, which is preferred over the general chat to prevent questions from getting lost.
    *   **Recording:** The session is not being recorded for public distribution due to regional privacy regulations.

### **Part 2: Crestron Support Resources**

The instructor provides a comprehensive walkthrough of the support resources available on the Crestron website, emphasizing their importance for both pre-sales design and post-sales technical issues.

*   **Crestron Training Institute (CTI) Portal:** This is the hub for all training-related activities. It allows users to browse learning paths for different products (like NVX), register for classes, and track their personal training progress, which follows the individual regardless of their employer.
*   **True Blue Support:**
    *   **Technical Support (Post-Sales):** For on-site commissioning, troubleshooting, and urgent issues with products already purchased. The instructor recommends calling or using live chat for immediate assistance.
    *   **Sales Support Services (Pre-Sales):** For design assistance, creating Bills of Materials (BOMs), interpreting redlines, and getting pre-sale product information.
*   **True Blue Community (Formerly Online Help):** This is the central knowledge base.
    *   **Content:** It contains FAQs, discussion forums, known issue tracking, technical documentation, and a glossary of terms. This is the same resource Crestron's internal support teams use.
    *   **Functionality:** Users can search for topics, subscribe to articles for updates, and track their support cases online.

### **Part 3: DM NVX® Product Line (AV over IP)**

This section provides a detailed breakdown of the DM NVX video and USB over IP product line.

*   **Core Concept:** DM NVX distributes digital audio, video, and USB over a standard 1-Gigabit Ethernet infrastructure.
*   **Common Features (All Hardware Endpoints):**
    *   Minimum support for 1080p60 4:4:4 video.
    *   Support for a secondary AES67 audio stream.
    *   Enterprise-grade security features.
*   **Product Categories:**
    *   **Hybrid Boxes:** Can be software-configured to function as either an encoder or a decoder.
    *   **Dedicated Boxes:** Function only as an encoder or only as a decoder, typically to meet a specific price point.
*   **Key NVX Models:**
    *   **DM-NVX-384 (Flagship):** A hybrid box that supports native **5K resolutions** (Ultrawide/Superwide), has a built-in 4x1 video switcher, and will support a **multi-view** feature (up to 6 streams) via a future firmware update.
    *   **DM-NVX-360/363 Series:** Hybrid boxes supporting 4K60 4:4:4. The 363 model adds **native Dante support** and audio down-mixing capabilities.
    *   **DM-NVX-E/D30 & E/D20 Series:** Dedicated encoders (E) and decoders (D). The 30 series supports 4K60 4:4:4, while the 20 series supports 4K60 4:2:0. They do not have built-in scaling or USB support.
    *   **DM-NVX-E20-2G:** The only true wall-plate style encoder in the NVX line.
    *   **DM-NVX-760:** A specialty encoder designed to integrate legacy DM® systems (DM 8G+®, HDBaseT) into a modern NVX network.

### **Part 4: DM NAX™ Product Line (Audio over IP)**

This segment covers the NAX line, which focuses on audio distribution over the network using the AES67 standard.

*   **Wall Plates (Edge Devices):** A series of input/output plates for various audio types:
    *   **NAX-BTIO:** Bluetooth audio.
    *   **NAX-XLR-I:** XLR input with phantom power.
    *   **NAX-USB-IO:** USB audio.
    *   **NAX-AUD-IO:** Balanced/unbalanced line-level audio.
*   **Preamps & Amplifiers:**
    *   **NAX-4ZSP / 8ZSA:** 4-zone and 8-zone streaming preamps/amplifiers that support services like AirPlay 2 and Spotify Connect, and feature "parallel zone" outputs (simultaneous speaker and streaming outputs).
    *   **AMP-X300:** The only NAX amplifier with **native Dante support** and the ability to drive 70/100-volt speaker systems.

### **Part 5: DM NUX™ Product Line (USB over IP)**

The final product deep-dive focuses on the NUX line for extending USB signals over the network.

*   **Core Components:** The system consists of **local** units (NUX-L2) that connect to the host PC and **remote** units (NUX-R2) that connect to peripherals.
*   **Key Features:**
    *   One local unit can support up to five remote units.
    *   NUX devices operate on **USB 2.0 (480 Mbps)** speed.
    *   They communicate via MAC address and do not take an IP address, meaning they are not managed through standard network tools like DM Tool.
*   **Important Distinction:** The NUX line is separate from the dedicated **USB-EXT-2** point-to-point extenders, which are the only products that support true **USB 3.0** speeds.

### Part 6: Networking Requirements

*   **Networking Requirements:** A managed, layer 3, gigabit switch with a non-blocking backplane is required for all endpoints. It needs to support IGMP snooping and have an IGMP querier. The instructor explains the differences between Unicast and Multicast communication, highlighting that content delivery is handled via Multicast (one-to-many), while device control uses Unicast (one-to-one).
*   **Network Ports & Connectivity:** The instructor details the network port configurations on the devices. Port 1 is the PoE port (1-Gigabit), the second copper port is also 1-Gigabit (non-PoE), and a third port, if present, is limited to 100 Mbps and is typically used for daisy-chaining or as a courtesy LAN port for non-video devices like a touch screen. The SFP port is 1-Gigabit, with its maximum distance depending on the fiber type used (e.g., 550m for OM3, ~6 miles for single-mode).
*   **NetGear Partnership:** The instructor explains that while Crestron supports any network switch that meets the minimum requirements, they have a partnership with NetGear. NetGear M4250 and M4350 series switches are specifically recommended because they have a simplified AV login and pre-configured profiles for DM NVX, making setup very straightforward. He mentions that NetGear offers a dedicated 1-day networking class for those who want to dive deeper.

### Part 7: Design exercises**.

*   **Exercise B: 8G+ Upgrade:** Students are tasked with upgrading an existing DM 8G+ system to an NVX system. The design must accommodate legacy DM wall plates and projectors that require scaling, while other displays do not.
*   **Exercise C: USB KVM System:** The next exercise involves designing a system with two PCs, a keyboard/mouse, and multiple interactive touch displays. The solution needs to handle both the video distribution and the USB KVM (Keyboard, Video, Mouse) functionality.
*   **Discussion on Design Solutions:** The instructor and students collaboratively discuss potential solutions for the exercises, highlighting the flexibility of using different NVX and NAX models (e.g., DM-NVX-360, DM-NAX-AUD-IO) to meet specific input/output and feature requirements.

### Part 8: DM NVX Management

*   **DM NVX Director:** This is an appliance that acts as a virtual matrix switcher, simplifying the management of large NVX systems. It's recommended for systems with 20-25 endpoints or more. The instructor demonstrates the web UI, showing how it can discover, configure, and update firmware for all connected NVX devices from a central location. It allows for the creation of domains (groups) and placeholder devices for future expansion.
*   **XIO Cloud:** The instructor explains that XIO Cloud is Crestron's cloud-based asset management service.
    *   **Functionality:** It allows for remote configuration, firmware updates, and monitoring of Crestron and some third-party devices. It features a free tier for basic management and a paid subscription for advanced features like metrics and remote control (screen scraping).
    *   **Security:** XIO Cloud is hosted on Microsoft Azure and uses HTTPS for secure communication. Devices on the local network reach out to the cloud; the cloud does not initiate connections into the local network.
    *   **Device Support:** A wide range of products are supported, including all NVX and NAX devices, touch screens, and even some third-party displays via a secure gateway.
