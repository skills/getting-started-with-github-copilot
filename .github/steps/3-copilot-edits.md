## Step 3: Getting work done even _faster_ with Copilot Edit Mode

In our previous steps, we used features of Copilot that require more hands-on guidance and they produced mostly localized results. Now, we will explore Copilot **Edit Mode**, a feature that allows working more holistically on our repo.

### 📖 Theory: Copilot Edit Mode

Copilot **Edit Mode** and **Agent Mode** both let you apply **natural‑language** driven changes across **multiple files**, however there are some differences between them.

In this step we will focus on **Edit Mode** and explore **Agent Mode** in the next step.

Edit Mode is best used for **well defined** tasks where you **know the scope** of the needed changes.

#### How Edit Mode works

```mermaid
flowchart LR
   A[Select Context Files] --> B[Prompt Copilot]
   B --> C[Proposed Changes]
   C --> D{Review Change}
   D --> E[Accept]
   D --> F[Discard]
   D -->|Refine Prompt| B

```

1. **Set Context**: Select files that Copilot should consider in it's changes
1. **Prompt Copilot**: Use natural language to describe the required changes.
1. **Review Changes**: See proposed changes in-place in your code.
1. **Accept or Discard**: Review each suggested edit and choose which to keep.
1. **Iterate**: If needed, provide follow-up instructions to refine the changes.

### :keyboard: Activity: Use Copilot to add a new feature! :rocket:

Our website lists activities, but it's keeping the guest list secret 🤫 

Let's use Copilot to change the website to display signed up students under each activity!

1. At the bottom of Copilot Chat window, use the dropdown to switch to **Edit** mode.

   <img width="350" alt="image" src="../images/edit-mode-dropdown.png" />

1. Open the files related to our webpage then drag each editor window (or file) to the chat panel, informing Copilot to use them as context.

   - `src/static/app.js`
   - `src/static/index.html`
   - `src/static/styles.css`

   <img width="400" alt="image showing files added to context" src="../images/files-added-to-context.png" />

   > 💡 **Tip:** You can also use the **Add Context...** button to provide other sources of context items, like a GitHub issue, the entire codebase, or the results of a terminal window.

1. Ask Copilot to update our project to display the current participants of activities. Wait a moment for the edit suggestions to arrive and be applied.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Hey Copilot, can you please edit the activity cards to add a participants section.
   > It will show what participants that are already signed up for that activity as a bulleted list.
   > Remember to make it pretty!
   > ```

   - An extra icon has appeared next to the file names and open editor windows indicating they have suggested edits.
   - A suggested edits panel has appeared in the bottom right of the editor window providing controls to jump to the recommended changes.

      <img width="200" alt="files with icons indicating they have been edited" src="../images/edited-files-icons.png" />

      <img width="250" alt="edit navigation panel" src="../images/edit-navigation-panel.png" />


1. Before we simply accept the changes, please check our website again and verify everything is updated as expected. Here is an example of an updated activity card. You may need to restart the app or refresh the page.

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

1. With our new feature complete, please **commit** and **push** the changes to GitHub.

1. Wait a moment for Mona to check your work, provide feedback, and share the next lesson.


<details>
<summary>Having trouble? 🤷</summary><br/>

If you don't get feedback, here are some things to check:

- Make sure your commit the changes in the `src/static/` directory to the branch `accelerate-with-copilot` and pushed/synchronized to GitHub.
- If Mona found a mistake, simply make a correction and push your changes again. Mona will check your work as many times as needed.

</details>
