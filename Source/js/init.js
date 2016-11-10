(function($) {
    $(function() {
    $('.button-collapse').sideNav();
    $('.modal').modal();

    $('#search').on('click', function(){

      $("#ocdx-title").animate({ opacity: 0}, 400).animate({ height: 10 }, 400);
      $('#manifest-table').empty().load("table.html").hide().fadeIn(800);
    })
  }); // end of document ready
})(jQuery); // end of jQuery name space
