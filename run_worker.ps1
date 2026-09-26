$watchDir = Join-Path $PSScriptRoot "incoming"
$outDir = Join-Path $PSScriptRoot "processed"
$script = Join-Path $PSScriptRoot "scripts\process_helmet.py"

Write-Host "Shinto worker listening for incoming raw models..."
while ($true) {
 $files = Get-ChildItem -Path $watchDir -Filter *.glb -File -ErrorAction SilentlyContinue
 foreach ($file in $files) {
 Write-Host "New asset detected: $($file.Name)"
 $dest = Join-Path $outDir "ready_$($file.Name)"
 # Pointing to confirmed Blender 3.4 location
 & "C:\Program Files\Blender Foundation\Blender 3.4\blender.exe" -b -P $script -- $file.FullName $dest
 $archiveName = "archive_$($file.Name)"
 Move-Item -Path $file.FullName -Destination (Join-Path $watchDir $archiveName) -Force
 Write-Host "Complete. Output saved to $dest"
 }
 Start-Sleep -Seconds 3
}
