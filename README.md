# Mergington High School Activities - Blazor WebAssembly

A Blazor WebAssembly application that allows students to view and sign up for extracurricular activities at Mergington High School.

## 🎯 Features

- ✅ View available extracurricular activities
- ✅ See activity details (description, schedule, availability)
- ✅ Sign up for activities with email
- ✅ Real-time spots availability tracking

## 🛠️ Prerequisites

- [.NET 8.0 SDK](https://dotnet.microsoft.com/download/dotnet/8.0) or later

## 🚀 Getting Started

1. Navigate to the Blazor project folder:
   ```bash
   cd BlazorApp
   ```

2. Restore dependencies:
   ```bash
   dotnet restore
   ```

3. Run the application:
   ```bash
   dotnet run
   ```

4. Open your browser and navigate to the URL shown in the terminal (typically `https://localhost:5001` or `http://localhost:5000`)

## 📁 Project Structure

```
BlazorApp/
├── Models/
│   └── Activity.cs          # Data models
├── Pages/
│   └── Index.razor          # Main page component
├── Services/
│   └── ActivityService.cs   # Activity data service
├── Shared/
│   └── MainLayout.razor     # Layout component
├── wwwroot/
│   ├── css/
│   │   └── app.css          # Application styles
│   └── index.html           # Host page
├── _Imports.razor           # Global imports
├── App.razor                # Root component
├── Program.cs               # Application entry point
└── BlazorApp.csproj         # Project file
```

## 💻 Technologies Used

- Blazor WebAssembly
- .NET 8.0
- C#

## 📸 Screenshots

The application displays:
- **Activities List**: Shows all available extracurricular activities with descriptions, schedules, and available spots
- **Sign Up Form**: Allows students to register for activities using their school email

---

## 🙏 Credits & Acknowledgments

This project is based on and inspired by the [Getting Started with GitHub Copilot](https://github.com/skills/getting-started-with-github-copilot) Skills course by GitHub.

**Original Project:**
- Repository: [github.com/skills/getting-started-with-github-copilot](https://github.com/skills/getting-started-with-github-copilot)
- Original Stack: Python (FastAPI) + HTML/CSS/JavaScript
- Purpose: An educational exercise to learn GitHub Copilot

**This Fork:**
- Converted from Python/FastAPI to **Blazor WebAssembly** (.NET 8.0)
- Maintains the same functionality and UI design
- Demonstrates cross-platform migration capabilities

---

&copy; 2025 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)