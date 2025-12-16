using BlazorApp.Models;

namespace BlazorApp.Services;

public class ActivityService
{
    // In-memory activity database (simulating the Python backend)
    private readonly Dictionary<string, Activity> _activities = new()
    {
        ["Chess Club"] = new Activity
        {
            Name = "Chess Club",
            Description = "Learn strategies and compete in chess tournaments",
            Schedule = "Fridays, 3:30 PM - 5:00 PM",
            MaxParticipants = 12,
            Participants = new List<string> { "michael@mergington.edu", "daniel@mergington.edu" }
        },
        ["Programming Class"] = new Activity
        {
            Name = "Programming Class",
            Description = "Learn programming fundamentals and build software projects",
            Schedule = "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            MaxParticipants = 20,
            Participants = new List<string> { "emma@mergington.edu", "sophia@mergington.edu" }
        },
        ["Gym Class"] = new Activity
        {
            Name = "Gym Class",
            Description = "Physical education and sports activities",
            Schedule = "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            MaxParticipants = 30,
            Participants = new List<string> { "john@mergington.edu", "olivia@mergington.edu" }
        }
    };

    public Task<List<Activity>> GetActivitiesAsync()
    {
        var activities = _activities.Values.ToList();
        return Task.FromResult(activities);
    }

    public Task<SignupResult> SignupForActivityAsync(string activityName, string email)
    {
        if (!_activities.TryGetValue(activityName, out var activity))
        {
            return Task.FromResult(new SignupResult
            {
                Success = false,
                Message = "Activity not found"
            });
        }

        if (activity.Participants.Contains(email))
        {
            return Task.FromResult(new SignupResult
            {
                Success = false,
                Message = $"{email} is already signed up for {activityName}"
            });
        }

        if (activity.SpotsLeft <= 0)
        {
            return Task.FromResult(new SignupResult
            {
                Success = false,
                Message = $"No spots left in {activityName}"
            });
        }

        activity.Participants.Add(email);
        
        return Task.FromResult(new SignupResult
        {
            Success = true,
            Message = $"Signed up {email} for {activityName}"
        });
    }
}
