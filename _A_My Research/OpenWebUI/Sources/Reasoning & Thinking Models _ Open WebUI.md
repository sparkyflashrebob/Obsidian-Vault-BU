---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Reasoning & Thinking Models / Open WebUI
[Skip to main content](https://docs.openwebui.com/features/chat-conversations/chat-features/reasoning-models#__docusaurus_skipToContent_fallback)
[Open WebUI](https://docs.openwebui.com/) [Blog](https://openwebui.com/blog)
[GitHub](https://github.com/open-webui/open-webui) [Discord](https://discord.com/invite/5rJgQTnV4s)

```

```

[Open WebUI](https://docs.openwebui.com/)
\* [Blog](https://openwebui.com/blog)
\* [GitHub](https://github.com/open-webui/open-webui)
\* [Discord](https://discord.com/invite/5rJgQTnV4s)
← Back to main menu
\* [🏡 Home](https://docs.openwebui.com/)
\* [🚀 Getting Started](https://docs.openwebui.com/getting-started/)
\* [📖 Reference](https://docs.openwebui.com/reference/)
\* [⭐ Features](https://docs.openwebui.com/features/)
\* [🔐 Authentication & Access](https://docs.openwebui.com/features/authentication-access/)
\* [🔧 Administration](https://docs.openwebui.com/features/administration/)
\* [💬 Chat & Conversations](https://docs.openwebui.com/features/chat-conversations/chat-features/reasoning-models)
\* [Chat Features](https://docs.openwebui.com/features/chat-conversations/chat-features/)
\* [Code Execution](https://docs.openwebui.com/features/chat-conversations/chat-features/code-execution/)
\* [Multi-Model Chats](https://docs.openwebui.com/features/chat-conversations/chat-features/multi-model-chats)
\* [Chat Sharing](https://docs.openwebui.com/features/chat-conversations/chat-features/chatshare)
\* [Folders & Projects](https://docs.openwebui.com/features/chat-conversations/chat-features/conversation-organization)
\* [Autocomplete](https://docs.openwebui.com/features/chat-conversations/chat-features/autocomplete)
\* [Chat Parameters](https://docs.openwebui.com/features/chat-conversations/chat-features/chat-params)
\* [URL Parameters](https://docs.openwebui.com/features/chat-conversations/chat-features/url-params)
\* [Follow-Up Prompts](https://docs.openwebui.com/features/chat-conversations/chat-features/follow-up-prompts)
\* [History & Search](https://docs.openwebui.com/features/chat-conversations/chat-features/history-search)
\* [Message Queue](https://docs.openwebui.com/features/chat-conversations/chat-features/message-queue)
\* [Reasoning & Thinking Models](https://docs.openwebui.com/features/chat-conversations/chat-features/reasoning-models)
\* [Temporal Awareness](https://docs.openwebui.com/features/chat-conversations/chat-features/temporal-awareness)
\* [Retrieval Augmented Generation (RAG)](https://docs.openwebui.com/features/chat-conversations/rag/)
\* [Data Controls](https://docs.openwebui.com/features/chat-conversations/data-controls/)
\* [Create & Edit Images](https://docs.openwebui.com/features/chat-conversations/image-generation-and-editing)
\* [Speech-to-Text & Text-to-Speech](https://docs.openwebui.com/features/chat-conversations/audio)
\* [Web Search](https://docs.openwebui.com/category/web-search)
\* [Memory & Personalization](https://docs.openwebui.com/features/chat-conversations/memory)
\* [Direct Connections](https://docs.openwebui.com/features/chat-conversations/direct-connections)
\* [🧠 Workspace](https://docs.openwebui.com/features/chat-conversations/chat-features/reasoning-models)
\* [📝 Notes](https://docs.openwebui.com/features/notes/)
\* [📢 Channels](https://docs.openwebui.com/features/channels/)
\* [💻 Open Terminal](https://docs.openwebui.com/features/open-terminal/)
\* [🔌 Plugins & Extensibility](https://docs.openwebui.com/features/extensibility/)
\* [🛠 Troubleshooting](https://docs.openwebui.com/troubleshooting/)
\* [🏢 Open WebUI for Enterprise](https://docs.openwebui.com/enterprise/)
\* [🎓 Tutorials](https://docs.openwebui.com/tutorials/)
\* [❓ FAQ](https://docs.openwebui.com/faq)
\* [🛣 Roadmap](https://docs.openwebui.com/roadmap)
\* [🛡 Security Policy](https://docs.openwebui.com/security)
\* [🤝 Contributing](https://docs.openwebui.com/contributing)
\* [💖 Sponsorships](https://docs.openwebui.com/sponsorships)
\* [🎨 Brand Guidelines](https://docs.openwebui.com/brand)
\* [⚖ Open WebUI License](https://docs.openwebui.com/license)
\* [🎯 Our Mission](https://docs.openwebui.com/mission)
\* [👥 Our Team](https://docs.openwebui.com/team)
\* [⭐ Features](https://docs.openwebui.com/features/)
\* 💬 Chat & Conversations
\* [Chat Features](https://docs.openwebui.com/features/chat-conversations/chat-features/)
\* Reasoning & Thinking Models
On this page

### Reasoning & Thinking Models

Open WebUI provides first-class support for models that exhibit "thinking" or "reasoning" behaviors (such as DeepSeek R1, OpenAI o1, and others). These models often generate internal chains of thought before providing a final answer.

#### How Thinking Tags Work

When a model generates reasoning content, it typically wraps that content in specific XML-like tags (e.g., or ).
Open WebUI automatically:
1. **Detects** these tags in the model's output stream.
1. **Extracts** the content between the tags.
1. **Renders** the extracted content in a collapsible UI element labeled "Thought" or "Thinking".
This keeps the main chat interface clean while still giving you access to the model's internal processing.

#### The reasoning\_tags Parameter

You can customize which tags Open WebUI should look for using the reasoning\_tags parameter. This can be set on a **per-chat** or **per-model** basis.

##### Default Tags

By default, Open WebUI looks for several common reasoning tag pairs:
\*
\*
\*
\*
\*
\* <|begin\_of\_thought|> , <|end\_of\_thought|>

##### Customization

If your model uses different tags, you can provide a list of tag pairs in the reasoning\_tags parameter. Each pair is a tuple or list of the opening and closing tag.

#### Configuration & Behavior

```
*   **Stripping from Payload** : The reasoning_tags parameter itself is an Open WebUI-specific control and is  **stripped**  from the payload before being sent to the LLM backend (OpenAI, Ollama, etc.). This ensures compatibility with providers that do not recognize this parameter.
*   **Chat History** : Reasoning content is preserved in chat history and  **sent back to the model**  across turns. When building messages for subsequent requests, Open WebUI serializes the reasoning content with its original tags (e.g., ... ) and includes it in the assistant message's content field. This allows the model to "remember" its previous reasoning steps across the entire conversation.
*   **UI Rendering** : Internally, reasoning blocks are processed and rendered using a specialized UI component. When saved or exported, they may be represented as HTML  tags.
```

#### Open WebUI Settings

Open WebUI provides several built-in settings to configure reasoning model behavior. These can be found in:
\* **Chat Controls** (sidebar) → **Advanced Parameters** — per-chat settings
\* **Workspace** → **Models** → **Edit Model** → **Advanced Parameters** — per-model settings (Admin only)
\* **Admin Panel** → **Settings** → **Models** → select a model → **Advanced Parameters** — alternative per-model settings location

##### Reasoning Tags Setting

This setting controls how Open WebUI parses and displays thinking/reasoning blocks:

| Option | Description |
| --- | --- |
| **Default** | Uses the system default behavior |
| **Enabled** | Explicitly enables reasoning tag detection using default tags |
| **Disabled** | Turns off reasoning tag detection entirely |
| **Custom** | Allows you to specify custom start and end tags |

###### Using Custom Tags

If your model uses non-standard reasoning tags (e.g., or [思考]...[/思考] ), select **Custom** and enter:
\* **Start Tag** : The opening tag (e.g., )
This is useful for:
\* Models with localized thinking tags
\* Custom fine-tuned models with unique tag formats
\* Models that use XML-style reasoning markers

##### think (Ollama)

This Ollama-specific setting enables or disables the model's built-in reasoning feature:

| Option | Description |
| --- | --- |
| **Default** | Uses Ollama's default behavior |
| **On** | Explicitly enables thinking mode for the model |
| **Off** | Disables thinking mode |

note
This setting sends the think parameter directly to Ollama. It's separate from how Open WebUI parses the response—you may need both this setting AND proper reasoning tags configuration for the full experience.

##### Reasoning Effort

For models that support variable reasoning depth (like some API providers), this setting controls how much effort the model puts into reasoning:
\* Common values: low , medium , high
\* Some providers accept numeric values
info
Reasoning Effort is only applicable to models from specific providers that support this parameter. It has no effect on local Ollama models.

#### Interleaved Thinking with Tool Calls

When a model uses **native function calling** (tool use) within a single turn, Open WebUI preserves the reasoning content and sends it back to the API for subsequent calls within that turn. This enables true "interleaved thinking" where:
1. Model generates reasoning → makes a tool call
1. Tool executes and returns results
1. Model receives: original messages + previous reasoning + tool call + tool result
1. Model continues reasoning → may make more tool calls or provide final answer
1. Process repeats until the turn completes

##### How It Works

During a multi-step tool calling turn, Open WebUI:
1. **Captures** reasoning content from the model's response (via reasoning\_content , reasoning , or thinking fields in the delta)
1. **Stores** it in content blocks alongside tool calls
1. **Serializes** the reasoning with its original tags (e.g., ) when building messages for the next API call
1. **Includes** the serialized content in the assistant message's content field
This ensures the model has access to its previous thought process when deciding on subsequent actions within the same turn.

##### How Reasoning Is Sent Back

When building the next API request during a tool call loop, Open WebUI serializes reasoning as **text wrapped in tags** inside the assistant message's content field:

```
Let me search for the current weather data...
```

The message structure looks like:

```
{
  "role": "assistant",
  "content": "reasoning content here",
  "tool_calls": [...]
}
```

##### Provider Compatibility

Open WebUI follows the **OpenAI Chat Completions API standard** . Reasoning content is serialized as text within the message content field, not as provider-specific structured blocks.

| Provider Type | Compatibility |
| --- | --- |
| OpenAI-compatible APIs | ✅ Works — reasoning is in the content text |
| Ollama | ✅ Works — Ollama processes the message content |
| Anthropic (extended thinking) | ❌ Not supported — Anthropic requires structured {"type": "thinking"} blocks, use a pipe function |
| OpenAI o-series (stateful) | ⚠ Limited — reasoning is hidden/internal, nothing to capture |

##### Important Notes

```
*   **Within-turn preservation** : Reasoning is preserved and sent back to the API within the same turn (while tool calls are being processed).
*   **Cross-turn behavior** : Reasoning content  **is**  sent back to the API across turns. When building messages for subsequent requests, Open WebUI serializes the reasoning content with its original tags (e.g., ... ) and includes it in the assistant message's content field. This allows the model to maintain context of its previous reasoning throughout the conversation.
*   **Text-based serialization** : Reasoning is sent as text wrapped in tags (e.g., thinking content ), not as structured content blocks. This works with most OpenAI-compatible APIs but may not align with provider-specific formats like Anthropic's extended thinking content blocks.
```

#### Streaming vs Non-Streaming

##### Streaming Mode (Default)

In streaming mode ( stream: true ), Open WebUI processes tokens as they arrive and can detect reasoning blocks in real-time. This generally works well without additional configuration.

##### Non-Streaming Mode

In non-streaming mode ( stream: false ), the entire response is returned at once. **This is where most parsing issues occur** because:
1. The response arrives as a single block of text
1. Without the reasoning parser, no post-processing separates the

#### API Usage

When using the Open WebUI API with reasoning models:

```
{
  "model": "qwen3:32b",
  "messages": [
    {"role": "user", "content": "Solve: What is 234 * 567?"}
  ],
  "stream": true
}
```

**Recommendation:** Use "stream": true for the most reliable reasoning block parsing.

#### Troubleshooting

##### Thinking Content Merged with Final Answer

**Symptom:** When using a reasoning model, the entire response (including blocks) is displayed as the final answer, instead of being separated into a hidden/collapsible thinking section.
**Example of incorrect display:**

```
Okay, the user wants a code snippet for a sticky header using CSS and JavaScript.
Let me think about how to approach this.
...
I think that's a solid approach. Let me write the code now.

Here's a complete code snippet that demonstrates a sticky header using CSS and JavaScript...
```

**Expected behavior:** The thinking content should be hidden or collapsible, with only the final answer visible.

##### For Ollama Users

The most common cause is that Ollama is not configured with the correct **reasoning parser** . When running Ollama, you need to specify the --reasoning-parser flag to enable proper parsing of thinking blocks.

###### Step 1: Configure the Reasoning Parser

When starting Ollama, add the --reasoning-parser flag:

```
# For DeepSeek-R1 style reasoning (recommended for most models)
ollama serve --reasoning-parser deepseek_r1

# Alternative parsers (if the above doesn't work for your model)
ollama serve --reasoning-parser qwen3
ollama serve --reasoning-parser deepseek_v3
```

Recommended Parser
For most reasoning models, including Qwen3 and DeepSeek variants, use --reasoning-parser deepseek\_r1 . This parser handles the standard format used by most reasoning models.

###### Step 2: Restart Ollama

After adding the flag, restart the Ollama service:

```
# Stop Ollama
# On Linux/macOS:
pkill ollama

# On Windows (PowerShell):
Stop-Process -Name ollama -Force

# Start with the reasoning parser
ollama serve --reasoning-parser deepseek_r1
```

###### Step 3: Verify in Open WebUI

```
1. Go to Open WebUI and start a new chat with your reasoning model
1. Ask a question that requires reasoning (e.g., a math problem or logic puzzle)
1. The response should now show the thinking content in a collapsible section
```

##### Available Reasoning Parsers

| Parser | Description | Use Case |
| --- | --- | --- |
| deepseek\_r1 | DeepSeek R1 format | Most reasoning models, including Qwen3 |
| deepseek\_v3 | DeepSeek V3 format | Some DeepSeek variants |
| qwen3 | Qwen3-specific format | If deepseek\_r1 doesn't work with Qwen |

##### Troubleshooting Checklist

###### 1. Verify Ollama Is Running with Reasoning Parser

Check if Ollama was started with the correct flag:

```
# Check the Ollama process
ps aux | grep ollama
# or on Windows:
Get-Process -Name ollama | Format-List *
```

Look for --reasoning-parser in the command line arguments.

###### 2. Check Model Compatibility

Not all models output reasoning in the same format. Verify your model's documentation for:
\* What tags it uses for thinking content (e.g.,

###### 3. Test with Streaming Enabled

If non-streaming isn't working, try enabling streaming in your chat:
1. Go to **Chat Controls** (sidebar)
1. Ensure streaming is enabled (this is the default)
1. Test the model again

###### 4. Check Open WebUI Version

Ensure you're running the latest version of Open WebUI, as reasoning model support continues to improve:

```
docker pull ghcr.io/open-webui/open-webui:main
```

###### 5. Verify the Model Response Format

Use the Ollama CLI directly to check what format your model outputs:

```
ollama run your-model:tag "Explain step by step: What is 15 + 27?"
```

Look for

##### Reasoning Lost Between Tool Calls

**Symptom:** The model seems to "forget" what it was thinking about after a tool call completes.
**Possible Causes:**
1. The model doesn't output reasoning in a captured format ( reasoning\_content , reasoning , or thinking delta fields)
1. The model uses text-based thinking tags that aren't being parsed as reasoning blocks
**Solution:** Check if your model outputs reasoning through:
\* Structured delta fields ( reasoning\_content , reasoning , thinking )
\* Text-based tags that Open WebUI detects (ensure reasoning tag detection is enabled)

##### Anthropic Extended Thinking Not Working with Tool Calls

**Symptom:** Using Anthropic's Claude models with extended thinking enabled, but tool calls fail with errors like:

```
Expected `thinking` or `redacted_thinking`, but found `text`. When `thinking` is enabled, 
a final `assistant` message must start with a thinking block.
```

**Cause:** This is a fundamental architectural difference. Open WebUI follows the **OpenAI Chat Completions API standard** and does not natively support Anthropic's proprietary API format. Anthropic's extended thinking requires structured content blocks with {"type": "thinking"} or {"type": "redacted\_thinking"} , which are Anthropic-specific formats that don't exist in the OpenAI standard.
Open WebUI serializes reasoning as text wrapped in tags (e.g., ) inside the message content field. This works with OpenAI-compatible APIs but does not satisfy Anthropic's requirement for structured thinking blocks.
**Why Open WebUI Doesn't Support This Natively:**
There is no standard way for storing reasoning content as part of the API payload across different providers. If Open WebUI implemented support for one provider's format, it would likely break existing deployments for many other inference providers. Given the wide variety of backends Open WebUI supports, we follow the OpenAI Completions API as the common standard. For more details on this architectural decision, see our **FAQ on protocol support** .
**Workarounds:**
1. **Use a Pipe Function** : Create a custom [pipe function](https://docs.openwebui.com/features/extensibility/pipelines/pipes) that converts Open WebUI's text-based thinking format to Anthropic's structured thinking blocks before sending requests to the Anthropic API.
1. **Disable Extended Thinking** : If you don't need extended thinking for tool-calling workflows, disable it to avoid the format mismatch.
note
This limitation applies specifically to combining Anthropic's extended thinking with tool calls. Extended thinking works without tool calls, and tool calls work without extended thinking—the issue only occurs when using both features together via the Anthropic API.

##### Stateful Reasoning Models (GPT-5.2, etc.)

**Symptom:** Using a model that hides its reasoning (stateful/internal reasoning), and reasoning is not being preserved.
**Cause:** Some newer models (like GPT-5.2) keep their reasoning internal and don't expose it in the API response. Open WebUI can only preserve reasoning that is actually returned by the model.
**Behavior:** If the model returns a reasoning summary instead of full reasoning content, that summary is what gets preserved and sent back.

#### Frequently Asked Questions

##### Why is the thinking block showing as raw text?

If the model uses tags that are not in the default list and have not been configured in reasoning\_tags , Open WebUI will treat them as regular text. You can fix this by adding the correct tags to the reasoning\_tags parameter in the Model Settings or Chat Controls.

##### Does the model see its own thinking?

**Yes.** Reasoning content is preserved and sent back to the model in both scenarios:
\* **Within the same turn (during tool calls)** : **Yes** . When a model makes tool calls, Open WebUI preserves the reasoning content and sends it back to the API as part of the assistant message. This enables the model to maintain context about what it was thinking when it made the tool call.
\* **Across different turns** : **Yes** . When building messages for subsequent requests, Open WebUI serializes reasoning content from previous turns with its original tags (e.g., ) and includes it in the assistant message's content field. This allows the model to reference its previous reasoning throughout the conversation.

##### How is reasoning sent during tool calls?

When tool calls are involved, reasoning is serialized as text with its original tags and included in the assistant message's content field. For example:

```
Let me search for the current weather...
```

This text-based format works with most OpenAI-compatible providers. However, some providers (like Anthropic) may expect structured thinking content blocks in a specific format—Open WebUI currently uses text-based serialization rather than provider-specific structured formats.
[Edit this page](https://github.com/open-webui/docs/blob/main/docs/features/chat-conversations/chat-features/reasoning-models.mdx)
[Previous Message Queue](https://docs.openwebui.com/features/chat-conversations/chat-features/message-queue)
[Next Temporal Awareness](https://docs.openwebui.com/features/chat-conversations/chat-features/temporal-awareness)
Docs
\* [Getting Started](https://docs.openwebui.com/getting-started)
\* [FAQ](https://docs.openwebui.com/faq)
\* [Help Improve The Docs](https://github.com/open-webui/docs)
Community
\* [GitHub](https://github.com/open-webui/open-webui)
\* [Discord](https://discord.gg/5rJgQTnV4s)
\* [Reddit](https://www.reddit.com/r/OpenWebUI/)
\* [𝕏](https://x.com/OpenWebUI)
More
\* [Release Notes](https://github.com/open-webui/open-webui/blob/main/CHANGELOG.md)
\* [About](https://openwebui.com/)
\* [Report a Vulnerability / Responsible Disclosure](https://github.com/open-webui/open-webui/security)