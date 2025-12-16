namespace BlazorApp.Models;

public class Activity
{
    public string Name { get; set; } = string.Empty;
    public string Description { get; set; } = string.Empty;
    public string Schedule { get; set; } = string.Empty;
    public int MaxParticipants { get; set; }
    public List<string> Participants { get; set; } = new();
    
    public int SpotsLeft => MaxParticipants - Participants.Count;
}

public class SignupResult
{
    public string Message { get; set; } = string.Empty;
    public bool Success { get; set; }
}
