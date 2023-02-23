// to get current year
function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();


// isotope js
$(window).on('load', function () {
    $('.filters_menu li').click(function () {
        $('.filters_menu li').removeClass('active');
        $(this).addClass('active');

        var data = $(this).attr('data-filter');
        $grid.isotope({
            filter: data
        })
    });

    var $grid = $(".grid").isotope({
        itemSelector: ".all",
        percentPosition: false,
        masonry: {
            columnWidth: ".all"
        }
    })
});

// nice select
$(document).ready(function() {
    $('select').niceSelect();
  });

/** google_map js **/
function myMap() {
    var mapProp = {
        center: new google.maps.LatLng(40.712775, -74.005973),
        zoom: 18,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}

// client section owl carousel
$(".client_owl-carousel").owlCarousel({
    loop: true,
    margin: 0,
    dots: false,
    nav: true,
    navText: [],
    autoplay: true,
    autoplayHoverPause: true,
    navText: [
        '<i class="fa fa-angle-left" aria-hidden="true"></i>',
        '<i class="fa fa-angle-right" aria-hidden="true"></i>'
    ],
    responsive: {
        0: {
            items: 1
        },
        768: {
            items: 2
        },
        1000: {
            items: 2
        }
    }
}); 



function myFunction() {
    var name = document.getElementById("name").textContent;
    var price = document.getElementById("price").textContent;
    // Code to execute when the link is clicked
    $.ajax({
      type: "POST",
      url: "add_order",
      data: {
        name: name,
        price: price,
      },
      success: function(data) {
        // handle the response from the server
        // update the page as needed without reloading
        alert(data.status);
      },
  })
  }


function getData(element) {
    // Get the parent detail-box element
    const parent = element.closest('.detail-box');

    // Get the name and price
    const name = parent.querySelector('.name').textContent.trim();
    const price = parent.querySelector('.price').textContent.trim();

    var user_name = document.querySelector('.user').textContent;
    $.ajax({
        type: "POST",
        url: "/add_order/" ,
        data: {
            user: user_name,
            name: name,
            price: price,
        },
        success: function(data) {
            alert(data.status);
        
        },
    })
}




