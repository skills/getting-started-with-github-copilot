## Step 4: Engage Hyperdrive - Copilot Agent Mode 🚀

### 📖 Theory: What is Copilot Agent Mode?

Copilot [agent mode](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode) is the next evolution in AI-assisted coding. Acting as an autonomous peer programmer, it performs multi-step coding tasks at your command.

Copilot Agent Mode responds to compile and lint errors, monitors terminal and test output, and auto-corrects in a loop until the task is completed.

#### Edit Mode vs Agent Mode (at a glance)

| Aspect         | ✏️ Edit Mode                      | 👩‍🚀 Agent Mode                                                                    |
| -------------- | --------------------------------- | -------------------------------------------------------------------------------- |
| Context scope  | Only the files you explicitly add | May read/add additional files & surfaces as needed                               |
| Self‑review    | Minimal (you drive iteration)     | Built‑in feedback & retry loop on errors/failures                                |
| Change scope   | Highly scoped & surgical          | Broader; may touch related layers for consistency                                |
| When to choose | You know exactly what to change   | Goal is broader or uncertain; requires exploration                               |
| Tool calling   | None (you run commands manually)  | Can invoke tools (read/edit files, run commands, inspect terminal & test output) |

#### 🧰 Agent Mode Tools

Agent mode uses tools to accomplish specialized tasks while processing a user request. Examples of such tasks are:

- Finding relevant files to complete your prompt
- Fetching contents of a webpage
- Running tests or terminal commands

> [!TIP]
> While VS Code provides many built‑in tools, you can also provide Agent Mode more domain‑specific powers through **MCP tools**.
>
> Read more on [MCP servers](https://code.visualstudio.com/docs/copilot/customization/mcp-servers) and [GitHub MCP Server](https://github.com/github/github-mcp-server)

Now, let's give **Agent Mode** a try! 👩‍🚀

### :keyboard: Activity: Use Agent mode to add functional "unregister" buttons

Let's experiment with some more open-ended requests that will add more functionality to our web application.

If you don't get the desired results, you can try other models or provided followup feedback to refine the results.

1. Open the **Copilot** chat panel and use the dropdown menu to switch to **Agent** mode.

   <img width="250" alt="agent mode" src="../images/agent-mode-dropdown.png" />

1. Click on the **Tools** icon and explore all Tools currently available to Copilot Agent Mode.

   <img width="250"  alt="tools icon" src="../images/tools-icon.png" />


1. Time for our test! Let's ask Copilot to add functionality for removing participants.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > #codebase Please add a delete icon next to each participant and hide the bullet points.
   > When clicked, it will unregister that participant from the activity.
   > ```

   The `#codebase` tool is used by Copilot to find relevant files, code chunks that are relevant to the task at hand.

   > 🪧 **Note:** In this lab we explicitly include the `#codebase` tool to get the most repeatable results.
   > Feel free to try the prompt **without** `#codebase` and observe whether Agent Mode decides to gather broader project context on its own.

1. When Copilot is finished, restart the debugger and inspect the results. If you like the results, press the **Keep** button. If not, try providing Copilot some feedback to refined the results.

1. Ask Copilot to fix a registration bug.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > I've noticed there seems to be a bug.
   > When a participant is registered, the page must be refreshed to see the change on the activity.
   > ```

1. When Copilot is finished, inspect the results. If you like the results, press the **Keep** button. If not, try providing Copilot some feedback.

### :keyboard: Activity: Use Agent mode to get test coverage 🧑‍🚀

Your backend is now feature‑rich—but still has zero test coverage. Use Copilot **Agent Mode** to add test dependencies, scaffold starter tests and run them.

1. Ask Copilot in **Agent mode** to set up and run tests for your backend.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-placeholder?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Add fastapi tests using pytest in a new tests directory and run them.
   > Make sure to add any new dependencies to requirements.txt
   > ```

1. As Copilot works on your prompt, different tools might need your approval.

   **🎯 Goal: Get all tests passing (green) — aim for a clean run! ✅**

   > 🪧 **Note:** Copilot may one-shot this with the initial prompt or need more guidance from you.

1. Once the tests are passing - **commit** and **push** all changes to your `accelerate-with-copilot` branch to progress to the last step! Almost done!
