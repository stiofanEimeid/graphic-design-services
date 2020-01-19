/* global $, AOS */

$(document).ready(function(){

        $('#submitBtn').click(function() {
             /* when the button in the form, display the entered values in the modal */
            //  $('#confirmType').text($('#type').val());
             $('#confirmType').text($('input[name=type]:checked', '#formfield').val());
             $('#confirmDescription').text($('#description').val());
             $('#confirmPrice').text($('#price').val());
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

// Quote Calculator

const myForm = document.querySelector("#formfield");

const type_prices = new Array();
type_prices[0]=20;
type_prices[1]=25;
type_prices[2]=35;
type_prices[3]=75;
 

function getTypePrice()
{  
    let typePrice=0;
    const selectedType = myForm.elements["type"];
    for(let i = 0; i < selectedType.length; i++)
    { 
        if(selectedType[i].checked)
        {
            typePrice = type_prices[i];
            break;
        }
    }
    return typePrice;
}

function calculateTotal()
{
    const totalCost = getTypePrice();
    const divobj = document.querySelector('#price');
    divobj.style.display='block';
    divobj.innerHTML = "Total Price For the Request €"+ totalCost;
    
    
};


var path = anime.path('.path1');

var easings = ['linear'];

var motionPath = anime({
  targets: '.ball',
  translateX: path('x'),
  translateY: path('y'),
  rotate: path('angle'),
  easing: function (el, i) {
    return easings[i];
  },
  duration: 10000,
  loop: true
});

var path2 = anime.path('.path2');

var motionPath2 = anime({
  targets: '.ball2',
  translateX: path2('x'),
  translateY: path2('y'),
  rotate: path2('angle'),
  easing: function (el, i) {
    return easings[i];
  },
  duration: 12500,
  loop: true
});

var path3 = anime.path('.path3');

var motionPath3 = anime({
  targets: '.ball3',
  translateX: path3('x'),
  translateY: path3('y'),
  rotate: path3('angle'),
  easing: function (el, i) {
    return easings[i];
  },
  duration: 15000,
  loop: true
});


        

// Launch AOS styles
AOS.init();