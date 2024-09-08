# Define a function to process the sentence
function Get-CaseSensitiveInitials {
    param (
        [string]$sentence
    )

    # Split the sentence into words based on spaces
    $words = $sentence -split '\s+'

    # Initialize an empty string to store the initials
    $initials = ""

    # Iterate through each word in the array
    foreach ($word in $words) {
        # Check if the word is not empty
        if ($word.Length -gt 0) {
            # Add the first character of each word to the initials string
            $initials += $word[0]
        }
    }

    # Return the initials
    return $initials
}

# Example usage
$sentence = ""
$initials = Get-CaseSensitiveInitials -sentence $sentence
Write-Output $initials
