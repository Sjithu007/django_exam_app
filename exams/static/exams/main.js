const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body')
const startBtn = document.getElementById('start-button')

const url = window.location.href

modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click', ()=>{

    const pk = modalBtn.getAttribute('data-bs-pk')
    const name = modalBtn.getAttribute('data-bs-exam')
    const numQuestions = modalBtn.getAttribute('data-bs-questions')
    const scoreToPass = modalBtn.getAttribute('data-bs-pass')
    const duration = modalBtn.getAttribute('data-bs-duration')

    modalBody.innerHTML += `
        <div class="mb-3">Are you sure you want to begin "<b>${name}</b>" exam?</div>
        <div class="text-muted">
            <ul>
                <li>Number of questions: <b>${numQuestions}</b></li>
                <li>Pass Mark: <b>${scoreToPass}</b></li>
                <li>Duration: <b>${duration} min</b></li>
            </ul>
        </div>
    `
    startBtn.addEventListener('click', ()=>{
        window.location.href = url + pk
    })
    
}))