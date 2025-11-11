document.addEventListener("DOMContentLoaded", () => {
  const activitiesList = document.getElementById("activities-list");
  const activitySelect = document.getElementById("activity");
  const signupForm = document.getElementById("signup-form");
  const messageDiv = document.getElementById("message");

  // Function to create a display name and initials from an email or name
  function nameFromIdentifier(id) {
    if (!id) return { display: "Unknown", initials: "?" };
    // if it's an email, use part before @
    const raw = id.includes("@") ? id.split("@")[0] : id;
    // replace dots/underscores with spaces and split to words
    const parts = raw.replace(/[._\-]+/g, " ").split(" ").filter(Boolean);
    const display = parts.map(p => p.charAt(0).toUpperCase() + p.slice(1)).join(" ");
    const initials = parts.length === 1
      ? parts[0].substring(0, 2).toUpperCase()
      : (parts[0][0] + parts[parts.length - 1][0]).toUpperCase();
    return { display: display || raw, initials };
  }

  // Function to fetch activities from API
  async function fetchActivities() {
    try {
      const response = await fetch("/activities");
      const activities = await response.json();

      // Clear loading message
      activitiesList.innerHTML = "";

      // Reset select (keep placeholder if present)
      const placeholderOption = activitySelect.querySelector('option[value=""]');
      activitySelect.innerHTML = "";
      if (placeholderOption) {
        activitySelect.appendChild(placeholderOption);
      } else {
        // ensure a default placeholder exists
        const opt = document.createElement("option");
        opt.value = "";
        opt.textContent = "-- Select an activity --";
        activitySelect.appendChild(opt);
      }

      // Populate activities list
      Object.entries(activities).forEach(([name, details]) => {
        const activityCard = document.createElement("div");
        activityCard.className = "activity-card";

        const spotsLeft = details.max_participants - (details.participants?.length || 0);

        // Basic info
        const infoHtml = `
          <h4>${name}</h4>
          <p>${details.description || ""}</p>
          <p><strong>Schedule:</strong> ${details.schedule || "TBA"}</p>
          <p><strong>Availability:</strong> ${spotsLeft} spots left</p>
        `;
        activityCard.innerHTML = infoHtml;

        // Participants section
        const participantsDiv = document.createElement("div");
        participantsDiv.className = "participants";
        participantsDiv.setAttribute("aria-label", `Participants for ${name}`);

        const title = document.createElement("h5");
        title.textContent = "Participants";
        participantsDiv.appendChild(title);

        const participants = details.participants || [];

        if (participants.length === 0) {
          const none = document.createElement("p");
          none.className = "info";
          none.textContent = "No participants yet";
          participantsDiv.appendChild(none);
        } else {
          const list = document.createElement("ul");
          list.style.listStyle = "none";
          list.style.padding = "0";
          participants.forEach((p) => {
            const { display, initials } = nameFromIdentifier(p);
            const li = document.createElement("li");

            const span = document.createElement("span");
            span.className = "participant-initials";
            span.textContent = initials;

            li.appendChild(span);
            li.appendChild(document.createTextNode(" " + display));

            // Add delete icon
            const delBtn = document.createElement("button");
            delBtn.className = "delete-participant";
            delBtn.title = "Remove participant";
            delBtn.innerHTML = "&#128465;"; // trash can icon
            delBtn.style.marginLeft = "8px";
            delBtn.style.background = "none";
            delBtn.style.border = "none";
            delBtn.style.cursor = "pointer";
            delBtn.style.color = "#c62828";
            delBtn.style.fontSize = "15px";
            delBtn.setAttribute("aria-label", `Remove ${display}`);
            delBtn.addEventListener("click", (e) => {
              e.stopPropagation();
              unregisterParticipant(name, p);
            });
            li.appendChild(delBtn);

            list.appendChild(li);
          });
          participantsDiv.appendChild(list);
        }

        activityCard.appendChild(participantsDiv);
        activitiesList.appendChild(activityCard);

        // Add option to select dropdown
        const option = document.createElement("option");
        option.value = name;
        option.textContent = name;
        activitySelect.appendChild(option);
      });
    } catch (error) {
      activitiesList.innerHTML = "<p>Failed to load activities. Please try again later.</p>";
      console.error("Error fetching activities:", error);
    }
  }

  // Handle form submission
  signupForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const activity = document.getElementById("activity").value;

    try {
      const response = await fetch(
        `/activities/${encodeURIComponent(activity)}/signup?email=${encodeURIComponent(email)}`,
        {
          method: "POST",
        }
      );

      const result = await response.json();

      if (response.ok) {
        messageDiv.textContent = result.message;
        messageDiv.className = "success";
        signupForm.reset();
        // Refresh activities to show updated participants & availability
        await fetchActivities();
      } else {
        messageDiv.textContent = result.detail || "An error occurred";
        messageDiv.className = "error";
      }

      messageDiv.classList.remove("hidden");

      // Hide message after 5 seconds
      setTimeout(() => {
        messageDiv.classList.add("hidden");
      }, 5000);
    } catch (error) {
      messageDiv.textContent = "Failed to sign up. Please try again.";
      messageDiv.className = "error";
      messageDiv.classList.remove("hidden");
      console.error("Error signing up:", error);
    }
  });

  // Initialize app
  fetchActivities();
  // Unregister participant function
  async function unregisterParticipant(activityName, participantId) {
    if (!confirm("Are you sure you want to remove this participant?")) return;
    try {
      const response = await fetch(`/activities/${encodeURIComponent(activityName)}/unregister?email=${encodeURIComponent(participantId)}`, {
        method: "POST"
      });
      const result = await response.json();
      if (response.ok) {
        messageDiv.textContent = result.message || "Participant removed.";
        messageDiv.className = "success";
        await fetchActivities();
      } else {
        messageDiv.textContent = result.detail || "Failed to remove participant.";
        messageDiv.className = "error";
      }
      messageDiv.classList.remove("hidden");
      setTimeout(() => messageDiv.classList.add("hidden"), 5000);
    } catch (error) {
      messageDiv.textContent = "Error removing participant.";
      messageDiv.className = "error";
      messageDiv.classList.remove("hidden");
      setTimeout(() => messageDiv.classList.add("hidden"), 5000);
      console.error("Error unregistering participant:", error);
    }
  }
});
