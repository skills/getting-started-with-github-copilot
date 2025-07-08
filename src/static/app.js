document.addEventListener("DOMContentLoaded", () => {
  const activitiesList = document.getElementById("activities-list");
  const activitySelect = document.getElementById("activity");
  const signupForm = document.getElementById("signup-form");
  const messageDiv = document.getElementById("message");

  // Função para buscar atividades da API
  async function fetchActivities() {
    try {
      const response = await fetch("/activities");
      const activities = await response.json();

      // Limpa mensagens e opções antigas
      activitiesList.innerHTML = "";
      activitySelect.innerHTML = '<option value="">-- Select an activity --</option>';

      // Popula lista de atividades
      Object.entries(activities).forEach(([name, details]) => {
        const activityCard = document.createElement("div");
        activityCard.className = "activity-card";

        const spotsLeft = details.max_participants - details.participants.length;

        activityCard.innerHTML = `
          <h4>${name}</h4>
          <p>${details.description}</p>
          <p><strong>Schedule:</strong> ${details.schedule}</p>
          <p><strong>Availability:</strong> ${spotsLeft} spots left</p>
          <div class="participants-list">
            <h5>Participantes inscritos:</h5>
            <ul>
              ${
                details.participants.length > 0
                  ? details.participants.map(email => `<li>${email}</li>`).join('')
                  : '<li style="color:#bbb;font-style:italic;">Nenhum participante ainda</li>'
              }
            </ul>
          </div>
        `;

        activitiesList.appendChild(activityCard);

        // Adiciona opção ao select
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
    const submitBtn = signupForm.querySelector('button[type="submit"]');
    submitBtn.disabled = true;

    try {
      const response = await fetch(
        `/activities/${encodeURIComponent(activity)}/signup`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
          },
          body: `email=${encodeURIComponent(email)}`,
        }
      );

      const result = await response.json();

      if (response.ok) {
        messageDiv.textContent = result.message;
        messageDiv.className = "success";
        signupForm.reset();
        // Atualiza a lista de participantes no DOM imediatamente
        const activityCards = document.querySelectorAll('.activity-card');
        activityCards.forEach(card => {
          if (card.querySelector('h4')?.textContent === activity) {
            const ul = card.querySelector('.participants-list ul');
            if (ul) {
              // Adiciona o novo participante
              const li = document.createElement('li');
              li.textContent = email;
              ul.appendChild(li);
              // Remove mensagem de "Nenhum participante ainda"
              const emptyMsg = ul.querySelector('li[style]');
              if (emptyMsg) emptyMsg.remove();
            }
          }
        });
        // Pequeno delay para garantir atualização do backend
        setTimeout(() => {
          fetchActivities();
        }, 300);
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
    } finally {
      submitBtn.disabled = false;
    }
  });

  // Initialize app
  fetchActivities();
});
