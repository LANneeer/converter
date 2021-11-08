let fromForm = document.querySelector('textarea[name="from"]')
let toForm = document.querySelector('textarea[name="to"]')

function sendRequest(event, url) {
    event.preventDefault()
    return fetch(url).then(response => {
        return response.text()
    }
    )
}
document.querySelector('.translator__translate-btn').addEventListener('click', (event) => {
    let url = 'http://127.0.0.1:8000/translate/?from=' + fromForm.value
    let response = sendRequest(event, url).then((r) => {
    toForm.innerText = JSON.parse(r)['result']
    })
})
