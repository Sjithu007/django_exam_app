const url = window.location.href

const examBox = document.getElementById('exam-box')
const scoreBox = document.getElementById('score-box')
const resultBox = document.getElementById('result-box')
const timerBox = document.getElementById('timer-box')


const activateTimer = (duration) => {
    if (duration.toString().length < 2) {
        timerBox.innerHTML = `<b>0${duration}:00</b>`
    } else {
        timerBox.innerHTML = `<b>${duration}:00</b>`
    }

    let minutes = duration - 1
    let seconds = 60
    let displaySeconds
    let displayMinutes

    const timer = setInterval(()=>{
        seconds --
        if (seconds < 0) {
            seconds = 59
            minutes --
        }
        if (minutes.toString().length < 2) {
            displayMinutes = '0'+minutes
        } else {
            displayMinutes = minutes
        }
        if(seconds.toString().length < 2) {
            displaySeconds = '0' + seconds
        } else {
            displaySeconds = seconds
        }
        if (minutes === 0 && seconds === 0) {
            timerBox.innerHTML = "<b>00:00</b>"
            clearInterval(timer)
            alert('Time Over')
            sendData()
        }

        timerBox.innerHTML = '<span class="text-muted">Time left: </span>' +`<b>${displayMinutes}:${displaySeconds}</b>`
    }, 1000)
}

$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: function(response){
        const data = response.data
        var i = 1
        data.forEach(el => {
            examBox.innerHTML += `<span class="h5">${i})&ensp;</span>`
            i = i+1
            for (const [question, answers] of Object.entries(el)){

                examBox.innerHTML += `
                    <span class="mb-5 h5">
                        ${question}
                    </span>
                `
                answers.forEach(answer => {
                    examBox.innerHTML += `
                        <div class="form-check pt-3">
                            <input class="form-check-input ans" type="radio" name="${question}" id="${question}-${answer}" value="${answer}">
                            <label class="form-check-label" for="${question}">${answer}</label>
                        </div>
                    `
                })
                examBox.innerHTML +='<hr>'
            }
        });
        activateTimer(response.duration)
        
    },
    error: function(error){
        console.log(error)
    }
})

const examForm = document.getElementById('exam-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const sendData = () => {
    const elements = [...document.getElementsByClassName('ans')]
    const data = {}
    data['csrfmiddlewaretoken'] = csrf[0].value
    elements.forEach(el=>{
        if (el.checked) {
            data[el.name] = el.value
        } else {
            if (!data[el.name]) {
                data[el.name] = null
            }
        }
    })

    $.ajax({
        type: 'POST',
        url: `${url}save/`,
        data: data,
        success: function(response){
            const results = response.results
            console.log(results)
            examForm.classList.add('not-visible')

            scoreBox.innerHTML = `<h2 class="lead">${response.passed ? 'Congratulations! ' : 'Sorry :( '}Your result is ${response.score.toFixed(2)}%</h2>`

            results.forEach(res=>{
                const resDiv = document.createElement("div")
                for (const [question, resp] of Object.entries(res)){

                    resDiv.innerHTML += question
                    const cls = ['container', 'my-2', 'p-3', 'bg-white', 'h6']
                    resDiv.classList.add(...cls)

                    if (resp=='not answered') {
                        resDiv.innerHTML += ' - Not Answered'
                        resDiv.classList.add('text-danger')
                    }
                    else {
                        const answer = resp['answered']
                        const correct = resp['correct_answer']

                        if (answer == correct) {
                            resDiv.classList.add('text-success')
                            resDiv.innerHTML += ` Answered: ${answer}`
                        } else {
                            resDiv.classList.add('text-danger')
                            resDiv.innerHTML += ` | Correct Answer: ${correct}`
                            resDiv.innerHTML += ` | Answered: ${answer}`
                        }
                    }
                }
                resultBox.append(resDiv)
            })
        },
        error: function(error){
            console.log(error)
        }
    })
}

examForm.addEventListener('submit', e=>{
    e.preventDefault()
    sendData()
})