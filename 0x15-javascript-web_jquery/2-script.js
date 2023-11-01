// updates the text color of the <header> element to red (#FF0000) when
// the user clicks on the tag DIV#red_header:
$('Div#red_header').click(function redH () {
  $('header').css('color', '#FF0000');
});

/*
 or we can do it like that:

 document.addEventListener('click', redH);
    function redH() {
      $('header').css('color', '#FF0000');
    }
*/
