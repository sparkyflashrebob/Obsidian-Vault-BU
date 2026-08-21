6/24/2025

### Overview

In this one-day, interactive online course, you will learn how to design Crestron AV-over-IP solutions, including DM NVX® AV-over-IP and DM NAX® audio-over-IP technology.

Through discussions and group exercises, participants will enhance their technical understanding of designing Crestron AVoIP solutions. The course culminates in a comprehensive design exercise covering audio, video, and USB delivery over the network.

**After completing this course, the student will be able to:**

- Evaluate the advantages of Crestron AVoIP
- Identify Crestron AVoIP solutions
- Navigate Crestron online design resources
- Utilize PoE and verify specifications
- Interpret common IT terminology and AVoIP network delivery
- Determine how to securely deliver AVoIP over a network
- Design Crestron AVoIP solutions around industry-specific scenarios
- Recognize when to use DM NVX Director® and how it has evolved
- Leverage XiO Cloud® to manage Crestron AVoIP solutions remotely

See PPT Presentation
file:///C:/Users/SparkyDesktop/Desktop/NVX%20Course/DMC-D-NVX%20Student%20PPT%20Rev%201.2.pdf

Erwin Monteyro - Dana Gibson

Switching is what gets confusing

2017 NVX

Same concerns as back then as now. 

Switches you don't need to do a lot of configuring via profile. 

What you need to know to converse with the IT folks. 

Agenda: 
- Introduction 
- Crestron Support 
- Crestron AVoIP Products 
- Network Requirements 
- Design Exercises Crestron AVoIP Endpoint Management


# Introduction

A digital audio, video, and USB distribution system that leverages a standard 1-Gigabit Ethernet infrastructure.
They do not do more than 1Gb currently
NV-384 5K @ 1Gb
also does multiview
scalable - no fixed switches - just need proper network support
audio video usb
interop with other Crestron products
3rd party ?  AES67 Dante
less than 1% fail rate apparently
# Crestron Support
### Learning Path Courses

[DM Certified Designer – DM NVX® (DMC-D-NVX)](https://trainingapps.crestron.com/CourseDetail/1607)  

### Optional Courses

[CTI-AVoIP-Design](https://trainingapps.crestron.com/CourseDetail/1605)

[Crestron® Technology and Netgear® AV Network Switches](https://trainingapps.crestron.com/OnlineCourse/10087) 

[Network Fundamentals for AV over IP presented by NETGEAR®](https://trainingapps.crestron.com/CourseDetail/1016)


https://trainingapps.crestron.com/Dashboard?categorygroupid=4

## True Blue Support

https://www.crestron.com/Support

https://www.crestron.com/support/tools

https://community.crestron.com/s/


# Crestron AVoIP Products

Crestron DM NVX® Products DM NVX® Endpoints Common Features: 
▪ 1080p60, 4:4:4 
▪ HDCP 1.4 
▪ Secondary 2-channel AES67 audio stream 
▪ Enterprise-grade security DM NVX® 

Resolution Support: 
▪ The DM-NVX-384 supports up to 5K 4:4:4 with scaling 
▪ ”36x” products support up to 4K60 4:4:4 with scaling 
▪ Products that end in “30” support up to 4K60 4:4:4, no scaling 
▪ Products that end in “20” support up to 4K60 4:2:0, no scaling


Hybrid Boxes
Encoder or Receiver

Dedicated Boxes
only encoders or decoders

NV-384
can do 5K
![[Pasted image 20250624082318.png]]

Has multi-inputs switch
4x1
2 HDMI
DP Alt

Decoder
5x1 add stream

USBC is actually USB 2.0
USB 3/4/5 more than that

bandwidth is the issue
has a 1G SFP

Not with this product
10G switch enables more high bandwidth options
each NIC 

## Limitations
mulitmode
video wall
384 encoder and 384 decoder
generate multiview stream
or 5K

![[Pasted image 20250624083606.png]]

NVX-363 has Dante
NVX-360 same as 363 but with no dante or downmixing
Hybrid units have scaling

E30 or D30 has no usb
![[Pasted image 20250624084401.png]]

D/E20 will 4k 4:2:0

![[Pasted image 20250624084328.png]]


### Specialty Products
E760
DM input 
card formfactor and surface 
allows for wall plate input

Decoder with scaler id NVX-D200

Only 1 wall plate
NVX-E20-2G

DM-NVX-SW-C310 
software
uses a dedicated computer
no HDCP

![[Pasted image 20250624085055.png]]

![[Pasted image 20250624085208.png]]



Class Exercise 
Answer the following DM NVX® questions: 
1. What DM NVX® product supports 5K resolutions? 384
2. What DM NVX® product supports DM-8G+® and DM® Essentials inputs? E760
3. What DM NVX® products have native Dante® audio support? 363
4. What is the maximum resolution and colorspace support for the DM-NVX-D20? 4k60 4:2:0 or 30Hz 4:4:4

## NAX

DM NAX® Products 
DM NAX® Endpoints Common Features: 
Wall Plates: 
▪ Encoder/Decoder 
▪ Mixer (Commercial mode) 
▪ Source selection (Residential mode) 
▪ PoE® 
▪ Enterprise-grade security 

Preamplifier and Amplifiers: 
▪ Dual LAN Ports 
▪ DSP 
▪ Enterprise-grade security


wall plates can encode or decode

DM-NAX_AUD-IO
balun

XLR version
output behind
they make a pass-thru plate

![[Pasted image 20250624091152.png]]
also has I/O
![[Pasted image 20250624091439.png]]

not bluetooth output
not receive BT
BT 5.2

![[Pasted image 20250624091644.png]]

## PREAMPS

![[Pasted image 20250624091949.png]]

Streaming and Casting

![[Pasted image 20250624092127.png]]

input box

## Amplifiers

![[Pasted image 20250624092227.png]]

output as speaker and as a stream
thsi more rezi

![[Pasted image 20250624092619.png]]
Class B

![[Pasted image 20250624092730.png]]

also supports Dante natively

## Specialty

![[Pasted image 20250624093010.png]]

eARC only unit that is supported DM-NAX-XSP
384 future

## Speaker

![[Pasted image 20250624093239.png]]

PoE+
AES67 w/ DSP

has a passive companion

up to 3 passive speakers

25W distributed

![[Pasted image 20250624093449.png]]


![[Pasted image 20250624093650.png]]


Class Exercise Answer the following DM NAX® questions: 
1. Which DM NAX® amplifier supports both Lo-Z and Hi-Z operation? x300
2. What DM NAX® product supports eARC? 
3. Name a DM NAX® product that has built-in music streaming services. 4
4. Which DM NAX® endpoint has native support for Bluetooth® audio? btio


## USB

![[Pasted image 20250624094237.png]]

L2 and R2

![[Pasted image 20250624094800.png]]

Notable - The DM-NUX boxes do _not_ show up in DM-Tool, and the routing is based on the serial number from the sticker on top of the boxes - so record those numbers before your guys install them inaccessibly or it'll cost you (time)

Layer 2 devices for discovery
not PoE

![[Pasted image 20250624095416.png]]

Class Exercise 
Answer the following DM NUX questions: 
1. What DM NUX wall plate product supports up to 4 USB input devices?  R
2. True or False – DM NUX endpoints are interoperable with DM NVX® endpoints. YES
3. What is the maximum data rate that DM NUX devices support? USB 2
4. How many DM-NUX-R2-1G does a single DM-NUX-L2-1G support? 5r to a single L

# Network

Connectivity and distance

![[Pasted image 20250624110602.png]]

audio for 2ndarcy audio
daisy chaining

ports configurable with web utility

Same with NAX
not daisy chaining

## Multicast

Control & Content Delivery
TCP and UDP
Control - Unicast/TCP 1-1
Content Multicast/broadcast 1-many

![[Pasted image 20250624111326.png]]

Can flood network
Zoom = multicast

Manage???

AVOIP Requirements
- Manged switch

![[Pasted image 20250624111905.png]]
![[Pasted image 20250624111920.png]]

IGMP is on Layer 3, v2 minimum 
IP Address Management
Non-blocking backplane (full-duplex)
Fast Leave - allow to leave quickly
Snooping Enabled
querier enabled (only 1)


IGMP v2
IGMPv3 (Internet Group Management Protocol version 3) is a network-layer protocol used by IPv4 devices to manage multicast group memberships. It ==enhances IGMPv2 by adding support for source filtering, allowing hosts to specify which sources they want to receive traffic from within a multicast group==. This feature is crucial for [Source-Specific Multicast](https://www.google.com/search?rlz=1C1RXQR_enUS1066US1066&cs=1&sca_esv=ccb8066356fd07b7&sxsrf=AE3TifPIViUL7AIZmZq25lvJVCZ4ZTx7tA%3A1750789354526&q=Source-Specific+Multicast&sa=X&ved=2ahUKEwiy-fLL1oqOAxXpOjQIHaPiBAYQxccNegQIBhAB&mstk=AUtExfBQqwWaOx-3Z1C_pCp1g9o1Fz0gNj4Au8kVUhL3_LqglIV0LkcCvdl4143m8EVBMnrasKpJiiB8qApCCWVLC1uy6GOQlY1jsWq-2BzWYFpZD4rKsE44kvRbQYx1JJGJl-LNMznvUaGrVmE57gd-_wYfI87U9mZfSvvBkZRvrVmdBa0&csui=3) (SSM) and helps optimize network resources by preventing unwanted traffic from being delivered. 

Key features of IGMPv3:

- **Source Filtering:**
    
    IGMPv3 allows hosts to express interest in receiving traffic from specific sources within a multicast group, using [INCLUDE](https://www.google.com/search?rlz=1C1RXQR_enUS1066US1066&cs=1&sca_esv=ccb8066356fd07b7&sxsrf=AE3TifPIViUL7AIZmZq25lvJVCZ4ZTx7tA%3A1750789354526&q=INCLUDE&sa=X&ved=2ahUKEwiy-fLL1oqOAxXpOjQIHaPiBAYQxccNegQIMhAB&mstk=AUtExfBQqwWaOx-3Z1C_pCp1g9o1Fz0gNj4Au8kVUhL3_LqglIV0LkcCvdl4143m8EVBMnrasKpJiiB8qApCCWVLC1uy6GOQlY1jsWq-2BzWYFpZD4rKsE44kvRbQYx1JJGJl-LNMznvUaGrVmE57gd-_wYfI87U9mZfSvvBkZRvrVmdBa0&csui=3) and [EXCLUDE](https://www.google.com/search?rlz=1C1RXQR_enUS1066US1066&cs=1&sca_esv=ccb8066356fd07b7&sxsrf=AE3TifPIViUL7AIZmZq25lvJVCZ4ZTx7tA%3A1750789354526&q=EXCLUDE&sa=X&ved=2ahUKEwiy-fLL1oqOAxXpOjQIHaPiBAYQxccNegQIMhAC&mstk=AUtExfBQqwWaOx-3Z1C_pCp1g9o1Fz0gNj4Au8kVUhL3_LqglIV0LkcCvdl4143m8EVBMnrasKpJiiB8qApCCWVLC1uy6GOQlY1jsWq-2BzWYFpZD4rKsE44kvRbQYx1JJGJl-LNMznvUaGrVmE57gd-_wYfI87U9mZfSvvBkZRvrVmdBa0&csui=3) modes. 
    
    - **INCLUDE mode:** A host explicitly lists the sources it wants to receive traffic from. 
    - **EXCLUDE mode:** A host lists the sources it doesn't want to receive traffic from, effectively receiving from all other sources. 
    
- **Support for SSM:**
    
    IGMPv3 is a requirement for Source-Specific Multicast (SSM), where receivers explicitly request traffic from a particular source. 
    
- **Enhanced Leave Latency:**
    
    While IGMPv2 improved leave latency compared to IGMPv1, IGMPv3 further optimizes this by allowing hosts to specify sources they are no longer interested in, reducing the time it takes for multicast routers to stop forwarding traffic from those sources. 
    
- **Robustness Variable:**
    
    IGMPv3 includes a robustness variable that allows for more flexible configuration of timer values for query intervals, response intervals, and other related parameters. 
    
- **[Basic IGMPv3 Snooping Support](https://www.google.com/search?rlz=1C1RXQR_enUS1066US1066&cs=1&sca_esv=ccb8066356fd07b7&sxsrf=AE3TifPIViUL7AIZmZq25lvJVCZ4ZTx7tA%3A1750789354526&q=Basic+IGMPv3+Snooping+Support&sa=X&ved=2ahUKEwiy-fLL1oqOAxXpOjQIHaPiBAYQxccNegQIFRAB&mstk=AUtExfBQqwWaOx-3Z1C_pCp1g9o1Fz0gNj4Au8kVUhL3_LqglIV0LkcCvdl4143m8EVBMnrasKpJiiB8qApCCWVLC1uy6GOQlY1jsWq-2BzWYFpZD4rKsE44kvRbQYx1JJGJl-LNMznvUaGrVmE57gd-_wYfI87U9mZfSvvBkZRvrVmdBa0&csui=3) (BISS):**
    
    IGMPv3 switches with BISS support help optimize multicast traffic forwarding by learning group memberships and only forwarding traffic to the necessary ports. 
    
- **Link-Local Address:**
    
    IGMPv3 uses the link-local address `224.0.0.22` as the destination address for membership reports, ensuring that all IGMPv3-capable devices listen to this address. 
    
- **No Report Suppression:**
    
    Unlike IGMPv2, IGMPv3 hosts always send membership reports upon receiving an IGMP query. 
    

RFCs:

- IGMPv3 is defined in [RFC 3376](https://www.google.com/search?rlz=1C1RXQR_enUS1066US1066&cs=1&sca_esv=ccb8066356fd07b7&sxsrf=AE3TifPIViUL7AIZmZq25lvJVCZ4ZTx7tA%3A1750789354526&q=RFC+3376&sa=X&ved=2ahUKEwiy-fLL1oqOAxXpOjQIHaPiBAYQxccNegQITBAB&mstk=AUtExfBQqwWaOx-3Z1C_pCp1g9o1Fz0gNj4Au8kVUhL3_LqglIV0LkcCvdl4143m8EVBMnrasKpJiiB8qApCCWVLC1uy6GOQlY1jsWq-2BzWYFpZD4rKsE44kvRbQYx1JJGJl-LNMznvUaGrVmE57gd-_wYfI87U9mZfSvvBkZRvrVmdBa0&csui=3). 
- A related document, RFC 4604, discusses the use of IGMPv3 and [MLDv2](https://www.google.com/search?rlz=1C1RXQR_enUS1066US1066&cs=1&sca_esv=ccb8066356fd07b7&sxsrf=AE3TifPIViUL7AIZmZq25lvJVCZ4ZTx7tA%3A1750789354526&q=MLDv2&sa=X&ved=2ahUKEwiy-fLL1oqOAxXpOjQIHaPiBAYQxccNegQISRAB&mstk=AUtExfBQqwWaOx-3Z1C_pCp1g9o1Fz0gNj4Au8kVUhL3_LqglIV0LkcCvdl4143m8EVBMnrasKpJiiB8qApCCWVLC1uy6GOQlY1jsWq-2BzWYFpZD4rKsE44kvRbQYx1JJGJl-LNMznvUaGrVmE57gd-_wYfI87U9mZfSvvBkZRvrVmdBa0&csui=3) (Multicast Listener Discovery version 2) for Source-Specific Multicast. 
- **[RFC 5790](https://www.google.com/search?rlz=1C1RXQR_enUS1066US1066&cs=1&sca_esv=ccb8066356fd07b7&sxsrf=AE3TifPIViUL7AIZmZq25lvJVCZ4ZTx7tA%3A1750789354526&q=RFC+5790&sa=X&ved=2ahUKEwiy-fLL1oqOAxXpOjQIHaPiBAYQxccNegQIQhAB&mstk=AUtExfBQqwWaOx-3Z1C_pCp1g9o1Fz0gNj4Au8kVUhL3_LqglIV0LkcCvdl4143m8EVBMnrasKpJiiB8qApCCWVLC1uy6GOQlY1jsWq-2BzWYFpZD4rKsE44kvRbQYx1JJGJl-LNMznvUaGrVmE57gd-_wYfI87U9mZfSvvBkZRvrVmdBa0&csui=3)**: defines a lightweight version of IGMPv3 and MLDv2. 
- **[RFC 9776](https://www.google.com/search?rlz=1C1RXQR_enUS1066US1066&cs=1&sca_esv=ccb8066356fd07b7&sxsrf=AE3TifPIViUL7AIZmZq25lvJVCZ4ZTx7tA%3A1750789354526&q=RFC+9776&sa=X&ved=2ahUKEwiy-fLL1oqOAxXpOjQIHaPiBAYQxccNegQIQRAB&mstk=AUtExfBQqwWaOx-3Z1C_pCp1g9o1Fz0gNj4Au8kVUhL3_LqglIV0LkcCvdl4143m8EVBMnrasKpJiiB8qApCCWVLC1uy6GOQlY1jsWq-2BzWYFpZD4rKsE44kvRbQYx1JJGJl-LNMznvUaGrVmE57gd-_wYfI87U9mZfSvvBkZRvrVmdBa0&csui=3)**: defines IGMPv3.
- 




## Bandwidth

![[Pasted image 20250624113418.png]]

Crestron best practice is CONSTANT

![[Pasted image 20250624113621.png]]

![[Pasted image 20250624113820.png]]

Can aggregate links
LAG

1GB is bi-directional
![[Pasted image 20250624114355.png]]
not work but not typical - camera in other direction

AES each stream 6Mbps Dante 4-channel in (1) dante channel

![[Pasted image 20250624114457.png]]

## Network Topologies

Point to Point
Daisy chain 
Star
Tree

![[Pasted image 20250624114827.png]]
common for VLAN
if different VLANS's
needs to be configured at the core
PIM


IP Addresses
![[Pasted image 20250624115259.png]]

![[Pasted image 20250624120603.png]]

![[Pasted image 20250624120622.png]]

NVC
- At least 2 address
-  1 control TCP
-  Dante additional
- audio/video primary 
- AES67 needs an address
On NAX
- multicast address for each zone


# Design Exercise
 #1 
(3) DM plates connect to NVX-E760  384 for the table maybe
(4) AV sources use NVX-E30
(4) NVX-360 for Projectors
(4) NVX-D30 for displays
would need a CP4

![[Pasted image 20250624123416.png]]

![[Pasted image 20250624124126.png]]
![[Pasted image 20250624124142.png]]

Exercise B:
speakers are 8 ohm
4 stereo
- (1) DM-NAX-8ZSA
Sources
SAT Radio 
BT 
 - (1)DM-NAX-BTIO-1G
 - (1) DM-NAX-8ZSA


![[Pasted image 20250624130118.png]]

Turntable in a separate room

## Security

![[Pasted image 20250624130421.png]]

NAX are not JIT secure
No NUX either

Content uses AES Encryption
802.1x uses certificates
SSL-based secure CIP - communication to the box is secure

(2) DM_NVX-360 for projectors

D30 has no USB

## DM NVX Director

![[Pasted image 20250624132150.png]]

Endpoint is managing subscriptions

Programmers not really need Director
Typical to have 20- 25 devices put a Director???
NVX tool can do Firmware updates

3 sizes


## XIO Cloud

![[Pasted image 20250624135205.png]]




































`































