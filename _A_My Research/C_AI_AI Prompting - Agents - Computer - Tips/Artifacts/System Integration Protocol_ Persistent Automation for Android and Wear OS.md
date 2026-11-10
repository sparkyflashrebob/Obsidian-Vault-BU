### System Integration Protocol: Persistent Automation for Android and Wear OS
To achieve high-reliability automation between a smartphone and a wearable device, an architect must look beyond basic application installation and address the aggressive nature of Android’s native power management. These system-level "optimizations" prioritize short-term energy savings by grouping alarms and terminating background processes, which inevitably leads to missed "Time contexts" and killed services. For frameworks like Tasker and AutoWear, establishing a stable environment requires a strategic bypass of these kernel-level restrictions to ensure the automation handshake remains persistent and uninterrupted.
##### 1. Architectural Foundation: OEM Power Management Mitigation
The primary technical hurdle in professional automation is the Android kernel's tendency to prune background tasks to extend battery life. When these measures are active, Tasker cannot receive the signals required to trigger profiles, resulting in a silent breakdown of the entire logic chain. System-level whitelisting is the mandatory first step in ensuring process survival.
###### 1.1. Device-Specific Configuration Matrix
The following matrix details the specific navigation paths and actions required to mitigate optimization across major OEM environments.
| Device Environment | Navigation Path | Required Action |
| ------ | ------ | ------ |
| **Vanilla Android (6.0+)** | Settings > Apps > Cog Icon (top-right) > Battery optimization | Select "All apps," find Tasker, and select  **"Don't optimize."** |
| **Samsung (5.1.1+)** | Smart Manager App > Battery > App optimisation > DETAIL | Locate Tasker and AutoWear; adjust settings to  **disable optimization.** |
| **MIUI 7** | Settings > Additional settings > Battery & performance > Manage apps battery usage | Set terminal toggle to  **OFF.** |

###### 1.2. Impact Analysis of Persistent Services
Simple background execution is insufficient for the Tasker-AutoWear ecosystem. Without explicit whitelisting, the "handshake" between the handset (the logic engine) and the wearable (the interface) fails. If the phone terminates the Tasker monitor or the AutoWear plugin, the watch becomes a disconnected peripheral, unable to update complications or respond to hardware triggers. Whitelisting ensures the phone remains a reliable host for the wearable’s operational logic.
###### 1.3. Concluding Summary
These system-level changes provide the necessary substrate for internal app configurations. By shielding these processes from the OS lifecycle manager, you create a stable environment where internal preferences can effectively demand the resources they require.
##### 2. Tasker Core Service Optimization
System-level whitelisting establishes the environment, but Tasker must be internally configured to demand persistent resources from the kernel. These internal preferences dictate how Tasker manages task scheduling and service priority.
###### 2.1. Critical Foreground and Alarm Preferences
To prevent the system from deprioritizing the automation monitor, adjust the following preferences:
1.  **Run In Foreground:**  Ensure this is  **checked**  (Menu > Prefs > Monitor > General). This creates a persistent notification that signals the system the service is vital.
2.  **Use Reliable Alarms:**  This must be set to  **"Always"**  or  **"When Off"**  (Menu > Prefs > Monitor > General).
    *   **Always / When Off:**  These selections force the system to wake the device for time-based triggers, ensuring precision.
    *   **Never:**  This setting allows Android to "batch" or delay alarms to save power, which frequently leads to the system killing Tasker during deep sleep.
###### 2.2. Battery Persistence Benchmarking (Samsung S24 Focus)
On the Samsung S24, native power management is notoriously aggressive. It is a non-negotiable requirement to navigate to the S24 App Settings for both Tasker and AutoWear and toggle  **"Allow Background Activity"**  to the ON position. Failure to do so is the primary cause of "Timeout" errors in the AutoWear plugin, as the system will periodically sever the background sync required to push data to watch complications.
###### 2.3. Transition
Once the phone is hardened against resource reclamation, it can function as a reliable bridge for pushing commands into the more restricted Wear OS environment.
##### 3. Wear OS & AutoWear Permission Framework
Modern wearable environments, specifically Wear OS 4+ and One UI 8.0, have moved away from native on-watch permission menus. This shift necessitates the use of ADB-based configurations to grant permissions that are no longer accessible via the system UI.
###### 3.1. The System Overlay (Draw Over Other Apps) Protocol
The "Draw Over Other Apps" permission is required for AutoWear to render custom UI elements. Since Samsung has removed the native toggle from the watch's system screens, follow this protocol:
1. Open the  **"Tasker Settings"**  app on the watch to trigger the permission request.
2. If the watch displays a "Permission Needed" screen, ensure ADB Debugging and Wireless Debugging are enabled in Developer Options.
3.  **Manual ADB Override:**  If the watch returns a "Can't connect to ADB WiFi" error, you must grant the permission from a PC using the following syntax: adb -s <watch_ip> shell pm grant com.joaomgcd.autowear android.permission.SYSTEM_ALERT_WINDOW
###### 3.2. Accessibility and Physical Button Remapping
Physical buttons can be remapped by monitoring system-level state changes rather than direct keyevents.
*   **The Triple Press Workaround:**  On the watch, navigate to Settings > Accessibility > Advanced > Triple press and select  **"Mute all."**
*   **Logic Routing:**  In AutoWear, create a monitor for the system setting all_sound_off.
*   **Command Filter Syntax:**  In Tasker, set the AutoWear Event Profile to use a Command Filter with the prefix=:= syntax (e.g., all_sound_off=:=) to listen for the toggle and execute the associated task.
###### 3.3. Evaluative Impact of Permission Tiers
Missing permissions result in silent failures that are difficult to debug:
*   **Physical Activity:**  If missing, AutoWear will return null or empty values for heart rate and step count data.
*   **Accessibility:**  If disabled, the watch cannot intercept the all_sound_off toggle or interact with the system UI, leaving complications unresponsive.
###### 3.4. Transition
Maintaining this permission-heavy environment requires a robust network handshake to facilitate the transfer of logic between the PC, phone, and watch.
##### 4. Cross-Device Handshake: ADB, Intents, and Connectivity
Professional deployments rely on a stable, wireless handshake between devices to manage configuration and logic injection without physical tethering.
###### 4.1. ADB WiFi and Wireless Debugging Setup
To maintain the connection between a Windows PC and a Samsung S24, use the following checklist:
*  [ ] Toggle  **Wireless Debugging**  to "On" in the S24 Developer Options.
*  [ ] Pair the PC using the specific  **port pairing numbers**  provided on the S24 screen.
*  [ ] Maintain an active ADB link to facilitate logic transfers (e.g., via Antigravity).
###### 4.2. Android Intent Routing for Logic Injection
For injecting logic from a PC to the handset, use the am broadcast command. This verifies the phone's ability to receive the trigger before complicating the chain with the watch.
*   **Command Syntax:**  adb shell am broadcast -a com.tasker.ACTION_NAME --es "data_key" "data_value"
*  Tasker must be configured with an "Intent Received" profile listening for com.tasker.ACTION_NAME.
###### 4.3. Strategic Importance of Routing
When updating the Galaxy Watch 7, utilize  **"Command to Execute"**  strings within the AutoWear plugin. This direct routing method is superior to native app interface links, which often fail to resolve or time out on Wear OS 4+ due to tightened security protocols.
###### 4.4. Transition
Even with perfect routing, architects must account for specific technical roadblocks inherent to the latest Wear OS versions.
##### 5. Diagnostic Protocol and Platform Limitations
###### 5.1. Wear OS 6 / One UI 8.0 Tap Event Interception
**LIMITATION:**  A critical platform-level bug in Wear OS 6.0/One UI 8.0 causes the native  **Watch Face Framework**  (DWF:GestureDetector) to intercept tap events before they reach the AutoWear or WatchMaker layer. This effectively disables all interactive tap actions on custom watch faces. No user-level workaround currently exists for this system-level conflict.
###### 5.2. Reliability Troubleshooting for Complications
When complications return "Timeout" errors or empty messages, apply these protocols:
*   **Execute Now:**  Ensure the "Execute Now" flag is set to  **true**  in the AutoWear App configuration.
*   **Action Repetition (3x):**  For unreliable sensors like heart rate, configure the Tasker task to repeat the action up to three times.
*   **Nuanced Data Check:**  Note that %errmsg may occasionally report "timeout" even if %awmessage contains valid data.  **Always check the contents of**  **%awmessage**  before discarding the result of a timed-out request.
###### 5.3. Log Analysis for Error Correction
Analyze Tasker logs to distinguish between the two primary failure states:
*   **Logic Errors:**  These appear as crashes or malformed commands within the task itself (check variable syntax).
*   **System Kills:**  These are characterized by the OS terminating the service, signaling a failure in the "Run in Foreground" or "Allow Background Activity" settings.
###### 5.4. Final Summary
Persistent automation is a state of ongoing mitigation. As Android and Wear OS systems evolve, the stability of the handshake depends entirely on the architect's ability to maintain these power management bypasses and ADB-level permissions.
