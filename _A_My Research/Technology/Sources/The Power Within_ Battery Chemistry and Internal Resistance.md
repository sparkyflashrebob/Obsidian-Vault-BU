---
tags:
  - notebooklm-import
notebook: "Technology"
category: "research"
---

Based on the provided source, internal resistance is a critical factor determining how a battery performs under load, particularly in high-drain devices like cameras or game controllers.

**What is Internal Resistance?**

Internal resistance is essentially the opposition to the flow of current inside the battery itself. When a device draws current from a battery, this resistance causes the voltage to drop. The higher the internal resistance, the significant the voltage drop when the device demands power.

**Why It Matters**

The source explains that a battery might show a healthy "open voltage" (e.g., 1.5V) when measured with a multimeter or used in a low-power device like a clock. However, when a high-drain device (like a camera trying to power a flash or autofocus) pulls a large burst of current, the internal resistance causes the voltage to plummet instantaneously.

If this voltage drops below the device's minimum operating threshold, the device will shut off, even if the battery still has plenty of chemical capacity remaining. This explains why a "fresh" cheap battery might fail to power a camera but work perfectly in a computer mouse.

**Impact by Battery Chemistry**

The source provides a clear comparison of how internal resistance varies across battery types and how it affects voltage under a 5-amp load:

* **Zinc-Carbon (R6):** These have very high internal resistance (~300 mΩ). Under a heavy load (5A), the voltage can collapse completely to **0.00 V**, making them useless for high-tech devices.
* **Alkaline (LR6):** These have moderate resistance (~120 mΩ). Under heavy load, the voltage might drop to **0.90 V**, which is often low enough to trigger a "low battery" shutdown.
* **NiMH Rechargeable (HR6):** These have very low resistance (~25 mΩ). Under the same heavy load, the voltage remains stable at **1.17 V**, keeping the device running.
* **Lithium (FR6):** These also have low resistance (~80 mΩ) and start at a higher voltage, maintaining a very stable **1.40 V** under load.

In summary, internal resistance explains why buying cheaper batteries (Zinc-Carbon or Alkaline) for high-performance electronics is often a waste of money—they cannot deliver the necessary current without the voltage crashing.