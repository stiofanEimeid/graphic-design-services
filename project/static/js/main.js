/* global $, AOS */

$(document).ready(function(){
    
        // $('#submitBtn').click(function() {
        //      /* when the button in the form, display the entered values in the modal */
        //      $('#confirmtype').text($('#type').val());
        //      $('#confirmdescription').text($('#description').val());
        // });
        
        // $('#submit').click(function(){
        //      /* when the submit button in the modal is clicked, submit the form */
        //     alert('submitting');
        //     $('#formfield').submit();
        // });
        
        
        

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