const show = document.querySelector('.btn-show');
const content = document.querySelector('#form')
show.addEventListener('click', function () {  
  content.style.display = 'block';
})

function openNav() {
  document.querySelector("#mySidebar").style.width = "250px";
  // document.querySelector("#main").style.marginLeft = "250px";
}

function closeNav() {
  document.querySelector("#mySidebar").style.width = "0";
  // document.querySelector("#main").style.marginLeft= "0";
}

