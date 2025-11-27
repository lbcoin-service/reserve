
function copyFormatText() {
    const text = document.getElementById('copyText').innerText;

    let cleanText = text
        .split('\n')           // split into lines
        .map(line => line.trim())  // remove leading/trailing spaces
        .join('\n'); 
    
    navigator.clipboard.writeText(cleanText)
        .then(() => {
            alert("Copied")
        })
        .catch(() => {
            alert("Copy failed")
        })
}

