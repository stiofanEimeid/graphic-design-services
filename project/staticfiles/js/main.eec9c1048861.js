/* global $, AOS */

$(document).ready(function(){
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

const type_prices = [];
type_prices[0]=30;
type_prices[1]=5;
type_prices[2]=15;
type_prices[3]=50;
 
function getTypePrice()
{  
    /*The value of the option selected in the form is taken
    and matched to the corresponding value in the list*/
    let typePrice=0;
    const selectedType = myForm.elements.type;
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
}

// Launch AOS styles
AOS.init();