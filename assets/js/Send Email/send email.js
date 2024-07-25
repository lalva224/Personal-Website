// import 'dotenv/config';
console.log('We are in script')
const name = document.getElementById('name')
const email = document.getElementById('email')
const message = document.getElementById('message')
const submitBtn = document.getElementById('submit')


async function sendEmail(){
  let send_email = await fetch('')
}

submitBtn.addEventListener('click',sendEmail)

