const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body')
const startBtn = document.getElementById('start-button')

const url = window.location.href

modalBtns.forEach(btn => btn.addEventListener('click', ()=>{

    const pk = btn.getAttribute('data-bs-pk')
    const name = btn.getAttribute('data-bs-exam')
    const numQuestions = btn.getAttribute('data-bs-questions')
    const totalMarks = btn.getAttribute('data-bs-marks')
    const scoreToPass = btn.getAttribute('data-bs-pass')
    const duration = btn.getAttribute('data-bs-duration')

    modalBody.innerHTML += `
        <div class="mb-3">Are you sure you want to begin <b>${name}</b> exam?</div>
        <div class="lead text-small">
            <ul>
                <li>Number of questions: <b>${numQuestions}</b></li>
                <li>Total Marks: <b>${totalMarks}</b></li>
                <li>Pass Mark: <b>${scoreToPass}</b></li>
                <li>Duration: <b>${duration} minutes</b></li>
            </ul>
        </div>
    `
    startBtn.addEventListener('click', ()=>{
        window.location.href = url + pk
    })
    
}))