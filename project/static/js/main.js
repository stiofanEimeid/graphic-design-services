/* global $, AOS */

$(document).ready(function(){
    
        $('#submitBtn').click(function() {
             /* when the button in the form, display the entered values in the modal */
             $('#confirmtype').text($('#type').val());
             $('#confirmdescription').text($('#description').val());
        });
        
        $('#submit').click(function(){
             /* when the submit button in the modal is clicked, submit the form */
            alert('submitting');
            $('#formfield').submit();
        });

        $('.nav-link').each(function(){
            if ($(this).prop('href') == window.location.href) {
                $(this).addClass('active');
            }
        });
 
        //   overlay only displayed when sidebar selected
       $(".openbtn" ).click(function(){
        $(".overlay").css("display", "block");
        $(".sidebar").addClass('translateMe').removeClass('untranslateMe');
        // Prevents user from scrolling through body while sidenav is open
        $("body").css('overflow', 'hidden');
      });
      
      $(".closebtn").click(function(){
         $(".overlay").css("display", "none");
         $(".sidebar").addClass('untranslateMe').removeClass('translateMe');
        // Allows user to scroll through body after closing sidenav
         $("body").css('overflow', 'visible');
      });
      
      $(".overlay").click(function(){
         $(".overlay").css("display", "none");
         $(".sidebar").addClass('untranslateMe').removeClass('translateMe');
         // Allows user to scroll through body after closing sidenav
        $("body").css('overflow', 'visible');
      });
    
    let prevScrollpos = window.pageYOffset;
    $(window).on('scroll', function(){
    var currentScrollPos = window.pageYOffset;
    /*
    If the user scrolls down the page area, the menu disappears.
    Scrolling up off the page is not recognised to keep the menu
    fixed at the top when the user is viewing that area of the page.
    The menu reappears on scroll up. 
    */
    if (prevScrollpos > currentScrollPos || prevScrollpos <= 0) {
    $(".navbar-wrapper").css('top',"0");
        } else {
            $(".navbar-wrapper").css('top', "-70px");
                }
        prevScrollpos = currentScrollPos;
        }
    );
});



AOS.init();
const slider = document.querySelector('#slider')
const carouselSlide = document.querySelector(".holder");
const carouselImages = document.querySelectorAll(".holder img"); 
const nextBtn = document.getElementById("nextBtn");
const prevBtn = document.getElementById("prevBtn");
const playBtn = document.getElementById("playBtn");
const pauseBtn = document.getElementById("pauseBtn");
let counter = 1;
// var play = true;
let myInterval;
const play = document.getElementById("playpause");


//hiding visibility

slider.addEventListener("mouseover", function(){
  prevBtn.classList.remove("hide"); //or toggle x 4// 
  nextBtn.classList.remove("hide");
});

slider.addEventListener("mouseout", function(){
  prevBtn.classList.add("hide");
  nextBtn.classList.add("hide");
});

// starting position:

carouselSlide.style.transform = "translateX(" + (counter * -10) + "%)";


// functions:

function slideRight(){
  carouselSlide.style.transition = "transform 0.4s ease-in-out"; 
	counter++;
	carouselSlide.style.transform = "translateX(" + (counter * -10) + "%)";
}

function slideLeft(){
  carouselSlide.style.transition = "transform 0.4s ease-in-out"; 
	counter--;
	carouselSlide.style.transform = "translateX(" + (counter * -10) + "%"  
}
// button navigation:

nextBtn.addEventListener("click", function(){
	if(counter >= carouselImages.length -1) return; 
  slideRight();
});


prevBtn.addEventListener("click", function(){
	if(counter <=0) return; 
  slideLeft();
});

// transitions:

carouselSlide.addEventListener("transitionend", function(){
  if(counter === 9){
  	carouselSlide.style.transition = "none"; 
  	counter = 1;
  	carouselSlide.style.transform = "translateX(" + (counter * -10) + "%";
  }

  if(counter === 0){
  	carouselSlide.style.transition = "none"; 
  	counter = 8;
  	carouselSlide.style.transform = "translateX(" + (counter * -10) + "%";
  }
});

// play+pause functionality:

   function myFunction() { 
        if(counter >= carouselImages.length -1) return; 
     slideRight();
      };

    play.addEventListener("change", function(){
        if(this.checked != true){
          myInterval=setInterval(myFunction, 3000);
        } else 
          clearInterval(myInterval);
        
});

// arrow-key navigation:

document.onkeydown = function(e) {
    switch (e.keyCode) {
        case 37:
            if(counter <=0) return; 
        slideLeft();
            break;
        case 39:
        slideRight();
            break;
    }
};
