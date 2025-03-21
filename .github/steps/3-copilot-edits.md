## Step 3: Getting work done even _faster_ with Copilot Edits

In our previous steps, we used features of Copilot that require more hands-on guidance and they produced mostly localized results. Now, we will explore Copilot Edits, a feature that allows working more holistically on our repo.

[Copilot Edits](https://code.visualstudio.com/docs/copilot/copilot-edits) is an AI-powered code editing session to make changes across **multiple files** using **natural language**, and applies the edits directly in the editor, where you can review them in-place, with the full context of the surrounding code.

#### Key features

- **Multi-file Editing**: Copilot Edits can make changes across multiple files in your workspace.
- **Iterative Workflow**: Designed for fast iteration, allowing you to review, accept, or discard AI-generated code.
- **In-place Edits**: Shows generated code directly in your editor, providing a code review-like flow.
- **Working Set**: Allows you to define which files the edits should be applied to.

#### How it works

1. **Set Context**: Select files to be in the working set.
1. **Provide Instructions**: Use natural language to describe the required changes.
1. **Review Changes**: See proposed changes in-place in your code.
1. **Accept or Discard**: Review each suggested edit and choose which to keep.
1. **Iterate**: If needed, provide follow-up instructions to refine the changes.

### :keyboard: Activity: Use Copilot to add a new feature! :rocket:

1. If the Copilot Chat panel is not visible, please reopen it.

1. In the top left part of Copilot Chat window, click the **Copilot Edits** icon to switch modes.

   <img width="200" alt="image" src="https://github.com/user-attachments/assets/0b17c5bd-d03b-41b1-b97d-624fcbf8ccd1" />

1. Open the files related to our webpage then drag each editor window (or file) to the chat panel, informing Copilot to use them as context.

   - `src/static/app.js`
   - `src/static/index.html`
   - `src/static/styles.css`

   > **Tip:** You can also use the **Attach files...** button to provide other sources of context items, like a GitHub issue, the entire codebase, or the results of a terminal window.

1. Ask Copilot to update our project to display the current participants of activities. Wait a moment for the edit suggestions to arrive and be applied.

   > <img width="13px" src="https://github.com/user-attachments/assets/98fd5d2e-ea29-4a4a-9212-c7050e177a69" /> **Prompt**
   >
   > ```prompt
   > Hey Copilot, can you please edit the activity cards to add a participants section.
   > It will show what participants that are already signed up for that activity as a bulleted list.
   > ```

   - An extra icon has appeared next to the file names and open editor windows indicating they have suggested edits.
   - A suggested edits panel has appeared in the bottom right of the editor window providing controls to jump to the recommended changes.

      <img width="200" alt="files with icons indicating they have been edited" src="https://github.com/user-attachments/assets/9c7c2e10-cd18-43c5-9947-cffd6dde0473" />

      <img width="250" alt="edit navigation panel" src="https://github.com/user-attachments/assets/a84965a5-2f43-4c93-a814-0fdeb3a06494" />

   <details>
   <summary>Need help? 🤷</summary><br/>

   Remember, to add the relevant files to the working set.

   ![image](https://github.com/user-attachments/assets/bdd7318b-50e3-46d0-88ce-7615f45ce334)

   </details>

1. Before we simply accept the changes, please check our website again and verify everything is updated as expected. Here is an example of an updated activity card. You may need to restart the app or refresh the page.

   <img width="350" alt="Activity card with participant info" src="https://github.com/user-attachments/assets/59fe792e-d587-487d-8525-2548ac0a7adf" />

   > **Note:** Your activity card may look different. Copilot won't always produce the same results.

   <details>
   <summary>Need help? 🤷</summary><br/>
   If the website is not loading, here are some things to check.

   - Restart the VS Code Debugger to make sure the latest version of the website is served.
   - If you forgot the url, or closed the window, please review step 1.
   - Try hard refreshing the webpage or opening in a private window so it downloads a fresh copy.

   </details>

1. Now that we have confirmed our changes are good, use the panel to cycle through each suggested edit and press **Keep** to apply the change.

   > **Tip:** You can accept the changes directly, modify them, or provide additional instruction to refine them using the chat interface.

1. With our new feature complete, please **commit** and **push** the changes to GitHub.

1. Wait a moment for Mona to check your work, provide feedback, and share the the final lesson. Almost done!

<details>
<summary>Having trouble? 🤷</summary><br/>

If you don't get feedback, here are some things to check:

- Make sure your commite the changes in the `src/static/` directory to the branch `accelerate-with-copilot` and pushed/synchronized to GitHub.
- If Mona found a mistake, simply make a correction and push your changes again. Mona will check your work as many times as needed.

</details>

<details>
<summary>Bonus content? 🧐</summary><br/>

> **Insider Tip:** Try adding an issue comment asking @professortocat about Copilot Agent mode. 😉

</details>
