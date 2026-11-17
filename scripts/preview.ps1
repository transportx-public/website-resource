param([int]$Port = 1314, [switch]$NoBrowser)
$ErrorActionPreference = 'Stop'
$repoPath = Split-Path $PSScriptRoot -Parent
$toolsPath = Join-Path (Split-Path $repoPath -Parent) '.tools'
$hugoPath = Join-Path $toolsPath 'hugo/hugo.exe'
if (-not (Test-Path -LiteralPath $hugoPath)) {
    $hugoCommand = Get-Command hugo -ErrorAction SilentlyContinue
    if (-not $hugoCommand) { throw 'Install Hugo Extended 0.134.1, or keep the sibling .tools folder.' }
    $hugoPath = $hugoCommand.Source
}
$goPath = Join-Path $toolsPath 'go/bin'
if (Test-Path -LiteralPath $goPath) { $env:PATH = $goPath + ';' + $env:PATH }
if (Test-Path -LiteralPath $toolsPath) {
    $env:GOPATH = Join-Path $toolsPath 'gopath'
    $env:HUGO_CACHEDIR = Join-Path $toolsPath 'hugo-cache'
}
$previewUrl = "http://127.0.0.1:$Port/zh/"
$client = [System.Net.WebClient]::new()
$client.Proxy = $null
try {
    $existingPage = $client.DownloadString($previewUrl)
    if ($existingPage -match 'TransportX') {
        Write-Host "Preview is already running: $previewUrl"
        if (-not $NoBrowser) { Start-Process -FilePath $previewUrl -WindowStyle Hidden }
        exit 0
    }
} catch { } finally { $client.Dispose() }
Write-Host "Starting TransportX preview..."
Write-Host "Chinese: $previewUrl"
Write-Host "Members: http://127.0.0.1:$Port/zh/people/"
Write-Host "English: http://127.0.0.1:$Port/"
Write-Host 'Keep this window open. Press Ctrl+C to stop the preview.'
# Open the browser when Hugo reports readiness. No global system settings are changed.
Push-Location $repoPath
try {
    $opened = $false
    & $hugoPath server --bind 127.0.0.1 --port $Port --baseURL "http://127.0.0.1:$Port/" --disableFastRender --destination '../preview-build' 2>&1 | ForEach-Object {
        Write-Host $_
        if (-not $opened -and $_ -match 'Web Server is available') {
            $opened = $true
            if (-not $NoBrowser) { Start-Process -FilePath $previewUrl -WindowStyle Hidden }
        }
    }
    if ($LASTEXITCODE -ne 0) { throw "Hugo exited with code $LASTEXITCODE" }
} finally { Pop-Location }
