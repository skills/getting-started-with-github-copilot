### :keyboard: Bonus Activity - Preview of GitHub Copilot Agent Mode

Nice! You found this hidden bonus level! 🎮 👾

If you have been keeping an eye on Github, you may have heard about **Agent** mode.
It's a public preview feature for GitHub Copilot.

But... it's only for _Insiders_! 😎🤫

But... good news. Anyone can access the Insiders version if they know the tricks. Yay! 🧐🎉

> [!IMPORTANT]
> This activity is optional and ungraded.
> Since the Insiders version is updated daily, please expect to see differences.

### What is "Agent" Mode?

**Agent** mode enhances Copilot by automatically providing it feedback, typically the types of feedback you would provide after reviewing Copilot's suggested edits.

**Agent** mode gives Copilot a feedback loop, enabling it to inspect its own results for issues, bugs, inconsistency, etc. in the code and even the terminal! This allows it to automatically revise its work in many situations. Similarly this means **Agent** mode can
typically handle more complex and multi-step tasks.

That's just a brief intro and there is much more to learn, but that's for a dedicated future exercise. (hint)

Now, let's give **Agent** mode a try! 👩‍🚀

### :keyboard: Activity: Test out Copilot Agent mode! 🧑‍🚀

> [!IMPORTANT]
> Copilot Agent mode is only available when using the insiders version of VS Code and the pre-release version of the GitHub Copilot extension.

1. If needed, use the below steps to switch your VS Code and Copilot extension to the **Insiders** version.

   1. Ensure you are in a browser-based instance of VS Code (your Codespace).

      > **Tip:** This allows switching to **Insiders** mode without installing another version on your local computer.

   1. In the bottom left, click the **Manage** icon and select the **Switch to Insiders Version...** option.

      <img width="300" alt="image" src="https://github.com/user-attachments/assets/11580b67-9891-4aa9-9a7c-04aff1e7ef9c" />

   1. In the left navigation, select the **Extensions** tab.
      Find the **GitHub Copilot** entry, click the **Manage** icon, and select **Switch to Pre-Release Version**.

      <img width="300" alt="image" src="https://github.com/user-attachments/assets/39e1d9ae-ba50-4cd7-b6b6-eb51aa0a35aa" />

1. Open the **Copilot Edits** side panel. Use the new dropdown menu to switch to **Agent** mode.

   <img width="250" alt="image" src="https://github.com/user-attachments/assets/1849c14d-99f5-48f9-a7fb-8f623bb6837f" />

1. Time for a test! Let's ask Copilot to add functionality for removing participants.

   > <img width="13px" src="https://github.com/user-attachments/assets/98fd5d2e-ea29-4a4a-9212-c7050e177a69" /> **Prompt**
   >
   > ```prompt
   > #codebase Please add a delete icon next to each participant and hide the bullet points.
   > When clicked, it will unregister that participant from the activity.
   > ```

   - If you try this prompt in **Edit** mode, you will find that the changes to the frontend and backend were made in a theoretical way. Although no syntax or runtime errors occurred, the changes were not compatible and didn't achieve the goal.
   - In **Agent** mode, Copilot reviewed its own work and refined it to ensure all changes were error free and coordinated together.

1. When Copilot is finished, restart the debugger and inspect the results. If you like the results, press the **Keep** button. If not, try providing Copilot some feedback.

1. Ask Copilot to fix a registration bug.

   > <img width="13px" src="https://github.com/user-attachments/assets/98fd5d2e-ea29-4a4a-9212-c7050e177a69" /> **Prompt**
   >
   > ```prompt
   > #codebase I've noticed there seems to be a bug.
   > When a participant is registered, the page must be refreshed to see the change on the activity.
   > ```

   - If you try this prompt in **Edit** mode, it may or may not work.

1. When Copilot is finished, inspect the results. If you like the results, press the **Keep** button. If not, try providing Copilot some feedback.

### :keyboard: Activity: Test out Copilot Agent mode, _again_! 🧑‍🚀🚀

Just for fun, let's try something even more difficult and see what happens!

> [!IMPORTANT]
> The below request asks much more of Copilot.
> As such is more open-ended and may not work everytime.

1. Ask Copilot to install a local database service.

   > <img width="13px" src="https://github.com/user-attachments/assets/98fd5d2e-ea29-4a4a-9212-c7050e177a69" /> **Prompt**
   >
   > ```prompt
   > Please install a local mongodb server for development reasons.
   > Afterward, run a command that lists the collections to verify the service is active and working.
   > Do not modify our program yet.
   > ```

   - We purposly made the default development environment not ready for installing a local MongoDB server.
   - You will see Copilot make mistakes, analyze the error messages, and ask to run various extra commands to make the environment suitable. Nice!

1. Ask Copilot to change our app to use the database service. 🤯

   > <img width="13px" src="https://github.com/user-attachments/assets/98fd5d2e-ea29-4a4a-9212-c7050e177a69" /> **Prompt**
   >
   > ```prompt
   > #codebase I don't like that we are storing the data in memory.
   > Let's switch to using mongodb.
   > For now use the local development instance.
   > Please prepopulate the database with the existing hardcoded json activities, keeping the the activity name as the key.
   > ```

1. That's your preview for now. We hope it was fun and please check back soon on the [Skills page](https://skills.github.com) for a dedicated exercise to explore even more of Agent Mode! 🧑‍🚀 🚀
