## Step 3: Engage Hyperdrive - Copilot Agent Mode 🚀

### 📖 Theory: What is Copilot Agent Mode?

Copilot [agent mode](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode) is the next evolution in AI-assisted coding. Acting as an autonomous peer programmer, it performs multi-step coding tasks at your command.

Copilot Agent Mode responds to compile and lint errors, monitors terminal and test output, and auto-corrects in a loop until the task is completed.

#### Agent Mode (at a glance)

| Aspect | 👩‍🚀 Agent Mode |
| --- | --- |
| Autonomy and planning | Breaks down high-level requests into multi-step work and iterates until the task is complete. |
| Context gathering | Uses your current context and can discover additional relevant files when needed. |
| Tool use | Selects and invokes tools automatically; you can also direct tools with mentions like `#codebase`. |
| Approval and safety gates | Sensitive actions can require approval before execution, helping you stay in control. |

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

### :keyboard: Activity: Use Copilot to add a new feature! :rocket:

Our website lists activities, but it's keeping the guest list secret 🤫 

Let's use Copilot to change the website to display signed up students under each activity!

1. At the bottom of Copilot Chat window, use the dropdown to switch to **Agent** mode.

   <img width="350" alt="image" src="../images/agent-mode-dropdown.png" />

1. Open the files related to our webpage then drag each editor window (or file) to the chat panel, informing Copilot to use them as context.

   - `src/static/app.js`
   - `src/static/index.html`
   - `src/static/styles.css`

   > 🪧 **Note:** Adding files as context is optional. If you skip this, Copilot Agent Mode can still use tools like `#codebase` to search for relevant files from your prompt. Adding specific files helps point Copilot in the right direction, which is especially useful in larger codebases.

   <img width="400" alt="image showing files added to context" src="../images/files-added-to-context.png" />

   > 💡 **Tip:** You can also use the **Add Context...** button to provide other sources of context items, like a GitHub issue or the results of a terminal window.

1. Ask Copilot to update our project to display the current participants of activities. Wait a moment for the edit suggestions to arrive and be applied.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Hey Copilot, can you please edit the activity cards to add a participants section.
   > It will show what participants that are already signed up for that activity as a bulleted list.
   > Remember to make it pretty!
   > ```

   After Copilot finishes work, you are in control of what changes get to stay. 

   Using the **Keep** buttons shown below, you can accept/discard all changes or review and decide change by change. This can be done either from the chat panel view or while inspecting each edited file.

      <img width="900" alt="buttons to keep or discard changes" src="../images/review-changes-buttons.png" />


1. Before we simply accept the changes, please check our website again and verify everything is updated as expected. 
   
   Here is an example of an updated activity card. You may need to restart the app or refresh the page.

   <img width="350" alt="Activity card with participant info" src="../images/activity-card-with-participants.png" />

   > 🪧 **Note:** Your activity card may look different. Copilot won't always produce the same results.

   <details>
   <summary>Need help? 🤷</summary><br/>
   If the website is not loading, here are some things to check.

   - Restart the VS Code Debugger to make sure the latest version of the website is served.
   - If you forgot the url, or closed the window, please review step 1.
   - Try hard refreshing the webpage or opening in a private window so it downloads a fresh copy.

   </details>

1. Now that we have confirmed our changes are good, use the panel to cycle through each suggested edit and press **Keep** to apply the change.

   > 💡 **Tip:** You can accept the changes directly, modify them, or provide additional instruction to refine them using the chat interface.

### :keyboard: Activity: Use Agent mode to add functional "unregister" buttons

Let's experiment with some more open-ended requests that will add more functionality to our web application.

If you don't get the desired results, you can try other models or provide follow-up feedback to refine the results.

1. Make sure your Copilot is still in **Agent** mode.

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

1. When Copilot is finished, inspect the code changes and the results on the website. If you like the results, press the **Keep** button. If not, try providing Copilot some feedback to refine the results.

   > 🪧 **Note:** If you don't see updates on the website, you may need to restart the debugger

1. Ask Copilot to fix a registration bug.

   > 💡 **Tip:** We recommend testing the registration flow yourself so you can clearly see the before/after changes behavior.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > I've noticed there seems to be a bug.
   > When a participant is registered, the page must be refreshed to see the change on the activity.
   > ```

1. When Copilot is finished, inspect the results and validate the registration flow on the website.

   If you like the results, press the **Keep** button. If not, try providing Copilot some feedback.

1. **Commit** and **push** all your changes to the `accelerate-with-copilot` branch.

1. Wait for Mona to check your work and share the next step.