## Step 4: Using GitHub Copilot within a pull request

Congratulations! You are finished with coding for this exercise (and VS Code). Now it's time to merge our work. :tada: To wrap up, let's learn about two limited-access Copilot features that can speed up our pull requests!

#### Copilot pull request summaries

Typically, you would review your notes and commit messages then summarize them for your pull request description. This may take some time, especially if commit messages are inconsistent or code is not documented well. Fortunately, Copilot can consider all changes in the pull request and provide the important highlights, and with references too!

> [!NOTE]
> This feature is not available in **GitHub Copilot Free**. [[docs]](https://docs.github.com/en/enterprise-cloud@latest/copilot/using-github-copilot/using-github-copilot-for-pull-requests/creating-a-pull-request-summary-with-github-copilot)

#### Copilot code review

More eyes on our work is always useful so let's ask Copilot to do a first pass before we do a normal peer review process. Copilot is great at catching common mistakes that are fixed by simple adjustments, but please remember to use it responsibly.

> [!NOTE]
> This feature is not available in **GitHub Copilot Free**. [[docs]](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review)

### :keyboard: Activity: Summarize and review a PR with Copilot

Both **Copilot pull request summaries** and **Copilot code review** have limited access, so this activity is mostly optional. If you have access, go ahead and try them though! If not, you can skip the optional steps.

1. In a web browser, open another tab and navigate to your exercise repository.

1. You might notice a **notification banner** suggesting to create a new pull request. Click that or use the **Pull Requests** tab at the top to create a new pull request. Please use the following details:

   - **base:** `main`
   - **compare:** `accelerate-with-copilot`
   - **title:** `Add registration validation and more activities`

1. (Optional) In the **Add a description** area, enter edit mode if needed, then click the **Copilot actions** icon and **Summary** action. After a moment, Copilot will add a description. :memo:

   <img alt="Copilot summarize button " width="300px" src="https://github.com/user-attachments/assets/3fc5fab4-db03-4ab8-8a16-cdd71ec2ded0">

1. (Optional) In the right side information panel at the top, locate the **Reviewers** section and click the **Request** button next to a **Copilot icon**. Wait a moment for Copilot to add a review comment to your pull request!

   <img alt="Copilot review button" width="300px" src="https://github.com/user-attachments/assets/39b15002-a235-4c25-b09d-6a8097e27b62">

   > **Tip:** Notice a log entry that Copilot was requested for a review.

1. At the bottom, press the **Merge pull request** button. Nice work! You are all done! :tada:

1. Wait a moment for Mona to check your work, provide feedback, and post a final review of this lesson!
