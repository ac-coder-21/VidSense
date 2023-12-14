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
            let arr_text = text.split("---")
            summrized.innerHTML = arr_text[0]
            
            const link_ele = document.getElementById("link_ele")
            link_ele.innerHTML = arr_text[1]
            let link_data =  arr_text[1].split(": ")
            link_ele.href = link_data[1]

            btn.disabled = false
            btn.innerHTML = "Derive Sense"
        }
        xhr.send()
    })
})