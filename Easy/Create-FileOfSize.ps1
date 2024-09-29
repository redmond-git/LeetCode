# Function to create a file of a specific size
function Create-FileOfSize {
    param (
        [string]$filePath,
        [int]$sizeInMB
    )

    # Convert size to bytes
    $sizeInBytes = $sizeInMB * 1MB
    
    # Create a file with the specified size
    $fileStream = [System.IO.File]::Create($filePath)
    $fileStream.SetLength($sizeInBytes)
    $fileStream.Close()

    Write-Host "File '$filePath' created with size $sizeInMB MB."
}

# Example usage:
$filePath = "C:\111\custom_size_file.bin"
$sizeInMB = 10  # Change this to the desired file size in MB
Create-FileOfSize -filePath $filePath -sizeInMB $sizeInMB