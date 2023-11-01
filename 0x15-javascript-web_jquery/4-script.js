// toggles the class of the <header> element when the user
// clicks on the tag DIV#toggle_header
$('DIV#toggle_header').click(function () {
  const h = $('header');
  if (h.hasClass('red')) {
    h.removeClass('red');
    h.addClass('green');
  } else {
    h.removeClass('green');
    h.addClass('red');
  }
});
