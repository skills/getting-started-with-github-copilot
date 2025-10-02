### :keyboard: Bonus Activity - GitHub Copilot Agent Mode

> 🪧 **Note:** This bonus activity is optional and not graded.

### 📖 Theory: What is Copilot Agent Mode?

Copilot **Agent Mode** extends beyond single-pass edits: it can plan, execute, inspect results (including build/terminal output), and iteratively refine its own work without you re‑prompting each micro-step.

**How it differs from Edit Mode** (at a glance):

| Ask / Inline Chat   | Edit Mode                       | Agent Mode                              |
| ------------------- | ------------------------------- | --------------------------------------- |
| One answer/snippet  | Multi‑file patch (single cycle) | Multi‑step adaptive workflow            |
| You curate context  | You supply context files        | Agent may add/read files & run commands |
| No self‑review loop | Minimal implicit review         | Explicit feedback & retry loop          |

#### Key capabilities

- Feedback loop: can detect errors or incomplete changes and attempt fixes automatically.
- Multi-step reasoning: chains several edit + verify cycles toward a broader goal.
- Tool usage: may run commands / examine terminal output (depending on your environment & permissions).
- Cross-file consistency: attempts to coordinate backend + frontend or related modules.

#### Good use cases

- Coordinated refactors (model + route + tests)
- Adding “glue” code across layers
- Resolving a bug that requires reading logs or compiler errors

#### Limitations / cautions

- Can produce more changes than you expect—always review the diff before keeping.
- Longer runs may drift; give it concise, outcome-focused follow-ups (“The API returns 500; inspect server logs and fix”).
- Side-effectful commands (like installing services) may fail or leave partial state—treat them as experiments.

> 💡 **Tip:** If Agent Mode starts to feel “lost,” stop, accept/undo what’s useful, and start a fresh Agent session with a clearer goal.

Now, let's give **Agent Mode** a try! 👩‍🚀

### :keyboard: Activity: Use Agent mode to add functional "unregister" buttons

Let's experiment with some more open-ended requests that will add more functionality to our web application. Remember, AI assistants often produce different results, even if the same prompt is provided. If you don't get the desired results, you can try other models or provided followup feedback to refine the results.

1. Open the **Copilot** chat panel and use the dropdown menu to switch to **Agent** mode.

   <img width="250" alt="image" src="https://github.com/user-attachments/assets/8c537e2a-d89a-4908-8d35-77c7f0830805" />

1. Time for our test! Let's ask Copilot to add functionality for removing participants.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > #codebase Please add a delete icon next to each participant and hide the bullet points.
   > When clicked, it will unregister that participant from the activity.
   > ```

   - If you try this prompt in **Edit** mode, you will probably find that the changes to the frontend and backend were made in a theoretical way. Although no syntax or runtime errors occurred, the changes were not compatible and didn't achieve the goal.
   - In **Agent** mode, Copilot reviewed its own work and refined it to ensure all changes were error free and coordinated together.

1. When Copilot is finished, restart the debugger and inspect the results. If you like the results, press the **Keep** button. If not, try providing Copilot some feedback to refined the results.

1. Ask Copilot to fix a registration bug.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > #codebase I've noticed there seems to be a bug.
   > When a participant is registered, the page must be refreshed to see the change on the activity.
   > ```

   - If you try this prompt in **Edit** mode, it may or may not work.

1. When Copilot is finished, inspect the results. If you like the results, press the **Keep** button. If not, try providing Copilot some feedback.

### :keyboard: Activity: Use Agent mode to change the database! 🧑‍🚀

Just for fun, let's try something even more difficult and open-ended to see what happens!

> [!TIP]
> In our experiments, we got working results most of the time, but not every time.
> You might try other models or pausing to provide Copilot feedback.

1. (optional) If it is available for you, you might try another model such as `Claude 3.5 Sonnet`.

   <img width="250" alt="image" src="https://github.com/user-attachments/assets/16125b88-8428-4f62-9c1b-5761e26ed888" />

1. Ask Copilot to install a local database service.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Please install a local mongodb server for development reasons.
   > Afterward, run a command that lists the collections to verify the service is active and working.
   > Do not modify our program yet.
   > ```

   - We purposely made the default development environment not ready for installing a local MongoDB server.
   - You will see Copilot make mistakes, analyze the error messages, and ask to run various extra commands to make the environment suitable. Nice!

1. Ask Copilot to change our app to use the database service. 🤯

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > #codebase I don't like that we are storing the data in memory.
   > Let's switch to using mongodb.
   > For now use the local development instance.
   > Please pre-populate the database with the existing hardcoded json activities, keeping the activity name as the key.
   > ```

1. That's your preview for now. We hope it was fun and please check back soon on the [Skills page](https://skills.github.com) for a dedicated exercise to explore even more of Agent Mode! 🧑‍🚀 🚀
