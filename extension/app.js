const btn = document.getElementById('summarize')

btn.addEventListener('click', ()=>{
    btn.disabled = true
    btn.innerHTML = "Derving and Summarizing..."
    chrome.tabs.query({currentWindow: true, active: true}, (tabs) => {
        var url = tabs[0].url
        var xhr = new XMLHttpRequest()
        xhr.open("GET", "http://127.0.0.1:5000/summary?url=" + url, true)
        xhr.onload = ()=>{
            var text = xhr.responseText;
            const summrized = document.getElementById("output")
            summrized.innerHTML = text
            btn.disabled = false
            btn.innerHTML = "Derive Sense"
        }
        xhr.send()
    })
})